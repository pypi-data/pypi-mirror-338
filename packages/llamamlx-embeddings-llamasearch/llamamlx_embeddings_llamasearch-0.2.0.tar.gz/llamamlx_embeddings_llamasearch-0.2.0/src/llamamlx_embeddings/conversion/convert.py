"""
Implementation of model conversion from Hugging Face to MLX.
"""

import json
import logging
import shutil
from pathlib import Path
from typing import Any, Dict, List, Optional

import mlx.core as mx
import torch
from huggingface_hub import snapshot_download
from transformers import AutoConfig, AutoModel, AutoTokenizer

from ..core.models import _SUPPORTED_MODELS
from ..core.models import get_model_info as get_model_info_core

# Configure logging
logger = logging.getLogger(__name__)


def list_supported_models() -> List[str]:
    """
    List models supported for conversion.

    Returns:
        List of supported model IDs
    """
    return list(_SUPPORTED_MODELS.keys())


def get_model_info(model_id: str) -> Dict[str, Any]:
    """
    Get information about a supported model.

    Args:
        model_id: Model identifier

    Returns:
        Dictionary with model information

    Raises:
        ValueError: If the model is not supported
    """
    model_info = get_model_info_core(model_id)
    if model_info is None:
        raise ValueError(f"Model {model_id} is not supported for conversion")
    return model_info


def _download_hf_model(
    model_id: str, revision: Optional[str] = None, cache_dir: Optional[str] = None
) -> str:
    """
    Download a model from Hugging Face.

    Args:
        model_id: Hugging Face model ID
        revision: Model revision to use
        cache_dir: Directory to cache the model

    Returns:
        Path to the downloaded model
    """
    logger.info(f"Downloading model {model_id} (revision: {revision or 'default'})")
    model_path = snapshot_download(
        repo_id=model_id, revision=revision, cache_dir=cache_dir, local_files_only=False
    )
    logger.info(f"Model downloaded to {model_path}")
    return model_path


def _convert_tensor_to_mlx(tensor: torch.Tensor) -> mx.array:
    """
    Convert a PyTorch tensor to MLX array.

    Args:
        tensor: PyTorch tensor

    Returns:
        MLX array
    """
    # Move tensor to CPU if it's on GPU
    if tensor.device.type != "cpu":
        tensor = tensor.cpu()
    # Convert to numpy and then to MLX
    return mx.array(tensor.numpy())


def _map_model_type_to_mlx(model_type: str) -> str:
    """
    Map Hugging Face model type to MLX model type.

    Args:
        model_type: Hugging Face model type

    Returns:
        MLX model type
    """
    # Map of HF model types to MLX model types
    mappings = {
        "bert": "bert",
        "roberta": "bert",  # RoBERTa uses BERT architecture
        "distilbert": "bert",
        "mpnet": "bert",  # MPNet uses BERT architecture
        "deberta": "bert",
        "electra": "bert",
    }

    # Convert to lowercase for case-insensitive matching
    model_type = model_type.lower()

    # Return mapped type or original if not found
    return mappings.get(model_type, model_type)


def convert_model(
    model_id: str,
    output_dir: Optional[str] = None,
    revision: Optional[str] = None,
    dtype: str = "float16",
    cache_dir: Optional[str] = None,
    overwrite: bool = False,
) -> str:
    """
    Convert a Hugging Face model to MLX format.

    Args:
        model_id: Hugging Face model ID
        output_dir: Directory to save the converted model
        revision: Model revision to use
        dtype: Data type for MLX model weights (float16, float32, bfloat16)
        cache_dir: Directory to cache the model
        overwrite: Whether to overwrite existing files

    Returns:
        Path to the converted model

    Raises:
        ValueError: If the data type is not supported
        FileExistsError: If the output directory exists and overwrite is False
    """
    # Validate dtype
    valid_dtypes = {"float16": mx.float16, "float32": mx.float32, "bfloat16": mx.bfloat16}
    if dtype not in valid_dtypes:
        raise ValueError(f"Unsupported dtype: {dtype}. Supported: {list(valid_dtypes.keys())}")
    mlx_dtype = valid_dtypes[dtype]

    # Determine output directory
    if output_dir is None:
        model_name = model_id.split("/")[-1]
        output_dir = Path.cwd() / "models" / model_name
    else:
        output_dir = Path(output_dir) / model_id.split("/")[-1]

    # Convert to Path object
    output_dir = Path(output_dir)

    # Check if output directory exists
    if output_dir.exists():
        if overwrite:
            logger.warning(f"Overwriting existing directory: {output_dir}")
            shutil.rmtree(output_dir)
        else:
            raise FileExistsError(
                f"Output directory already exists: {output_dir}. "
                "Use overwrite=True to overwrite."
            )

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Download model from Hugging Face
    hf_model_path = _download_hf_model(model_id, revision, cache_dir)

    # Load Hugging Face model and tokenizer
    logger.info(f"Loading model {model_id} with PyTorch")
    config = AutoConfig.from_pretrained(hf_model_path)
    model = AutoModel.from_pretrained(hf_model_path)
    tokenizer = AutoTokenizer.from_pretrained(hf_model_path)

    # Save tokenizer to output directory
    logger.info(f"Saving tokenizer to {output_dir}")
    tokenizer.save_pretrained(output_dir)

    # Create MLX config
    mlx_config = {
        "model_type": _map_model_type_to_mlx(config.model_type),
        "dtype": dtype,
        "model_args": {
            "vocab_size": config.vocab_size,
            "hidden_size": config.hidden_size,
            "num_hidden_layers": config.num_hidden_layers,
            "num_attention_heads": config.num_attention_heads,
            "intermediate_size": getattr(config, "intermediate_size", 4 * config.hidden_size),
            "hidden_act": getattr(config, "hidden_act", "gelu"),
            "hidden_dropout_prob": getattr(config, "hidden_dropout_prob", 0.1),
            "attention_probs_dropout_prob": getattr(config, "attention_probs_dropout_prob", 0.1),
            "max_position_embeddings": getattr(config, "max_position_embeddings", 512),
            "type_vocab_size": getattr(config, "type_vocab_size", 2),
            "initializer_range": getattr(config, "initializer_range", 0.02),
            "layer_norm_eps": getattr(config, "layer_norm_eps", 1e-12),
            "pad_token_id": getattr(config, "pad_token_id", 0),
            "position_embedding_type": getattr(config, "position_embedding_type", "absolute"),
            "use_cache": getattr(config, "use_cache", True),
            "classifier_dropout": getattr(config, "classifier_dropout", None),
        },
        "original_model": {
            "model_id": model_id,
            "revision": revision,
            "torch_dtype": str(model.dtype).split(".")[-1],
        },
    }

    # Save MLX config
    config_path = output_dir / "config.json"
    with open(config_path, "w") as f:
        json.dump(mlx_config, f, indent=2)

    # Extract weights from Hugging Face model
    logger.info(f"Converting weights to MLX format with dtype {dtype}")
    weights = {}

    # Process the model's state_dict
    for name, param in model.state_dict().items():
        # Convert the name to MLX format
        # This may need customization based on the model architecture
        mlx_name = name.replace(".", "/")

        # Convert the tensor to MLX
        mlx_tensor = _convert_tensor_to_mlx(param)

        # Cast to the target dtype if it's a floating point tensor
        if mlx_tensor.dtype in [mx.float32, mx.float16, mx.bfloat16]:
            mlx_tensor = mlx_tensor.astype(mlx_dtype)

        # Store the converted tensor
        weights[mlx_name] = mlx_tensor

    # Save MLX weights
    weights_path = output_dir / "weights.safetensors"
    logger.info(f"Saving weights to {weights_path}")
    mx.save(str(weights_path), weights, safe_serialization=True)

    # Save a README
    readme_path = output_dir / "README.md"
    with open(readme_path, "w") as f:
        f.write(f"# {model_id} converted to MLX format\n\n")
        f.write(f"Original model: [{model_id}](https://huggingface.co/{model_id})\n\n")
        f.write(f"Converted with llamamlx-embeddings using dtype: {dtype}\n\n")
        f.write("## Usage\n\n")
        f.write("```python\n")
        f.write("from llamamlx_embeddings.core.embeddings import Embeddings\n\n")
        f.write(f"model = Embeddings.from_pretrained('{output_dir}')\n")
        f.write("```\n")

    logger.info(f"Model converted and saved to {output_dir}")
    return str(output_dir)
