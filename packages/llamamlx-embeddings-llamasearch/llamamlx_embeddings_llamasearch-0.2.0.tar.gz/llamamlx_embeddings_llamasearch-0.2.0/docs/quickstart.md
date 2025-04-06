# Quickstart Guide

This guide will help you get started with `llamamlx-embeddings` quickly. We'll cover basic usage for generating and working with embeddings.

## Basic Usage

### Generating Embeddings

```python
from llamamlx_embeddings import TextEmbedding
import numpy as np

# Create an embedding model (this will download the model if needed)
model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

# Generate an embedding for a single query
query = "How do neural networks work?"
query_embedding = model.embed_query(query)
print(f"Query embedding shape: {len(query_embedding)}")

# Generate embeddings for multiple documents
documents = [
    "Neural networks are computing systems vaguely inspired by the biological neural networks that constitute animal brains.",
    "The human brain contains approximately 86 billion neurons connected by trillions of synapses.",
    "Machine learning is a subset of artificial intelligence focused on developing systems that learn from data."
]

document_embeddings = model.embed_documents(documents)
print(f"Generated {len(document_embeddings)} document embeddings")
```

### Computing Similarities

```python
# Calculate cosine similarity between query and documents
for i, doc_emb in enumerate(document_embeddings):
    # Cosine similarity calculation
    similarity = np.dot(query_embedding, doc_emb) / (np.linalg.norm(query_embedding) * np.linalg.norm(doc_emb))
    print(f"Document {i+1} similarity: {similarity:.4f}")
```

## Using Mock Embeddings for Testing

Mock embeddings are useful during development to avoid downloading actual models:

```python
from llamamlx_embeddings import MockEmbedding

# Create a mock embedding model with specified dimensions
model = MockEmbedding(dimensions=384)

# Use like a regular embedding model
query_embedding = model.embed_query("How do neural networks work?")
document_embeddings = model.embed_documents(documents)

# Mock models produce deterministic embeddings based on text content
print(f"Mock embedding dimension: {len(query_embedding)}")
```

## Working with Batches

For large document collections, use batching for better performance:

```python
from llamamlx_embeddings import TextEmbedding

model = TextEmbedding()

# Create a large list of documents
documents = ["Document " + str(i) for i in range(1000)]

# Process in batches (generator that yields batches of embeddings)
batch_size = 32
embeddings = []

for batch in model.embed(documents, batch_size=batch_size):
    embeddings.extend(batch)
    print(f"Processed batch, total embeddings: {len(embeddings)}")
```

## Using the API Server

### Starting the Server

```bash
# Start the server
llamamlx-embeddings serve --host 127.0.0.1 --port 8000
```

### Using the Client

```python
from llamamlx_embeddings import LlamamlxEmbeddingsClient

# Create a client
client = LlamamlxEmbeddingsClient(base_url="http://localhost:8000")

# List available models
models = client.list_models()
print(f"Available models: {len(models)}")

# Generate embeddings
query = "How do neural networks work?"
query_embedding = client.get_embeddings(query, is_query=True)[0]

documents = [
    "Neural networks are computing systems vaguely inspired by the biological neural networks.",
    "The human brain contains approximately 86 billion neurons."
]
doc_embeddings = client.get_embeddings(documents)
```

## Vector Database Integration

### Qdrant Example

```python
from llamamlx_embeddings import TextEmbedding
from llamamlx_embeddings.integrations.qdrant import QdrantClient

# Create embedding model
model = TextEmbedding()

# Initialize Qdrant client
vector_db = QdrantClient(
    url="http://localhost:6333",  # Use your Qdrant instance URL
    collection_name="articles",
    embedding_model=model
)

# Add documents to the vector database
vector_db.add(
    documents=["Document 1 text", "Document 2 text"],
    metadata=[
        {"source": "article1.txt", "author": "John Doe"},
        {"source": "article2.txt", "author": "Jane Smith"}
    ]
)

# Search with a query
results = vector_db.query("Your search query", limit=5)
for res in results:
    print(f"Document: {res['document']}")
    print(f"Similarity: {res['similarity']:.4f}")
    print(f"Metadata: {res['metadata']}")
```

## What's Next?

- Explore the [API Reference](api_reference.md) for detailed documentation
- Check out the [Examples](examples.md) for more usage patterns
- Learn about [Model Conversion and Quantization](models.md) for better performance 