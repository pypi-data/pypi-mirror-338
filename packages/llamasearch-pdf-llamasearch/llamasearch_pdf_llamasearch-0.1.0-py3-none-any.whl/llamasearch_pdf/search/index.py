"""
Search index functionality for PDF documents.

This module provides capabilities to index and search text content from PDF documents,
supporting both in-memory and on-disk indices for efficient text search operations.
"""

import os
import json
import pickle
import logging
import tempfile
from pathlib import Path
from typing import Dict, List, Optional, Union, Tuple, Any, Set, Callable
from dataclasses import dataclass, field

# Standard library for text processing
import re
from collections import defaultdict, Counter

# For token ranking
import math

from ..core.text import extract_text

logger = logging.getLogger(__name__)

@dataclass
class SearchResult:
    """Represents a search result with document and position information."""
    document_path: str
    page_number: int
    score: float
    snippet: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __repr__(self) -> str:
        """String representation of the search result."""
        return f"SearchResult(doc='{os.path.basename(self.document_path)}', page={self.page_number}, score={self.score:.4f})"

class SearchIndex:
    """Search index for PDF documents enabling efficient text searches."""
    
    def __init__(self, 
                 case_sensitive: bool = False,
                 tokenizer: Optional[Callable[[str], List[str]]] = None,
                 stopwords: Optional[Set[str]] = None,
                 index_path: Optional[str] = None):
        """
        Initialize a search index for PDF documents.
        
        Args:
            case_sensitive: Whether to preserve case when indexing and searching
            tokenizer: Custom tokenizer function (defaults to simple word tokenization)
            stopwords: Set of words to exclude from indexing
            index_path: Path to store/load the index (None for in-memory only)
        """
        self.case_sensitive = case_sensitive
        self.tokenizer = tokenizer or self._default_tokenizer
        self.stopwords = stopwords or set()
        self.index_path = index_path
        
        # Main inverted index: token -> [(doc_id, page_num, positions)]
        self.inverted_index = defaultdict(list)
        
        # Document store: doc_id -> document path
        self.documents = {}
        
        # Document text cache: (doc_id, page_num) -> text
        self.text_cache = {}
        
        # Document frequency: token -> number of documents containing the token
        self.doc_frequencies = Counter()
        
        # Total number of documents
        self.doc_count = 0
        
        # Document metadata
        self.metadata = {}
        
        if index_path and os.path.exists(index_path):
            self.load()
    
    def _default_tokenizer(self, text: str) -> List[str]:
        """
        Default tokenizer that splits text into words.
        
        Args:
            text: The text to tokenize
            
        Returns:
            A list of tokens
        """
        if not self.case_sensitive:
            text = text.lower()
        
        # Split on word boundaries and filter empty tokens
        tokens = re.findall(r'\b\w+\b', text)
        return [t for t in tokens if t and t not in self.stopwords]
    
    def _get_doc_id(self, doc_path: str) -> str:
        """
        Get or create a document ID for a document path.
        
        Args:
            doc_path: Path to the document
            
        Returns:
            A unique document ID
        """
        # Create a normalized path for consistency
        normalized_path = str(Path(doc_path).resolve())
        
        # If document already exists, return its ID
        for doc_id, path in self.documents.items():
            if path == normalized_path:
                return doc_id
        
        # Otherwise, create a new ID
        doc_id = str(len(self.documents))
        self.documents[doc_id] = normalized_path
        return doc_id
    
    def add_document(self, 
                     doc_path: str, 
                     metadata: Optional[Dict[str, Any]] = None,
                     pages: Optional[List[int]] = None) -> None:
        """
        Add a document to the search index.
        
        Args:
            doc_path: Path to the PDF document
            metadata: Optional metadata to associate with the document
            pages: Specific pages to index (None for all pages)
        """
        doc_id = self._get_doc_id(doc_path)
        
        try:
            # Extract text from the document
            extracted_data = extract_text(doc_path, pages=pages)
            
            # Store metadata if provided
            if metadata:
                self.metadata[doc_id] = metadata
            
            # Index each page
            for page_num, page_text in extracted_data.items():
                self._index_page(doc_id, page_num, page_text)
            
            # Update document count if this is a new document
            if doc_id == str(len(self.documents) - 1):
                self.doc_count += 1
                
            logger.info(f"Indexed document: {os.path.basename(doc_path)}")
            
        except Exception as e:
            logger.error(f"Failed to index document {doc_path}: {str(e)}")
            raise
    
    def _index_page(self, doc_id: str, page_num: int, text: str) -> None:
        """
        Index a single page of a document.
        
        Args:
            doc_id: Document identifier
            page_num: Page number (0-based)
            text: Text content of the page
        """
        # Cache the text for snippet generation
        self.text_cache[(doc_id, page_num)] = text
        
        # Tokenize the text
        tokens = self.tokenizer(text)
        
        # Track tokens for this document/page
        doc_tokens = set()
        
        # Index each token with position
        for position, token in enumerate(tokens):
            # Add to inverted index
            posting = (doc_id, page_num, position)
            self.inverted_index[token].append(posting)
            
            # Track unique tokens in this document
            doc_tokens.add(token)
        
        # Update document frequencies
        for token in doc_tokens:
            self.doc_frequencies[token] += 1
    
    def search(self, 
               query: str, 
               max_results: int = 10, 
               min_score: float = 0.0,
               snippet_size: int = 100) -> List[SearchResult]:
        """
        Search the index for documents matching the query.
        
        Args:
            query: Search query text
            max_results: Maximum number of results to return
            min_score: Minimum score threshold for results
            snippet_size: Size of text snippet to include with results
            
        Returns:
            List of SearchResult objects sorted by relevance
        """
        # Tokenize query
        query_tokens = self.tokenizer(query)
        
        if not query_tokens:
            logger.warning("Empty query after tokenization")
            return []
        
        # Calculate TF-IDF scores
        scores = self._score_documents(query_tokens)
        
        # Filter by minimum score and sort by score (descending)
        filtered_scores = [(doc_info, score) for doc_info, score in scores.items() 
                          if score >= min_score]
        sorted_results = sorted(filtered_scores, key=lambda x: x[1], reverse=True)
        
        # Limit to max_results
        top_results = sorted_results[:max_results]
        
        # Convert to SearchResult objects with snippets
        search_results = []
        for (doc_id, page_num), score in top_results:
            doc_path = self.documents[doc_id]
            snippet = self._generate_snippet(doc_id, page_num, query_tokens, snippet_size)
            
            # Get metadata if available
            result_metadata = {}
            if doc_id in self.metadata:
                result_metadata = self.metadata[doc_id]
            
            result = SearchResult(
                document_path=doc_path,
                page_number=page_num,
                score=score,
                snippet=snippet,
                metadata=result_metadata
            )
            search_results.append(result)
        
        return search_results
    
    def _score_documents(self, query_tokens: List[str]) -> Dict[Tuple[str, int], float]:
        """
        Score documents based on TF-IDF for the query tokens.
        
        Args:
            query_tokens: Tokenized query
            
        Returns:
            Dictionary mapping (doc_id, page_num) to score
        """
        scores = defaultdict(float)
        
        # Count query term frequencies
        query_tf = Counter(query_tokens)
        
        # For each query token
        for token in set(query_tokens):
            if token not in self.inverted_index:
                continue
                
            # Calculate IDF
            idf = math.log(self.doc_count / (self.doc_frequencies[token] + 1))
            
            # Calculate query TF-IDF
            query_weight = query_tf[token] * idf
            
            # For each document containing the token
            for doc_id, page_num, _ in self.inverted_index[token]:
                # Count token occurrences in this document/page
                doc_tf = sum(1 for d, p, _ in self.inverted_index[token] 
                            if d == doc_id and p == page_num)
                
                # Calculate document TF-IDF
                doc_weight = doc_tf * idf
                
                # Add to score
                scores[(doc_id, page_num)] += query_weight * doc_weight
        
        return scores
    
    def _generate_snippet(self, 
                         doc_id: str, 
                         page_num: int, 
                         query_tokens: List[str],
                         size: int = 100) -> str:
        """
        Generate a text snippet for search results.
        
        Args:
            doc_id: Document ID
            page_num: Page number
            query_tokens: Query tokens to highlight
            size: Approximate size of snippet in characters
            
        Returns:
            Text snippet with context around query terms
        """
        # Get page text from cache
        page_key = (doc_id, page_num)
        if page_key not in self.text_cache:
            return ""
            
        text = self.text_cache[page_key]
        
        # Find positions of query tokens in text
        positions = []
        for token in query_tokens:
            if not self.case_sensitive:
                token_pattern = re.compile(r'\b' + re.escape(token) + r'\b', re.IGNORECASE)
            else:
                token_pattern = re.compile(r'\b' + re.escape(token) + r'\b')
                
            for match in token_pattern.finditer(text):
                positions.append((match.start(), match.end()))
        
        if not positions:
            # Fallback to beginning of text
            return text[:size] + "..." if len(text) > size else text
        
        # Sort positions
        positions.sort()
        
        # Find the best snippet position
        best_pos = positions[0][0]
        
        # Extract snippet around the best position
        half_size = size // 2
        start = max(0, best_pos - half_size)
        end = min(len(text), best_pos + half_size)
        
        # Adjust to word boundaries
        if start > 0:
            # Find the previous space
            prev_space = text.rfind(' ', 0, start)
            if prev_space != -1:
                start = prev_space + 1
        
        if end < len(text):
            # Find the next space
            next_space = text.find(' ', end)
            if next_space != -1:
                end = next_space
        
        snippet = text[start:end]
        
        # Add ellipsis if needed
        if start > 0:
            snippet = "..." + snippet
        if end < len(text):
            snippet = snippet + "..."
            
        return snippet
    
    def save(self, path: Optional[str] = None) -> None:
        """
        Save the index to disk.
        
        Args:
            path: Path to save the index (defaults to self.index_path)
        """
        save_path = path or self.index_path
        if not save_path:
            raise ValueError("No path specified for saving the index")
            
        save_path = Path(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            with open(save_path, 'wb') as f:
                pickle.dump({
                    'case_sensitive': self.case_sensitive,
                    'inverted_index': dict(self.inverted_index),
                    'documents': self.documents,
                    'doc_frequencies': self.doc_frequencies,
                    'doc_count': self.doc_count,
                    'metadata': self.metadata
                }, f)
            logger.info(f"Index saved to {save_path}")
        except Exception as e:
            logger.error(f"Failed to save index: {str(e)}")
            raise
    
    def load(self, path: Optional[str] = None) -> None:
        """
        Load the index from disk.
        
        Args:
            path: Path to load the index from (defaults to self.index_path)
        """
        load_path = path or self.index_path
        if not load_path:
            raise ValueError("No path specified for loading the index")
            
        try:
            with open(load_path, 'rb') as f:
                data = pickle.load(f)
                self.case_sensitive = data['case_sensitive']
                self.inverted_index = defaultdict(list, data['inverted_index'])
                self.documents = data['documents']
                self.doc_frequencies = data['doc_frequencies']
                self.doc_count = data['doc_count']
                self.metadata = data.get('metadata', {})
            logger.info(f"Index loaded from {load_path}")
        except Exception as e:
            logger.error(f"Failed to load index: {str(e)}")
            raise
    
    def clear(self) -> None:
        """Clear the index, removing all documents and tokens."""
        self.inverted_index = defaultdict(list)
        self.documents = {}
        self.text_cache = {}
        self.doc_frequencies = Counter()
        self.doc_count = 0
        self.metadata = {}
        logger.info("Index cleared")
    
    def get_stats(self) -> Dict[str, Any]:
        """
        Get statistics about the index.
        
        Returns:
            Dictionary with index statistics
        """
        return {
            'document_count': self.doc_count,
            'unique_terms': len(self.inverted_index),
            'indexed_pages': len(set((doc_id, page) for token in self.inverted_index 
                                  for doc_id, page, _ in self.inverted_index[token])),
            'case_sensitive': self.case_sensitive
        }


def create_index(case_sensitive: bool = False, 
                stopwords: Optional[List[str]] = None,
                index_path: Optional[str] = None) -> SearchIndex:
    """
    Create a new search index with the specified configuration.
    
    Args:
        case_sensitive: Whether to preserve case in the index
        stopwords: List of words to exclude from the index
        index_path: Path to store/load the index
        
    Returns:
        A new SearchIndex instance
    """
    stopwords_set = set(stopwords) if stopwords else None
    return SearchIndex(case_sensitive=case_sensitive, 
                      stopwords=stopwords_set,
                      index_path=index_path)


def search_pdfs(query: str, 
               pdf_paths: List[str], 
               case_sensitive: bool = False,
               max_results: int = 10) -> List[SearchResult]:
    """
    Convenience function to search a list of PDFs without explicitly creating an index.
    
    Args:
        query: Search query
        pdf_paths: List of PDF file paths to search
        case_sensitive: Whether to perform a case-sensitive search
        max_results: Maximum number of results to return
        
    Returns:
        List of SearchResult objects
    """
    # Create a temporary index
    index = create_index(case_sensitive=case_sensitive)
    
    # Add documents to the index
    for pdf_path in pdf_paths:
        try:
            index.add_document(pdf_path)
        except Exception as e:
            logger.warning(f"Could not index {pdf_path}: {str(e)}")
    
    # Perform the search
    return index.search(query, max_results=max_results) 