"""
KerdosAI - Universal LLM Training Agent
"""

__version__ = "0.1.1"

from .agent import KerdosAgent
from .trainer import TrainingOrchestrator
from .processor import DataProcessor
from .deployer import DeploymentManager

__all__ = ["KerdosAgent", "TrainingOrchestrator", "DataProcessor", "DeploymentManager"] 