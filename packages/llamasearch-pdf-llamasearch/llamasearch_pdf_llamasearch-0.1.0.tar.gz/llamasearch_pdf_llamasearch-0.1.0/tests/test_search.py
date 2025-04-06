"""
Tests for the search module.

This module tests the PDF search functionality, including index creation,
document indexing, searching, and result evaluation.
"""

import os
import sys
import unittest
import tempfile
from pathlib import Path

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from llamasearch_pdf.search import (
    SearchResult,
    SearchIndex,
    create_index,
    search_pdfs
)


class TestSearchIndex(unittest.TestCase):
    """Test case for SearchIndex class and related functions."""
    
    def setUp(self):
        """Set up test environment."""
        # Create a temporary directory
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.temp_dir.name)
        
        # Path to test files
        self.test_files_dir = Path(os.path.dirname(__file__)) / "test_files"
        self.test_files_dir.mkdir(exist_ok=True)
        
        # Create a sample PDF for testing if it doesn't exist
        self.create_test_pdf()
    
    def tearDown(self):
        """Clean up after tests."""
        self.temp_dir.cleanup()
    
    def create_test_pdf(self):
        """Create a test PDF file for testing."""
        test_pdf_path = self.test_files_dir / "search_test.pdf"
        
        # Skip if the file already exists
        if test_pdf_path.exists():
            return test_pdf_path
        
        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.pdfgen import canvas
            
            c = canvas.Canvas(str(test_pdf_path), pagesize=letter)
            
            # Page 1
            c.setFont("Helvetica", 12)
            c.drawString(100, 750, "Test Document for Search")
            c.drawString(100, 700, "This is a sample document created for search testing.")
            c.drawString(100, 650, "It contains specific words and phrases for search evaluation.")
            c.drawString(100, 600, "Keywords: python programming language")
            c.showPage()
            
            # Page 2
            c.setFont("Helvetica", 12)
            c.drawString(100, 750, "Search Test Page 2")
            c.drawString(100, 700, "Search algorithms for text retrieval")
            c.drawString(100, 650, "Inverted indices for efficient search")
            c.drawString(100, 600, "TF-IDF scoring for relevance ranking")
            c.showPage()
            
            c.save()
            
            return test_pdf_path
            
        except ImportError:
            self.skipTest("reportlab package is required for creating test PDFs")
    
    def test_search_index_creation(self):
        """Test creating a search index."""
        # Create an in-memory index
        index = create_index(case_sensitive=False)
        
        # Check initial state
        self.assertEqual(index.doc_count, 0)
        self.assertEqual(len(index.inverted_index), 0)
        self.assertEqual(len(index.documents), 0)
    
    def test_add_document(self):
        """Test adding a document to the index."""
        # Create an index
        index = create_index()
        
        # Get test PDF path
        test_pdf = self.create_test_pdf()
        
        # Add document to index
        if not test_pdf.exists():
            self.skipTest("Test PDF could not be created")
            
        index.add_document(str(test_pdf))
        
        # Check document was added
        self.assertEqual(index.doc_count, 1)
        self.assertGreater(len(index.inverted_index), 0)
        self.assertEqual(len(index.documents), 1)
    
    def test_search_functionality(self):
        """Test basic search functionality."""
        # Create an index
        index = create_index()
        
        # Get test PDF path
        test_pdf = self.create_test_pdf()
        
        # Add document to index
        if not test_pdf.exists():
            self.skipTest("Test PDF could not be created")
            
        index.add_document(str(test_pdf))
        
        # Perform searches
        results_python = index.search("python")
        results_search = index.search("search")
        results_nonexistent = index.search("nonexistent")
        
        # Check results
        self.assertGreater(len(results_python), 0)
        self.assertGreater(len(results_search), 0)
        self.assertEqual(len(results_nonexistent), 0)
        
        # Check result properties
        if results_python:
            result = results_python[0]
            self.assertEqual(result.document_path, str(test_pdf))
            self.assertIsInstance(result.page_number, int)
            self.assertIsInstance(result.score, float)
            self.assertIsInstance(result.snippet, str)
    
    def test_case_sensitivity(self):
        """Test case sensitivity in search."""
        # Create case-sensitive and case-insensitive indices
        index_case_sensitive = create_index(case_sensitive=True)
        index_case_insensitive = create_index(case_sensitive=False)
        
        # Get test PDF path
        test_pdf = self.create_test_pdf()
        
        # Add document to both indices
        if not test_pdf.exists():
            self.skipTest("Test PDF could not be created")
            
        index_case_sensitive.add_document(str(test_pdf))
        index_case_insensitive.add_document(str(test_pdf))
        
        # Perform searches with different cases
        results_sensitive_lower = index_case_sensitive.search("python")
        results_sensitive_upper = index_case_sensitive.search("PYTHON")
        results_insensitive_lower = index_case_insensitive.search("python")
        results_insensitive_upper = index_case_insensitive.search("PYTHON")
        
        # Case-sensitive index should differentiate between cases
        if "PYTHON" not in str(test_pdf):  # Only if the test PDF doesn't contain "PYTHON"
            self.assertNotEqual(len(results_sensitive_lower), len(results_sensitive_upper))
        
        # Case-insensitive index should find both
        self.assertEqual(len(results_insensitive_lower), len(results_insensitive_upper))
    
    def test_save_and_load(self):
        """Test saving and loading the index."""
        # Create an index
        index_path = self.temp_path / "test_index.pkl"
        index = create_index(index_path=str(index_path))
        
        # Get test PDF path
        test_pdf = self.create_test_pdf()
        
        # Add document to index
        if not test_pdf.exists():
            self.skipTest("Test PDF could not be created")
            
        index.add_document(str(test_pdf))
        
        # Save the index
        index.save()
        
        # Verify file was created
        self.assertTrue(index_path.exists())
        
        # Load the index
        loaded_index = create_index(index_path=str(index_path))
        
        # Check loaded index has the same data
        self.assertEqual(loaded_index.doc_count, index.doc_count)
        self.assertEqual(len(loaded_index.inverted_index), len(index.inverted_index))
        self.assertEqual(len(loaded_index.documents), len(index.documents))
        
        # Perform a search to verify functionality
        results = loaded_index.search("python")
        self.assertGreater(len(results), 0)
    
    def test_search_results_class(self):
        """Test the SearchResult class."""
        # Create a search result
        result = SearchResult(
            document_path="/path/to/doc.pdf",
            page_number=1,
            score=0.75,
            snippet="This is a snippet",
            metadata={"author": "Test Author"}
        )
        
        # Check properties
        self.assertEqual(result.document_path, "/path/to/doc.pdf")
        self.assertEqual(result.page_number, 1)
        self.assertEqual(result.score, 0.75)
        self.assertEqual(result.snippet, "This is a snippet")
        self.assertEqual(result.metadata, {"author": "Test Author"})
        
        # Check string representation
        self.assertIn("doc.pdf", str(result))
        self.assertIn("0.75", str(result))
    
    def test_search_pdfs_function(self):
        """Test the search_pdfs convenience function."""
        # Get test PDF path
        test_pdf = self.create_test_pdf()
        
        if not test_pdf.exists():
            self.skipTest("Test PDF could not be created")
        
        # Use the convenience function
        results = search_pdfs("python", [str(test_pdf)])
        
        # Check results
        self.assertIsInstance(results, list)
        if results:
            self.assertIsInstance(results[0], SearchResult)


if __name__ == "__main__":
    unittest.main() 