"""
Setup script for llamamlx-embeddings.
"""

import os
from setuptools import setup, find_packages

# Read the content of README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read version from version.py
with open(os.path.join("src", "llamamlx_embeddings", "version.py"), "r") as f:
    exec(f.read())

setup(
    name="llamamlx-embeddings-llamasearch",
    version=locals()["__version__"],
    author="LlamaSearch AI",
    author_email="nikjois@llamasearch.ai",
    description="Fast and efficient text embeddings using MLX on Apple Silicon",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://llamasearch.ai",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/llamamlx-embeddings/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "mlx>=0.2.0",
        "numpy>=1.20.0",
        "transformers>=4.30.0",
        "huggingface-hub>=0.15.0",
        "torch>=2.0.0",
        "fastapi>=0.100.0",
        "uvicorn>=0.22.0",
        "pydantic>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "mypy>=1.0.0",
            "flake8>=6.0.0",
        ],
        "onnx": [
            "onnxruntime>=1.15.0",
        ],
        "pinecone": [
            "pinecone>=3.0.0",
        ],
        "qdrant": [
            "qdrant-client>=1.5.0",
        ],
        "visualization": [
            "matplotlib>=3.6.0",
            "seaborn>=0.12.0",
            "scikit-learn>=1.2.0",
        ],
        "docs": [
            "sphinx>=6.0.0",
            "sphinx-rtd-theme>=1.2.0",
            "myst-parser>=2.0.0",
        ],
        "all": [
            "onnxruntime>=1.15.0",
            "pinecone>=3.0.0",
            "qdrant-client>=1.5.0",
            "matplotlib>=3.6.0",
            "seaborn>=0.12.0",
            "scikit-learn>=1.2.0",
            "nltk>=3.8.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "llamamlx-embeddings=llamamlx_embeddings.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)