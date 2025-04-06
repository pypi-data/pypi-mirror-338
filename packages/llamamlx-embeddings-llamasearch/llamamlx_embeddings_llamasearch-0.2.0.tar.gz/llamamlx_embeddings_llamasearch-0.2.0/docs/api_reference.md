# API Reference

This document provides detailed information about the core classes and functions available in the `llamamlx-embeddings` library.

## Core Embedding Models

### TextEmbedding

```python
from llamamlx_embeddings import TextEmbedding

model = TextEmbedding(
    model_name="BAAI/bge-small-en-v1.5",  # Model identifier
    normalize=True,                        # Whether to normalize embeddings
    cache_dir=None,                        # Custom cache directory
    quantize=False                         # Whether to use quantization
)
```

#### Methods

- **`embed(inputs, batch_size=32, **kwargs)`**  
  Generate embeddings for inputs in batches, returning a generator of embedding batches.
  
- **`embed_query(query, **kwargs)`**  
  Generate an embedding for a single query text, optimized for query embedding.
  
- **`embed_documents(documents, **kwargs)`**  
  Generate embeddings for multiple documents, optimized for document embedding.

### SparseTextEmbedding

```python
from llamamlx_embeddings import SparseTextEmbedding

model = SparseTextEmbedding(
    model_name="prithivida/Splade_PP_en_v1",  # Model identifier
    normalize=True,                          # Whether to normalize embeddings
    cache_dir=None                           # Custom cache directory
)
```

#### Methods

- **`embed(inputs, batch_size=2, **kwargs)`**  
  Generate sparse embeddings for inputs in batches.
  
- **`embed_query(query, **kwargs)`**  
  Generate a sparse embedding for a single query text.
  
- **`embed_documents(documents, **kwargs)`**  
  Generate sparse embeddings for multiple documents.

### MockEmbedding

```python
from llamamlx_embeddings import MockEmbedding

model = MockEmbedding(
    dimensions=384,               # Embedding dimension
    model_id="mock-embedding",    # Custom model identifier
    seed=42                       # Random seed for deterministic embeddings
)
```

#### Methods

- **`encode(texts, **kwargs)`**  
  Generate mock embeddings for one or more texts.
  
- **`encode_query(query, **kwargs)`**  
  Generate a mock embedding for a query.
  
- **`encode_documents(documents, **kwargs)`**  
  Generate mock embeddings for documents.
  
- **`rerank(query, documents, **kwargs)`**  
  Generate mock relevance scores for reranking.

## Model Management

### Supported Models

```python
from llamamlx_embeddings import list_supported_models

# Get a list of all supported models
models = list_supported_models()
```

### Custom Models

```python
from llamamlx_embeddings import add_custom_model

# Register a custom model
add_custom_model(
    model_name="my-custom-model",
    model_path="/path/to/model/files",
    model_type="dense",
    dimensions=768,
    description="My custom embedding model"
)
```

## Text Processing

### Preprocessing

```python
from llamamlx_embeddings import preprocess_text

# Preprocess text
processed_text = preprocess_text(
    text="Your raw text here",
    lowercase=True,
    strip_new_lines=True,
    strip_extra_spaces=True,
    remove_urls=False,
    remove_html=False
)
```

### Chunking

```python
from llamamlx_embeddings import chunk_text

# Split text into chunks
chunks = chunk_text(
    text="Your long document text here...",
    chunk_size=1000,
    chunk_overlap=200,
    separator=" "
)

# Split text by delimiter
from llamamlx_embeddings import chunk_text_by_delimiter

chunks = chunk_text_by_delimiter(
    text="Your document with paragraphs...",
    delimiter="\n\n",
    chunk_size=1000,
    chunk_overlap=0
)
```

## Model Conversion and Quantization

### Converting Models

```python
from llamamlx_embeddings import convert_model

# Convert a Hugging Face model to MLX format
converted_path = convert_model(
    model_id="BAAI/bge-small-en-v1.5",
    output_dir="./models",
    revision=None,
    dtype="float16",
    cache_dir=None,
    overwrite=False
)
```

### Quantizing Models

```python
from llamamlx_embeddings import quantize_model

# Quantize a model to reduce size and improve performance
quantized_path = quantize_model(
    model_dir="./models/bge-small-en-v1.5",
    output_dir="./models/quantized",
    method="int8",
    overwrite=False
)
```

## API Client

```python
from llamamlx_embeddings import LlamamlxEmbeddingsClient

# Create a client
client = LlamamlxEmbeddingsClient(
    base_url="http://localhost:8000",
    timeout=30,
    default_model="BAAI/bge-small-en-v1.5"
)

# Generate embeddings
embeddings = client.get_embeddings(
    texts=["Text 1", "Text 2"],
    model_name="BAAI/bge-small-en-v1.5",
    is_query=False
)

# Rerank documents
scores = client.rerank(
    query="Search query",
    documents=["Doc 1", "Doc 2", "Doc 3"],
    model_name="Xenova/ms-marco-MiniLM-L-6-v2"
)

# List available models
models = client.list_models()
```

## Vector Database Integrations

### Qdrant

```python
from llamamlx_embeddings import TextEmbedding
from llamamlx_embeddings.integrations.qdrant import QdrantClient

# Initialize Qdrant client with embedding model
vector_db = QdrantClient(
    url="http://localhost:6333",
    collection_name="documents",
    embedding_model=TextEmbedding(),
    api_key=None
)

# Add documents
vector_db.add(
    documents=["Doc 1", "Doc 2"],
    metadata=[{"source": "file1"}, {"source": "file2"}],
    ids=["id1", "id2"],
    batch_size=32
)

# Query documents
results = vector_db.query(
    query_text="Search query",
    limit=10,
    filters={"source": "file1"}
)
```

### Pinecone

```python
from llamamlx_embeddings import TextEmbedding
from llamamlx_embeddings.integrations.pinecone import PineconeClient

# Initialize Pinecone client with embedding model
vector_db = PineconeClient(
    api_key="your-api-key",
    environment="us-west1-gcp",
    index_name="documents",
    embedding_model=TextEmbedding(),
    namespace=""
)

# Add documents
vector_db.add(
    documents=["Doc 1", "Doc 2"],
    metadata=[{"source": "file1"}, {"source": "file2"}],
    ids=["id1", "id2"],
    batch_size=32
)

# Query documents
results = vector_db.query(
    query_text="Search query",
    limit=10,
    filters={"source": {"$eq": "file1"}}
)
``` 