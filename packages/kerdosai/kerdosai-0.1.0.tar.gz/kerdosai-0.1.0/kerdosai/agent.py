"""
Main KerdosAgent class that orchestrates the training and deployment process.
"""

from typing import Optional, Union
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from .trainer import TrainingOrchestrator
from .processor import DataProcessor
from .deployer import DeploymentManager


class KerdosAgent:
    """
    Main agent class for KerdosAI that handles the training and deployment of LLMs.
    """

    def __init__(
        self,
        base_model: str,
        training_data: str,
        device: Optional[str] = None,
        model_config: Optional[dict] = None,
    ):
        """
        Initialize the KerdosAgent.

        Args:
            base_model (str): Name or path of the base LLM model
            training_data (str): Path to the training data
            device (str, optional): Device to run the model on ('cuda' or 'cpu')
            model_config (dict, optional): Additional model configuration
        """
        self.base_model = base_model
        self.training_data = training_data
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model_config = model_config or {}

        # Initialize components
        self.model = None
        self.tokenizer = None
        self.trainer = None
        self.processor = None
        self.deployer = None

        self._initialize_components()

    def _initialize_components(self):
        """Initialize all the necessary components."""
        # Load model and tokenizer
        self.model = AutoModelForCausalLM.from_pretrained(
            self.base_model,
            **self.model_config
        ).to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(self.base_model)

        # Initialize other components
        self.processor = DataProcessor(self.training_data)
        self.trainer = TrainingOrchestrator(
            model=self.model,
            tokenizer=self.tokenizer,
            device=self.device
        )
        self.deployer = DeploymentManager(
            model=self.model,
            tokenizer=self.tokenizer,
            device=self.device
        )

    def train(
        self,
        epochs: int = 3,
        batch_size: int = 8,
        learning_rate: float = 2e-5,
        **kwargs
    ):
        """
        Train the model on the provided data.

        Args:
            epochs (int): Number of training epochs
            batch_size (int): Batch size for training
            learning_rate (float): Learning rate for training
            **kwargs: Additional training parameters
        """
        # Process training data
        processed_data = self.processor.process_data()

        # Train the model
        self.trainer.train(
            processed_data,
            epochs=epochs,
            batch_size=batch_size,
            learning_rate=learning_rate,
            **kwargs
        )

    def deploy(
        self,
        deployment_type: str = "rest",
        **kwargs
    ):
        """
        Deploy the trained model.

        Args:
            deployment_type (str): Type of deployment ('rest', 'docker', or 'kubernetes')
            **kwargs: Additional deployment parameters
        """
        return self.deployer.deploy(deployment_type=deployment_type, **kwargs)

    def predict(self, text: str, **kwargs):
        """
        Generate predictions using the trained model.

        Args:
            text (str): Input text for prediction
            **kwargs: Additional prediction parameters

        Returns:
            str: Generated prediction
        """
        return self.model.generate(
            self.tokenizer(text, return_tensors="pt").to(self.device),
            **kwargs
        )

    def save(self, path: str):
        """
        Save the trained model and tokenizer.

        Args:
            path (str): Path to save the model and tokenizer
        """
        self.model.save_pretrained(path)
        self.tokenizer.save_pretrained(path)

    def load(self, path: str):
        """
        Load a trained model and tokenizer.

        Args:
            path (str): Path to load the model and tokenizer from
        """
        self.model = AutoModelForCausalLM.from_pretrained(path).to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(path) 