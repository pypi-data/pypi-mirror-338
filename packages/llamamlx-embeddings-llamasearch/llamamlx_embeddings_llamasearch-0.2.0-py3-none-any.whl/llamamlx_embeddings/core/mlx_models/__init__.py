"""
MLX model implementations for different embedding architectures.
"""

# Import all model implementations
from .bert import Model as BertModel
from .bert import ModelArgs as BertModelArgs

# Model registry for dynamic loading
_MODEL_REGISTRY = {
    "bert": (BertModel, BertModelArgs),
    # Add more model types as they're implemented
}


def get_model_class(model_type: str):
    """
    Get the model and model args classes for a specific model type.

    Args:
        model_type: Type of the model (e.g., "bert", "roberta")

    Returns:
        A tuple of (ModelClass, ModelArgsClass)

    Raises:
        ValueError: If the model type is not supported
    """
    model_type = model_type.lower()
    if model_type not in _MODEL_REGISTRY:
        raise ValueError(
            f"Model type '{model_type}' is not supported. "
            f"Supported types: {list(_MODEL_REGISTRY.keys())}"
        )

    return _MODEL_REGISTRY[model_type]
