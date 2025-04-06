"""
Model loading, management, and information for text embeddings with MLX.
"""

import glob
import importlib
import json
import logging
import os
from pathlib import Path
from typing import Tuple, Type, Callable, Optional, Dict, Any, List, Union

import mlx.core as mx
import mlx.nn as nn
from huggingface_hub import snapshot_download, HfApi
from huggingface_hub.utils import RepositoryNotFoundError
from mlx.utils import tree_flatten
from transformers import AutoTokenizer, PreTrainedTokenizer

from ..utils.error_handling import ModelNotFoundError, safe_import

# Configure logging
logger = logging.getLogger(__name__)

# Constants
MODEL_REMAPPING = {}  # For remapping model types if needed
MAX_FILE_SIZE_GB = 5
DEFAULT_MODEL = "BAAI/bge-small-en-v1.5"  # Default embedding model

# --- Model Type Definitions ---
DENSE_MODEL_TYPES = ["bert", "xlm-roberta", "e5", "bge"]
SPARSE_MODEL_TYPES = ["splade"]  # For now, just SPLADE++
LATE_INTERACTION_MODEL_TYPES = ["colbert"]
CROSS_ENCODER_MODEL_TYPES = [
    "ms-marco-MiniLM-L-6-v2"
]  # Example - expand as needed

# --- Supported Models (Centralized) ---
# This dictionary holds information about supported models.
_SUPPORTED_MODELS = {
    "BAAI/bge-small-en-v1.5": {
        "model_type": "dense",
        "dim": 384,
        "description": "BGE small English model, v1.5",
    },
    "intfloat/e5-small-v2": {
        "model_type": "dense",
        "dim": 384,
        "description": "E5 small model, v2",
    },
    "sentence-transformers/all-MiniLM-L6-v2": {
        "model_type": "dense",
        "dim": 384,
        "description": "All MiniLM L6 v2 model",
    },
    "prithivida/Splade_PP_en_v1": {
        "model_type": "sparse",
        "dim": 30522,  # Vocab size (for now) - could be different
        "description": "SPLADE++ English model.",
    },
    "colbert-ir/colbertv2.0": {
        "model_type": "late_interaction",
        "dim": 128,  # Usually the per-token dimension
        "description": "ColBERT v2.0",
    },
    "Xenova/ms-marco-MiniLM-L-6-v2": {  # Example cross-encoder
        "model_type": "cross_encoder",
        "dim": 384,  # Output dim (though not directly used for embeddings)
        "description": "MS MARCO MiniLM-L6-v2 cross-encoder",
    },
    # Add other supported models here
}

_CUSTOM_MODELS: Dict[str, Dict[str, Any]] = {}  # Store custom model info

# --- Utility Functions ---

def get_model_info(model_name: str) -> Optional[Dict[str, Any]]:
    """
    Gets model information from the supported or custom models.
    
    Args:
        model_name: Name of the model to get info for
        
    Returns:
        Dictionary with model information or None if not found
    """
    if model_name in _SUPPORTED_MODELS:
        return {**_SUPPORTED_MODELS[model_name], "model": model_name}
    elif model_name in _CUSTOM_MODELS:
        return {**_CUSTOM_MODELS[model_name], "model": model_name}
    else:
        return None


def register_custom_model(
    model_name: str,
    model_path: str,
    model_type: str,
    dimension: int,
    description: str = "",
    **kwargs
) -> None:
    """
    Register a custom model for use with the library.
    
    Args:
        model_name: The name to use for the model
        model_path: Path to the model directory
        model_type: Type of model ("dense", "sparse", etc.)
        dimension: Embedding dimension
        description: Optional description of the model
        **kwargs: Additional model information
    """
    _CUSTOM_MODELS[model_name] = {
        "model_type": model_type,
        "dim": dimension,
        "model_path": model_path,
        "description": description,
        **kwargs
    }
    logger.info(f"Registered custom model: {model_name}")


def list_supported_models() -> Dict[str, List[str]]:
    """
    List all supported models by category.
    
    Returns:
        Dictionary mapping model categories to lists of model names
    """
    # Combine built-in and custom models
    all_models = {**_SUPPORTED_MODELS, **_CUSTOM_MODELS}
    
    # Group by model type
    model_categories = {
        "DENSE": [],
        "SPARSE": [],
        "LATE_INTERACTION": [],
        "CROSS_ENCODER": [],
        "OTHER": [],
    }
    
    for model_name, info in all_models.items():
        model_type = info.get("model_type", "").lower()
        
        if model_type == "dense":
            model_categories["DENSE"].append(model_name)
        elif model_type == "sparse":
            model_categories["SPARSE"].append(model_name)
        elif model_type == "late_interaction":
            model_categories["LATE_INTERACTION"].append(model_name)
        elif model_type == "cross_encoder":
            model_categories["CROSS_ENCODER"].append(model_name)
        else:
            model_categories["OTHER"].append(model_name)
    
    # Remove empty categories
    return {k: v for k, v in model_categories.items() if v}


def get_model_path(path_or_hf_repo: str, revision: Optional[str] = None) -> Path:
    """
    Ensures the model is available locally. Downloads from HF Hub if needed.
    
    Args:
        path_or_hf_repo: Local path or Hugging Face repository ID
        revision: Specific revision to download
        
    Returns:
        Path to the local model directory
        
    Raises:
        ModelNotFoundError: If the model cannot be found or downloaded
    """
    model_path = Path(path_or_hf_repo)
    if not model_path.exists():
        try:
            logger.info(f"Downloading model from HF Hub: {path_or_hf_repo}")
            model_path = Path(
                snapshot_download(
                    repo_id=path_or_hf_repo,
                    revision=revision,
                    allow_patterns=[
                        "*.json",
                        "*.safetensors",
                        "*.py",
                        "tokenizer.model",
                        "*.tiktoken",
                        "*.txt",
                    ],
                )
            )
            logger.info(f"Model downloaded to: {model_path}")
        except RepositoryNotFoundError:
            error_msg = (
                f"Model not found: {path_or_hf_repo}.\n"
                "Check path/repo ID, or ensure you're authenticated for private repos."
            )
            logger.error(error_msg)
            raise ModelNotFoundError(path_or_hf_repo, error_msg)
        except Exception as e:
            error_msg = f"Error downloading model {path_or_hf_repo}: {str(e)}"
            logger.error(error_msg)
            raise ModelNotFoundError(path_or_hf_repo, error_msg)
    
    return model_path


def load_model_config(model_path: Path) -> dict:
    """
    Loads the model's config.json.
    
    Args:
        model_path: Path to the model directory
        
    Returns:
        Dictionary containing model configuration
        
    Raises:
        FileNotFoundError: If config.json is missing
    """
    try:
        config_path = model_path / "config.json"
        with open(config_path, "r") as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        error_msg = f"Config file not found in {model_path}"
        logger.error(error_msg)
        raise FileNotFoundError(error_msg)
    except json.JSONDecodeError:
        error_msg = f"Invalid JSON in config file: {config_path}"
        logger.error(error_msg)
        raise


def _get_mlx_model_classes(config: dict) -> Tuple[Type[nn.Module], Type]:
    """
    Dynamically imports the correct Model and ModelArgs classes based on config.
    
    Args:
        config: Model configuration dictionary
        
    Returns:
        Tuple of (Model class, ModelArgs class)
        
    Raises:
        ValueError: If model type is not supported by mlx_models
    """
    model_type = config["model_type"].replace("-", "_")
    model_type = MODEL_REMAPPING.get(model_type, model_type)
    
    # First try using mlx_models package
    try:
        arch = importlib.import_module(f".{model_type}", package="mlx_models.models")
        return arch.Model, arch.ModelArgs
    except ImportError:
        # Fall back to local implementations in models directory
        try:
            models_dir = Path(__file__).parent / "models"
            if not models_dir.exists():
                # Create models directory if it doesn't exist
                models_dir.mkdir(exist_ok=True)
                # Create __init__.py file
                with open(models_dir / "__init__.py", "w") as f:
                    f.write("# Model implementations\n")
            
            # Check if model implementation exists
            implementation_path = models_dir / f"{model_type}.py"
            if not implementation_path.exists():
                raise ValueError(f"No implementation found for model type: {model_type}")
            
            # Load the model module
            spec = importlib.util.spec_from_file_location(
                f"models.{model_type}", implementation_path
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            return module.Model, module.ModelArgs
        except Exception as e:
            msg = f"Model type {model_type} not supported: {str(e)}"
            logger.error(msg)
            raise ValueError(msg)


def load_mlx_tokenizer(model_path: Path, **kwargs) -> PreTrainedTokenizer:
    """
    Loads the tokenizer (using Hugging Face `transformers`).
    
    Args:
        model_path: Path to model directory
        **kwargs: Additional arguments for tokenizer
        
    Returns:
        Loaded tokenizer
    """
    try:
        return AutoTokenizer.from_pretrained(model_path, **kwargs)
    except Exception as e:
        error_msg = f"Error loading tokenizer from {model_path}: {str(e)}"
        logger.error(error_msg)
        raise


def load_mlx_model(
    model_name: str,
    *,
    quantize: bool = False,
    model_type: str = "dense",  # "dense", "sparse", "late_interaction"
    **kwargs,
) -> Tuple[nn.Module, PreTrainedTokenizer]:
    """
    Loads an MLX model and tokenizer, handling built-in and custom models.

    Args:
        model_name: Name of the model (either built-in or custom)
        quantize: Whether to quantize the model
        model_type: Model type string ("dense", "sparse", "late_interaction")
        **kwargs: Additional arguments for model and tokenizer

    Returns:
        A tuple of (model, tokenizer)
        
    Raises:
        ValueError: If model is not supported or can't be loaded
    """
    logger.info(f"Loading model: {model_name} (type: {model_type}, quantize: {quantize})")

    # Determine if it's a custom model, and retrieve the model path
    if model_name in _CUSTOM_MODELS:
        model_info = _CUSTOM_MODELS[model_name]
        model_path_str = model_info["model_path"]
        model_path = Path(model_path_str)  # Ensure it's a Path object
    else:
        model_path = get_model_path(model_name)

    # Load the model and tokenizer
    config = load_model_config(model_path)
    model_class, model_args_class = _get_mlx_model_classes(config)
    model = model_class(model_args_class(**config["model_args"]))
    tokenizer = load_mlx_tokenizer(model_path)

    return model, tokenizer
