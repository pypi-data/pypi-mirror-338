"""
Utilities for converting models from Hugging Face to MLX format.
"""

import glob
import logging
import os
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Union

import mlx.core as mx
import numpy as np
from transformers import AutoModel, AutoConfig, AutoTokenizer
from huggingface_hub import hf_hub_download

from .models import get_model_path, load_model_config

# Configure logging
logger = logging.getLogger(__name__)


class ConversionError(Exception):
    """Error during model conversion."""


# Define save_weights function locally since it's no longer in models.py
def save_weights(path: Union[str, Path], weights: Dict[str, mx.array]) -> None:
    """
    Save model weights to a file.

    Args:
        path: Path to save the weights to
        weights: Dictionary of weight tensors
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.suffix == ".safetensors":
        logger.info(f"Saving weights in safetensors format to: {path}")
        mx.save_safetensors(str(path), weights)
    else:
        logger.info(f"Saving weights in npz format to: {path}")
        mx.save(str(path), weights)

    logger.info(f"Saved {len(weights)} weight tensors to {path}")


def convert_hf_to_mlx(
    model_id: str,
    output_dir: Optional[str] = None,
    revision: Optional[str] = None,
    dtype: str = "float16",
    use_safetensors: bool = True,
    overwrite: bool = False,
) -> Path:
    """
    Converts a Hugging Face model to MLX format.

    Args:
        model_id: Hugging Face model ID
        output_dir: Directory to save the converted model (defaults to model_id)
        revision: Model revision to use
        dtype: Data type for the weights (float16 or float32)
        use_safetensors: Whether to use safetensors format
        overwrite: Whether to overwrite existing files

    Returns:
        Path to the converted model

    Raises:
        ConversionError: If model conversion fails
    """
    try:
        logger.info(f"Converting model {model_id} to MLX format")

        # Set output directory
        if output_dir is None:
            output_dir = model_id.split("/")[-1] + "-mlx"

        output_path = Path(output_dir)

        # Check if output directory exists
        if output_path.exists():
            if overwrite:
                logger.warning(f"Overwriting existing directory: {output_path}")
                shutil.rmtree(output_path)
            else:
                logger.info(f"Output directory already exists: {output_path}")
                return output_path

        # Create output directory
        output_path.mkdir(parents=True, exist_ok=True)

        # Download the model files
        logger.info(f"Downloading model {model_id}")
        model_path = get_model_path(model_id, revision)

        # Load the model configuration
        config = load_model_config(model_path)

        # Load the model
        logger.info("Loading HuggingFace model")
        hf_model = AutoModel.from_pretrained(model_id, revision=revision)

        # Convert the weights to MLX format
        logger.info(f"Converting weights to MLX format (dtype={dtype})")
        mlx_weights = {}

        # Get weights from HuggingFace model
        for name, param in hf_model.named_parameters():
            # Convert to MLX array
            if dtype == "float16":
                mlx_weights[name] = mx.array(param.detach().cpu().numpy().astype(np.float16))
            else:
                mlx_weights[name] = mx.array(param.detach().cpu().numpy())

        # Save the weights
        output_weights_path = output_path / "weights.safetensors"
        save_weights(output_weights_path, mlx_weights)

        # Copy configuration files
        config_path = model_path / "config.json"
        shutil.copy(config_path, output_path / "config.json")

        # Copy tokenizer files
        tokenizer_files = [
            "tokenizer_config.json",
            "vocab.json",
            "tokenizer.json",
            "merges.txt",
            "special_tokens_map.json",
            "vocab.txt",
        ]

        for file in tokenizer_files:
            src_file = model_path / file
            if src_file.exists():
                shutil.copy(src_file, output_path / file)

        logger.info(f"Model converted successfully to {output_path}")
        return output_path

    except Exception as e:
        error_msg = f"Error converting model {model_id}: {str(e)}"
        logger.error(error_msg)
        raise ConversionError(error_msg) from e


def optimize_mlx_model(
    model_dir: Union[str, Path],
    quantize: bool = False,
    target_file: Optional[str] = None,
) -> Path:
    """
    Optimizes a MLX model (quantization, pruning, etc.).

    Args:
        model_dir: Directory containing the MLX model
        quantize: Whether to quantize the model
        target_file: Target filename for the optimized weights

    Returns:
        Path to the optimized model

    Raises:
        ConversionError: If model optimization fails
    """
    try:
        model_dir = Path(model_dir)
        logger.info(f"Optimizing MLX model in {model_dir}")

        # Set target filename
        if target_file is None:
            if quantize:
                target_file = "weights_quantized.safetensors"
            else:
                target_file = "weights_optimized.safetensors"

        # Load weights
        weights_files = glob.glob(str(model_dir / "*.safetensors"))
        if not weights_files:
            raise ConversionError(f"No safetensors files found in {model_dir}")

        weights_file = weights_files[0]
        logger.info(f"Loading weights from {weights_file}")
        weights = mx.load(weights_file)

        # Perform optimizations
        if quantize:
            from .quantization import quantize_weights

            logger.info("Quantizing weights")
            weights = quantize_weights(weights)

        # Save optimized weights
        output_path = model_dir / target_file
        logger.info(f"Saving optimized weights to {output_path}")
        mx.save_safetensors(str(output_path), weights)

        return model_dir

    except Exception as e:
        error_msg = f"Error optimizing model: {str(e)}"
        logger.error(error_msg)
        raise ConversionError(error_msg) from e
