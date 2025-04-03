"""
Deployment manager that handles model deployment in various environments.
"""

from typing import Optional, Dict, Any
import torch
from pathlib import Path
import docker
from kubernetes import client, config
import fastapi
from fastapi import FastAPI
import uvicorn


class DeploymentManager:
    """
    Manages the deployment of trained models in various environments.
    """

    def __init__(
        self,
        model: torch.nn.Module,
        tokenizer: Any,
        device: str = "cuda",
    ):
        """
        Initialize the deployment manager.

        Args:
            model (torch.nn.Module): The trained model
            tokenizer: The tokenizer for the model
            device (str): Device to run the model on
        """
        self.model = model
        self.tokenizer = tokenizer
        self.device = device
        self.app = None

    def deploy(
        self,
        deployment_type: str = "rest",
        **kwargs
    ) -> Any:
        """
        Deploy the model in the specified environment.

        Args:
            deployment_type (str): Type of deployment ('rest', 'docker', or 'kubernetes')
            **kwargs: Additional deployment parameters

        Returns:
            Deployment information or endpoint URL
        """
        if deployment_type == "rest":
            return self._deploy_rest(**kwargs)
        elif deployment_type == "docker":
            return self._deploy_docker(**kwargs)
        elif deployment_type == "kubernetes":
            return self._deploy_kubernetes(**kwargs)
        else:
            raise ValueError(f"Unsupported deployment type: {deployment_type}")

    def _deploy_rest(self, host: str = "0.0.0.0", port: int = 8000) -> str:
        """
        Deploy the model as a REST API.

        Args:
            host (str): Host to bind the API to
            port (int): Port to bind the API to

        Returns:
            str: API endpoint URL
        """
        app = FastAPI(title="KerdosAI API")

        @app.post("/predict")
        async def predict(text: str):
            inputs = self.tokenizer(text, return_tensors="pt").to(self.device)
            outputs = self.model.generate(**inputs)
            return {"prediction": self.tokenizer.decode(outputs[0])}

        self.app = app
        uvicorn.run(app, host=host, port=port)
        return f"http://{host}:{port}/predict"

    def _deploy_docker(self, image_name: str = "kerdosai") -> str:
        """
        Deploy the model in a Docker container.

        Args:
            image_name (str): Name for the Docker image

        Returns:
            str: Docker image ID
        """
        client = docker.from_env()

        # Create Dockerfile
        dockerfile = """
        FROM python:3.8-slim
        WORKDIR /app
        COPY requirements.txt .
        RUN pip install -r requirements.txt
        COPY . .
        CMD ["python", "-m", "kerdosai.serve"]
        """
        with open("Dockerfile", "w") as f:
            f.write(dockerfile)

        # Build and run container
        image, _ = client.images.build(path=".", tag=image_name)
        container = client.containers.run(
            image.id,
            ports={"8000/tcp": 8000},
            detach=True
        )

        return container.id

    def _deploy_kubernetes(self, namespace: str = "default") -> Dict[str, Any]:
        """
        Deploy the model in a Kubernetes cluster.

        Args:
            namespace (str): Kubernetes namespace

        Returns:
            Dict[str, Any]: Deployment information
        """
        config.load_kube_config()
        k8s_apps_v1 = client.AppsV1Api()
        k8s_core_v1 = client.CoreV1Api()

        # Create deployment
        deployment = {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "metadata": {"name": "kerdosai"},
            "spec": {
                "replicas": 1,
                "selector": {"matchLabels": {"app": "kerdosai"}},
                "template": {
                    "metadata": {"labels": {"app": "kerdosai"}},
                    "spec": {
                        "containers": [{
                            "name": "kerdosai",
                            "image": "kerdosai:latest",
                            "ports": [{"containerPort": 8000}]
                        }]
                    }
                }
            }
        }

        # Create service
        service = {
            "apiVersion": "v1",
            "kind": "Service",
            "metadata": {"name": "kerdosai"},
            "spec": {
                "selector": {"app": "kerdosai"},
                "ports": [{"port": 80, "targetPort": 8000}],
                "type": "LoadBalancer"
            }
        }

        # Apply deployment and service
        k8s_apps_v1.create_namespaced_deployment(
            namespace=namespace,
            body=deployment
        )
        k8s_core_v1.create_namespaced_service(
            namespace=namespace,
            body=service
        )

        return {
            "deployment": "kerdosai",
            "namespace": namespace,
            "service": "kerdosai"
        }

    def stop(self):
        """Stop the deployed model."""
        if self.app:
            self.app.shutdown() 