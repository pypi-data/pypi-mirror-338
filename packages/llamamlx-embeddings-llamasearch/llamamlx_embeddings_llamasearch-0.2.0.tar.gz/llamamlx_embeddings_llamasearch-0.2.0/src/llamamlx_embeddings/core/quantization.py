"""
Utilities for quantizing and dequantizing MLX models.
"""

import logging
from typing import Any, Dict, List, Optional

import mlx.core as mx
import mlx.nn as nn
from mlx.utils import tree_unflatten

# Configure logging
logger = logging.getLogger(__name__)


class QuantizationError(Exception):
    """Error during model quantization."""


def quantize(model: nn.Module, q_group_size: int = 64, q_bits: int = 4) -> nn.Module:
    """
    Quantizes the model, reducing memory footprint and potentially improving inference speed.

    Args:
        model: The model to quantize
        q_group_size: Group size for quantization
        q_bits: Bits per weight for quantization

    Returns:
        The quantized model
    """
    logger.info(f"Quantizing model with group_size={q_group_size}, bits={q_bits}")
    try:
        nn.quantize(model, q_group_size, q_bits)
        return model
    except Exception as e:
        logger.error(f"Quantization failed: {str(e)}")
        raise


def dequantize(model: nn.Module) -> nn.Module:
    """
    Dequantize the quantized linear layers in the model.

    Args:
        model: The model with quantized linear layers

    Returns:
        The model with dequantized layers
    """
    logger.info("Dequantizing model")
    try:
        de_quantize_layers = []
        quantized_layer_count = 0

        for name, module in model.named_modules():
            if isinstance(module, nn.QuantizedLinear):
                quantized_layer_count += 1
                # Dequantize linear layer
                bias = "bias" in module
                weight = module.weight
                weight = mx.dequantize(
                    weight,
                    module.scales,
                    module.biases,
                    module.group_size,
                    module.bits,
                ).astype(mx.float16)

                output_dims, input_dims = weight.shape
                linear = nn.Linear(input_dims, output_dims, bias=bias)
                linear.weight = weight

                if bias:
                    linear.bias = module.bias

                de_quantize_layers.append((name, linear))

            elif isinstance(module, nn.QuantizedEmbedding):
                quantized_layer_count += 1
                # Dequantize embedding layer
                weight = mx.dequantize(
                    module.weight,
                    module.scales,
                    module.biases,
                    module.group_size,
                    module.bits,
                ).astype(mx.float16)

                num_embeddings, dims = weight.shape
                emb = nn.Embedding(num_embeddings, dims)
                emb.weight = weight

                de_quantize_layers.append((name, emb))

        if de_quantize_layers:
            logger.info(f"Dequantized {len(de_quantize_layers)} layers")
            model.update_modules(tree_unflatten(de_quantize_layers))
        else:
            logger.warning("No quantized layers found to dequantize")

        return model

    except Exception as e:
        logger.error(f"Dequantization failed: {str(e)}")
        raise


def check_quantization_support(model: nn.Module) -> bool:
    """
    Check if the model has any layers that can be quantized.

    Args:
        model: The model to check

    Returns:
        True if the model has quantizable layers, False otherwise
    """
    for _, module in model.named_modules():
        if isinstance(module, (nn.Linear, nn.Embedding)):
            return True
    return False


def get_quantization_status(model: nn.Module) -> Dict[str, Any]:
    """
    Get information about the quantization status of a model.

    Args:
        model: The model to check

    Returns:
        Dictionary with quantization information
    """
    quantized_count = 0
    quantizable_count = 0

    for _, module in model.named_modules():
        if isinstance(module, (nn.QuantizedLinear, nn.QuantizedEmbedding)):
            quantized_count += 1

        if isinstance(module, (nn.Linear, nn.Embedding)):
            quantizable_count += 1

    # If model has quantized layers, get their quantization parameters
    q_bits = None
    q_group_size = None

    for _, module in model.named_modules():
        if isinstance(module, (nn.QuantizedLinear, nn.QuantizedEmbedding)):
            q_bits = module.bits
            q_group_size = module.group_size
            break

    return {
        "is_quantized": quantized_count > 0,
        "quantized_layers": quantized_count,
        "quantizable_layers": quantizable_count,
        "quantization_ratio": quantized_count / (quantizable_count + 1e-10),
        "bits": q_bits,
        "group_size": q_group_size,
    }


def quantize_weights(
    weights: Dict[str, mx.array],
    bits: int = 8,
    exclude_layers: Optional[List[str]] = None,
) -> Dict[str, mx.array]:
    """
    Quantize MLX weights to lower precision.

    Args:
        weights: Dictionary of weight tensors
        bits: Bit width for quantization (4 or 8)
        exclude_layers: List of layer names to exclude from quantization

    Returns:
        Dictionary of quantized weight tensors

    Raises:
        QuantizationError: If quantization fails
    """
    try:
        logger.info(f"Quantizing weights to {bits} bits")

        if bits not in [4, 8]:
            raise QuantizationError(f"Unsupported bit width: {bits}. Must be 4 or 8.")

        if exclude_layers is None:
            exclude_layers = ["embeddings", "layernorm", "norm", "ln", "bias"]

        quantized_weights = {}

        for name, weight in weights.items():
            # Skip excluded layers
            if any(exclude in name.lower() for exclude in exclude_layers):
                logger.info(f"Skipping quantization for {name}")
                quantized_weights[name] = weight
                continue

            # Skip non-float tensors
            if weight.dtype not in [mx.float16, mx.float32]:
                quantized_weights[name] = weight
                continue

            # Skip small tensors
            if weight.size < 1024:  # Skip tensors smaller than 1K elements
                quantized_weights[name] = weight
                continue

            # Quantize
            logger.debug(f"Quantizing {name} with shape {weight.shape}")

            if bits == 8:
                quantized_weights[name] = quantize_to_int8(weight)
            else:  # bits == 4
                quantized_weights[name] = quantize_to_int4(weight)

        logger.info(f"Quantized {len(weights)} weight tensors")
        return quantized_weights

    except Exception as e:
        error_msg = f"Error during quantization: {str(e)}"
        logger.error(error_msg)
        raise QuantizationError(error_msg) from e


def quantize_to_int8(tensor: mx.array) -> mx.array:
    """
    Quantize a tensor to int8.

    Args:
        tensor: Input tensor

    Returns:
        Quantized tensor
    """
    # Convert to float32 for calculations
    tensor_f32 = tensor.astype(mx.float32)

    # Get min and max values per channel
    if len(tensor.shape) > 1:
        # For matrices, quantize per output channel (axis 0)
        axis = tuple(range(1, len(tensor.shape)))
        scale = 127.0 / mx.maximum(mx.abs(tensor_f32).max(axis=axis, keepdims=True), 1e-5)
    else:
        # For vectors, quantize the entire tensor
        scale = 127.0 / mx.maximum(mx.abs(tensor_f32).max(), 1e-5)

    # Quantize
    quantized = mx.round(tensor_f32 * scale).astype(mx.int8)

    # Store scale as an attribute
    setattr(quantized, "scale", scale.astype(mx.float32))

    return quantized


def quantize_to_int4(tensor: mx.array) -> mx.array:
    """
    Quantize a tensor to int4 (packed as int8).

    Args:
        tensor: Input tensor

    Returns:
        Quantized tensor (with lower 4 bits and upper 4 bits packed into int8)
    """
    # Convert to float32 for calculations
    tensor_f32 = tensor.astype(mx.float32)

    # Get min and max values per channel
    if len(tensor.shape) > 1:
        # For matrices, quantize per output channel (axis 0)
        axis = tuple(range(1, len(tensor.shape)))
        scale = 7.0 / mx.maximum(mx.abs(tensor_f32).max(axis=axis, keepdims=True), 1e-5)
    else:
        # For vectors, quantize the entire tensor
        scale = 7.0 / mx.maximum(mx.abs(tensor_f32).max(), 1e-5)

    # Quantize
    quantized = mx.round(tensor_f32 * scale).astype(mx.int8)

    # Clamp to [-7, 7] range for 4-bit signed integer with one bit for sign
    quantized = mx.clip(quantized, -7, 7)

    # Reshape for packing
    if len(tensor.shape) > 1:
        # For matrices
        orig_shape = tensor.shape
        tensor_2d = tensor_f32.reshape(-1, tensor.shape[-1])

        # Ensure even number of elements for packing
        if tensor_2d.shape[0] % 2 != 0:
            padding = mx.zeros((1, tensor_2d.shape[1]), dtype=mx.float32)
            tensor_2d = mx.concatenate([tensor_2d, padding], axis=0)

        # Reshape for packing two 4-bit values into one 8-bit value
        packed_shape = (tensor_2d.shape[0] // 2, tensor_2d.shape[1])

        # Pack
        evens = quantized.reshape(-1, tensor.shape[-1])[::2]
        odds = quantized.reshape(-1, tensor.shape[-1])[1::2]
        packed = (evens & 0x0F) | ((odds & 0x0F) << 4)

        # Store original shape for unpacking
        setattr(packed, "orig_shape", orig_shape)
    else:
        # For vectors
        # Ensure even number of elements for packing
        if tensor.shape[0] % 2 != 0:
            padded = mx.concatenate([tensor_f32, mx.zeros(1, dtype=mx.float32)])
            quantized = mx.concatenate([quantized, mx.zeros(1, dtype=mx.int8)])
        else:
            padded = tensor_f32

        # Pack
        evens = quantized[::2]
        odds = quantized[1::2]
        packed = (evens & 0x0F) | ((odds & 0x0F) << 4)

        # Store original shape for unpacking
        setattr(packed, "orig_shape", tensor.shape)

    # Store scale as an attribute
    setattr(packed, "scale", scale.astype(mx.float32))
    setattr(packed, "is_4bit", True)

    return packed


def dequantize_weights(weights: Dict[str, mx.array]) -> Dict[str, mx.array]:
    """
    Dequantize MLX weights back to floating point.

    Args:
        weights: Dictionary of quantized weight tensors

    Returns:
        Dictionary of dequantized weight tensors
    """
    dequantized_weights = {}

    for name, weight in weights.items():
        # Check if tensor is quantized
        if hasattr(weight, "scale"):
            # Check if 4-bit or 8-bit
            if hasattr(weight, "is_4bit") and weight.is_4bit:
                # Dequantize 4-bit
                dequantized_weights[name] = dequantize_int4(weight)
            else:
                # Dequantize 8-bit
                dequantized_weights[name] = dequantize_int8(weight)
        else:
            # Not quantized, keep as is
            dequantized_weights[name] = weight

    return dequantized_weights


def dequantize_int8(tensor: mx.array) -> mx.array:
    """
    Dequantize an int8 tensor.

    Args:
        tensor: Quantized tensor

    Returns:
        Dequantized tensor
    """
    if not hasattr(tensor, "scale"):
        return tensor

    # Dequantize
    dequantized = tensor.astype(mx.float32) / tensor.scale

    return dequantized.astype(mx.float16)


def dequantize_int4(tensor: mx.array) -> mx.array:
    """
    Dequantize an int4 tensor (packed as int8).

    Args:
        tensor: Quantized tensor

    Returns:
        Dequantized tensor
    """
    if not hasattr(tensor, "scale") or not hasattr(tensor, "orig_shape"):
        return tensor

    # Unpack
    lower = tensor & 0x0F
    upper = (tensor & 0xF0) >> 4

    # Sign extend from 4 bits to 8 bits
    lower = ((lower ^ 0x8) - 0x8).astype(mx.int8)
    upper = ((upper ^ 0x8) - 0x8).astype(mx.int8)

    # Interleave
    orig_shape = tensor.orig_shape

    if len(orig_shape) > 1:
        # For matrices
        unpacked = mx.zeros((tensor.shape[0] * 2, tensor.shape[1]), dtype=mx.int8)
        unpacked[::2] = lower
        unpacked[1::2] = upper

        # Reshape to original shape
        unpacked = unpacked[: orig_shape[0]].reshape(orig_shape)
    else:
        # For vectors
        unpacked = mx.zeros(tensor.shape[0] * 2, dtype=mx.int8)
        unpacked[::2] = lower
        unpacked[1::2] = upper

        # Trim to original shape
        unpacked = unpacked[: orig_shape[0]]

    # Dequantize
    dequantized = unpacked.astype(mx.float32) / tensor.scale

    return dequantized.astype(mx.float16)
