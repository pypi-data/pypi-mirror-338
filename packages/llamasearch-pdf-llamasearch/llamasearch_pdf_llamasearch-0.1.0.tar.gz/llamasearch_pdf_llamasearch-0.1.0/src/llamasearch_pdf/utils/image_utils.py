"""
Image compression and optimization utilities.

This module provides functions for optimizing images for PDF inclusion,
with configurable quality settings and progress tracking.
"""

import os
import logging
from pathlib import Path
from typing import List, Optional, Tuple, Union, Dict, Any, Set

from PIL import Image, ImageOps, UnidentifiedImageError
from rich.progress import Progress, TextColumn, BarColumn, TaskID

# Configure logging
logger = logging.getLogger(__name__)

class ImageCompressor:
    """
    A utility class for compressing and optimizing images for PDF inclusion.
    
    This class provides methods for compressing individual images or batch
    processing entire directories with configurable quality settings.
    """
    
    # Default supported image formats
    SUPPORTED_FORMATS: Set[str] = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp'}
    
    def __init__(
        self, 
        jpeg_quality: int = 85, 
        png_compression: int = 9,
        webp_quality: int = 80,
        auto_orient: bool = True,
        max_dimension: Optional[int] = None,
        supported_formats: Optional[Set[str]] = None
    ):
        """
        Initialize the image compressor with quality settings.
        
        Args:
            jpeg_quality: Quality setting for JPEG images (0-100)
            png_compression: Compression level for PNG images (0-9)
            webp_quality: Quality setting for WebP images (0-100)
            auto_orient: Whether to automatically rotate images based on EXIF data
            max_dimension: Maximum dimension (width or height) to resize images to
            supported_formats: Set of file extensions to process. Defaults to class constant if None.
        """
        self.jpeg_quality = jpeg_quality
        self.png_compression = png_compression
        self.webp_quality = webp_quality
        self.auto_orient = auto_orient
        self.max_dimension = max_dimension
        self.supported_formats = supported_formats or self.SUPPORTED_FORMATS
        
    def compress_image(
        self, 
        input_path: Union[str, Path], 
        output_path: Union[str, Path],
        preserve_metadata: bool = True
    ) -> bool:
        """
        Compress a single image with optimized settings for PDF inclusion.
        
        Args:
            input_path: Path to the input image
            output_path: Path where the compressed image should be saved
            preserve_metadata: Whether to preserve image metadata during compression
            
        Returns:
            bool: True if compression succeeded, False otherwise
        """
        try:
            input_path = Path(input_path)
            output_path = Path(output_path)
            
            # Create output directory if it doesn't exist
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with Image.open(input_path) as img:
                # Auto-orient based on EXIF data if requested
                if self.auto_orient:
                    img = ImageOps.exif_transpose(img)
                
                # Resize image if max_dimension is specified
                if self.max_dimension:
                    width, height = img.size
                    if width > self.max_dimension or height > self.max_dimension:
                        if width > height:
                            new_width = self.max_dimension
                            new_height = int(height * (self.max_dimension / width))
                        else:
                            new_height = self.max_dimension
                            new_width = int(width * (self.max_dimension / height))
                        img = img.resize((new_width, new_height), Image.LANCZOS)
                
                # Convert RGBA to RGB if saving as JPEG
                if img.mode in ('RGBA', 'LA') and output_path.suffix.lower() in ('.jpg', '.jpeg'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    background.paste(img, mask=img.split()[-1])
                    img = background
                elif img.mode == 'P' and output_path.suffix.lower() not in ('.png', '.gif'):
                    img = img.convert('RGB')
                
                # Save with format-specific optimizations
                if output_path.suffix.lower() in ('.jpg', '.jpeg'):
                    img.save(output_path, 'JPEG', 
                             quality=self.jpeg_quality, 
                             optimize=True,
                             progressive=True)
                elif output_path.suffix.lower() == '.png':
                    img.save(output_path, 'PNG', 
                             optimize=True, 
                             compress_level=self.png_compression)
                elif output_path.suffix.lower() == '.webp':
                    img.save(output_path, 'WEBP', 
                             quality=self.webp_quality,
                             method=6)  # Higher value = better compression but slower
                else:
                    img.save(output_path, optimize=True)
                
            return True
            
        except UnidentifiedImageError as e:
            logger.warning(f"Unidentified image format in {input_path}: {e}")
            return False
        except Exception as e:
            logger.error(f"Failed to compress image {input_path}: {e}")
            return False
    
    def process_directory(
        self, 
        folder_path: Union[str, Path],
        output_folder: Optional[Union[str, Path]] = None,
        recursive: bool = True,
        suffix: str = "-compressed",
        progress: Optional[Progress] = None
    ) -> Tuple[int, int]:
        """
        Process all supported images in a directory, compressing each one.
        
        Args:
            folder_path: Directory containing images to compress
            output_folder: Directory where compressed images should be saved (if None, 
                           images are saved in the same location with a suffix)
            recursive: Whether to process subdirectories
            suffix: Suffix to add to filenames when saving in the same directory
            progress: Optional rich Progress instance for tracking
            
        Returns:
            Tuple[int, int]: (number of successfully compressed images, total images processed)
        """
        folder_path = Path(folder_path)
        if output_folder:
            output_folder = Path(output_folder)
            output_folder.mkdir(parents=True, exist_ok=True)
        
        # Find all image files
        image_files = []
        
        if recursive:
            for root, _, files in os.walk(folder_path):
                root_path = Path(root)
                for file in files:
                    file_path = root_path / file
                    if file_path.suffix.lower() in self.supported_formats:
                        image_files.append(file_path)
        else:
            for file in folder_path.iterdir():
                if file.is_file() and file.suffix.lower() in self.supported_formats:
                    image_files.append(file)
        
        # Process the images
        success_count = 0
        task_id = None
        
        # If a progress instance was provided, create a task
        if progress:
            task_id = progress.add_task(
                "[cyan]Compressing images...", 
                total=len(image_files)
            )
            
        for img_path in image_files:
            # Determine output path
            if output_folder:
                rel_path = img_path.relative_to(folder_path) if recursive else img_path.name
                out_path = output_folder / rel_path
            else:
                stem = img_path.stem
                out_path = img_path.with_name(f"{stem}{suffix}{img_path.suffix}")
            
            # Compress the image
            if self.compress_image(img_path, out_path):
                success_count += 1
                
            # Update progress if a progress instance was provided
            if progress and task_id is not None:
                progress.update(task_id, advance=1)
        
        return success_count, len(image_files)


def compress_images_cli(
    input_dir: str, 
    output_dir: Optional[str] = None, 
    quality: int = 85,
    recursive: bool = True
) -> None:
    """
    Command-line interface for the image compression utility.
    
    Args:
        input_dir: Directory containing images to compress
        output_dir: Directory where compressed images should be saved
        quality: JPEG quality setting (0-100)
        recursive: Whether to process subdirectories
    """
    from rich.console import Console
    from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn
    
    console = Console()
    console.print("[bold]LlamaSearch Image Compression Utility[/bold]")
    console.print("=======================================")
    
    compressor = ImageCompressor(jpeg_quality=quality)
    
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        "•",
        TimeElapsedColumn(),
        "•",
        TimeRemainingColumn(),
        console=console
    ) as progress:
        success_count, total_count = compressor.process_directory(
            input_dir, 
            output_dir, 
            recursive=recursive,
            progress=progress
        )
    
    console.print(f"\n[green]Successfully compressed {success_count} of {total_count} images.")
    if output_dir:
        console.print(f"Compressed images saved to: [bold]{output_dir}[/bold]")
    else:
        console.print("Compressed images saved in the original directory with '-compressed' suffix.")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Compress and optimize images for PDF inclusion")
    parser.add_argument("input_dir", help="Directory containing images to compress")
    parser.add_argument("-o", "--output-dir", help="Directory where compressed images should be saved")
    parser.add_argument("-q", "--quality", type=int, default=85, help="JPEG quality (0-100)")
    parser.add_argument("-r", "--recursive", action="store_true", help="Process subdirectories")
    
    args = parser.parse_args()
    
    compress_images_cli(args.input_dir, args.output_dir, args.quality, args.recursive) 