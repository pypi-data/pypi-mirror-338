"""
OCR engines for extracting text from PDF documents and images.

This module provides a unified interface for multiple OCR backends:
- Hugging Face models (stepfun-ai/GOT-OCR2_0)
- Tesseract OCR
- OCRmyPDF integration

Each OCR engine is implemented as a class that adheres to a common interface,
allowing for easy swapping between different backends.
"""

import os
import sys
import tempfile
import logging
import subprocess
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Dict, Optional, Union, Any, Tuple
import shutil

import pytesseract
from pdf2image import convert_from_path
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter

# Initialize logging
logger = logging.getLogger(__name__)


class OCREngine(ABC):
    """
    Abstract base class for OCR engines.
    
    This class defines the interface that all OCR engines must implement,
    providing a consistent way to perform OCR operations regardless of the
    underlying implementation.
    """
    
    @abstractmethod
    def process_image(self, image: Union[str, Path, Image.Image], **kwargs) -> str:
        """
        Process a single image and return the extracted text.
        
        Args:
            image: Path to image file or PIL Image object
            **kwargs: Additional implementation-specific options
            
        Returns:
            Extracted text content
        """
        pass
    
    @abstractmethod
    def process_pdf(
        self, 
        pdf_path: Union[str, Path], 
        output_path: Optional[Union[str, Path]] = None,
        **kwargs
    ) -> Optional[Union[str, Path]]:
        """
        Process a PDF file and either return the extracted text or save to an output file.
        
        Args:
            pdf_path: Path to the PDF file
            output_path: Path where the OCR'd PDF should be saved (optional)
            **kwargs: Additional implementation-specific options
            
        Returns:
            Extracted text content as string or Path to the output file, depending on implementation
        """
        pass
    
    @classmethod
    def is_available(cls) -> bool:
        """
        Check if the OCR engine is available on the current system.
        
        Returns:
            True if the engine is available, False otherwise
        """
        return True


class TesseractOCR(OCREngine):
    """
    OCR engine that uses Tesseract OCR via the pytesseract Python wrapper.
    """
    
    def __init__(
        self, 
        lang: str = 'eng',
        config: str = '--psm 1 --oem 3',
        timeout: int = 300,
        tesseract_path: Optional[str] = None
    ):
        """
        Initialize the Tesseract OCR engine.
        
        Args:
            lang: Language(s) to use (comma-separated list of ISO 639-2 codes)
            config: Tesseract configuration string
            timeout: Timeout in seconds for OCR operations
            tesseract_path: Path to the Tesseract executable (optional)
        """
        self.lang = lang
        self.config = config
        self.timeout = timeout
        
        # Configure Tesseract path if provided or if on Windows
        if tesseract_path:
            pytesseract.pytesseract.tesseract_cmd = tesseract_path
        elif sys.platform == 'win32' and not os.environ.get('TESSERACT_CMD'):
            # Default Windows path
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
    def process_image(self, image: Union[str, Path, Image.Image], **kwargs) -> str:
        """
        Process a single image using Tesseract OCR.
        
        Args:
            image: Path to image file or PIL Image object
            **kwargs: Additional options:
                - lang: Override default language
                - config: Override default configuration
                - timeout: Override default timeout
            
        Returns:
            Extracted text content
        """
        try:
            # Get configuration from kwargs or use instance defaults
            lang = kwargs.get('lang', self.lang)
            config = kwargs.get('config', self.config)
            timeout = kwargs.get('timeout', self.timeout)
            
            # Process using pytesseract
            if isinstance(image, (str, Path)):
                return pytesseract.image_to_string(
                    str(image),
                    lang=lang,
                    config=config,
                    timeout=timeout
                )
            else:
                return pytesseract.image_to_string(
                    image,
                    lang=lang,
                    config=config,
                    timeout=timeout
                )
        except Exception as e:
            logger.error(f"Error in Tesseract OCR: {e}")
            return f"[OCR Error: {str(e)}]"
    
    def process_pdf(
        self, 
        pdf_path: Union[str, Path], 
        output_path: Optional[Union[str, Path]] = None,
        **kwargs
    ) -> Optional[Union[str, Path]]:
        """
        Process a PDF file using Tesseract OCR.
        
        Args:
            pdf_path: Path to the PDF file
            output_path: Path where the OCR'd PDF should be saved (if None, extracted text is returned)
            **kwargs: Additional options:
                - lang: Override default language
                - config: Override default configuration
                - dpi: DPI for image conversion (default: 300)
                - img_format: Format for temporary images (default: 'png')
                - output_format: 'text' or 'pdf' (default is 'pdf' if output_path is provided, else 'text')
                - pages: List of page indices to process (default: all pages)
            
        Returns:
            If output_path is provided, returns the path to the OCR'd PDF.
            Otherwise, returns the extracted text content.
        """
        pdf_path = Path(pdf_path)
        output_format = kwargs.get('output_format', 'pdf' if output_path else 'text')
        pages = kwargs.get('pages', None)  # None means all pages
        dpi = kwargs.get('dpi', 300)
        img_format = kwargs.get('img_format', 'png')
        
        # Create a temporary directory for intermediate files
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir_path = Path(temp_dir)
            
            # Convert PDF to images
            try:
                images = convert_from_path(
                    str(pdf_path),
                    dpi=dpi,
                    output_folder=temp_dir,
                    fmt=img_format,
                    paths_only=True,
                    first_page=pages[0] + 1 if pages else None,
                    last_page=pages[-1] + 1 if pages else None
                )
            except Exception as e:
                logger.error(f"Error converting PDF to images: {e}")
                return None
            
            if not images:
                logger.warning(f"No images created from PDF: {pdf_path}")
                return None
            
            # Process the images
            if output_format == 'text':
                # Extract text from each image
                text_results = []
                for img_path in images:
                    text = self.process_image(img_path, **kwargs)
                    text_results.append(text)
                
                # Remove temporary files
                for img_path in images:
                    os.unlink(img_path)
                
                # Return the combined text
                return "\n\n".join(text_results)
            else:
                # Create OCR'd PDF
                if not output_path:
                    output_path = pdf_path.with_stem(f"{pdf_path.stem}_ocr")
                
                output_path = Path(output_path)
                
                # Create writer for the output PDF
                writer = PdfWriter()
                
                # Process each image
                for i, img_path in enumerate(images):
                    # Convert image to PDF with OCR
                    try:
                        # Generate searchable PDF from image
                        pdf_bytes = pytesseract.image_to_pdf_or_hocr(
                            str(img_path),
                            extension='pdf',
                            lang=kwargs.get('lang', self.lang),
                            config=kwargs.get('config', self.config)
                        )
                        
                        # Save the PDF to a temporary file
                        ocr_pdf_path = temp_dir_path / f"page_{i}.pdf"
                        with open(ocr_pdf_path, 'wb') as f:
                            f.write(pdf_bytes)
                        
                        # Add to the writer
                        writer.append(str(ocr_pdf_path))
                        
                    except Exception as e:
                        logger.error(f"Error OCRing page {i+1}: {e}")
                
                # Write the output file
                with open(output_path, 'wb') as f:
                    writer.write(f)
                
                return output_path
    
    @classmethod
    def is_available(cls) -> bool:
        """
        Check if Tesseract OCR is available on the current system.
        
        Returns:
            True if Tesseract is available, False otherwise
        """
        try:
            version = pytesseract.get_tesseract_version()
            return version is not None
        except Exception:
            return False


class OCRMyPDF(OCREngine):
    """
    OCR engine that uses the OCRmyPDF command-line tool.
    """
    
    def __init__(
        self, 
        lang: str = 'eng',
        deskew: bool = True,
        clean: bool = True,
        optimize: int = 1,
        jobs: Optional[int] = None,
        output_type: str = 'pdf',
        force_ocr: bool = False,
        binary_path: Optional[str] = None
    ):
        """
        Initialize the OCRmyPDF engine.
        
        Args:
            lang: Language(s) to use (comma-separated list of ISO 639-2 codes)
            deskew: Whether to deskew pages before OCR
            clean: Whether to clean pages before OCR
            optimize: Optimization level (0-3)
            jobs: Number of parallel jobs (default: system CPU count)
            output_type: Output type ('pdf', 'pdfa')
            force_ocr: Whether to force OCR on all pages
            binary_path: Path to the OCRmyPDF executable (optional)
        """
        self.lang = lang
        self.deskew = deskew
        self.clean = clean
        self.optimize = optimize
        self.jobs = jobs or os.cpu_count() or 1
        self.output_type = output_type
        self.force_ocr = force_ocr
        self.binary_path = binary_path or 'ocrmypdf'
    
    def process_image(self, image: Union[str, Path, Image.Image], **kwargs) -> str:
        """
        Process a single image using OCRmyPDF.
        
        Note: OCRmyPDF doesn't directly support image input, so this method
        converts the image to a temporary PDF first.
        
        Args:
            image: Path to image file or PIL Image object
            **kwargs: Additional options
            
        Returns:
            Extracted text content
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir_path = Path(temp_dir)
            
            # Convert image to temporary PDF
            if isinstance(image, (str, Path)):
                image_path = Path(image)
                img = Image.open(image_path)
            else:
                img = image
                image_path = temp_dir_path / "input.png"
                img.save(image_path)
            
            # Save as PDF
            pdf_path = temp_dir_path / "input.pdf"
            img.save(pdf_path, 'PDF')
            
            # Process the PDF
            output_path = temp_dir_path / "output.pdf"
            self.process_pdf(pdf_path, output_path, **kwargs)
            
            # Extract text from the OCR'd PDF
            try:
                output_text = ""
                reader = PdfReader(str(output_path))
                for page in reader.pages:
                    output_text += page.extract_text() + "\n\n"
                return output_text.strip()
            except Exception as e:
                logger.error(f"Error extracting text from OCR'd PDF: {e}")
                return f"[OCR Error: {str(e)}]"
    
    def process_pdf(
        self, 
        pdf_path: Union[str, Path], 
        output_path: Optional[Union[str, Path]] = None,
        **kwargs
    ) -> Optional[Path]:
        """
        Process a PDF file using OCRmyPDF.
        
        Args:
            pdf_path: Path to the PDF file
            output_path: Path where the OCR'd PDF should be saved
            **kwargs: Additional options:
                - lang: Override default language
                - deskew: Override default deskew setting
                - clean: Override default clean setting
                - optimize: Override default optimization level
                - force_ocr: Override default force_ocr setting
                - jobs: Override default jobs setting
                - output_type: Override default output type
                - extra_args: List of additional command-line arguments
            
        Returns:
            Path to the OCR'd PDF or None if processing failed
        """
        pdf_path = Path(pdf_path)
        
        if output_path is None:
            output_path = pdf_path.with_stem(f"{pdf_path.stem}_ocr")
        
        output_path = Path(output_path)
        
        # Build the command
        cmd = [self.binary_path]
        
        # Add common options
        if kwargs.get('force_ocr', self.force_ocr):
            cmd.append('--force-ocr')
        
        if kwargs.get('deskew', self.deskew):
            cmd.append('--deskew')
        
        if kwargs.get('clean', self.clean):
            cmd.append('--clean')
        
        # Language
        lang = kwargs.get('lang', self.lang)
        cmd.extend(['--language', lang])
        
        # Optimization
        optimize = kwargs.get('optimize', self.optimize)
        cmd.extend(['--optimize', str(optimize)])
        
        # Output type
        output_type = kwargs.get('output_type', self.output_type)
        cmd.extend(['--output-type', output_type])
        
        # Jobs
        jobs = kwargs.get('jobs', self.jobs)
        cmd.extend(['--jobs', str(jobs)])
        
        # Skip text
        cmd.append('--skip-text')
        
        # Extra arguments
        extra_args = kwargs.get('extra_args', [])
        if extra_args:
            cmd.extend(extra_args)
        
        # Input and output paths
        cmd.extend([str(pdf_path), str(output_path)])
        
        # Run the command
        try:
            subprocess.run(
                cmd, 
                check=True, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                text=True
            )
            return output_path
        except subprocess.CalledProcessError as e:
            logger.error(f"OCRmyPDF error: {e}, stderr: {e.stderr}")
            return None
        except Exception as e:
            logger.error(f"Error running OCRmyPDF: {e}")
            return None
    
    @classmethod
    def is_available(cls) -> bool:
        """
        Check if OCRmyPDF is available on the current system.
        
        Returns:
            True if OCRmyPDF is available, False otherwise
        """
        try:
            result = subprocess.run(
                ['ocrmypdf', '--version'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            return result.returncode == 0
        except Exception:
            return False


class HuggingFaceOCR(OCREngine):
    """
    OCR engine that uses Hugging Face models for OCR.
    """
    
    def __init__(
        self,
        model_name: str = 'stepfun-ai/GOT-OCR2_0',
        device: str = 'auto',
        trust_remote_code: bool = True,
        load_in_8bit: bool = False,
        load_in_4bit: bool = False,
        ocr_type: str = 'ocr'
    ):
        """
        Initialize the Hugging Face OCR engine.
        
        Args:
            model_name: Name of the Hugging Face model to use
            device: Device to use ('auto', 'cpu', 'cuda', etc.)
            trust_remote_code: Whether to trust remote code
            load_in_8bit: Whether to load the model in 8-bit precision
            load_in_4bit: Whether to load the model in 4-bit precision
            ocr_type: OCR type ('ocr' for plain text, 'format' for formatted OCR)
        """
        self.model_name = model_name
        self.device = device
        self.trust_remote_code = trust_remote_code
        self.load_in_8bit = load_in_8bit
        self.load_in_4bit = load_in_4bit
        self.ocr_type = ocr_type
        self.model = None
        self.tokenizer = None
    
    def _load_model(self):
        """
        Load the Hugging Face model if not already loaded.
        """
        if self.model is not None:
            return
        
        try:
            from transformers import AutoModel, AutoTokenizer
            
            # Load tokenizer
            self.tokenizer = AutoTokenizer.from_pretrained(
                self.model_name,
                trust_remote_code=self.trust_remote_code
            )
            
            # Load model
            self.model = AutoModel.from_pretrained(
                self.model_name,
                trust_remote_code=self.trust_remote_code,
                device_map=self.device,
                load_in_8bit=self.load_in_8bit,
                load_in_4bit=self.load_in_4bit
            )
            
            # Set model to evaluation mode
            self.model = self.model.eval()
            
            logger.info(f"Successfully loaded Hugging Face model: {self.model_name}")
        except Exception as e:
            logger.error(f"Error loading Hugging Face model: {e}")
            raise
    
    def process_image(self, image: Union[str, Path, Image.Image], **kwargs) -> str:
        """
        Process a single image using a Hugging Face model.
        
        Args:
            image: Path to image file or PIL Image object
            **kwargs: Additional options:
                - ocr_type: OCR type ('ocr' or 'format')
            
        Returns:
            Extracted text content
        """
        # Load model if not already loaded
        if self.model is None:
            self._load_model()
        
        # Prepare the image
        img_path = None
        is_temp = False
        
        try:
            if isinstance(image, (str, Path)):
                img_path = str(image)
            else:
                # Save image to a temporary file
                tmp_dir = tempfile.mkdtemp()
                img_path = os.path.join(tmp_dir, "image.png")
                image.save(img_path)
                is_temp = True
            
            # Process the image
            ocr_type = kwargs.get('ocr_type', self.ocr_type)
            result = self.model.chat(
                self.tokenizer,
                img_path,
                ocr_type=ocr_type.lower()
            )
            
            return result
        except Exception as e:
            logger.error(f"Error processing image with Hugging Face model: {e}")
            return f"[OCR Error: {str(e)}]"
        finally:
            # Clean up temporary file if created
            if is_temp and img_path:
                try:
                    os.unlink(img_path)
                    os.rmdir(os.path.dirname(img_path))
                except:
                    pass
    
    def process_pdf(
        self, 
        pdf_path: Union[str, Path], 
        output_path: Optional[Union[str, Path]] = None,
        **kwargs
    ) -> Optional[Union[str, Path]]:
        """
        Process a PDF file using a Hugging Face model.
        
        Args:
            pdf_path: Path to the PDF file
            output_path: Path where the OCR'd text should be saved
            **kwargs: Additional options:
                - ocr_type: OCR type ('ocr' or 'format')
                - format: Output format ('md' or 'txt')
                - dpi: DPI for image conversion (default: 300)
            
        Returns:
            Extracted text content or path to output file
        """
        # Load model if not already loaded
        if self.model is None:
            self._load_model()
        
        pdf_path = Path(pdf_path)
        output_format = kwargs.get('format', 'md')
        dpi = kwargs.get('dpi', 300)
        
        # Create a temporary directory for intermediate files
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir_path = Path(temp_dir)
            
            # Convert PDF to images
            try:
                images = convert_from_path(
                    str(pdf_path),
                    dpi=dpi,
                    output_folder=temp_dir,
                    fmt='png'
                )
            except Exception as e:
                logger.error(f"Error converting PDF to images: {e}")
                return None
            
            if not images:
                logger.warning(f"No images created from PDF: {pdf_path}")
                return None
            
            # Extract text using the model
            extracted_text = []
            for idx, image in enumerate(images, start=1):
                temp_image_path = temp_dir_path / f"page_{idx}.png"
                image.save(temp_image_path, "PNG")
                
                try:
                    ocr_result = self.process_image(
                        temp_image_path,
                        ocr_type=kwargs.get('ocr_type', self.ocr_type)
                    )
                    extracted_text.append(f"## Page {idx}\n\n{ocr_result}\n" if output_format == 'md' else f"Page {idx}\n\n{ocr_result}\n")
                except Exception as e:
                    logger.error(f"Error during OCR on page {idx}: {e}")
                    extracted_text.append(f"## Page {idx}\n\n[Error during OCR]\n" if output_format == 'md' else f"Page {idx}\n\n[Error during OCR]\n")
            
            # Save or return the extracted text
            if output_path:
                output_path = Path(output_path)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                
                with open(output_path, 'w', encoding='utf-8') as f:
                    if output_format == 'md':
                        f.write(f"# OCR Extraction: {pdf_path.name}\n\n")
                    for page_text in extracted_text:
                        f.write(page_text)
                
                return output_path
            else:
                return "\n".join(extracted_text)
    
    @classmethod
    def is_available(cls) -> bool:
        """
        Check if the required packages for Hugging Face OCR are available.
        
        Returns:
            True if required packages are available, False otherwise
        """
        try:
            from importlib import import_module
            import_module('transformers')
            return True
        except ImportError:
            return False


def get_available_engines() -> Dict[str, OCREngine]:
    """
    Get a dictionary of available OCR engines on the current system.
    
    Returns:
        Dictionary mapping engine names to engine classes
    """
    engines = {}
    
    # Check Tesseract
    if TesseractOCR.is_available():
        engines['tesseract'] = TesseractOCR
    
    # Check OCRmyPDF
    if OCRMyPDF.is_available():
        engines['ocrmypdf'] = OCRMyPDF
    
    # Check Hugging Face
    if HuggingFaceOCR.is_available():
        engines['huggingface'] = HuggingFaceOCR
    
    return engines


def get_default_engine() -> Optional[OCREngine]:
    """
    Get the best available OCR engine on the current system.
    
    Returns:
        An instance of the best available OCR engine or None if no engine is available
    """
    engines = get_available_engines()
    
    # Prefer OCRmyPDF, then Hugging Face, then Tesseract
    for engine_name in ['ocrmypdf', 'huggingface', 'tesseract']:
        if engine_name in engines:
            return engines[engine_name]()
    
    return None 