"""
Implementation of quantization for MLX embedding models.
"""

import json
import logging
import shutil
from pathlib import Path
from typing import Dict, Optional, Union

import mlx.core as mx
import mlx.nn as nn

# Configure logging
logger = logging.getLogger(__name__)

# Define available quantization methods
QUANTIZATION_METHODS = {
    "int8": "8-bit integer quantization, good balance of performance and quality",
    "int4": "4-bit integer quantization, highest performance but with quality tradeoff",
}


def list_quantization_methods() -> Dict[str, str]:
    """
    List available quantization methods with descriptions.

    Returns:
        Dictionary mapping method names to descriptions
    """
    return QUANTIZATION_METHODS.copy()


def quantize(model: nn.Module, method: str = "int8") -> nn.Module:
    """
    Quantize an MLX model.

    Args:
        model: MLX model to quantize
        method: Quantization method to use

    Returns:
        Quantized model

    Raises:
        ValueError: If the quantization method is not supported
    """
    if method not in QUANTIZATION_METHODS:
        raise ValueError(
            f"Unsupported quantization method: {method}. "
            f"Supported methods: {list(QUANTIZATION_METHODS.keys())}"
        )

    logger.info(f"Quantizing model using {method} quantization")

    if method == "int8":
        return nn.quantize(model, mx.int8)
    elif method == "int4":
        return nn.quantize(model, mx.int4)
    else:
        # Should not reach here due to earlier check, but just in case
        raise ValueError(f"Unsupported quantization method: {method}")


def quantize_model(
    model_dir: Union[str, Path],
    output_dir: Optional[Union[str, Path]] = None,
    method: str = "int8",
    overwrite: bool = False,
) -> str:
    """
    Quantize a model from disk and save it to a new directory.

    Args:
        model_dir: Directory containing the model to quantize
        output_dir: Directory to save the quantized model (defaults to model_dir_{method})
        method: Quantization method to use
        overwrite: Whether to overwrite existing output directory

    Returns:
        Path to the quantized model directory

    Raises:
        ValueError: If the quantization method is not supported
        FileNotFoundError: If the model directory doesn't exist
        FileExistsError: If the output directory exists and overwrite is False
    """
    model_dir = Path(model_dir)

    # Check if model directory exists
    if not model_dir.exists() or not model_dir.is_dir():
        raise FileNotFoundError(f"Model directory not found: {model_dir}")

    # Determine output directory
    if output_dir is None:
        output_dir = f"{model_dir}_{method}"
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

    # Copy all non-weight files to output directory
    for file_path in model_dir.glob("*"):
        if file_path.suffix not in [".safetensors", ".npz", ".bin"]:
            if file_path.is_file():
                shutil.copy2(file_path, output_dir)
            elif file_path.is_dir():
                shutil.copytree(file_path, output_dir / file_path.name)

    # Update config to indicate quantization
    config_path = output_dir / "config.json"
    if config_path.exists():
        with open(config_path, "r") as f:
            config = json.load(f)

        # Add quantization info to config
        config["quantization"] = {"method": method, "original_model": str(model_dir)}

        with open(config_path, "w") as f:
            json.dump(config, f, indent=2)

    # Find weight files
    weight_files = list(model_dir.glob("*.safetensors")) or list(model_dir.glob("*.npz"))
    if not weight_files:
        raise FileNotFoundError(f"No weight files found in {model_dir}")

    # Process each weight file
    for weight_path in weight_files:
        # Load weights
        logger.info(f"Loading weights from {weight_path}")
        weights = mx.load(str(weight_path))

        # Apply quantization to appropriate tensors
        quantized_weights = {}
        for name, tensor in weights.items():
            # Only quantize Linear weights
            # Skip bias, layer norm, and embedding layers
            if (
                "weight" in name
                and not any(skip in name for skip in ["layernorm", "layer_norm", "embed"])
                and len(tensor.shape) == 2  # Most linear weights are 2D
            ):
                if method == "int8":
                    quantized_weights[name] = mx.quantize(tensor, mx.int8)
                elif method == "int4":
                    quantized_weights[name] = mx.quantize(tensor, mx.int4)
                else:
                    # Should not reach here, but just in case
                    quantized_weights[name] = tensor
            else:
                # Keep other tensors unchanged
                quantized_weights[name] = tensor

        # Save quantized weights
        output_weight_path = output_dir / weight_path.name
        logger.info(f"Saving quantized weights to {output_weight_path}")
        mx.save(str(output_weight_path), quantized_weights)

    logger.info(f"Model quantized and saved to {output_dir}")
    return str(output_dir)
