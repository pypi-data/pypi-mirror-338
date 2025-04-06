"""
OCR (Optical Character Recognition) module for extracting text from PDFs and images.

This module provides functionality for performing OCR on PDF documents and images,
with support for multiple OCR engines including Tesseract, OCRmyPDF, and Hugging Face models.

Example usage:
    from llamasearch_pdf.ocr import ocr_pdf, ocr_image, process_directory
    
    # OCR a PDF file
    ocr_pdf('document.pdf', 'document_ocr.pdf')
    
    # Extract text from an image
    text = ocr_image('scan.jpg')
    
    # Process a directory of PDFs and images
    results = process_directory('documents/', 'documents_ocr/', output_format='text')
"""

from .processor import (
    OCRProcessor,
    ocr_image,
    ocr_pdf,
    process_directory
)

from .engines import (
    OCREngine,
    TesseractOCR,
    OCRMyPDF,
    HuggingFaceOCR,
    get_available_engines,
    get_default_engine
)

__all__ = [
    # Main functions
    'ocr_image',
    'ocr_pdf',
    'process_directory',
    
    # Classes
    'OCRProcessor',
    'OCREngine',
    'TesseractOCR',
    'OCRMyPDF',
    'HuggingFaceOCR',
    
    # Utility functions
    'get_available_engines',
    'get_default_engine'
] 