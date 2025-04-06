"""
Base module for model implementations.
"""

import logging
from typing import Tuple, Type

import mlx.nn as nn

logger = logging.getLogger(__name__)

# Registry of model types to model classes
MODEL_REGISTRY = {}


def register_model(model_type: str):
    """Decorator to register a model class."""

    def decorator(cls):
        MODEL_REGISTRY[model_type] = cls
        return cls

    return decorator


def get_model_class(model_type: str) -> Tuple[Type[nn.Module], Type]:
    """
    Get the model class for a given model type.

    Args:
        model_type: The model type (e.g., 'bert', 'e5', etc.)

    Returns:
        Tuple of (Model class, ModelArgs class)

    Raises:
        ValueError: If model type is not supported
    """
    # Convert hyphens to underscores and lowercase
    model_type = model_type.replace("-", "_").lower()

    # Handle special remappings
    if model_type == "e5":
        model_type = "bert"  # E5 models use bert architecture
    elif model_type == "bge":
        model_type = "bert"  # BGE models use bert architecture
    elif model_type == "xlm_roberta":
        model_type = "bert"  # XLM-Roberta is similar enough to BERT for our purposes

    if model_type in MODEL_REGISTRY:
        model_class = MODEL_REGISTRY[model_type]
        return model_class, model_class.ModelArgs
    else:
        logger.error(f"Model type {model_type} not supported.")
        supported = list(MODEL_REGISTRY.keys())
        raise ValueError(f"Model type {model_type} not supported. Supported: {supported}")
