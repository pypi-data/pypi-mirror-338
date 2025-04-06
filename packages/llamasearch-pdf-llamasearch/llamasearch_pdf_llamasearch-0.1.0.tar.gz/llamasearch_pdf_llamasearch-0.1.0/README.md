# LlamaSearch PDF

A comprehensive PDF processing toolkit for document processing workflows.

## Features

- **OCR (Optical Character Recognition)** - Extract text from scanned PDFs and images with support for multiple OCR engines:
  - Tesseract OCR
  - OCRmyPDF
  - Hugging Face Models
  
- **PDF Manipulation** - Core utilities for working with PDF files:
  - Merging multiple PDFs
  - Splitting PDFs
  - Converting images to PDFs
  - Optimizing PDF file size
  
- **Text Extraction** - Extract and process text from PDF documents:
  - Direct text extraction from PDF content streams
  - OCR fallback for scanned documents
  - Text normalization and processing options
  
- **Metadata Management** - Extract, update, and manage PDF document metadata:
  - Standard document information (title, author, etc.)
  - XMP metadata extraction
  - Text-based metadata detection
  
- **Search and Indexing** - Create searchable indices for PDF documents:
  - Full-text search with TF-IDF ranking
  - Page-level search results with context snippets
  - Search across multiple documents
  - Save and load search indices
  
- **Batch Processing** - Process multiple files efficiently:
  - Multi-threaded processing
  - Directory processing with filtering
  - Progress tracking and logging

## Installation

```
pip install llamasearch-pdf
```

For additional OCR engines:

```
# For OCRmyPDF support
pip install llamasearch-pdf[ocrmypdf]

# For Hugging Face OCR support
pip install llamasearch-pdf[huggingface]

# For search example functionality
pip install llamasearch-pdf[search]

# For all features
pip install llamasearch-pdf[all]
```

## Command-Line Usage

The package provides a command-line interface for common operations:

### OCR Operations

```bash
# List available OCR engines
llamasearch-pdf ocr list-engines

# OCR a single PDF file
llamasearch-pdf ocr file document.pdf --output document_ocr.pdf

# Extract text from a PDF via OCR
llamasearch-pdf ocr file document.pdf --format text --output document_text.txt

# Process a directory of PDFs
llamasearch-pdf ocr directory ./documents --output ./documents_ocr --format pdf --recursive
```

### Text Extraction

```bash
# Extract text from a PDF
llamasearch-pdf text extract document.pdf --output document_text.txt

# Extract text with layout preservation
llamasearch-pdf text extract document.pdf --preserve-layout --output document_text.txt

# Batch extract text from a directory
llamasearch-pdf text batch ./documents --output ./extracted_text --recursive
```

### Metadata Operations

```bash
# Extract metadata from a PDF
llamasearch-pdf metadata extract document.pdf

# Extract detailed metadata including XMP
llamasearch-pdf metadata extract document.pdf --detailed

# Update metadata in a PDF
llamasearch-pdf metadata update document.pdf --title "New Title" --author "New Author"

# Extract metadata from text content
llamasearch-pdf metadata text document.pdf

# Batch extract metadata from a directory
llamasearch-pdf metadata batch ./documents --output ./metadata --recursive
```

### Search Operations

```bash
# Create a search index for a directory of PDFs
llamasearch-pdf search create-index ./documents --output-path ./search_index.pkl

# Search using a saved index
llamasearch-pdf search search "quantum computing" --index-path ./search_index.pkl

# Search specific PDF files directly
llamasearch-pdf search search "neural networks" --files doc1.pdf doc2.pdf doc3.pdf

# Search with custom options and JSON output
llamasearch-pdf search search "machine learning" --index-path ./search_index.pkl --max-results 20 --min-score 0.5 --json
```

## Python API Usage

### OCR Operations

```python
from llamasearch_pdf.ocr import ocr_pdf, ocr_image, process_directory

# OCR a PDF file
ocr_pdf('document.pdf', 'document_ocr.pdf')

# Extract text from an image
text = ocr_image('scan.jpg')

# Process a directory of PDFs and images
results = process_directory('documents/', 'documents_ocr/', output_format='text')
```

### Text Extraction

```python
from llamasearch_pdf.core import extract_text, TextExtractor

# Simple text extraction
text_dict = extract_text('document.pdf', preserve_layout=True)

# Advanced extraction with custom options
extractor = TextExtractor(
    preserve_layout=True,
    remove_hyphenation=True,
    normalize_whitespace=True,
    fallback_to_ocr=True
)
text_dict = extractor.extract_text_from_pdf('document.pdf')
```

### Metadata Operations

```python
from llamasearch_pdf.core import extract_metadata, update_metadata, MetadataManager

# Extract metadata
metadata = extract_metadata('document.pdf')

# Update metadata
new_metadata = {'/Title': 'New Document Title', '/Author': 'Document Author'}
update_metadata('document.pdf', 'updated_document.pdf', new_metadata)

# Advanced metadata operations
manager = MetadataManager()
metadata = manager.extract_metadata('document.pdf')
manager.print_metadata_summary(metadata)

# Extract metadata from text content
text_dict = extract_text('document.pdf')
text_content = "\n".join(text_dict.values())
text_metadata = manager.extract_text_metadata(text_content)
```

### Search Operations

```python
from llamasearch_pdf.search import create_index, search_pdfs, SearchIndex

# Create a search index
index = create_index(case_sensitive=False)

# Add documents to the index
index.add_document('document1.pdf')
index.add_document('document2.pdf')

# Save the index for later use
index.save('search_index.pkl')

# Load a previously saved index
loaded_index = create_index(index_path='search_index.pkl')

# Search the index
results = loaded_index.search('quantum computing', max_results=10)

# Display search results
for result in results:
    print(f"Document: {result.document_path}, Page: {result.page_number}")
    print(f"Score: {result.score}")
    print(f"Context: {result.snippet}")
    print()

# Quick search without creating an explicit index
results = search_pdfs('neural networks', ['doc1.pdf', 'doc2.pdf', 'doc3.pdf'])
```

### PDF Processing

```python
from llamasearch_pdf.core.processor import PDFProcessor

# Initialize the processor
processor = PDFProcessor()

# Convert images to PDFs
pdf_files = processor.batch_convert_images(['image1.jpg', 'image2.png'])

# Merge PDFs
merged_pdf = processor.merge_pdfs(pdf_files, 'merged.pdf')

# Process a directory with PDFs and images
processor.process_directory('documents/', merge=True, optimize=True)
```

## Requirements

- Python 3.8+
- For Tesseract OCR: Tesseract must be installed on your system
- For OCRmyPDF: OCRmyPDF must be installed on your system
- For image processing: Poppler must be installed for PDF to image conversion

## License

MIT 