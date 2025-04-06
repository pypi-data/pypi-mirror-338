"""
Error handling utilities for llamamlx-embeddings.

This module provides standardized error handling and logging utilities
to ensure consistent error reporting and user experience.
"""

import importlib
import logging
import os
import sys
import traceback
from typing import Callable, Optional, Type, TypeVar, Union, Any

# Configure logging
logger = logging.getLogger(__name__)

# Type variable for generic functions
T = TypeVar('T')


class DependencyError(ImportError):
    """
    Error raised when an optional dependency is missing.

    This error provides useful installation instructions to the user.
    """

    def __init__(self, package_name: str, extra_name: Optional[str] = None):
        """
        Initialize with the missing package name and optional extra name.

        Args:
            package_name: The name of the missing package
            extra_name: The name of the corresponding extra in setup.py
        """
        self.package_name = package_name
        self.extra_name = extra_name
        
        message = f"Optional dependency '{package_name}' is not installed."
        
        if extra_name:
            message += f" Install with: pip install llamamlx-embeddings[{extra_name}]"
        else:
            message += f" Install with: pip install {package_name}"
        
        super().__init__(message)


class ModelNotFoundError(Exception):
    """
    Error raised when a model or tokenizer cannot be found.
    """
    
    def __init__(self, model_id: str, details: Optional[str] = None):
        """
        Initialize with the model ID and optional details.

        Args:
            model_id: The ID of the model that couldn't be found
            details: Additional details about the error
        """
        self.model_id = model_id
        message = f"Model '{model_id}' not found."
        
        if details:
            message += f" Details: {details}"
            
        super().__init__(message)


def check_dependency(package_name: str, extra_name: Optional[str] = None) -> bool:
    """
    Check if an optional dependency is installed.

    Args:
        package_name: The name of the package to check
        extra_name: The name of the corresponding extra in setup.py

    Returns:
        True if the package is installed, False otherwise
    """
    try:
        importlib.import_module(package_name)
        return True
    except ImportError:
        return False


def require_dependency(package_name: str, extra_name: Optional[str] = None) -> None:
    """
    Require an optional dependency, raising an informative error if missing.

    Args:
        package_name: The name of the package to require
        extra_name: The name of the corresponding extra in setup.py

    Raises:
        DependencyError: If the package is not installed
    """
    if not check_dependency(package_name):
        raise DependencyError(package_name, extra_name)


def safe_import(
    module_name: str,
    package_name: Optional[str] = None,
    extra_name: Optional[str] = None,
    placeholder: Any = None,
) -> Any:
    """
    Safely import a module, providing a placeholder if the import fails.

    Args:
        module_name: The name of the module to import
        package_name: The name of the package (if different from module)
        extra_name: The name of the corresponding extra in setup.py
        placeholder: A placeholder value to return if the import fails

    Returns:
        The imported module or the placeholder if the import fails
    """
    try:
        # Special case for pinecone which raises an Exception instead of ImportError
        if module_name == "pinecone":
            try:
                return importlib.import_module(module_name)
            except Exception as e:
                if "renamed from `pinecone-client` to `pinecone`" in str(e):
                    logger.warning(
                        "Pinecone SDK found but it's raising the rename warning. "
                        "This might be because both old and new packages are installed. "
                        "Install with: pip install -U pinecone-client==3.0.0"
                    )
                else:
                    logger.warning(f"Error importing {module_name}: {str(e)}")
                return placeholder
        else:
            # Standard case - try to import
            return importlib.import_module(module_name)
    except ImportError:
        pkg = package_name or module_name
        if extra_name:
            logger.warning(
                f"Optional dependency '{pkg}' is not installed. "
                f"Install with: pip install llamamlx-embeddings[{extra_name}]"
            )
        else:
            logger.warning(
                f"Optional dependency '{pkg}' is not installed. "
                f"Install with: pip install {pkg}"
            )
        return placeholder


def with_fallback(
    func: Callable[..., T],
    fallback: Union[T, Callable[..., T]],
    error_types: Union[Type[Exception], tuple] = Exception,
    log_error: bool = True,
) -> Callable[..., T]:
    """
    Decorate a function to use a fallback value if it raises an error.

    Args:
        func: The function to wrap
        fallback: The fallback value or function to call on error
        error_types: The types of exceptions to catch
        log_error: Whether to log the error

    Returns:
        The wrapped function
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except error_types as e:
            if log_error:
                logger.error(f"Error in {func.__name__}: {str(e)}")
            
            if callable(fallback):
                return fallback(*args, **kwargs)
            else:
                return fallback
    
    # Preserve the original function's metadata
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    
    return wrapper


def configure_logging(
    level: str = "INFO",
    to_file: Optional[str] = None,
    format_string: Optional[str] = None,
) -> None:
    """
    Configure logging for the library.

    Args:
        level: The logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        to_file: Optional path to a log file
        format_string: Optional custom format string for log messages
    """
    # Convert string level to logging constant
    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {level}")
    
    # Default format string
    if format_string is None:
        format_string = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Set up handlers
    handlers = [logging.StreamHandler()]
    
    if to_file:
        # Ensure directory exists
        os.makedirs(os.path.dirname(os.path.abspath(to_file)), exist_ok=True)
        handlers.append(logging.FileHandler(to_file))
    
    # Configure root logger
    logging.basicConfig(
        level=numeric_level,
        format=format_string,
        handlers=handlers,
    )
    
    # Set level for library loggers
    library_logger = logging.getLogger("llamamlx_embeddings")
    library_logger.setLevel(numeric_level)


def handle_fatal_error(error: Exception, exit_code: int = 1) -> None:
    """
    Handle a fatal error by logging it and exiting the program.

    Args:
        error: The exception that was raised
        exit_code: The exit code to use
    """
    logger.error(f"Fatal error: {str(error)}")
    logger.debug(f"Traceback: {traceback.format_exc()}")
    sys.exit(exit_code) 