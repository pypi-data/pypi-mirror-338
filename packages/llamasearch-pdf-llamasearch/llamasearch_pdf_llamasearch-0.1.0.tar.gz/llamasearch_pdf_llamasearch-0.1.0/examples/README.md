# LlamaSearch PDF Examples

This directory contains example scripts demonstrating how to use the LlamaSearch PDF package for various PDF processing tasks.

## Available Examples

- **[text_extraction_example.py](text_extraction_example.py)** - Demonstrates how to extract and process text from PDF documents using both basic and advanced approaches.
- **[ocr_example.py](ocr_example.py)** - Shows how to perform OCR (Optical Character Recognition) on PDFs and images.
- **[metadata_example.py](metadata_example.py)** - Illustrates how to extract, update, and manage metadata in PDF documents.
- **[search_example.py](search_example.py)** - Demonstrates how to create search indices, perform searches, and process search results from PDF documents.

## Running the Examples

The examples can be run directly from this directory. You'll need to ensure you have installed the LlamaSearch PDF package and its dependencies.

### Text Extraction Example

```bash
# Basic usage
python text_extraction_example.py --input path/to/document.pdf --simple

# Advanced usage with output directory
python text_extraction_example.py --input path/to/document.pdf --output ./output --advanced

# Compare native extraction with OCR
python text_extraction_example.py --input path/to/document.pdf --compare

# Run all examples
python text_extraction_example.py --input path/to/document.pdf --all
```

### OCR Example

```bash
# Basic OCR on a PDF
python ocr_example.py --input path/to/document.pdf

# OCR with specific engine
python ocr_example.py --input path/to/document.pdf --engine tesseract

# Batch OCR on a directory
python ocr_example.py --input path/to/directory --output ./output --batch
```

### Metadata Example

```bash
# Extract metadata from a PDF
python metadata_example.py --input path/to/document.pdf --extract

# Update metadata in a PDF
python metadata_example.py --input path/to/document.pdf --output ./output --update

# Extract metadata from text content
python metadata_example.py --input path/to/document.pdf --text

# Export metadata to JSON
python metadata_example.py --input path/to/document.pdf --output ./output --export

# Run all metadata examples
python metadata_example.py --input path/to/document.pdf --output ./output --all
```

### Search Example

```bash
# Run the search example (creates sample PDFs automatically)
python search_example.py

# The search example demonstrates:
# - Creating and managing search indices
# - Adding documents to an index
# - Saving and loading indices
# - Performing searches on indexed documents
# - Quick search functionality without explicit index creation
# - Combining text extraction with search
```

## Creating Your Own Examples

You can use these examples as templates for creating your own scripts. The general pattern is:

1. Import the necessary modules from `llamasearch_pdf`
2. Configure the processor or extractor with your desired options
3. Process your documents
4. Handle the output

Feel free to modify these examples to suit your specific needs or to experiment with different options and settings. 