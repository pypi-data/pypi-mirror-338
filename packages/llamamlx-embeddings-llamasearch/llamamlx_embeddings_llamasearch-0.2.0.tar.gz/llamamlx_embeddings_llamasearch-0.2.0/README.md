# llamamlx-embeddings

<p align="center">
  <img src="https://raw.githubusercontent.com/yourusername/llamamlx-embeddings/main/docs/assets/logo.png" alt="llamamlx-embeddings Logo" width="200" />
</p>

<p align="center">
<a href="https://github.com/yourusername/llamamlx-embeddings/actions/workflows/tests.yml">
    <img src="https://github.com/yourusername/llamamlx-embeddings/actions/workflows/tests.yml/badge.svg" alt="Tests">
</a>
<a href="https://pypi.org/project/llamamlx-embeddings/">
    <img src="https://img.shields.io/pypi/v/llamamlx-embeddings.svg" alt="PyPI">
</a>
<a href="https://pypi.org/project/llamamlx-embeddings/">
    <img src="https://img.shields.io/pypi/pyversions/llamamlx-embeddings.svg" alt="Python Versions">
</a>
<a href="https://github.com/yourusername/llamamlx-embeddings/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/yourusername/llamamlx-embeddings.svg" alt="License">
</a>
<a href="https://codecov.io/gh/yourusername/llamamlx-embeddings">
    <img src="https://codecov.io/gh/yourusername/llamamlx-embeddings/branch/main/graph/badge.svg" alt="codecov">
</a>
</p>

<p align="center">
  <b>High-performance embeddings with Apple MLX 🚀</b><br>
  <small>Version 0.2.0</small>
</p>

## Overview

llamamlx-embeddings is a Python library that provides high-performance text embeddings using Apple's MLX framework, optimized for Apple Silicon. It offers a unified interface for generating embeddings with various models, efficient batch processing, quantization options, seamless integration with vector databases, and easy deployment as a FastAPI service.

## Project Structure

This package follows a standardized structure for ease of use and maintainability:

```
llamamlx-embeddings/
├── src/                      # Source code directory
│   └── llamamlx_embeddings/  # Main package
│       ├── api/              # API interfaces and handlers
│       ├── benchmarks/       # Benchmarking tools
│       ├── core/             # Core functionality
│       ├── conversion/       # Model conversion utilities
│       ├── integrations/     # Vector DB integrations
│       ├── processing/       # Text processing utilities
│       ├── quantization/     # Model quantization tools
│       ├── utils/            # Common utility functions
│       ├── visualization/    # Visualization utilities
│       ├── __init__.py       # Package initialization
│       ├── cli.py            # Command-line interface
│       ├── client.py         # API client
│       ├── logging.py        # Logging configuration
│       └── version.py        # Version information
├── tests/                    # Test directory
├── docs/                     # Documentation
├── examples/                 # Example scripts
├── benchmarks/               # Benchmark results
├── setup.py                  # Package setup script
├── pyproject.toml            # Project configuration
├── MANIFEST.in               # Package manifest
├── README.md                 # Project README
└── LICENSE                   # License information
```

## What's New in v0.2.0

- Fixed import and dependency issues
- Improved package structure and organization
- Added support for the renamed Pinecone package
- Enhanced GitHub Actions workflows for testing and publishing 
- Updated build system with modern Python packaging tools
- Added comprehensive test suite
- Improved documentation

## ✨ Features

- 🚀 **MLX Optimizations**: Leverages Apple Silicon's full potential 
- 🧩 **Multiple Model Types**: Dense, sparse, and late interaction models
- 💻 **Cross-Platform**: ONNX fallback for non-Apple hardware
- 🔍 **Vector DB Integration**: Easy integration with Qdrant and Pinecone
- 🌐 **FastAPI Server**: Ready-to-use REST API
- 📦 **Batch Processing**: Efficient handling of large datasets
- 🔧 **Quantization**: Reduce memory footprint and improve speed

## 📊 Benchmarks

On Apple M2 Pro, using batch size 32:

| Model                          | Texts/sec | Dim | Type            |
|--------------------------------|-----------|-----|-----------------|
| BAAI/bge-small-en-v1.5         | ~245      | 384 | Dense           |
| sentence-transformers/all-MiniLM-L6-v2 | ~285 | 384 | Dense       |
| intfloat/e5-small-v2           | ~230      | 384 | Dense           |
| prithivida/Splade_PP_en_v1     | ~80       | var | Sparse          |

*With INT8 quantization, throughput improves by ~30% and model size reduces by ~69%*

## 🛠️ Installation

### From PyPI

```bash
# Basic installation
pip install llamamlx-embeddings

# With vector database integrations
pip install llamamlx-embeddings[qdrant,pinecone]

# Full installation with all features
pip install llamamlx-embeddings[all]
```

### From source

```bash
git clone https://github.com/yourusername/llamamlx-embeddings.git
cd llamamlx-embeddings
pip install -e .
```

## 🚀 Quickstart

### Basic Usage

```python
from llamamlx_embeddings import TextEmbedding
import numpy as np

# Create an embedding model (will download if needed)
model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

# Generate embeddings
query = "How to make a delicious pizza?"
query_embedding = model.embed_query(query)

documents = [
    "Pizza is a dish of Italian origin consisting of a usually round, flat base of leavened wheat-based dough.",
    "To make pizza, you need flour, water, yeast, salt, olive oil, tomato sauce, and cheese."
]
doc_embeddings = model.embed_documents(documents)

# Calculate similarities
for i, doc_emb in enumerate(doc_embeddings):
    similarity = np.dot(query_embedding, doc_emb) / (np.linalg.norm(query_embedding) * np.linalg.norm(doc_emb))
    print(f"Document {i+1} similarity: {similarity:.4f}")
```

### Mock Embeddings for Testing

```python
from llamamlx_embeddings import MockEmbedding

# Create a mock embedding model
model = MockEmbedding(dimensions=384)

# Use it like a regular embedding model
query_embedding = model.embed_query("How to make pizza?")
document_embeddings = model.embed_documents(["Document 1", "Document 2"])

# Perfect for testing applications without downloading large models
```

### API Server

Start the server:

```bash
llamamlx-embeddings serve --host 0.0.0.0 --port 8000
```

Use the client:

```python
from llamamlx_embeddings import LlamamlxEmbeddingsClient

# Create a client
client = LlamamlxEmbeddingsClient(base_url="http://localhost:8000")

# Generate embeddings
query = "How to make a delicious pizza?"
query_embedding = client.get_embeddings(query, is_query=True)[0]

documents = [
    "Pizza is a dish of Italian origin consisting of a usually round, flat base of leavened wheat-based dough.",
    "To make pizza, you need flour, water, yeast, salt, olive oil, tomato sauce, and cheese."
]
doc_embeddings = client.get_embeddings(documents)
```

## 📚 Documentation

For comprehensive documentation, visit our [documentation site](https://github.com/yourusername/llamamlx-embeddings/tree/main/docs).

- [Installation Guide](docs/installation.md)
- [Quickstart Guide](docs/quickstart.md)
- [API Reference](docs/api_reference.md)
- [Examples](docs/examples.md)
- [Benchmarks](docs/benchmarks.md)
- [Contributing Guide](docs/contributing.md)

## 🧩 Supported Models

- **Dense models**:
  - BAAI/bge-small-en-v1.5 (default)
  - intfloat/e5-small-v2
  - sentence-transformers/all-MiniLM-L6-v2
  - and more...

- **Sparse models**:
  - prithivida/Splade_PP_en_v1

- **Late interaction models**:
  - colbert-ir/colbertv2.0

- **Cross-encoder models**:
  - Xenova/ms-marco-MiniLM-L-6-v2

## 🔍 Vector Database Integration

### Qdrant

```python
from llamamlx_embeddings import TextEmbedding, QdrantClient

# Create embedding model
model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

# Initialize Qdrant client
vector_db = QdrantClient(
    url="https://your-qdrant-instance.com",
    collection_name="my_collection",
    embedding_model=model
)

# Add documents
vector_db.add(
    documents=["Document 1 text", "Document 2 text"],
    metadata=[{"source": "file1.txt"}, {"source": "file2.txt"}]
)

# Search with query
results = vector_db.query("My search query", limit=5)
```

## 🔧 Advanced Usage

### Quantization

```python
from llamamlx_embeddings import TextEmbedding

# Load a quantized model
model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5", quantize=True)

# Query and document embeddings work the same way
query_embedding = model.embed_query("How to make pizza?")
```

### Custom Models

```python
from llamamlx_embeddings import add_custom_model, TextEmbedding

# Add a custom model
add_custom_model(
    model_name="my-custom-model",
    model_path="/path/to/model/files",
    model_type="dense",
    dimensions=768,
    description="My custom embedding model"
)

# Use the custom model
model = TextEmbedding(model_name="my-custom-model")
```

## 🤝 Contributing

Contributions are welcome! Please check out our [contributing guide](docs/contributing.md) to get started.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [MLX](https://github.com/ml-explore/mlx) by Apple
- [Transformers](https://github.com/huggingface/transformers) by Hugging Face 