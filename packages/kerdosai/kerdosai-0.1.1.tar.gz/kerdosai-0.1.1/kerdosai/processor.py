"""
Data processor that handles data preprocessing and validation for training.
"""

import json
import pandas as pd
from typing import Union, Dict, Any, List
from pathlib import Path
from transformers import AutoTokenizer


class DataProcessor:
    """
    Processes and validates training data for the LLM.
    """

    def __init__(
        self,
        data_path: Union[str, Path],
        tokenizer: Any = None,
        max_length: int = 512,
    ):
        """
        Initialize the data processor.

        Args:
            data_path (Union[str, Path]): Path to the training data
            tokenizer: Tokenizer for text processing
            max_length (int): Maximum sequence length
        """
        self.data_path = Path(data_path)
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.data = None

    def process_data(self) -> Any:
        """
        Process and validate the training data.

        Returns:
            Processed dataset ready for training
        """
        # Load data
        self._load_data()

        # Validate data
        self._validate_data()

        # Process data
        processed_data = self._process_data()

        return processed_data

    def _load_data(self):
        """Load data from the specified path."""
        if self.data_path.suffix == ".json":
            with open(self.data_path, "r") as f:
                self.data = json.load(f)
        elif self.data_path.suffix in [".csv", ".tsv"]:
            self.data = pd.read_csv(self.data_path)
        else:
            raise ValueError(f"Unsupported file format: {self.data_path.suffix}")

    def _validate_data(self):
        """Validate the loaded data."""
        if self.data is None:
            raise ValueError("No data loaded")

        # Check minimum data requirements
        if isinstance(self.data, list):
            if len(self.data) < 1000:
                raise ValueError("Insufficient training data. Minimum 1000 examples required.")
        elif isinstance(self.data, pd.DataFrame):
            if len(self.data) < 1000:
                raise ValueError("Insufficient training data. Minimum 1000 examples required.")

        # Validate data structure
        if isinstance(self.data, list):
            for item in self.data:
                if not isinstance(item, dict):
                    raise ValueError("Each item in the data must be a dictionary")
                if "text" not in item:
                    raise ValueError("Each item must contain a 'text' field")
        elif isinstance(self.data, pd.DataFrame):
            if "text" not in self.data.columns:
                raise ValueError("DataFrame must contain a 'text' column")

    def _process_data(self) -> Any:
        """
        Process the validated data.

        Returns:
            Processed dataset
        """
        if self.tokenizer is None:
            raise ValueError("Tokenizer must be set before processing data")

        processed_data = []
        for item in self.data:
            if isinstance(self.data, list):
                text = item["text"]
            else:
                text = item["text"]

            # Tokenize text
            encoded = self.tokenizer(
                text,
                max_length=self.max_length,
                padding="max_length",
                truncation=True,
                return_tensors="pt"
            )

            processed_data.append({
                "input_ids": encoded["input_ids"].squeeze(),
                "attention_mask": encoded["attention_mask"].squeeze()
            })

        return processed_data

    def save_processed_data(self, output_path: Union[str, Path]):
        """
        Save the processed data to a file.

        Args:
            output_path (Union[str, Path]): Path to save the processed data
        """
        if self.data is None:
            raise ValueError("No data to save")

        output_path = Path(output_path)
        if output_path.suffix == ".json":
            with open(output_path, "w") as f:
                json.dump(self.data, f)
        elif output_path.suffix in [".csv", ".tsv"]:
            if isinstance(self.data, pd.DataFrame):
                self.data.to_csv(output_path, index=False)
            else:
                pd.DataFrame(self.data).to_csv(output_path, index=False)
        else:
            raise ValueError(f"Unsupported output format: {output_path.suffix}") 