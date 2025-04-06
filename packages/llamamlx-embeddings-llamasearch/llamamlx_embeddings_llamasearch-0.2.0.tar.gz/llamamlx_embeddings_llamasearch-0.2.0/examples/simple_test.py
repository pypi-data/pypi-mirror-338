#!/usr/bin/env python
"""
Simple test script for llamamlx-embeddings.
This version avoids loading actual models but tests the code structure.
"""

import logging
import sys
import os

# Add parent directory to path to run examples standalone
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from llamamlx_embeddings.core.models import list_supported_models
from llamamlx_embeddings import configure_logging

# Configure logging
configure_logging(level="INFO")
logger = logging.getLogger(__name__)


def main():
    """Run a simple test of the embedding functionality."""
    print("Running simple test for llamamlx-embeddings package...")
    
    # List available models
    models = list_supported_models()
    print("\nAvailable models by type:")
    
    for model_type, model_list in models.items():
        print(f"- {model_type.upper()}: {len(model_list)} models")
        for model in model_list[:3]:  # Show first 3 models of each type
            print(f"  - {model}")
    
    # Test the basic structures
    print("\nTesting the package structure...")
    
    print("Testing the integration structure...")
    from llamamlx_embeddings.integrations.base import VectorDBClient
    
    print("Testing the sparse embedding structure...")
    from llamamlx_embeddings.core.sparse import SparseEmbedding
    
    print("\nBasic structure test PASSED!")
    print("llamamlx-embeddings package is properly installed and importable.")


if __name__ == "__main__":
    main() 