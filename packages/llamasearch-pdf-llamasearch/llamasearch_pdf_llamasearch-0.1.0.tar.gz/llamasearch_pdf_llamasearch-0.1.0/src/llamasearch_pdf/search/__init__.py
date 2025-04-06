"""
PDF search module for LlamaSearch PDF.

This module provides functionality for indexing and searching text content in PDF documents.
It includes capabilities for creating and managing search indices, performing text searches,
and retrieving relevant results with context snippets.

Example usage:
    >>> from llamasearch_pdf.search import create_index, search_pdfs
    >>> # Create a search index
    >>> index = create_index(case_sensitive=False)
    >>> index.add_document("document.pdf")
    >>> index.save("index.pkl")
    >>>
    >>> # Search for content
    >>> results = index.search("quantum computing")
    >>> for result in results:
    >>>     print(f"Found in {result.document_path}, page {result.page_number}")
    >>>     print(f"Score: {result.score}")
    >>>     print(f"Context: {result.snippet}")
    >>>
    >>> # Quick search without creating an index
    >>> results = search_pdfs("quantum computing", ["doc1.pdf", "doc2.pdf"])
"""

from .index import (
    SearchResult,
    SearchIndex,
    create_index,
    search_pdfs
)

__all__ = [
    'SearchResult',
    'SearchIndex',
    'create_index',
    'search_pdfs'
] 