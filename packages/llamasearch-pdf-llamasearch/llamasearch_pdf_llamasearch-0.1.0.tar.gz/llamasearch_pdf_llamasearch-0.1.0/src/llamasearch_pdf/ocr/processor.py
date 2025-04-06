"""
OCR processor for extracting text from PDF documents and images.

This module provides a high-level interface for OCR operations, handling
the selection of appropriate OCR engines and providing a unified API for
text extraction from PDFs and images.
"""

import os
import logging
from pathlib import Path
from typing import Optional, Union, List, Dict, Any, Tuple
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed

from .engines import (
    OCREngine, 
    get_default_engine, 
    get_available_engines,
    TesseractOCR,
    OCRMyPDF,
    HuggingFaceOCR
)

# Initialize logging
logger = logging.getLogger(__name__)


class OCRProcessor:
    """
    High-level processor for OCR operations on PDFs and images.
    
    This class provides a simplified interface for OCR operations,
    handling the selection of appropriate OCR engines and managing
    batch processing of multiple files.
    """
    
    def __init__(
        self,
        engine: Optional[Union[str, OCREngine]] = None,
        engine_options: Optional[Dict[str, Any]] = None,
        num_workers: int = 1,
        verbose: bool = False
    ):
        """
        Initialize the OCR processor.
        
        Args:
            engine: OCR engine to use. Can be:
                   - Name of engine ("tesseract", "ocrmypdf", "huggingface")
                   - Instance of OCREngine
                   - None (automatically selects best available engine)
            engine_options: Dictionary of options to pass to the OCR engine
            num_workers: Number of parallel workers for batch processing
            verbose: Whether to print verbose output
        """
        self.num_workers = num_workers
        self.verbose = verbose
        self.engine_options = engine_options or {}
        
        # Set up the OCR engine
        if engine is None:
            self.engine = get_default_engine()
            if self.engine is None:
                raise ValueError("No OCR engines available. Please install Tesseract OCR, OCRmyPDF, or transformers.")
        elif isinstance(engine, str):
            # Get engine by name
            engines = get_available_engines()
            if engine.lower() not in engines:
                available = ", ".join(engines.keys())
                raise ValueError(f"OCR engine '{engine}' not available. Available engines: {available}")
            
            # Initialize the engine with options
            self.engine = engines[engine.lower()](**self.engine_options)
        else:
            # Use the provided engine
            self.engine = engine
        
        if self.verbose:
            logger.info(f"Using OCR engine: {self.engine.__class__.__name__}")
    
    def ocr_image(
        self, 
        image_path: Union[str, Path],
        output_text_path: Optional[Union[str, Path]] = None,
        **kwargs
    ) -> str:
        """
        Perform OCR on a single image file.
        
        Args:
            image_path: Path to the image file
            output_text_path: Path to save the extracted text (optional)
            **kwargs: Additional options to pass to the OCR engine
            
        Returns:
            Extracted text from the image
        """
        image_path = Path(image_path)
        if not image_path.exists():
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
        # Merge engine options with kwargs
        options = {**self.engine_options, **kwargs}
        
        if self.verbose:
            logger.info(f"Processing image: {image_path}")
        
        # Process the image
        text = self.engine.process_image(image_path, **options)
        
        # Save the text to file if requested
        if output_text_path:
            output_text_path = Path(output_text_path)
            output_text_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_text_path, 'w', encoding='utf-8') as f:
                f.write(text)
            
            if self.verbose:
                logger.info(f"Saved OCR text to: {output_text_path}")
        
        return text
    
    def ocr_pdf(
        self,
        pdf_path: Union[str, Path],
        output_path: Optional[Union[str, Path]] = None,
        output_format: str = 'pdf',
        pages: Optional[List[int]] = None,
        **kwargs
    ) -> Union[str, Path]:
        """
        Perform OCR on a PDF file.
        
        Args:
            pdf_path: Path to the PDF file
            output_path: Path to save the OCR'd PDF or text
            output_format: Format of the output ('pdf' or 'text')
            pages: List of page indices to process (0-based)
            **kwargs: Additional options to pass to the OCR engine
            
        Returns:
            If output_format is 'pdf', returns the path to the OCR'd PDF.
            If output_format is 'text', returns the extracted text.
        """
        pdf_path = Path(pdf_path)
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        # Merge engine options with kwargs
        options = {**self.engine_options, **kwargs}
        
        # Add pages if specified
        if pages is not None:
            options['pages'] = pages
        
        if self.verbose:
            logger.info(f"Processing PDF: {pdf_path}")
            if pages:
                logger.info(f"Processing pages: {pages}")
        
        # Process the PDF
        if output_format.lower() == 'pdf':
            # If no output path is provided, use default
            if output_path is None:
                output_path = pdf_path.with_stem(f"{pdf_path.stem}_ocr")
            
            output_path = Path(output_path)
            result = self.engine.process_pdf(pdf_path, output_path, **options)
            
            if self.verbose and result:
                logger.info(f"Saved OCR'd PDF to: {result}")
            
            return result
        else:
            # Extract text
            options['output_format'] = 'text'
            text = self.engine.process_pdf(pdf_path, None, **options)
            
            # Save the text to file if requested
            if output_path:
                output_path = Path(output_path)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(text)
                
                if self.verbose:
                    logger.info(f"Saved OCR text to: {output_path}")
            
            return text
    
    def batch_process(
        self,
        files: List[Union[str, Path]],
        output_dir: Optional[Union[str, Path]] = None,
        output_format: str = 'pdf',
        **kwargs
    ) -> Dict[str, Union[str, Path]]:
        """
        Process multiple files in batch.
        
        Args:
            files: List of file paths (PDFs or images)
            output_dir: Directory to save the OCR'd files
            output_format: Format of the output ('pdf' or 'text')
            **kwargs: Additional options to pass to the OCR engine
            
        Returns:
            Dictionary mapping input files to output files or extracted text
        """
        # Prepare output directory
        if output_dir:
            output_dir = Path(output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
        
        results = {}
        
        # Use ThreadPoolExecutor for parallel processing
        if self.num_workers > 1:
            if self.verbose:
                logger.info(f"Processing {len(files)} files with {self.num_workers} workers")
            
            with ThreadPoolExecutor(max_workers=self.num_workers) as executor:
                # Submit all tasks
                future_to_file = {}
                for file_path in files:
                    file_path = Path(file_path)
                    
                    # Determine output path
                    output_path = None
                    if output_dir:
                        if output_format.lower() == 'pdf':
                            output_path = output_dir / f"{file_path.stem}_ocr{file_path.suffix}"
                        else:
                            output_path = output_dir / f"{file_path.stem}.txt"
                    
                    # Submit the appropriate task based on file type
                    if file_path.suffix.lower() in ['.pdf']:
                        future = executor.submit(
                            self.ocr_pdf,
                            file_path,
                            output_path,
                            output_format,
                            **kwargs
                        )
                    else:
                        # Assume image
                        if output_format.lower() == 'pdf':
                            # Not applicable for images
                            continue
                        
                        future = executor.submit(
                            self.ocr_image,
                            file_path,
                            output_path,
                            **kwargs
                        )
                    
                    future_to_file[future] = file_path
                
                # Collect results as they complete
                for future in as_completed(future_to_file):
                    file_path = future_to_file[future]
                    try:
                        result = future.result()
                        results[str(file_path)] = result
                        if self.verbose:
                            logger.info(f"Completed processing: {file_path}")
                    except Exception as e:
                        logger.error(f"Error processing {file_path}: {e}")
        else:
            # Process sequentially
            for file_path in files:
                file_path = Path(file_path)
                
                # Determine output path
                output_path = None
                if output_dir:
                    if output_format.lower() == 'pdf':
                        output_path = output_dir / f"{file_path.stem}_ocr{file_path.suffix}"
                    else:
                        output_path = output_dir / f"{file_path.stem}.txt"
                
                try:
                    # Process based on file type
                    if file_path.suffix.lower() in ['.pdf']:
                        result = self.ocr_pdf(
                            file_path,
                            output_path,
                            output_format,
                            **kwargs
                        )
                    else:
                        # Assume image
                        if output_format.lower() == 'pdf':
                            # Not applicable for images, skip
                            continue
                        
                        result = self.ocr_image(
                            file_path,
                            output_path,
                            **kwargs
                        )
                    
                    results[str(file_path)] = result
                    if self.verbose:
                        logger.info(f"Completed processing: {file_path}")
                except Exception as e:
                    logger.error(f"Error processing {file_path}: {e}")
        
        return results
    
    def process_directory(
        self,
        directory: Union[str, Path],
        output_dir: Optional[Union[str, Path]] = None,
        output_format: str = 'pdf',
        file_extensions: List[str] = ['.pdf', '.png', '.jpg', '.jpeg', '.tiff', '.tif', '.bmp'],
        recursive: bool = False,
        **kwargs
    ) -> Dict[str, Union[str, Path]]:
        """
        Process all files in a directory.
        
        Args:
            directory: Path to the directory containing files
            output_dir: Directory to save the OCR'd files
            output_format: Format of the output ('pdf' or 'text')
            file_extensions: List of file extensions to process
            recursive: Whether to process subdirectories recursively
            **kwargs: Additional options to pass to the OCR engine
            
        Returns:
            Dictionary mapping input files to output files or extracted text
        """
        directory = Path(directory)
        if not directory.exists() or not directory.is_dir():
            raise ValueError(f"Directory not found: {directory}")
        
        # Collect files
        files = []
        
        # Normalize extensions
        file_extensions = [ext.lower() if ext.startswith('.') else f'.{ext.lower()}' for ext in file_extensions]
        
        if recursive:
            for ext in file_extensions:
                files.extend(directory.glob(f'**/*{ext}'))
        else:
            for ext in file_extensions:
                files.extend(directory.glob(f'*{ext}'))
        
        if not files:
            logger.warning(f"No files with extensions {file_extensions} found in {directory}")
            return {}
        
        if self.verbose:
            logger.info(f"Found {len(files)} files to process in {directory}")
        
        # Process the files
        return self.batch_process(
            files,
            output_dir,
            output_format,
            **kwargs
        )
    
    @staticmethod
    def get_available_engines() -> Dict[str, str]:
        """
        Get a dictionary of available OCR engines on the current system.
        
        Returns:
            Dictionary mapping engine names to description strings
        """
        engines = get_available_engines()
        return {name: engine.__doc__.strip().split('\n')[0] for name, engine in engines.items()}


# Convenience functions

def ocr_image(
    image_path: Union[str, Path],
    output_path: Optional[Union[str, Path]] = None,
    engine: Optional[Union[str, OCREngine]] = None,
    engine_options: Optional[Dict[str, Any]] = None,
    **kwargs
) -> str:
    """
    Convenience function to OCR a single image.
    
    Args:
        image_path: Path to the image file
        output_path: Path to save the extracted text (optional)
        engine: OCR engine to use
        engine_options: Dictionary of options for the OCR engine
        **kwargs: Additional options to pass to the OCR engine
        
    Returns:
        Extracted text from the image
    """
    processor = OCRProcessor(engine=engine, engine_options=engine_options)
    return processor.ocr_image(image_path, output_path, **kwargs)


def ocr_pdf(
    pdf_path: Union[str, Path],
    output_path: Optional[Union[str, Path]] = None,
    output_format: str = 'pdf',
    engine: Optional[Union[str, OCREngine]] = None,
    engine_options: Optional[Dict[str, Any]] = None,
    **kwargs
) -> Union[str, Path]:
    """
    Convenience function to OCR a single PDF.
    
    Args:
        pdf_path: Path to the PDF file
        output_path: Path to save the OCR'd PDF or text
        output_format: Format of the output ('pdf' or 'text')
        engine: OCR engine to use
        engine_options: Dictionary of options for the OCR engine
        **kwargs: Additional options to pass to the OCR engine
        
    Returns:
        If output_format is 'pdf', returns the path to the OCR'd PDF.
        If output_format is 'text', returns the extracted text.
    """
    processor = OCRProcessor(engine=engine, engine_options=engine_options)
    return processor.ocr_pdf(pdf_path, output_path, output_format, **kwargs)


def process_directory(
    directory: Union[str, Path],
    output_dir: Optional[Union[str, Path]] = None,
    output_format: str = 'pdf',
    engine: Optional[Union[str, OCREngine]] = None,
    engine_options: Optional[Dict[str, Any]] = None,
    num_workers: int = 1,
    **kwargs
) -> Dict[str, Union[str, Path]]:
    """
    Convenience function to process all files in a directory.
    
    Args:
        directory: Path to the directory containing files
        output_dir: Directory to save the OCR'd files
        output_format: Format of the output ('pdf' or 'text')
        engine: OCR engine to use
        engine_options: Dictionary of options for the OCR engine
        num_workers: Number of parallel workers
        **kwargs: Additional options to pass to the OCR engine
        
    Returns:
        Dictionary mapping input files to output files or extracted text
    """
    processor = OCRProcessor(
        engine=engine, 
        engine_options=engine_options,
        num_workers=num_workers,
        verbose=kwargs.pop('verbose', False)
    )
    return processor.process_directory(directory, output_dir, output_format, **kwargs) 