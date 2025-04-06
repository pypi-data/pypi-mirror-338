"""
Text processing utilities for llamamlx-embeddings.
"""

import logging
import re
from typing import Any, Dict, List, Tuple

import nltk

# Configure logging
logger = logging.getLogger(__name__)


def download_nltk_resources(quiet: bool = True) -> None:
    """
    Download required NLTK resources.

    Args:
        quiet: Whether to suppress download messages
    """
    resources = [
        "punkt",
        "stopwords",
        "wordnet",
    ]

    for resource in resources:
        try:
            nltk.download(resource, quiet=quiet)
        except Exception as e:
            logger.warning(f"Failed to download NLTK resource {resource}: {str(e)}")


# Download NLTK resources when the module is imported
try:
    download_nltk_resources()
except Exception as e:
    logger.warning(f"Failed to download NLTK resources: {str(e)}")


def preprocess_text(
    text: str,
    lowercase: bool = False,
    strip_new_lines: bool = True,
    strip_extra_spaces: bool = True,
    remove_urls: bool = False,
    remove_html: bool = False,
) -> str:
    """
    Preprocess text with various cleaning operations.

    Args:
        text: Input text to preprocess
        lowercase: Whether to convert text to lowercase
        strip_new_lines: Whether to replace newlines with spaces
        strip_extra_spaces: Whether to reduce multiple spaces to single spaces
        remove_urls: Whether to remove URLs from text
        remove_html: Whether to remove HTML tags from text

    Returns:
        Preprocessed text
    """
    if not text:
        return ""

    # Convert to lowercase if requested
    if lowercase:
        text = text.lower()

    # Remove URLs if requested
    if remove_urls:
        text = re.sub(r"https?://\S+|www\.\S+", " ", text)

    # Remove HTML tags if requested
    if remove_html:
        text = re.sub(r"<.*?>", " ", text)

    # Replace newlines with spaces if requested
    if strip_new_lines:
        text = re.sub(r"\n+", " ", text)

    # Reduce multiple spaces to single space if requested
    if strip_extra_spaces:
        text = re.sub(r"\s+", " ", text)
        text = text.strip()

    return text


def batch_preprocess(texts: List[str], **kwargs) -> List[str]:
    """
    Preprocess a batch of texts.

    Args:
        texts: List of input texts
        **kwargs: Arguments for preprocess_text

    Returns:
        List of preprocessed texts
    """
    return [preprocess_text(text, **kwargs) for text in texts]


def chunk_text(
    text: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
    separator: str = " ",
) -> List[str]:
    """
    Split text into overlapping chunks.

    Args:
        text: Input text to split
        chunk_size: Maximum size of each chunk (in characters)
        chunk_overlap: Overlap between chunks (in characters)
        separator: String to split text on (default is space)

    Returns:
        List of text chunks

    Raises:
        ValueError: If chunk_size < chunk_overlap
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer")

    if chunk_overlap < 0:
        raise ValueError("chunk_overlap must be a non-negative integer")

    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size")

    # Handle empty text
    if not text:
        return []

    # If text is shorter than chunk_size, return it as a single chunk
    if len(text) <= chunk_size:
        return [text]

    chunks = []
    words = text.split(separator)
    current_chunk = []
    current_length = 0

    for word in words:
        word_length = len(word) + len(separator)

        # Check if adding this word would exceed the chunk size
        if current_length + word_length > chunk_size and current_chunk:
            # Join words in current chunk and add to chunks
            chunks.append(separator.join(current_chunk))

            # Calculate how many words to keep for overlap
            if chunk_overlap > 0:
                # Keep words that fit within the overlap length
                overlap_length = 0
                overlap_words = []

                for w in reversed(current_chunk):
                    w_len = len(w) + len(separator)
                    if overlap_length + w_len <= chunk_overlap:
                        overlap_words.insert(0, w)
                        overlap_length += w_len
                    else:
                        break

                current_chunk = overlap_words
                current_length = overlap_length
            else:
                current_chunk = []
                current_length = 0

        # Add word to current chunk
        current_chunk.append(word)
        current_length += word_length

    # Add the last chunk if not empty
    if current_chunk:
        chunks.append(separator.join(current_chunk))

    logger.debug(f"Split text into {len(chunks)} chunks")
    return chunks


def chunk_text_by_delimiter(
    text: str,
    delimiter: str = "\n\n",
    chunk_size: int = 1000,
    chunk_overlap: int = 0,
) -> List[str]:
    """
    Split text by delimiter first, then chunk to maximum size.

    Args:
        text: Input text to split
        delimiter: Delimiter to split text on
        chunk_size: Maximum size of each chunk (in characters)
        chunk_overlap: Overlap between chunks (in characters)

    Returns:
        List of text chunks
    """
    # First split by delimiter
    sections = text.split(delimiter)

    # Remove empty sections
    sections = [section.strip() for section in sections if section.strip()]

    chunks = []
    current_chunk = []
    current_length = 0

    for section in sections:
        section_length = len(section) + len(delimiter)

        # If section itself is longer than chunk_size, recursively chunk it
        if section_length > chunk_size:
            # Process current accumulated chunk before handling the long section
            if current_chunk:
                chunks.append(delimiter.join(current_chunk))
                current_chunk = []
                current_length = 0

            # Recursively chunk the long section
            section_chunks = chunk_text(section, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
            chunks.extend(section_chunks)
            continue

        # Check if adding this section would exceed the chunk size
        if current_length + section_length > chunk_size and current_chunk:
            # Join sections in current chunk and add to chunks
            chunks.append(delimiter.join(current_chunk))

            # Calculate overlap if needed
            if chunk_overlap > 0 and current_chunk:
                # Keep sections that fit within the overlap length
                overlap_length = 0
                overlap_sections = []

                for s in reversed(current_chunk):
                    s_len = len(s) + len(delimiter)
                    if overlap_length + s_len <= chunk_overlap:
                        overlap_sections.insert(0, s)
                        overlap_length += s_len
                    else:
                        break

                current_chunk = overlap_sections
                current_length = overlap_length
            else:
                current_chunk = []
                current_length = 0

        # Add section to current chunk
        current_chunk.append(section)
        current_length += section_length

    # Add the last chunk if not empty
    if current_chunk:
        chunks.append(delimiter.join(current_chunk))

    logger.debug(f"Split text into {len(chunks)} chunks using delimiter chunking")
    return chunks


def extract_metadata(text: str) -> Tuple[str, Dict[str, Any]]:
    """
    Extract metadata from text in YAML/Markdown format.

    This function looks for metadata at the beginning of the text,
    enclosed between triple dashes (---).

    Args:
        text: Input text potentially containing metadata

    Returns:
        Tuple of (text without metadata, metadata dictionary)
    """
    metadata = {}
    clean_text = text

    # Check for metadata section at the beginning (YAML front matter)
    yaml_pattern = r"^\s*---\s*\n(.*?)\n\s*---\s*\n"
    match = re.search(yaml_pattern, text, re.DOTALL)

    if match:
        # Extract metadata content
        metadata_text = match.group(1)

        # Parse metadata lines
        for line in metadata_text.split("\n"):
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            # Parse key-value pairs
            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip()

                # Convert value types if possible
                if value.lower() == "true":
                    value = True
                elif value.lower() == "false":
                    value = False
                elif value.isdigit():
                    value = int(value)
                elif _is_float(value):
                    value = float(value)

                metadata[key] = value

        # Remove metadata section from text
        clean_text = text[match.end() :].strip()

    return clean_text, metadata


def _is_float(text: str) -> bool:
    """Check if a string can be converted to a float."""
    try:
        float(text)
        return True
    except ValueError:
        return False


def chunk_documents(
    documents: List[Dict[str, Any]],
    text_key: str = "text",
    chunk_size: int = 256,
    chunk_overlap: int = 64,
    separator: str = " ",
    include_metadata: bool = True,
) -> List[Dict[str, Any]]:
    """
    Split documents into overlapping chunks.

    Args:
        documents: List of documents with text and metadata
        text_key: Key for the text field in documents
        chunk_size: Maximum chunk size in tokens
        chunk_overlap: Overlap between chunks in tokens
        separator: Token separator
        include_metadata: Whether to include document metadata in chunks

    Returns:
        List of document chunks
    """
    chunked_documents = []

    for doc in documents:
        # Skip documents without text
        if text_key not in doc or not doc[text_key]:
            continue

        # Get document text
        text = doc[text_key]

        # Chunk text
        text_chunks = chunk_text(
            text=text,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separator=separator,
        )

        # Create chunked documents
        for i, chunk in enumerate(text_chunks):
            chunk_doc = {text_key: chunk}

            # Add chunk metadata
            chunk_doc["chunk_id"] = i
            chunk_doc["chunk_total"] = len(text_chunks)

            # Include original document metadata
            if include_metadata:
                for key, value in doc.items():
                    if key != text_key:
                        chunk_doc[key] = value

            chunked_documents.append(chunk_doc)

    return chunked_documents
