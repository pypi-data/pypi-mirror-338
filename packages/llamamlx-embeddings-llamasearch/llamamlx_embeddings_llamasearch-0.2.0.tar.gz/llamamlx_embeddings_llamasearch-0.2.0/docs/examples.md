# Examples

This document provides examples of how to use `llamamlx-embeddings` for common tasks. For full code examples, check the [`examples/`](https://github.com/yourusername/llamamlx-embeddings/tree/main/examples) directory.

## Semantic Search

This example demonstrates how to perform semantic search using embeddings:

```python
from llamamlx_embeddings import TextEmbedding
import numpy as np

# Load the embedding model
model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

# Sample documents
documents = [
    "Neural networks are computing systems vaguely inspired by the biological neural networks that constitute animal brains.",
    "GPT (Generative Pre-trained Transformer) is an autoregressive language model that uses deep learning to produce human-like text.",
    "MLX is a machine learning framework for Apple silicon, designed to leverage the full power of the hardware.",
    "Embeddings are dense vector representations that capture semantic meaning of text or other content types.",
    "Retrieval-augmented generation (RAG) combines retrieval-based methods with text generation for better responses."
]

# Create a query
query = "How do embeddings help with semantic search?"

# Generate embeddings
query_embedding = model.embed_query(query)
document_embeddings = model.embed_documents(documents)

# Calculate similarities
results = []
for i, doc_emb in enumerate(document_embeddings):
    similarity = np.dot(query_embedding, doc_emb) / (np.linalg.norm(query_embedding) * np.linalg.norm(doc_emb))
    results.append({"document": documents[i], "similarity": similarity})

# Sort by similarity (highest first)
results.sort(key=lambda x: x["similarity"], reverse=True)

# Display results
for i, result in enumerate(results):
    print(f"Result {i+1} (Score: {result['similarity']:.4f}):")
    print(result["document"])
    print()
```

## Document Similarity Matrix

This example shows how to create a similarity matrix between documents:

```python
from llamamlx_embeddings import TextEmbedding
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load embedding model
model = TextEmbedding()

# Sample documents
documents = [
    "Apple released the new M3 MacBook Pro",
    "The latest MacBook features the M3 chip from Apple",
    "Google announced their new Pixel phone today",
    "The Pixel is Google's flagship smartphone",
    "Microsoft Surface laptops run Windows 11"
]

# Generate document embeddings
document_embeddings = model.embed_documents(documents)

# Create similarity matrix
similarity_matrix = np.zeros((len(documents), len(documents)))
for i, emb1 in enumerate(document_embeddings):
    for j, emb2 in enumerate(document_embeddings):
        similarity = np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))
        similarity_matrix[i, j] = similarity

# Visualize similarity matrix
plt.figure(figsize=(10, 8))
sns.heatmap(similarity_matrix, annot=True, cmap='viridis', 
            xticklabels=[f"Doc {i+1}" for i in range(len(documents))],
            yticklabels=[f"Doc {i+1}" for i in range(len(documents))])
plt.title('Document Similarity Matrix')
plt.tight_layout()
plt.show()
```

## Text Chunking for Long Documents

This example demonstrates how to process long documents by chunking:

```python
from llamamlx_embeddings import TextEmbedding
from llamamlx_embeddings import chunk_text

# Load the embedding model
model = TextEmbedding()

# Long document text
long_document = """
Machine learning is a branch of artificial intelligence (AI) and computer science which focuses on the use of data and algorithms to imitate the way that humans learn, gradually improving its accuracy.

IBM has a rich history with machine learning. One of its own, Arthur Samuel, is credited for coining the term, "machine learning" with his research (PDF, 481 KB) (link resides outside IBM) around the game of checkers. Robert Nealey, the self-proclaimed checkers master, played the game on an IBM 7094 computer in 1962, and he lost to the computer. Compared to what can be done today, this feat seems trivial, but it's considered a major milestone in the field of artificial intelligence.

Over the coming decades, the technological developments around storage and processing power will enable some innovative products that we know and love today, such as Netflix's recommendation engine or self-driving cars.

Machine learning is an important component of the growing field of data science. Through the use of statistical methods, algorithms are trained to make classifications or predictions, uncovering key insights within data mining projects. These insights subsequently drive decision making within applications and businesses, ideally impacting key growth metrics. As big data continues to expand and grow, the market demand for data scientists will increase, requiring them to assist in the identification of the most relevant business questions and subsequently the data to answer them.
"""

# Split into chunks
chunks = chunk_text(
    text=long_document,
    chunk_size=200,
    chunk_overlap=50,
    separator=" "
)

print(f"Split document into {len(chunks)} chunks")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1} ({len(chunk)} chars):")
    print(chunk[:100] + "...")
    print()

# Generate embeddings for each chunk
chunk_embeddings = model.embed_documents(chunks)
print(f"Generated {len(chunk_embeddings)} embeddings")
```

## Converting and Quantizing Models

This example shows how to convert a Hugging Face model to MLX format and quantize it:

```python
from llamamlx_embeddings import convert_model, quantize_model
import os

# Convert a Hugging Face model to MLX format
model_name = "BAAI/bge-small-en-v1.5"
output_dir = "./models"

print(f"Converting {model_name} to MLX format...")
mlx_model_path = convert_model(
    model_id=model_name,
    output_dir=output_dir,
    dtype="float16",
    overwrite=False
)

print(f"Model converted successfully to {mlx_model_path}")

# Quantize the converted model to 8-bit precision
print("Quantizing model to 8-bit precision...")
quantized_path = quantize_model(
    model_dir=mlx_model_path,
    output_dir=os.path.join(output_dir, "quantized"),
    method="int8",
    overwrite=False
)

print(f"Model quantized successfully to {quantized_path}")

# Compare file sizes
original_size = sum(os.path.getsize(os.path.join(mlx_model_path, f)) for f in os.listdir(mlx_model_path) if os.path.isfile(os.path.join(mlx_model_path, f)))
quantized_size = sum(os.path.getsize(os.path.join(quantized_path, f)) for f in os.listdir(quantized_path) if os.path.isfile(os.path.join(quantized_path, f)))

print(f"Original model size: {original_size / (1024*1024):.2f} MB")
print(f"Quantized model size: {quantized_size / (1024*1024):.2f} MB")
print(f"Size reduction: {(1 - quantized_size / original_size) * 100:.2f}%")
```

## Benchmarking Model Performance

This example demonstrates how to benchmark models:

```python
from llamamlx_embeddings import TextEmbedding
from llamamlx_embeddings.benchmarks import (
    generate_random_texts,
    time_function,
    save_benchmark_results
)
import json

# Models to benchmark
models = [
    "BAAI/bge-small-en-v1.5",
    "sentence-transformers/all-MiniLM-L6-v2",
    "intfloat/e5-small-v2"
]

# Generate random texts for benchmarking
texts_short = generate_random_texts(count=100, min_length=50, max_length=100)
texts_medium = generate_random_texts(count=100, min_length=200, max_length=300)
texts_long = generate_random_texts(count=100, min_length=500, max_length=1000)

# Batch sizes to test
batch_sizes = [1, 4, 8, 16, 32]

results = {}

for model_name in models:
    print(f"Benchmarking {model_name}...")
    model_results = {}
    
    # Create model
    model = TextEmbedding(model_name=model_name)
    
    # Benchmark different text lengths and batch sizes
    for texts, length_name in [(texts_short, "short"), (texts_medium, "medium"), (texts_long, "long")]:
        length_results = {}
        
        for batch_size in batch_sizes:
            print(f"  Testing batch_size={batch_size} with {length_name} texts...")
            
            # Time the embedding operation
            timing = time_function(
                model.embed_documents,
                texts,
                n_runs=3,
                warmup=1,
                batch_size=batch_size
            )
            
            texts_per_second = len(texts) / timing["avg_time"]
            
            length_results[str(batch_size)] = {
                "avg_time_seconds": timing["avg_time"],
                "throughput_texts_per_second": texts_per_second,
                "throughput_tokens_per_second": texts_per_second * 100,  # Rough estimate
            }
        
        model_results[length_name] = length_results
    
    results[model_name] = model_results

# Save results
save_benchmark_results(results, "benchmark_results.json")
print("Benchmark results saved to benchmark_results.json")

# Display summary
print("\nSummary (texts per second, batch_size=32):")
for model_name in models:
    short_tps = results[model_name]["short"]["32"]["throughput_texts_per_second"]
    medium_tps = results[model_name]["medium"]["32"]["throughput_texts_per_second"]
    long_tps = results[model_name]["long"]["32"]["throughput_texts_per_second"]
    
    print(f"{model_name}:")
    print(f"  - Short texts: {short_tps:.1f}")
    print(f"  - Medium texts: {medium_tps:.1f}")
    print(f"  - Long texts: {long_tps:.1f}")
```

## Visualization of Embeddings

This example demonstrates how to visualize embeddings using dimensionality reduction:

```python
from llamamlx_embeddings import TextEmbedding
from llamamlx_embeddings.visualization import visualize_embeddings_2d
import numpy as np

# Load model
model = TextEmbedding()

# Generate some sample data (tech company descriptions)
companies = [
    "Apple designs and produces consumer electronics, computer software, and online services.",
    "Microsoft is a technology company known for Windows OS and Office software suite.",
    "Google is a technology company specializing in Internet-related services and products.",
    "Amazon is an e-commerce company focused on online retail, cloud computing, and AI.",
    "Facebook (Meta) is a social media conglomerate offering social networking services.",
    "Netflix is a streaming service offering movies, TV shows, and original content.",
    "Tesla develops electric vehicles, battery energy storage, and solar products.",
    "NVIDIA designs graphics processing units for gaming, professional, and AI markets.",
    "Intel is a technology company that produces semiconductor chips and processors.",
    "AMD creates computer processors and related technologies for consumers and businesses."
]

categories = [
    "Hardware", "Software", "Internet", "E-commerce", "Social Media", 
    "Entertainment", "Automotive", "Hardware", "Hardware", "Hardware"
]

# Generate embeddings
embeddings = model.embed_documents(companies)

# Convert to numpy arrays for visualization
embeddings_np = np.array(embeddings)

# Visualize embeddings with t-SNE
visualize_embeddings_2d(
    embeddings=embeddings_np,
    labels=categories,
    method="tsne",
    title="Tech Company Embeddings (t-SNE)",
    figsize=(12, 10),
    save_path="embeddings_tsne.png"
)

# Visualize embeddings with PCA
visualize_embeddings_2d(
    embeddings=embeddings_np,
    labels=categories,
    method="pca",
    title="Tech Company Embeddings (PCA)",
    figsize=(12, 10),
    save_path="embeddings_pca.png"
)
```

## Using Vector Database Integrations

### Qdrant Example:

```python
from llamamlx_embeddings import TextEmbedding
from llamamlx_embeddings.integrations.qdrant import QdrantClient

# Sample documents about programming languages
documents = [
    "Python is a high-level, general-purpose programming language known for its readability.",
    "JavaScript is a programming language that is one of the core technologies of the World Wide Web.",
    "Java is a high-level, class-based, object-oriented programming language.",
    "C++ is a general-purpose programming language created as an extension of the C programming language.",
    "Rust is a multi-paradigm, high-level, general-purpose programming language focused on safety and performance.",
    "Go is a statically typed, compiled programming language designed at Google.",
    "Swift is a general-purpose, multi-paradigm, compiled programming language developed by Apple.",
    "Ruby is an interpreted, high-level, general-purpose programming language."
]

metadata = [
    {"language": "Python", "paradigm": "multi-paradigm", "typing": "dynamic", "year": 1991},
    {"language": "JavaScript", "paradigm": "multi-paradigm", "typing": "dynamic", "year": 1995},
    {"language": "Java", "paradigm": "object-oriented", "typing": "static", "year": 1995},
    {"language": "C++", "paradigm": "multi-paradigm", "typing": "static", "year": 1985},
    {"language": "Rust", "paradigm": "multi-paradigm", "typing": "static", "year": 2010},
    {"language": "Go", "paradigm": "concurrent", "typing": "static", "year": 2009},
    {"language": "Swift", "paradigm": "multi-paradigm", "typing": "static", "year": 2014},
    {"language": "Ruby", "paradigm": "multi-paradigm", "typing": "dynamic", "year": 1995}
]

# Initialize embedding model
model = TextEmbedding()

# Initialize Qdrant client
qdrant = QdrantClient(
    url="http://localhost:6333",  # Replace with your Qdrant instance URL
    collection_name="programming_languages",
    embedding_model=model
)

# Add documents
qdrant.add(documents=documents, metadata=metadata)

# Perform semantic search
results = qdrant.query(
    query_text="Which programming languages have static typing?",
    limit=5
)

# Display results
for i, result in enumerate(results):
    print(f"Result {i+1} (Score: {result['similarity']:.4f}):")
    print(f"Document: {result['document']}")
    print(f"Metadata: {result['metadata']}")
    print()

# Filter by metadata
filtered_results = qdrant.query(
    query_text="Modern programming languages",
    limit=3,
    filters={"year": {"$gte": 2000}}
)

print("\nModern programming languages (after 2000):")
for i, result in enumerate(filtered_results):
    print(f"Result {i+1} (Score: {result['similarity']:.4f}):")
    print(f"Document: {result['document']}")
    print(f"Metadata: {result['metadata']}")
    print()
```

For more examples, visit the [`examples/`](https://github.com/yourusername/llamamlx-embeddings/tree/main/examples) directory. 