"""
Pytest configuration for llamamlx_embeddings tests.
"""

import os
import sys

# Add the parent directory to sys.path to make the package importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 