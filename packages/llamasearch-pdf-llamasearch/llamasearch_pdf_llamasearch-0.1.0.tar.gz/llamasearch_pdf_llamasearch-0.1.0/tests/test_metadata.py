"""
Tests for the metadata module.
"""

import os
import sys
import unittest
from pathlib import Path
import tempfile
import datetime

# Add the parent directory to the Python path to allow importing llamasearch_pdf
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from llamasearch_pdf.core import (
    MetadataManager,
    extract_metadata,
    update_metadata,
    create_basic_metadata
)
from llamasearch_pdf.core.text import extract_text


class TestMetadataExtraction(unittest.TestCase):
    """Test metadata extraction functionality."""
    
    def setUp(self):
        """Set up test environment."""
        self.test_dir = Path(__file__).parent / "test_files"
        self.test_dir.mkdir(exist_ok=True)
        
        # Create a simple PDF for testing if needed
        self.sample_pdf = self.test_dir / "sample.pdf"
        if not self.sample_pdf.exists():
            try:
                # Try to create a simple PDF using PyPDF2
                from PyPDF2 import PdfWriter
                
                writer = PdfWriter()
                writer.add_blank_page(width=612, height=792)  # US Letter size
                
                # Add metadata
                writer.add_metadata({
                    '/Title': 'Sample Test PDF',
                    '/Author': 'LlamaSearch Test Suite',
                    '/Subject': 'PDF Testing',
                    '/Keywords': 'test, metadata, pdf',
                    '/Creator': 'PyPDF2',
                    '/Producer': 'PyPDF2'
                })
                
                with open(self.sample_pdf, 'wb') as f:
                    writer.write(f)
            except Exception as e:
                print(f"Warning: Could not create test PDF file: {e}")
                self.skipTest("Could not create test PDF file")
    
    def test_metadata_manager_creation(self):
        """Test creating a MetadataManager."""
        manager = MetadataManager()
        self.assertIsNotNone(manager)
        self.assertEqual(manager.strict, True)
        
        # Test with non-strict mode
        manager = MetadataManager(strict=False)
        self.assertEqual(manager.strict, False)
    
    def test_extract_metadata(self):
        """Test extracting metadata from a PDF."""
        if not self.sample_pdf.exists():
            self.skipTest("Test PDF file does not exist")
            
        # Use the convenience function
        metadata = extract_metadata(self.sample_pdf)
        self.assertIsNotNone(metadata)
        
        # Check for expected fields
        self.assertIn('page_count', metadata)
        self.assertEqual(metadata['page_count'], 1)
        
        # Check for standard metadata fields (these may vary based on the test PDF)
        standard_fields = ['Title', 'Author', 'Subject', 'Keywords', 'Creator', 'Producer']
        for field in standard_fields:
            # Check with or without slash prefix
            self.assertTrue(
                field in metadata or f'/{field}' in metadata,
                f"Field {field} not found in metadata"
            )
    
    def test_update_metadata(self):
        """Test updating metadata in a PDF."""
        if not self.sample_pdf.exists():
            self.skipTest("Test PDF file does not exist")
            
        # Create new metadata
        new_metadata = {
            '/Title': 'Updated Title',
            '/Author': 'Test Author',
            '/Keywords': 'updated, test'
        }
        
        # Create a temporary file for the updated PDF
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            output_path = tmp.name
        
        try:
            # Update the PDF
            update_metadata(self.sample_pdf, output_path, new_metadata)
            
            # Extract metadata from the updated PDF
            updated_metadata = extract_metadata(output_path)
            
            # Check that the metadata was updated
            self.assertEqual(updated_metadata.get('/Title'), 'Updated Title')
            self.assertEqual(updated_metadata.get('/Author'), 'Test Author')
            self.assertEqual(updated_metadata.get('/Keywords'), 'updated, test')
            
        finally:
            # Clean up
            if os.path.exists(output_path):
                os.remove(output_path)
    
    def test_create_basic_metadata(self):
        """Test creating basic metadata."""
        metadata = create_basic_metadata(
            title="Test Title",
            author="Test Author"
        )
        
        self.assertEqual(metadata.get('/Title'), 'Test Title')
        self.assertEqual(metadata.get('/Author'), 'Test Author')
        self.assertIn('/Producer', metadata)
        self.assertIn('/CreationDate', metadata)
    
    def test_extract_text_metadata(self):
        """Test extracting metadata from text content."""
        # Sample text with metadata patterns
        text = """Sample Document Title
        
        This is a test document for metadata extraction.
        
        Author: John Doe
        Date: January 1, 2023
        
        This document contains some example text for testing the metadata extraction
        capabilities of the MetadataManager class.
        """
        
        manager = MetadataManager()
        text_metadata = manager.extract_text_metadata(text)
        
        self.assertIsNotNone(text_metadata)
        self.assertIn('title_candidate', text_metadata)
        self.assertEqual(text_metadata['title_candidate'], 'Sample Document Title')
        
        # Check for author candidates
        if 'author_candidates' in text_metadata:
            self.assertIn('John Doe', text_metadata['author_candidates'][0])
        
        # Check for date candidates
        if 'date_candidates' in text_metadata:
            self.assertIn('January 1, 2023', text_metadata['date_candidates'])


if __name__ == '__main__':
    unittest.main() 