"""
Logging configuration for llamamlx-embeddings.
Provides consistent and configurable logging throughout the library.
"""

import logging
import os
import sys
from typing import Any, Dict, Optional

DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Initialize the package logger
logger = logging.getLogger("llamamlx_embeddings")


def configure_logging(
    level: Optional[int] = None,
    format_string: Optional[str] = None,
    date_format: Optional[str] = None,
    log_file: Optional[str] = None,
    config: Optional[Dict[str, Any]] = None,
) -> None:
    """
    Configure logging for llamamlx-embeddings.

    Args:
        level: Log level (default: INFO)
        format_string: Log format string
        date_format: Date format string for log entries
        log_file: Optional path to a log file
        config: Dictionary with logging configuration, overrides other parameters

    Example:
        >>> from llamamlx_embeddings.logging import configure_logging
        >>> configure_logging(level=logging.DEBUG)
    """
    # Get log level from environment variable if not provided
    if level is None:
        env_level = os.environ.get("LLAMAMLX_LOG_LEVEL", "").upper()
        level = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }.get(env_level, DEFAULT_LOG_LEVEL)

    # Apply config if provided
    if config is not None:
        level = config.get("level", level)
        format_string = config.get("format", format_string)
        date_format = config.get("date_format", date_format)
        log_file = config.get("file", log_file)

    # Set default format if not provided
    if format_string is None:
        format_string = DEFAULT_LOG_FORMAT

    if date_format is None:
        date_format = DEFAULT_DATE_FORMAT

    # Configure the root logger
    logger.setLevel(level)

    # Remove existing handlers to avoid duplicates
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Create formatter
    formatter = logging.Formatter(format_string, date_format)

    # Create and configure console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Create and configure file handler if requested
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    logger.debug(f"Logging configured at level {logging.getLevelName(level)}")


def get_logger(name: str) -> logging.Logger:
    """
    Get a configured logger for a specific module.

    Args:
        name: Name to use for the logger, typically __name__

    Returns:
        Configured logger instance

    Example:
        >>> from llamamlx_embeddings.logging import get_logger
        >>> logger = get_logger(__name__)
        >>> logger.info("This is a log message")
    """
    return logging.getLogger(f"llamamlx_embeddings.{name}")


# Configure default logging when the module is imported
configure_logging()
