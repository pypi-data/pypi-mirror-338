#!/usr/bin/env python
"""
Example of converting and quantizing models with llamamlx-embeddings.
"""

import argparse
import logging
import time
import os
import sys
from typing import List, Dict, Optional, Any

# Add parent directory to path to run examples standalone
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from llamamlx_embeddings.core.models import list_supported_models, get_model_info
from llamamlx_embeddings import configure_logging

# Configure logging
configure_logging(level="INFO")
logger = logging.getLogger(__name__)


# Mock implementations for demo purposes
def convert_model(
    model_id: str,
    output_dir: str,
    revision: str = "main",
    dtype: str = "float16",
    overwrite: bool = False
) -> str:
    """
    Mock implementation of converting a model from Hugging Face to MLX format.
    
    Args:
        model_id: Hugging Face model ID
        output_dir: Directory to save the converted model
        revision: Model revision to use
        dtype: Data type for conversion (float16, float32, bfloat16)
        overwrite: Whether to overwrite existing files
        
    Returns:
        Path to the converted model
    """
    logger.info(f"[MOCK] Converting model {model_id} to MLX format")
    logger.info(f"[MOCK] Using dtype: {dtype}")
    
    # Create output directory
    model_name = model_id.split("/")[-1] if "/" in model_id else model_id
    model_dir = os.path.join(output_dir, model_name)
    
    os.makedirs(model_dir, exist_ok=True)
    
    # Simulate conversion by creating a dummy file
    with open(os.path.join(model_dir, "config.json"), "w") as f:
        f.write('{"model_name": "' + model_id + '", "dtype": "' + dtype + '"}')
        
    # Wait a bit to simulate work
    time.sleep(1)
    
    logger.info(f"[MOCK] Model converted to {model_dir}")
    return model_dir


def quantize_model(
    model_dir: str,
    output_dir: str,
    method: str = "int8",
    overwrite: bool = False
) -> str:
    """
    Mock implementation of quantizing a model.
    
    Args:
        model_dir: Path to the model directory
        output_dir: Directory to save the quantized model
        method: Quantization method (int8, int4)
        overwrite: Whether to overwrite existing files
        
    Returns:
        Path to the quantized model
    """
    logger.info(f"[MOCK] Quantizing model in {model_dir}")
    logger.info(f"[MOCK] Using method: {method}")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Simulate quantization by creating a dummy file
    with open(os.path.join(output_dir, "config.json"), "w") as f:
        f.write('{"model_dir": "' + model_dir + '", "quantization": "' + method + '"}')
        
    # Wait a bit to simulate work
    time.sleep(1)
    
    logger.info(f"[MOCK] Model quantized to {output_dir}")
    return output_dir


def list_quantization_methods() -> Dict[str, str]:
    """
    List available quantization methods.
    
    Returns:
        Dictionary mapping method names to descriptions
    """
    return {
        "int8": "8-bit integer quantization (good balance of quality and size)",
        "int4": "4-bit integer quantization (smallest size, lower quality)",
        "fp16": "16-bit floating point (best quality, largest size)"
    }


def print_model_info(model_id: str):
    """
    Print information about a specific model.
    
    Args:
        model_id: Model identifier
    """
    try:
        # For real implementation, we would use:
        # model_info = get_model_info(model_id)
        
        # Mock implementation for demo purposes
        model_info = {
            "model_type": "dense",
            "embedding_size": 384,
            "description": "Mock model information for " + model_id,
            "recommended_for": "Demonstration purposes",
            "url": "https://huggingface.co/" + model_id
        }
        
        print(f"\nModel Information for {model_id}:")
        print(f"  Model Type: {model_info.get('model_type', 'Unknown')}")
        print(f"  Embedding Size: {model_info.get('embedding_size', 'Unknown')}")
        print(f"  Description: {model_info.get('description', 'No description available')}")
        print(f"  Recommended For: {model_info.get('recommended_for', 'General use')}")
        print(f"  URL: {model_info.get('url', 'No URL available')}")
    except Exception as e:
        logger.error(f"Failed to get model info: {e}")
        print(f"Could not retrieve information for model: {model_id}")


def convert_and_quantize(
    model_id: str,
    output_dir: str = "models",
    revision: str = "main",
    dtype: str = "float16",
    quantization: str = None,
    overwrite: bool = False
) -> Dict[str, Any]:
    """
    Convert a model from Hugging Face to MLX format and optionally quantize it.
    
    Args:
        model_id: Hugging Face model ID
        output_dir: Directory to save the converted model
        revision: Model revision to use
        dtype: Data type for conversion (float16, float32, bfloat16)
        quantization: Quantization method to apply (None, int8, int4)
        overwrite: Whether to overwrite existing files
        
    Returns:
        Dictionary with conversion and quantization results
    """
    results = {
        "model_id": model_id,
        "output_dir": output_dir,
        "model_dir": os.path.join(output_dir, model_id.split("/")[-1]),
        "dtype": dtype,
        "conversion_successful": False,
        "quantization_applied": False,
        "quantized_model_dir": None,
        "conversion_time": 0,
        "quantization_time": 0,
        "error": None
    }
    
    try:
        # Convert model
        logger.info(f"Converting model {model_id} to MLX format...")
        start_time = time.time()
        
        convert_model(
            model_id=model_id,
            output_dir=output_dir,
            revision=revision,
            dtype=dtype,
            overwrite=overwrite
        )
        
        results["conversion_time"] = time.time() - start_time
        results["conversion_successful"] = True
        
        logger.info(f"Model converted successfully in {results['conversion_time']:.2f} seconds")
        
        # Quantize model if requested
        if quantization:
            logger.info(f"Quantizing model using {quantization} method...")
            quantized_dir = f"{results['model_dir']}_{quantization}"
            results["quantized_model_dir"] = quantized_dir
            
            start_time = time.time()
            
            quantize_model(
                model_dir=results["model_dir"],
                output_dir=quantized_dir,
                method=quantization,
                overwrite=overwrite
            )
            
            results["quantization_time"] = time.time() - start_time
            results["quantization_applied"] = True
            
            logger.info(f"Model quantized successfully in {results['quantization_time']:.2f} seconds")
    
    except Exception as e:
        logger.error(f"Error during conversion/quantization: {e}")
        results["error"] = str(e)
    
    return results


def main():
    parser = argparse.ArgumentParser(description="Convert and quantize models using llamamlx-embeddings")
    parser.add_argument("--model-id", type=str, help="Hugging Face model ID to convert")
    parser.add_argument("--output-dir", type=str, default="models", help="Directory to save the converted model")
    parser.add_argument("--revision", type=str, default="main", help="Model revision to use")
    parser.add_argument("--dtype", type=str, default="float16", choices=["float16", "float32", "bfloat16"], 
                        help="Data type for conversion")
    parser.add_argument("--quantization", type=str, default=None, choices=[None, "int8", "int4"], 
                        help="Quantization method to apply")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    parser.add_argument("--list-models", action="store_true", help="List supported models")
    parser.add_argument("--list-quantization", action="store_true", help="List quantization methods")
    parser.add_argument("--info", type=str, help="Show info for specific model ID")
    
    args = parser.parse_args()
    
    print("\n" + "="*80)
    print("Model Conversion and Quantization Example using llamamlx-embeddings")
    print("="*80)
    
    # List supported models
    if args.list_models:
        print("\nSupported Models:")
        models = list_supported_models()
        for model_type, model_list in models.items():
            print(f"  {model_type.upper()}:")
            for model in model_list:
                print(f"    - {model}")
        return
    
    # List quantization methods
    if args.list_quantization:
        print("\nAvailable Quantization Methods:")
        for method, description in list_quantization_methods().items():
            print(f"- {method}: {description}")
        return
    
    # Show model info
    if args.info:
        print_model_info(args.info)
        return
    
    # Check if model ID is provided
    if not args.model_id:
        print("\nPlease provide a model ID using --model-id")
        print("Example: python convert_and_quantize.py --model-id BAAI/bge-small-en-v1.5")
        print("Or run with --list-models to see supported models")
        return
    
    # Convert and quantize model
    print(f"\nConverting model: {args.model_id}")
    print(f"Output directory: {args.output_dir}")
    print(f"Data type: {args.dtype}")
    print(f"Quantization: {args.quantization if args.quantization else 'None'}")
    
    results = convert_and_quantize(
        model_id=args.model_id,
        output_dir=args.output_dir,
        revision=args.revision,
        dtype=args.dtype,
        quantization=args.quantization,
        overwrite=args.overwrite
    )
    
    # Print results
    print("\nConversion Results:")
    print(f"  Model ID: {results['model_id']}")
    print(f"  Conversion successful: {'✓' if results['conversion_successful'] else '✗'}")
    print(f"  Conversion time: {results['conversion_time']:.2f} seconds")
    print(f"  Model directory: {results['model_dir']}")
    
    if args.quantization:
        print(f"  Quantization applied: {'✓' if results['quantization_applied'] else '✗'}")
        print(f"  Quantization time: {results['quantization_time']:.2f} seconds")
        print(f"  Quantized model directory: {results['quantized_model_dir']}")
    
    if results["error"]:
        print(f"\nError: {results['error']}")
    
    # Print next steps
    if results["conversion_successful"]:
        model_path = results["quantized_model_dir"] if results["quantization_applied"] else results["model_dir"]
        print("\nNext steps:")
        print(f"  1. Use the model with: python -m llamamlx_embeddings.cli serve --model-id {model_path}")
        print(f"  2. Or import in your code: from llamamlx_embeddings import TextEmbedding")
        print(f"     model = TextEmbedding('{model_path}')")


if __name__ == "__main__":
    main() 