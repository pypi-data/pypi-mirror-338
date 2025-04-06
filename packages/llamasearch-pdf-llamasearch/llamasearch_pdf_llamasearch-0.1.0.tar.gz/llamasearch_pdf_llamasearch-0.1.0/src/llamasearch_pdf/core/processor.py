"""
Core PDF processing functionality.

This module provides the main PDF processing capabilities, including:
- File scanning
- PDF merging
- PDF conversion
- Image to PDF conversion
- Multi-threaded processing

The PDFProcessor class serves as the main entry point for PDF operations
with flexible configuration options and progress tracking.
"""

import os
import sys
import logging
import tempfile
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple, Set, Union, Any, Callable
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn, TimeRemainingColumn
from rich.logging import RichHandler

# Third-party imports for PDF operations
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
from PIL import Image, ImageOps

# Initialize logging
logger = logging.getLogger(__name__)


class PDFProcessor:
    """
    Core PDF processing class that provides a unified interface for PDF operations.
    
    This class handles file discovery, PDF conversion, merging, and other operations
    with configurable options and progress tracking.
    """
    
    # Default supported image formats
    SUPPORTED_IMAGE_FORMATS: Set[str] = {'.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif', '.webp'}
    
    def __init__(
        self,
        output_dir: Optional[Union[str, Path]] = None,
        temp_dir: Optional[Union[str, Path]] = None,
        max_workers: Optional[int] = None,
        supported_image_formats: Optional[Set[str]] = None,
        console: Optional[Console] = None
    ):
        """
        Initialize the PDF processor with configuration options.
        
        Args:
            output_dir: Directory where processed PDF files will be saved
            temp_dir: Directory for temporary files
            max_workers: Maximum number of worker threads for parallel processing
            supported_image_formats: Set of image file extensions to process
            console: Rich console instance for output
        """
        # Initialize configuration
        self.output_base_dir = Path(output_dir) if output_dir else Path("llamasearch_output")
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.max_workers = max_workers or (os.cpu_count() or 4)
        self.supported_image_formats = supported_image_formats or self.SUPPORTED_IMAGE_FORMATS
        self.console = console or Console()
        
        # Runtime properties
        self._temp_dir = None
        self._temp_created = False
        
        # Create output directory
        self.output_base_dir.mkdir(parents=True, exist_ok=True)
        
        # Set up temp directory if provided
        if temp_dir:
            self._temp_dir = Path(temp_dir)
            self._temp_dir.mkdir(parents=True, exist_ok=True)
    
    @property
    def temp_dir(self) -> Path:
        """
        Get the temporary directory, creating it if necessary.
        
        Returns:
            Path to the temporary directory
        """
        if self._temp_dir is None:
            self._temp_dir = Path(tempfile.mkdtemp(prefix="llamapdf_"))
            self._temp_created = True
        return self._temp_dir
    
    def create_output_dir(self, suffix: str = "") -> Path:
        """
        Create a timestamped output directory for the current operation.
        
        Args:
            suffix: Optional suffix to add to the directory name
            
        Returns:
            Path to the created output directory
        """
        dir_name = f"{suffix}_{self.timestamp}" if suffix else self.timestamp
        output_dir = self.output_base_dir / dir_name
        output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir
    
    def cleanup(self) -> None:
        """
        Clean up temporary resources.
        """
        if self._temp_created and self._temp_dir and self._temp_dir.exists():
            shutil.rmtree(self._temp_dir)
            self._temp_dir = None
            self._temp_created = False
    
    def find_files(
        self, 
        directory: Union[str, Path],
        recursive: bool = True,
        progress: Optional[Progress] = None
    ) -> Tuple[List[Path], List[Path]]:
        """
        Find all PDF files and supported image files in a directory.
        
        Args:
            directory: Directory to scan
            recursive: Whether to scan subdirectories
            progress: Optional Progress instance for tracking
            
        Returns:
            Tuple containing (list of PDF files, list of image files)
        """
        directory = Path(directory)
        pdf_files = []
        image_files = []
        
        task_id = None
        if progress:
            task_id = progress.add_task(
                "[cyan]Scanning directory...", 
                total=None
            )
        
        try:
            if recursive:
                for root, _, files in os.walk(directory):
                    root_path = Path(root)
                    for file in files:
                        file_path = root_path / file
                        suffix = file_path.suffix.lower()
                        
                        if suffix == '.pdf':
                            pdf_files.append(file_path)
                        elif suffix in self.supported_image_formats:
                            image_files.append(file_path)
            else:
                for file_path in directory.iterdir():
                    if not file_path.is_file():
                        continue
                        
                    suffix = file_path.suffix.lower()
                    if suffix == '.pdf':
                        pdf_files.append(file_path)
                    elif suffix in self.supported_image_formats:
                        image_files.append(file_path)
        finally:
            if progress and task_id is not None:
                progress.update(task_id, completed=True)
        
        return pdf_files, image_files
    
    def convert_image_to_pdf(
        self,
        image_path: Union[str, Path],
        output_path: Optional[Union[str, Path]] = None,
        dpi: int = 300,
        quality: int = 90
    ) -> Optional[Path]:
        """
        Convert an image to a PDF file.
        
        Args:
            image_path: Path to the input image
            output_path: Path where the PDF should be saved (if None, a path in
                         the temp directory will be generated)
            dpi: DPI setting for the PDF
            quality: Quality setting for JPEG compression (0-100)
            
        Returns:
            Path to the created PDF file or None if conversion failed
        """
        image_path = Path(image_path)
        
        if output_path is None:
            output_path = self.temp_dir / f"{image_path.stem}_converted.pdf"
        else:
            output_path = Path(output_path)
            
        try:
            # Create output directory if needed
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with Image.open(image_path) as img:
                # Auto-orient based on EXIF data
                img = ImageOps.exif_transpose(img)
                
                # Convert transparency to white background if needed
                if img.mode in ('RGBA', 'LA'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[-1])
                    img = background
                elif img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Save as PDF
                img.save(
                    output_path,
                    'PDF',
                    resolution=dpi,
                    quality=quality
                )
                
            return output_path
        except Exception as e:
            logger.error(f"Error converting image {image_path} to PDF: {e}")
            return None
    
    def batch_convert_images(
        self,
        image_files: List[Union[str, Path]],
        output_dir: Optional[Union[str, Path]] = None,
        progress: Optional[Progress] = None
    ) -> List[Path]:
        """
        Convert multiple images to PDF files in parallel.
        
        Args:
            image_files: List of image files to convert
            output_dir: Directory where PDFs should be saved (if None, temp directory is used)
            progress: Optional Progress instance for tracking
            
        Returns:
            List of paths to the created PDF files
        """
        converted_pdfs = []
        if not image_files:
            return converted_pdfs
        
        task_id = None
        if progress:
            task_id = progress.add_task(
                "[cyan]Converting images to PDF...",
                total=len(image_files)
            )
        
        def convert_image_with_progress(image_path: Path) -> Optional[Path]:
            pdf_path = self.convert_image_to_pdf(
                image_path,
                output_path=output_dir / f"{image_path.stem}.pdf" if output_dir else None
            )
            if progress and task_id is not None:
                progress.update(task_id, advance=1)
            return pdf_path
        
        # Process in parallel
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(convert_image_with_progress, img) for img in image_files]
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    converted_pdfs.append(result)
        
        return converted_pdfs
    
    def merge_pdfs(
        self,
        pdf_files: List[Union[str, Path]],
        output_path: Union[str, Path],
        progress: Optional[Progress] = None
    ) -> Optional[Path]:
        """
        Merge multiple PDF files into a single PDF.
        
        Args:
            pdf_files: List of PDF files to merge
            output_path: Path where the merged PDF should be saved
            progress: Optional Progress instance for tracking
            
        Returns:
            Path to the merged PDF file or None if merging failed
        """
        if not pdf_files:
            logger.warning("No PDF files provided for merging")
            return None
        
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        task_id = None
        if progress:
            task_id = progress.add_task(
                "[cyan]Merging PDF files...",
                total=len(pdf_files)
            )
        
        merger = PdfMerger()
        
        try:
            for pdf in pdf_files:
                try:
                    merger.append(str(pdf))
                    if progress and task_id is not None:
                        progress.update(task_id, advance=1)
                except Exception as e:
                    logger.error(f"Error merging {pdf}: {e}")
            
            merger.write(str(output_path))
            merger.close()
            return output_path
        except Exception as e:
            logger.error(f"Error during PDF merging: {e}")
            return None
    
    def validate_pdf(
        self,
        pdf_path: Union[str, Path]
    ) -> bool:
        """
        Validate if a PDF file is readable and not corrupted.
        
        Args:
            pdf_path: Path to the PDF file to validate
            
        Returns:
            True if the PDF is valid, False otherwise
        """
        try:
            pdf_path = Path(pdf_path)
            if not pdf_path.exists():
                logger.error(f"PDF file does not exist: {pdf_path}")
                return False
                
            reader = PdfReader(str(pdf_path))
            # Try accessing the first page to verify it's readable
            if len(reader.pages) > 0:
                _ = reader.pages[0]
                return True
            else:
                logger.warning(f"PDF file contains no pages: {pdf_path}")
                return False
        except Exception as e:
            logger.error(f"Error validating PDF {pdf_path}: {e}")
            return False
    
    def process_directory(
        self,
        input_dir: Union[str, Path],
        output_name: Optional[str] = None,
        recursive: bool = True,
        merge: bool = True,
        optimize: bool = True
    ) -> Optional[Path]:
        """
        Process a directory containing PDFs and/or images, producing a merged PDF.
        
        Args:
            input_dir: Directory to process
            output_name: Base name for the output PDF (without extension)
            recursive: Whether to scan subdirectories
            merge: Whether to merge all PDFs into one file
            optimize: Whether to optimize the output PDF
            
        Returns:
            Path to the processed PDF file or None if processing failed
        """
        input_dir = Path(input_dir)
        
        # Create output directory
        output_dir = self.create_output_dir(suffix="processed")
        
        output_name = output_name or input_dir.name
        merged_path = output_dir / f"{output_name}_merged.pdf"
        
        # Set up console and progress tracking
        self.console.print(f"[bold cyan]Processing directory: {input_dir}[/bold cyan]")
        
        # Find files
        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            "[progress.percentage]{task.percentage:>3.0f}%",
            "•",
            TimeElapsedColumn(),
            "•",
            TimeRemainingColumn(),
            console=self.console
        ) as progress:
            pdf_files, image_files = self.find_files(input_dir, recursive, progress)
            
            total_files = len(pdf_files) + len(image_files)
            if total_files == 0:
                self.console.print("[yellow]No PDF or image files found to process!")
                return None
            
            self.console.print(f"Found [cyan]{len(pdf_files)}[/cyan] PDFs and [cyan]{len(image_files)}[/cyan] images")
            
            # Convert images to PDFs
            converted_pdfs = []
            if image_files:
                self.console.print("Converting images to PDFs...")
                converted_pdfs = self.batch_convert_images(image_files, progress=progress)
            
            # Merge PDFs if requested
            if merge and (pdf_files or converted_pdfs):
                self.console.print("Merging PDFs...")
                all_pdfs = pdf_files + converted_pdfs
                if self.merge_pdfs(all_pdfs, merged_path, progress=progress):
                    self.console.print(f"[green]Successfully created merged PDF: {merged_path}")
                    
                    # Optimize the PDF if requested
                    if optimize:
                        optimized_path = output_dir / f"{output_name}_optimized.pdf"
                        if self.optimize_pdf(merged_path, optimized_path, progress=progress):
                            self.console.print(f"[green]Successfully optimized PDF: {optimized_path}")
                            return optimized_path
                    
                    return merged_path
            else:
                # Just return the list of PDF files
                self.console.print(f"[green]Processed {len(pdf_files) + len(converted_pdfs)} PDF files")
                return merged_path if merge else None
        
        return None
    
    def optimize_pdf(
        self,
        input_path: Union[str, Path],
        output_path: Union[str, Path],
        progress: Optional[Progress] = None
    ) -> Optional[Path]:
        """
        Optimize a PDF file by reducing its size.
        
        Args:
            input_path: Path to the input PDF
            output_path: Path where the optimized PDF should be saved
            progress: Optional Progress instance for tracking
            
        Returns:
            Path to the optimized PDF file or None if optimization failed
        """
        input_path = Path(input_path)
        output_path = Path(output_path)
        
        task_id = None
        if progress:
            task_id = progress.add_task(
                "[cyan]Optimizing PDF...",
                total=None
            )
        
        try:
            # Basic optimization using PyPDF2
            reader = PdfReader(str(input_path))
            writer = PdfWriter()
            
            # Copy pages with optimization
            for page in reader.pages:
                writer.add_page(page)
            
            # Set metadata
            metadata = reader.metadata or {}
            writer.add_metadata(metadata)
            
            # Write optimized file
            with open(output_path, 'wb') as f:
                writer.write(f)
            
            if progress and task_id is not None:
                progress.update(task_id, completed=True)
            
            return output_path
        except Exception as e:
            logger.error(f"Error optimizing PDF {input_path}: {e}")
            if progress and task_id is not None:
                progress.update(task_id, completed=True)
            return None
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cleanup()
        
    def __del__(self):
        self.cleanup() 