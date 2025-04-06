"""
Test that all imports work correctly.
"""

import sys
import unittest.mock
import pytest


@pytest.fixture
def mock_imports():
    """Mock imports to prevent errors from optional dependencies."""
    # Special case for problematic imports
    pinecone_mock = unittest.mock.MagicMock()
    pinecone_mock.__name__ = "pinecone"
    
    qdrant_mock = unittest.mock.MagicMock()
    qdrant_mock.__name__ = "qdrant_client"
    
    onnx_mock = unittest.mock.MagicMock()
    onnx_mock.__name__ = "onnxruntime"
    
    with unittest.mock.patch.dict(sys.modules, {
        'pinecone': pinecone_mock,
        'qdrant_client': qdrant_mock,
        'onnxruntime': onnx_mock,
    }):
        yield


def test_base_imports(mock_imports):
    """Verify that base imports work correctly."""
    import llamamlx_embeddings
    assert llamamlx_embeddings.__version__ is not None


def test_core_imports():
    """Verify that core module imports work correctly."""
    from llamamlx_embeddings.core import embeddings, models, sparse
    assert hasattr(embeddings, "TextEmbedding")
    assert hasattr(models, "get_model_info")
    assert hasattr(sparse, "SparseEmbedding")


def test_utils_imports():
    """Verify that utility imports work correctly."""
    from llamamlx_embeddings.utils import error_handling
    assert hasattr(error_handling, "configure_logging")
    assert hasattr(error_handling, "safe_import")


def test_integrations_imports_directly():
    """Verify that direct integration imports work correctly without requiring the actual dependencies."""
    # Import individual modules directly to bypass the problematic imports
    from llamamlx_embeddings.integrations import base
    assert hasattr(base, "VectorDBClient")


def test_public_api_exports(mock_imports):
    """Verify that all expected exports are available in the public API."""
    import llamamlx_embeddings
    
    expected_exports = [
        # Core classes
        "TextEmbedding",
        "SparseTextEmbedding",
        "LateInteractionTextEmbedding",
        "BaseEmbedding",
        "Embeddings",
        "MockEmbedding",
        "SparseEmbedding",
        
        # Utility functions
        "configure_logging",
        "get_logger",
        "list_supported_models",
        "get_model_info",
        "sparse_normalize",
        "sparse_dot_product",
        
        # Error classes
        "ModelNotFoundError",
        "DependencyError",
    ]
    
    for export in expected_exports:
        assert hasattr(llamamlx_embeddings, export), f"{export} not found in public API"


def test_safe_import_function():
    """Test the safe_import function directly to ensure it handles errors properly."""
    from llamamlx_embeddings.utils.error_handling import safe_import
    
    # This should return None without raising an error
    nonexistent_module = safe_import("this_module_does_not_exist", placeholder=None)
    assert nonexistent_module is None
    
    # Test with custom placeholder
    placeholder = object()
    result = safe_import("another_nonexistent_module", placeholder=placeholder)
    assert result is placeholder 