"""
PDF metadata extraction, editing, and management functionality.

This module provides tools for extracting, updating, and managing PDF document metadata,
including document properties, XMP metadata, and embedded document information.
"""

import os
import re
import uuid
import datetime
import logging
from pathlib import Path
from typing import Dict, List, Optional, Any, Set, Union, Tuple

import PyPDF2
from PyPDF2 import PdfReader, PdfWriter

logger = logging.getLogger(__name__)


class MetadataManager:
    """
    Class for extracting and managing PDF document metadata.
    
    Provides functionality to read, modify, and write metadata in PDF documents,
    including standard document information and XMP metadata.
    """
    
    # Common metadata fields in PDFs
    STANDARD_FIELDS = {
        'title', 'author', 'subject', 'keywords', 'creator',
        'producer', 'creation_date', 'modification_date'
    }
    
    def __init__(self, strict: bool = True, fallback_encoding: str = 'utf-8'):
        """
        Initialize the MetadataManager.
        
        Args:
            strict: Whether to use strict parsing mode for PDFs
            fallback_encoding: Encoding to use when extracting text if UTF-8 fails
        """
        self.strict = strict
        self.fallback_encoding = fallback_encoding
    
    def extract_metadata(self, pdf_path: Union[str, Path]) -> Dict[str, Any]:
        """
        Extract all available metadata from a PDF file.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Dictionary containing all extracted metadata
        """
        pdf_path = Path(pdf_path)
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        try:
            reader = PdfReader(pdf_path, strict=self.strict)
            metadata = {}
            
            # Extract document info
            if reader.metadata:
                for key, value in reader.metadata.items():
                    # Clean up key name (remove leading '/')
                    clean_key = key[1:] if key.startswith('/') else key
                    metadata[clean_key] = value
            
            # Extract additional metadata
            metadata['page_count'] = len(reader.pages)
            
            # Extract page sizes
            page_sizes = []
            for page in reader.pages:
                if '/MediaBox' in page:
                    # MediaBox is typically [0, 0, width, height]
                    media_box = page['/MediaBox']
                    page_sizes.append({
                        'width': float(media_box[2]),
                        'height': float(media_box[3]),
                        'unit': 'points'  # PDF dimensions are in points
                    })
            
            metadata['page_sizes'] = page_sizes
            
            # Try to extract XMP metadata if available
            try:
                xmp_metadata = self._extract_xmp_metadata(reader)
                if xmp_metadata:
                    metadata['xmp'] = xmp_metadata
            except Exception as e:
                logger.warning(f"Failed to extract XMP metadata: {e}")
            
            return metadata
        
        except Exception as e:
            logger.error(f"Error extracting metadata from {pdf_path}: {e}")
            raise
    
    def _extract_xmp_metadata(self, reader: PdfReader) -> Dict[str, Any]:
        """
        Extract XMP metadata from a PDF.
        
        Args:
            reader: A PdfReader object
            
        Returns:
            Dictionary containing XMP metadata or empty dict if not available
        """
        # This is a simplified extraction - a full implementation would
        # use a proper XMP parser to extract structured data
        xmp_metadata = {}
        
        # Check if XMP metadata exists in the catalog
        if '/Metadata' in reader.trailer['/Root']:
            try:
                metadata_object = reader.trailer['/Root']['/Metadata']
                xmp_data = metadata_object.get_data()
                
                # Extract basic XMP information using regex
                # This is a simplification - real-world code would use an XML parser
                title_match = re.search(r'<dc:title>.*?<rdf:Alt>.*?<rdf:li.*?>(.*?)</rdf:li>', 
                                         xmp_data.decode('utf-8', errors='ignore'), re.DOTALL)
                if title_match:
                    xmp_metadata['dc:title'] = title_match.group(1)
                
                creator_match = re.search(r'<dc:creator>.*?<rdf:Seq>.*?<rdf:li>(.*?)</rdf:li>', 
                                           xmp_data.decode('utf-8', errors='ignore'), re.DOTALL)
                if creator_match:
                    xmp_metadata['dc:creator'] = creator_match.group(1)
                
                # Add more XMP extractions as needed
                
            except Exception as e:
                logger.warning(f"Error parsing XMP metadata: {e}")
        
        return xmp_metadata
    
    def update_metadata(self, pdf_path: Union[str, Path], output_path: Union[str, Path], 
                        metadata: Dict[str, Any]) -> None:
        """
        Update metadata in a PDF file.
        
        Args:
            pdf_path: Path to the input PDF file
            output_path: Path where the updated PDF will be saved
            metadata: Dictionary of metadata fields to update
        """
        pdf_path = Path(pdf_path)
        output_path = Path(output_path)
        
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        # Create output directory if it doesn't exist
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            reader = PdfReader(pdf_path, strict=self.strict)
            writer = PdfWriter()
            
            # Copy all pages from the reader to the writer
            for page in reader.pages:
                writer.add_page(page)
            
            # Update document metadata
            writer.add_metadata(metadata)
            
            # Write the updated PDF to the output path
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            
            logger.info(f"Updated metadata in PDF saved to {output_path}")
        
        except Exception as e:
            logger.error(f"Error updating metadata in {pdf_path}: {e}")
            raise
    
    def create_metadata(self, title: Optional[str] = None, author: Optional[str] = None,
                        subject: Optional[str] = None, keywords: Optional[str] = None,
                        creator: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new metadata dictionary with standard fields.
        
        Args:
            title: Document title
            author: Document author
            subject: Document subject
            keywords: Document keywords (comma-separated)
            creator: Application that created the document
            
        Returns:
            Dictionary with metadata fields
        """
        metadata = {}
        now = datetime.datetime.now()
        
        # Add provided fields
        if title:
            metadata['/Title'] = title
        if author:
            metadata['/Author'] = author
        if subject:
            metadata['/Subject'] = subject
        if keywords:
            metadata['/Keywords'] = keywords
        
        # Add default fields if not provided
        if '/Creator' not in metadata and creator:
            metadata['/Creator'] = creator
        if '/Producer' not in metadata:
            metadata['/Producer'] = f"LlamaSearch PDF Toolkit"
        
        # Add timestamps
        metadata['/CreationDate'] = now
        metadata['/ModDate'] = now
        
        return metadata
    
    def print_metadata_summary(self, metadata: Dict[str, Any]) -> None:
        """
        Print a human-readable summary of PDF metadata.
        
        Args:
            metadata: Dictionary of metadata as returned by extract_metadata()
        """
        print("PDF Metadata Summary:")
        print("-" * 40)
        
        # Print standard fields first
        for field in sorted(self.STANDARD_FIELDS):
            # Try with and without leading slash
            value = metadata.get(field, metadata.get(f"/{field.capitalize()}", None))
            if value:
                print(f"{field.replace('_', ' ').title()}: {value}")
        
        # Print page information
        page_count = metadata.get('page_count', 0)
        print(f"Page Count: {page_count}")
        
        # Print page sizes if available
        if 'page_sizes' in metadata and metadata['page_sizes']:
            first_page = metadata['page_sizes'][0]
            if len(set(tuple(p.items()) for p in metadata['page_sizes'])) == 1:
                # All pages same size
                print(f"Page Size: {first_page['width']} × {first_page['height']} {first_page['unit']}")
            else:
                # Mixed page sizes
                print("Page Sizes: Mixed (multiple sizes detected)")
        
        # Print any XMP metadata
        if 'xmp' in metadata and metadata['xmp']:
            print("\nXMP Metadata:")
            for key, value in metadata['xmp'].items():
                print(f"  {key}: {value}")
        
        # Print any additional fields
        other_fields = set(metadata.keys()) - self.STANDARD_FIELDS - {'page_count', 'page_sizes', 'xmp'}
        if other_fields:
            print("\nAdditional Fields:")
            for field in sorted(other_fields):
                value = metadata[field]
                print(f"  {field}: {value}")
    
    @staticmethod
    def extract_text_metadata(text: str) -> Dict[str, Any]:
        """
        Extract potential metadata from text content.
        
        This method attempts to identify common metadata patterns in text,
        such as titles, authors, dates, etc.
        
        Args:
            text: Text content to analyze
            
        Returns:
            Dictionary of extracted metadata
        """
        metadata = {}
        
        # Try to extract title (often at the beginning, in larger font)
        title_match = re.search(r'^(?:\s*?)([\w\s,.:;-]{5,100})(?:\s*?)$', 
                                 text.strip().split('\n')[0], re.MULTILINE)
        if title_match:
            metadata['title_candidate'] = title_match.group(1).strip()
        
        # Try to find author pattern
        author_matches = re.findall(r'(?:author|by|written by)[^\n\.\,]{0,20}?[:]\s*?([\w\s\.,-]{3,50}?)[\n\.]', 
                                     text.lower(), re.IGNORECASE)
        if author_matches:
            metadata['author_candidates'] = [a.strip() for a in author_matches]
        
        # Try to find date patterns
        date_patterns = [
            # ISO date format
            r'\b(\d{4}-\d{2}-\d{2})\b',
            # Month name, day, year
            r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}\b',
            # Day month year
            r'\b\d{1,2}\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\b',
        ]
        
        date_matches = []
        for pattern in date_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            date_matches.extend(matches)
        
        if date_matches:
            metadata['date_candidates'] = date_matches
        
        return metadata


# Convenience functions

def extract_metadata(pdf_path: Union[str, Path], 
                    strict: bool = True) -> Dict[str, Any]:
    """
    Convenience function to extract metadata from a PDF file.
    
    Args:
        pdf_path: Path to the PDF file
        strict: Whether to use strict PDF parsing
        
    Returns:
        Dictionary containing the metadata
    """
    manager = MetadataManager(strict=strict)
    return manager.extract_metadata(pdf_path)


def update_metadata(pdf_path: Union[str, Path], output_path: Union[str, Path],
                   metadata: Dict[str, Any], strict: bool = True) -> None:
    """
    Convenience function to update metadata in a PDF file.
    
    Args:
        pdf_path: Path to the input PDF file
        output_path: Path where the updated PDF will be saved
        metadata: Dictionary of metadata fields to update
        strict: Whether to use strict PDF parsing
    """
    manager = MetadataManager(strict=strict)
    manager.update_metadata(pdf_path, output_path, metadata)


def create_basic_metadata(title: Optional[str] = None, author: Optional[str] = None) -> Dict[str, Any]:
    """
    Convenience function to create basic metadata for a PDF.
    
    Args:
        title: Document title
        author: Document author
        
    Returns:
        Dictionary with metadata fields
    """
    manager = MetadataManager()
    return manager.create_metadata(title=title, author=author, 
                                  creator="LlamaSearch PDF Toolkit") 