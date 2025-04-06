# llamamlx-embeddings Examples

This directory contains example scripts demonstrating how to use the llamamlx-embeddings package for various tasks.

## Running Examples

All examples can be run directly from this directory, as they automatically add the parent directory to the Python path.

For instance:

```bash
python basic_embedding.py
```

or if you made them executable:

```bash
./basic_embedding.py
```

## Examples Overview

### Basic Usage
- **simple_test.py**: A minimal script for verifying that the package works correctly.
- **basic_embedding.py**: Demonstrates basic dense embedding functionality, including document similarity and relevance scoring.
- **basic_usage.py**: Comprehensive example showing various features of the library.

### Embedding Types
- **sparse_embedding.py**: Shows how to use sparse embeddings, including exploring non-zero elements and similarity calculation.
  
### Search and Similarity
- **semantic_search.py**: Demonstrates how to perform semantic search on a collection of documents.
- **semantic_search_mock.py**: Same as semantic_search but using mock embeddings for testing.
- **document_similarity.py**: Shows how to compute and visualize pairwise similarity between documents.

### Text Processing
- **text_chunking.py**: Demonstrates text preprocessing and chunking functionality for handling longer documents.

### Performance and Optimization
- **model_benchmarking.py**: Benchmarks embedding models with different configurations and batch sizes.
- **convert_and_quantize.py**: Shows how to convert models from Hugging Face format to MLX format and quantize them.

## Mock Models

Most examples use mock embedding models for demonstration purposes, which means:

1. They run without needing to download any actual models from Hugging Face.
2. They work quickly even without MLX hardware acceleration.
3. The embeddings are deterministic based on text hashes but don't represent real semantic meaning.

For real applications, replace the mock model with a real model ID, e.g.:

```python
# Instead of:
model = MockEmbedding(embedding_size=384)

# Use:
model = TextEmbedding("BAAI/bge-small-en-v1.5")
```

## API Examples

To demonstrate the FastAPI server functionality, see the documentation for running the API server:

```bash
# Start the API server (from the project root)
python -m llamamlx_embeddings.api
```

Then you can interact with it using the client or curl commands:

```python
from llamamlx_embeddings import LlamamlxEmbeddingsClient

client = LlamamlxEmbeddingsClient("http://localhost:8000")
embeddings = client.embed_documents(["Your text here"])
```

## Additional Resources

For more detailed documentation on the `llamamlx-embeddings` library, refer to the main project README and documentation. 