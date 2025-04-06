#!/usr/bin/env python
"""
Example of text chunking for processing longer documents with llamamlx-embeddings.
"""

import logging
import re
from typing import List, Dict, Tuple, Any
import sys
import os

# Add parent directory to path to run examples standalone
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import from llamamlx_embeddings
from llamamlx_embeddings.core.mock_embeddings import MockEmbedding
from llamamlx_embeddings.processing.text import chunk_text, preprocess_text

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def get_sample_text() -> str:
    """
    Return a sample long text for chunking demonstration.
    """
    return """
    # Introduction to Embeddings and Semantic Search
    
    ## What are Embeddings?
    
    Embeddings are dense vector representations of data, such as text, images, or audio. In the context of natural language processing (NLP), embeddings map words, phrases, or entire documents to vectors of real numbers in a high-dimensional space. These vectors capture semantic relationships, allowing similar concepts to have similar vector representations.
    
    The key idea behind embeddings is that the geometric relationships between vectors correspond to semantic relationships between the entities they represent. For example, in a well-trained embedding space, the vector for "king" minus "man" plus "woman" might be close to the vector for "queen". This property makes embeddings powerful tools for various NLP tasks.
    
    ## How are Embeddings Generated?
    
    Modern embeddings are typically generated using neural networks, especially transformer-based models like BERT, RoBERTa, or MPNet. These models are trained on vast amounts of text data to predict words or tokens based on their context. Through this training, they learn to create vector representations that capture the meaning and relationships between words and phrases.
    
    The dimensionality of embeddings can vary widely, from a few hundred to thousands of dimensions. Higher-dimensional embeddings can capture more nuanced relationships but require more computational resources to generate and store.
    
    ## Applications of Embeddings
    
    Embeddings have numerous applications in natural language processing and beyond:
    
    1. **Semantic Search**: Finding documents or passages that are semantically similar to a query, even if they don't share exact keywords.
    
    2. **Question Answering**: Identifying passages in a corpus that contain answers to specific questions.
    
    3. **Document Classification**: Categorizing documents based on their content and meaning.
    
    4. **Recommendation Systems**: Suggesting similar items or content based on embedding similarity.
    
    5. **Clustering**: Grouping similar documents or passages together.
    
    6. **Anomaly Detection**: Identifying outliers or unusual patterns in data.
    
    ## Semantic Search
    
    Semantic search refers to search techniques that understand the searcher's intent and the contextual meaning of terms to improve search accuracy. Unlike traditional keyword-based search, which matches exact words or phrases, semantic search can find relevant results even when they use different terminology.
    
    ### How Semantic Search Works
    
    The basic process for semantic search using embeddings involves these steps:
    
    1. **Document Processing**: Split documents into manageable chunks and generate embeddings for each chunk.
    
    2. **Query Processing**: Generate an embedding for the search query.
    
    3. **Similarity Computation**: Calculate the similarity between the query embedding and all document embeddings, typically using cosine similarity.
    
    4. **Ranking**: Sort the documents based on their similarity scores and return the most relevant ones.
    
    ### Advantages of Semantic Search
    
    Semantic search offers several advantages over traditional keyword-based search:
    
    - **Understanding Context**: It can understand the context and meaning behind queries rather than just matching keywords.
    
    - **Handling Synonyms**: It can find relevant documents even if they use synonyms or related terms instead of the exact query terms.
    
    - **Multilingual Support**: With multilingual embedding models, semantic search can work across different languages.
    
    - **Improved Relevance**: By understanding the meaning of queries and documents, it can provide more relevant results.
    
    ### Challenges in Semantic Search
    
    Despite its advantages, semantic search also faces several challenges:
    
    - **Computational Cost**: Generating and comparing embeddings requires more computational resources than keyword matching.
    
    - **Vector Database Requirements**: Efficient semantic search requires specialized vector databases or indices.
    
    - **Quality Dependence on Embedding Models**: The quality of search results depends heavily on the quality of the embedding model used.
    
    ## Conclusion
    
    Embeddings and semantic search represent a significant advancement in how we process and retrieve information. By capturing the meaning and relationships between words and documents, they enable more intelligent and context-aware search capabilities. As embedding models continue to improve and become more efficient, we can expect semantic search to become even more powerful and widespread in various applications.
    """


def embed_chunks(
    chunks: List[str],
    model: MockEmbedding
) -> Dict[str, Any]:
    """
    Embed text chunks and return chunk info with embeddings.
    
    Args:
        chunks: List of text chunks
        model: Embedding model
        
    Returns:
        Dictionary with chunk info and embeddings
    """
    # Get document embeddings
    logger.info(f"Generating embeddings for {len(chunks)} chunks")
    embeddings = model.encode_documents(chunks)
    
    # Create result object
    result = {
        "num_chunks": len(chunks),
        "embedding_dim": len(embeddings[0]) if embeddings else 0,
        "chunks": [
            {
                "id": i,
                "text": chunk[:100] + "..." if len(chunk) > 100 else chunk,  # Truncate for display
                "length": len(chunk),
                "embedding_norm": float(sum(e*e for e in embeddings[i])**0.5)  # Just for demonstration
            }
            for i, chunk in enumerate(chunks)
        ]
    }
    
    return result


def main():
    print("\n" + "="*80)
    print("Text Chunking Example using llamamlx-embeddings")
    print("="*80)
    
    # Get sample text
    sample_text = get_sample_text()
    print(f"\nSample text length: {len(sample_text)} characters")
    
    # Initialize mock embedding model
    model = MockEmbedding(embedding_size=384, model_id="mock-model")
    
    # Preprocess text
    logger.info("Preprocessing text")
    processed_text = preprocess_text(sample_text)
    print(f"Processed text length: {len(processed_text)} characters")
    
    # Create chunks with different configurations
    print("\nChunking with different configurations:")
    
    chunk_configs = [
        {"chunk_size": 200, "chunk_overlap": 0},
        {"chunk_size": 200, "chunk_overlap": 50},
        {"chunk_size": 500, "chunk_overlap": 100},
    ]
    
    for config in chunk_configs:
        chunk_size = config["chunk_size"]
        chunk_overlap = config["chunk_overlap"]
        
        print(f"\n{'-'*40}")
        print(f"Configuration: chunk_size={chunk_size}, chunk_overlap={chunk_overlap}")
        
        # Chunk text
        logger.info(f"Chunking text with size={chunk_size}, overlap={chunk_overlap}")
        chunks = chunk_text(processed_text, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        
        print(f"Number of chunks: {len(chunks)}")
        print(f"Average chunk length: {sum(len(c) for c in chunks)/len(chunks):.1f} characters")
        
        # Embed chunks
        chunk_info = embed_chunks(chunks, model)
        
        # Display first 3 chunks with their info
        print("\nFirst 3 chunks:")
        for i, chunk_data in enumerate(chunk_info["chunks"][:3]):
            print(f"Chunk {i+1}:")
            print(f"  Length: {chunk_data['length']} characters")
            print(f"  Embedding norm: {chunk_data['embedding_norm']:.4f}")
            print(f"  Preview: {chunk_data['text']}")
    
    print("\nNote: In a real application, these chunks would be stored along with their")
    print("embeddings in a vector database for efficient semantic search.")


if __name__ == "__main__":
    main() 