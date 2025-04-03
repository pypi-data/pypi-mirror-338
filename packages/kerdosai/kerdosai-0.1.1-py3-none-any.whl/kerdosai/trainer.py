"""
Training orchestrator that manages the training process for the LLM.
"""

from typing import Optional, Dict, Any
import torch
from torch.utils.data import DataLoader
from transformers import Trainer, TrainingArguments
from tqdm import tqdm


class TrainingOrchestrator:
    """
    Orchestrates the training process for the LLM.
    """

    def __init__(
        self,
        model: torch.nn.Module,
        tokenizer: Any,
        device: str = "cuda",
    ):
        """
        Initialize the training orchestrator.

        Args:
            model (torch.nn.Module): The model to train
            tokenizer: The tokenizer for the model
            device (str): Device to train on ('cuda' or 'cpu')
        """
        self.model = model
        self.tokenizer = tokenizer
        self.device = device
        self.trainer = None

    def train(
        self,
        training_data: Any,
        epochs: int = 3,
        batch_size: int = 8,
        learning_rate: float = 2e-5,
        **kwargs
    ):
        """
        Train the model on the provided data.

        Args:
            training_data: The processed training data
            epochs (int): Number of training epochs
            batch_size (int): Batch size for training
            learning_rate (float): Learning rate for training
            **kwargs: Additional training parameters
        """
        # Prepare training arguments
        training_args = TrainingArguments(
            output_dir="./results",
            num_train_epochs=epochs,
            per_device_train_batch_size=batch_size,
            learning_rate=learning_rate,
            weight_decay=0.01,
            logging_dir="./logs",
            logging_steps=100,
            save_strategy="epoch",
            **kwargs
        )

        # Initialize trainer
        self.trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=training_data,
        )

        # Train the model
        self.trainer.train()

    def evaluate(self, eval_data: Any) -> Dict[str, float]:
        """
        Evaluate the model on the provided data.

        Args:
            eval_data: The evaluation data

        Returns:
            Dict[str, float]: Evaluation metrics
        """
        if self.trainer is None:
            raise ValueError("Model must be trained before evaluation")

        return self.trainer.evaluate(eval_dataset=eval_data)

    def predict(self, inputs: Any) -> Any:
        """
        Generate predictions using the trained model.

        Args:
            inputs: Input data for prediction

        Returns:
            Model predictions
        """
        if self.trainer is None:
            raise ValueError("Model must be trained before prediction")

        return self.trainer.predict(inputs)

    def save_model(self, path: str):
        """
        Save the trained model.

        Args:
            path (str): Path to save the model
        """
        if self.trainer is None:
            raise ValueError("No trained model to save")

        self.trainer.save_model(path) 