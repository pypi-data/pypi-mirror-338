"""
Utility functions for llamamlx-embeddings.

This package contains various utilities used by the library.
"""

from .error_handling import (
    configure_logging,
    check_dependency,
    require_dependency,
    safe_import,
    with_fallback,
    handle_fatal_error,
    DependencyError,
    ModelNotFoundError,
)

__all__ = [
    "configure_logging",
    "check_dependency",
    "require_dependency",
    "safe_import",
    "with_fallback",
    "handle_fatal_error",
    "DependencyError",
    "ModelNotFoundError",
] 