"""
Text extraction functionality for PDF documents.

This module provides tools for extracting and processing text content from PDFs,
with options for maintaining layout, handling different types of PDFs, and
preprocessing the extracted text for downstream applications.
"""

import os
import re
import logging
from pathlib import Path
from typing import List, Dict, Optional, Union, Any, Tuple, Iterator, Set

from PyPDF2 import PdfReader
from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn

from ..ocr import ocr_pdf

# Initialize logging
logger = logging.getLogger(__name__)


class TextExtractor:
    """
    Extract and process text from PDF documents.
    
    This class provides methods for extracting text from PDFs,
    preserving layout information, and preprocessing the text
    for downstream applications.
    """
    
    def __init__(
        self,
        preserve_layout: bool = True,
        remove_hyphenation: bool = True,
        normalize_whitespace: bool = True,
        fallback_to_ocr: bool = False,
        ocr_engine: Optional[str] = None,
        ocr_engine_options: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize the text extractor.
        
        Args:
            preserve_layout: Whether to attempt to preserve layout information
            remove_hyphenation: Whether to remove hyphenation from text
            normalize_whitespace: Whether to normalize whitespace
            fallback_to_ocr: Whether to use OCR as fallback for PDFs with no text
            ocr_engine: OCR engine to use for fallback
            ocr_engine_options: Options to pass to the OCR engine
        """
        self.preserve_layout = preserve_layout
        self.remove_hyphenation = remove_hyphenation
        self.normalize_whitespace = normalize_whitespace
        self.fallback_to_ocr = fallback_to_ocr
        self.ocr_engine = ocr_engine
        self.ocr_engine_options = ocr_engine_options or {}
    
    def extract_text_from_pdf(
        self,
        pdf_path: Union[str, Path],
        page_numbers: Optional[List[int]] = None,
        progress: Optional[Progress] = None
    ) -> Dict[int, str]:
        """
        Extract text from a PDF document.
        
        Args:
            pdf_path: Path to the PDF file
            page_numbers: List of page numbers to extract (0-based, None means all pages)
            progress: Optional Progress instance for tracking
            
        Returns:
            Dictionary mapping page numbers to extracted text
        """
        pdf_path = Path(pdf_path)
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        task_id = None
        if progress:
            task_id = progress.add_task(
                f"Extracting text from {pdf_path.name}", 
                total=None
            )
        
        try:
            reader = PdfReader(str(pdf_path))
            num_pages = len(reader.pages)
            
            if progress and task_id is not None:
                progress.update(task_id, total=num_pages if page_numbers is None else len(page_numbers))
            
            # Determine page range
            pages_to_extract = page_numbers if page_numbers is not None else range(num_pages)
            
            # Extract text from each page
            extracted_text = {}
            
            for i in pages_to_extract:
                if i < 0 or i >= num_pages:
                    logger.warning(f"Page {i} is out of range for PDF {pdf_path} ({num_pages} pages)")
                    continue
                
                page = reader.pages[i]
                
                try:
                    # Try to extract text directly
                    text = page.extract_text()
                    
                    # Check if text extraction yielded meaningful text
                    if not text or text.isspace():
                        if self.fallback_to_ocr:
                            logger.info(f"No text found in page {i} of {pdf_path}. Falling back to OCR.")
                            text = self._ocr_page(pdf_path, i)
                    else:
                        # Process the extracted text
                        text = self._process_text(text)
                    
                    extracted_text[i] = text
                    
                    if progress and task_id is not None:
                        progress.update(task_id, advance=1)
                        
                except Exception as e:
                    logger.error(f"Error extracting text from page {i} of {pdf_path}: {e}")
                    extracted_text[i] = f"[Error: {str(e)}]"
                    
                    if progress and task_id is not None:
                        progress.update(task_id, advance=1)
            
            return extracted_text
            
        except Exception as e:
            logger.error(f"Error opening PDF {pdf_path}: {e}")
            raise
        finally:
            if progress and task_id is not None:
                progress.update(task_id, completed=True)
    
    def extract_text_from_pdfs(
        self,
        pdf_paths: List[Union[str, Path]],
        progress: Optional[Progress] = None
    ) -> Dict[str, Dict[int, str]]:
        """
        Extract text from multiple PDF documents.
        
        Args:
            pdf_paths: List of paths to PDF files
            progress: Optional Progress instance for tracking
            
        Returns:
            Dictionary mapping PDF paths to dictionaries of page texts
        """
        results = {}
        
        # Create a nested progress instance if one was provided
        task_id = None
        if progress:
            task_id = progress.add_task(
                "Processing PDF files", 
                total=len(pdf_paths)
            )
        
        for pdf_path in pdf_paths:
            try:
                pdf_path = Path(pdf_path)
                results[str(pdf_path)] = self.extract_text_from_pdf(pdf_path, progress=progress)
                
                if progress and task_id is not None:
                    progress.update(task_id, advance=1)
                    
            except Exception as e:
                logger.error(f"Error processing {pdf_path}: {e}")
                results[str(pdf_path)] = {0: f"[Error: {str(e)}]"}
                
                if progress and task_id is not None:
                    progress.update(task_id, advance=1)
        
        return results
    
    def _process_text(self, text: str) -> str:
        """
        Process extracted text according to configuration options.
        
        Args:
            text: Raw text extracted from PDF
            
        Returns:
            Processed text
        """
        if not text:
            return text
        
        # Remove hyphenation at line breaks if requested
        if self.remove_hyphenation:
            text = self._remove_hyphenation(text)
        
        # Normalize whitespace if requested
        if self.normalize_whitespace:
            text = self._normalize_whitespace(text)
        
        return text
    
    def _remove_hyphenation(self, text: str) -> str:
        """
        Remove hyphenation from text.
        
        Args:
            text: Text with potential hyphenation
            
        Returns:
            Text with hyphenation removed
        """
        # Pattern: hyphen at the end of a line followed by a word at the beginning of the next line
        return re.sub(r'(\w+)-\s*\n(\w+)', r'\1\2', text)
    
    def _normalize_whitespace(self, text: str) -> str:
        """
        Normalize whitespace in text.
        
        Args:
            text: Text with potentially inconsistent whitespace
            
        Returns:
            Text with normalized whitespace
        """
        # Replace multiple spaces with a single space
        text = re.sub(r' +', ' ', text)
        
        # Replace multiple newlines with a single newline
        text = re.sub(r'\n+', '\n', text)
        
        # If preserve_layout is False, replace newlines with spaces
        if not self.preserve_layout:
            text = re.sub(r'\n', ' ', text)
            
            # Remove extraneous whitespace after normalization
            text = re.sub(r' +', ' ', text)
        
        return text.strip()
    
    def _ocr_page(self, pdf_path: Path, page_number: int) -> str:
        """
        Use OCR to extract text from a specific page.
        
        Args:
            pdf_path: Path to the PDF file
            page_number: Page number to OCR (0-based)
            
        Returns:
            OCR'd text
        """
        try:
            # Use OCR module to extract text
            return ocr_pdf(
                pdf_path,
                output_path=None,
                output_format='text',
                pages=[page_number],
                engine=self.ocr_engine,
                engine_options=self.ocr_engine_options
            )
        except Exception as e:
            logger.error(f"OCR failed for page {page_number} of {pdf_path}: {e}")
            return f"[OCR Error: {str(e)}]"


def extract_text(
    pdf_path: Union[str, Path],
    output_path: Optional[Union[str, Path]] = None,
    page_numbers: Optional[List[int]] = None,
    preserve_layout: bool = True,
    verbose: bool = False
) -> Union[Dict[int, str], Path]:
    """
    Convenience function to extract text from a PDF.
    
    Args:
        pdf_path: Path to the PDF file
        output_path: Path where extracted text should be saved (if provided)
        page_numbers: List of page numbers to extract (0-based, None means all pages)
        preserve_layout: Whether to preserve layout in extracted text
        verbose: Whether to display verbose output
        
    Returns:
        If output_path is None, dictionary mapping page numbers to text
        If output_path is provided, path to the output file
    """
    extractor = TextExtractor(preserve_layout=preserve_layout)
    
    # Configure logging for verbose mode
    if verbose:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)
    
    # Extract text
    extracted_text = extractor.extract_text_from_pdf(pdf_path, page_numbers)
    
    # Save to file if output path is provided
    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            for page_num, text in sorted(extracted_text.items()):
                f.write(f"=== Page {page_num + 1} ===\n\n")
                f.write(text)
                f.write("\n\n")
        
        return output_path
    
    return extracted_text 