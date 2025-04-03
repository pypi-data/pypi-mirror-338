"""
Tests for the KerdosAI package.
"""

import pytest
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from kerdosai import KerdosAgent, DataProcessor, TrainingOrchestrator, DeploymentManager


@pytest.fixture
def sample_data(tmp_path):
    """Create sample training data."""
    data = [
        {"text": "This is a test sentence 1."},
        {"text": "This is a test sentence 2."},
        {"text": "This is a test sentence 3."},
    ]
    data_path = tmp_path / "test_data.json"
    with open(data_path, "w") as f:
        import json
        json.dump(data, f)
    return str(data_path)


@pytest.fixture
def model_and_tokenizer():
    """Create a small test model and tokenizer."""
    model_name = "gpt2"  # Using a small model for testing
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer


def test_data_processor(sample_data, model_and_tokenizer):
    """Test the DataProcessor class."""
    _, tokenizer = model_and_tokenizer
    processor = DataProcessor(sample_data, tokenizer=tokenizer)
    processed_data = processor.process_data()
    assert len(processed_data) == 3
    assert "input_ids" in processed_data[0]
    assert "attention_mask" in processed_data[0]


def test_training_orchestrator(model_and_tokenizer):
    """Test the TrainingOrchestrator class."""
    model, tokenizer = model_and_tokenizer
    trainer = TrainingOrchestrator(model, tokenizer)
    assert trainer.model is not None
    assert trainer.tokenizer is not None


def test_deployment_manager(model_and_tokenizer):
    """Test the DeploymentManager class."""
    model, tokenizer = model_and_tokenizer
    deployer = DeploymentManager(model, tokenizer)
    assert deployer.model is not None
    assert deployer.tokenizer is not None


def test_kerdos_agent(sample_data):
    """Test the main KerdosAgent class."""
    agent = KerdosAgent(
        base_model="gpt2",
        training_data=sample_data
    )
    assert agent.model is not None
    assert agent.tokenizer is not None
    assert agent.processor is not None
    assert agent.trainer is not None
    assert agent.deployer is not None 