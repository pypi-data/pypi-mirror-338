#!/usr/bin/env python3
"""
Example script demonstrating PDF search functionality.

This example shows how to:
1. Create a search index for a collection of PDF documents
2. Add documents to the index
3. Save and load the index
4. Perform searches on the indexed documents
5. Process and display search results
"""

import os
import sys
import tempfile
from pathlib import Path

# Add the parent directory to the path to enable importing
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from llamasearch_pdf.search import create_index, search_pdfs
from llamasearch_pdf.core import extract_text


def create_sample_pdf(output_path):
    """Create a sample PDF file for demonstration if none exists."""
    # Check if file already exists
    if os.path.exists(output_path):
        return
    
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas
        
        c = canvas.Canvas(output_path, pagesize=letter)
        
        # Page 1
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, "LlamaSearch PDF Example Document")
        c.drawString(100, 730, "This is a sample document for search demonstration.")
        c.drawString(100, 700, "Page 1: Introduction to Quantum Computing")
        c.drawString(100, 680, "Quantum computing is a rapidly emerging technology that leverages")
        c.drawString(100, 660, "the principles of quantum mechanics to process information.")
        c.drawString(100, 640, "Unlike classical computers that use bits, quantum computers")
        c.drawString(100, 620, "use quantum bits or qubits that can exist in multiple states simultaneously.")
        c.showPage()
        
        # Page 2
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, "Page 2: Applications of Quantum Computing")
        c.drawString(100, 730, "Quantum computing shows promise in several domains:")
        c.drawString(100, 710, "- Cryptography and security")
        c.drawString(100, 690, "- Drug discovery and materials science")
        c.drawString(100, 670, "- Optimization problems")
        c.drawString(100, 650, "- Artificial intelligence and machine learning")
        c.drawString(100, 630, "These applications could revolutionize their respective fields.")
        c.showPage()
        
        # Page 3
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, "Page 3: Natural Language Processing")
        c.drawString(100, 730, "Natural Language Processing (NLP) is a field of artificial intelligence")
        c.drawString(100, 710, "that focuses on the interaction between computers and human language.")
        c.drawString(100, 690, "NLP enables computers to understand, interpret, and generate human text.")
        c.drawString(100, 670, "Applications include machine translation, sentiment analysis,")
        c.drawString(100, 650, "chatbots, and text summarization.")
        c.showPage()
        
        c.save()
        print(f"Created sample PDF at {output_path}")
    except ImportError:
        print("Could not create sample PDF. reportlab package is required.")
        print("Please install it with: pip install reportlab")
        sys.exit(1)


def demonstrate_search_index():
    """Demonstrate creating and using a search index."""
    print("\n" + "="*60)
    print("DEMONSTRATION: Creating and Using a Search Index")
    print("="*60)
    
    # Create a temporary directory for our example
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_dir_path = Path(temp_dir)
        
        # Create some sample PDFs
        pdf_files = []
        for i, topic in enumerate([
            "quantum_computing", 
            "artificial_intelligence", 
            "natural_language_processing"
        ]):
            pdf_path = temp_dir_path / f"{topic}.pdf"
            create_sample_pdf(pdf_path)
            pdf_files.append(pdf_path)
            
        # Create a search index
        print("\nStep 1: Creating a search index")
        index_path = temp_dir_path / "search_index.pkl"
        index = create_index(case_sensitive=False, index_path=str(index_path))
        
        # Add documents to the index
        print("\nStep 2: Adding documents to the index")
        for pdf_file in pdf_files:
            print(f"  Adding {pdf_file.name} to the index")
            index.add_document(str(pdf_file))
        
        # Get index statistics
        stats = index.get_stats()
        print("\nIndex Statistics:")
        for key, value in stats.items():
            print(f"  {key.replace('_', ' ').title()}: {value}")
        
        # Save the index
        print("\nStep 3: Saving the index")
        index.save()
        print(f"  Index saved to {index_path}")
        
        # Load the index
        print("\nStep 4: Loading the index")
        loaded_index = create_index(index_path=str(index_path))
        print(f"  Index loaded successfully with {loaded_index.get_stats()['document_count']} documents")
        
        # Perform searches
        print("\nStep 5: Performing searches")
        
        # Example searches
        queries = [
            "quantum computing",
            "artificial intelligence",
            "natural language"
        ]
        
        for query in queries:
            print(f"\nSearching for: '{query}'")
            results = loaded_index.search(query, max_results=5)
            
            if results:
                print(f"  Found {len(results)} results:")
                for i, result in enumerate(results):
                    print(f"  {i+1}. Document: {Path(result.document_path).name}")
                    print(f"     Page: {result.page_number}")
                    print(f"     Score: {result.score:.4f}")
                    print(f"     Snippet: \"{result.snippet}\"")
            else:
                print("  No results found")
        
        print("\nSearch completed successfully!")


def demonstrate_quick_search():
    """Demonstrate the quick search functionality."""
    print("\n" + "="*60)
    print("DEMONSTRATION: Quick Search Without Creating an Index")
    print("="*60)
    
    # Create a temporary directory for our example
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_dir_path = Path(temp_dir)
        
        # Create some sample PDFs
        pdf_files = []
        for i, topic in enumerate([
            "quantum_computing", 
            "artificial_intelligence"
        ]):
            pdf_path = temp_dir_path / f"{topic}.pdf"
            create_sample_pdf(pdf_path)
            pdf_files.append(str(pdf_path))
        
        # Use the convenience function to search without explicitly creating an index
        print("\nSearching multiple PDFs with a single query:")
        query = "quantum computing applications"
        
        print(f"Query: '{query}'")
        print(f"Files: {[Path(f).name for f in pdf_files]}")
        
        results = search_pdfs(query, pdf_files)
        
        if results:
            print(f"\nFound {len(results)} results:")
            for i, result in enumerate(results):
                print(f"{i+1}. Document: {Path(result.document_path).name}")
                print(f"   Page: {result.page_number}")
                print(f"   Score: {result.score:.4f}")
                print(f"   Snippet: \"{result.snippet}\"")
        else:
            print("\nNo results found")


def demonstrate_text_extraction_and_search():
    """Demonstrate text extraction and then searching the extracted text."""
    print("\n" + "="*60)
    print("DEMONSTRATION: Text Extraction and Search")
    print("="*60)
    
    # Create a temporary directory for our example
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_dir_path = Path(temp_dir)
        
        # Create a sample PDF
        pdf_path = temp_dir_path / "sample.pdf"
        create_sample_pdf(pdf_path)
        
        # Extract text from the PDF
        print(f"\nExtracting text from {pdf_path.name}")
        extracted_text = extract_text(pdf_path)
        
        # Print the extracted text for demonstration
        print("\nExtracted Text (first 150 characters of each page):")
        for page_num, text in extracted_text.items():
            print(f"\nPage {page_num}:")
            print(text[:150] + "..." if len(text) > 150 else text)
        
        # Create a simple in-memory index from the extracted text
        print("\nCreating an in-memory search index from extracted text")
        index = create_index(case_sensitive=False)
        index.add_document(str(pdf_path))
        
        # Search within the extracted text
        query = "quantum principles"
        print(f"\nSearching for: '{query}'")
        
        results = index.search(query)
        
        if results:
            print(f"Found {len(results)} results:")
            for i, result in enumerate(results):
                print(f"{i+1}. Page: {result.page_number}")
                print(f"   Score: {result.score:.4f}")
                print(f"   Snippet: \"{result.snippet}\"")
        else:
            print("No results found")


if __name__ == "__main__":
    print("LlamaSearch PDF - Search Functionality Example")
    print("This example demonstrates how to use the search capabilities of LlamaSearch PDF.")
    
    # Run the demonstrations
    demonstrate_search_index()
    demonstrate_quick_search()
    demonstrate_text_extraction_and_search()
    
    print("\nExample completed successfully!") 