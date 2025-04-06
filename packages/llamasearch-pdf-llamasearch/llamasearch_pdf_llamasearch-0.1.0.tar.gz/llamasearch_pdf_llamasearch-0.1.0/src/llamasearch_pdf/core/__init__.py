"""
Core functionality for PDF processing operations.

This module contains the primary PDF processing capabilities including:
- PDF reading and parsing
- PDF text extraction and processing
- PDF merging and splitting
- PDF metadata manipulation
- PDF conversion utilities
"""

from .processor import PDFProcessor
from .text import TextExtractor, extract_text
from .metadata import MetadataManager, extract_metadata, update_metadata, create_basic_metadata

__all__ = [
    'PDFProcessor',
    'TextExtractor',
    'extract_text',
    'MetadataManager',
    'extract_metadata',
    'update_metadata',
    'create_basic_metadata',
] 