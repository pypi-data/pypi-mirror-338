"""
Command-line interface for OCR operations.

This module provides a CLI for optical character recognition 
capabilities, allowing users to extract text from PDFs and images.
"""

import os
import sys
import argparse
import logging
from pathlib import Path
from typing import List, Optional

from rich.console import Console
from rich.progress import Progress, TextColumn, BarColumn
from rich.logging import RichHandler

from ..ocr import (
    ocr_pdf,
    ocr_image,
    process_directory,
    get_available_engines
)


def setup_logging(verbose: bool = False):
    """
    Set up logging configuration.
    
    Args:
        verbose: Whether to use verbose (DEBUG) logging
    """
    level = logging.DEBUG if verbose else logging.INFO
    
    # Configure rich logger
    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)]
    )
    
    # Set level for other libraries' loggers
    logging.getLogger("PIL").setLevel(logging.WARNING)
    logging.getLogger("pdf2image").setLevel(logging.WARNING)


def list_engines_command(args):
    """
    List available OCR engines.
    
    Args:
        args: Command-line arguments
    """
    console = Console()
    console.print("\n[bold cyan]Available OCR Engines:[/bold cyan]")
    
    engines = get_available_engines()
    if not engines:
        console.print("[yellow]  No OCR engines available. Please install one of:[/yellow]")
        console.print("  - Tesseract OCR (pytesseract)")
        console.print("  - OCRmyPDF")
        console.print("  - Hugging Face Transformers")
        return 1
    
    for name, description in engines.items():
        console.print(f"  [green]✓[/green] [bold]{name}[/bold]: {description}")
    
    return 0


def ocr_file_command(args):
    """
    OCR a single file (PDF or image).
    
    Args:
        args: Command-line arguments
    """
    console = Console()
    file_path = Path(args.input)
    
    # Validate input file
    if not file_path.exists():
        console.print(f"[red]Error:[/red] File not found: {file_path}")
        return 1
    
    # Prepare engine options
    engine_options = {}
    if args.language:
        engine_options['lang'] = args.language
    
    # Determine output path
    output_path = args.output
    if output_path and Path(output_path).is_dir():
        if args.format == "pdf" and file_path.suffix.lower() == '.pdf':
            output_path = Path(output_path) / f"{file_path.stem}_ocr.pdf"
        else:
            output_path = Path(output_path) / f"{file_path.stem}.txt"
    
    try:
        # Process based on file type
        if file_path.suffix.lower() == '.pdf':
            console.print(f"Processing PDF: [cyan]{file_path}[/cyan]")
            result = ocr_pdf(
                file_path, 
                output_path, 
                output_format=args.format,
                engine=args.engine,
                engine_options=engine_options,
                verbose=args.verbose
            )
            
            if args.format == "text" and not output_path:
                # Print extracted text to console
                console.print("\n[bold cyan]Extracted Text:[/bold cyan]")
                console.print("-" * 40)
                console.print(result)
            else:
                console.print(f"Output saved to: [green]{result}[/green]")
                
        else:
            # Assume it's an image
            console.print(f"Processing image: [cyan]{file_path}[/cyan]")
            result = ocr_image(
                file_path, 
                output_path,
                engine=args.engine,
                engine_options=engine_options,
                verbose=args.verbose
            )
            
            if not output_path:
                # Print extracted text to console
                console.print("\n[bold cyan]Extracted Text:[/bold cyan]")
                console.print("-" * 40)
                console.print(result)
            else:
                console.print(f"Output saved to: [green]{output_path}[/green]")
                
        return 0
        
    except Exception as e:
        console.print(f"[red]Error processing file:[/red] {str(e)}")
        if args.verbose:
            console.print_exception()
        return 1


def process_directory_command(args):
    """
    Process all PDFs and images in a directory.
    
    Args:
        args: Command-line arguments
    """
    console = Console()
    
    input_dir = Path(args.input)
    if not input_dir.is_dir():
        console.print(f"[red]Error:[/red] Directory not found: {input_dir}")
        return 1
    
    output_dir = Path(args.output)
    
    # Prepare engine options
    engine_options = {}
    if args.language:
        engine_options['lang'] = args.language
    
    console.print(f"Processing directory: [cyan]{input_dir}[/cyan]")
    console.print(f"Output directory: [cyan]{output_dir}[/cyan]")
    console.print(f"Output format: [cyan]{args.format}[/cyan]")
    
    try:
        results = process_directory(
            input_dir,
            output_dir,
            output_format=args.format,
            engine=args.engine,
            engine_options=engine_options,
            num_workers=args.workers,
            recursive=args.recursive,
            verbose=args.verbose,
            file_extensions=args.extensions.split(",") if args.extensions else None
        )
        
        console.print(f"Successfully processed [green]{len(results)}[/green] files.")
        return 0
        
    except Exception as e:
        console.print(f"[red]Error processing directory:[/red] {str(e)}")
        if args.verbose:
            console.print_exception()
        return 1


def main(argv: Optional[List[str]] = None) -> int:
    """
    Main entry point for the OCR CLI.
    
    Args:
        argv: Command-line arguments
        
    Returns:
        Exit code (0 for success, non-zero for errors)
    """
    parser = argparse.ArgumentParser(
        description="LlamaSearch PDF OCR Command-Line Tool",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    # Global options
    parser.add_argument("--verbose", "-v", action="store_true", 
                        help="Enable verbose output")
    
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # List OCR engines command
    list_parser = subparsers.add_parser("list-engines", 
                                       help="List available OCR engines")
    list_parser.set_defaults(func=list_engines_command)
    
    # File OCR command
    file_parser = subparsers.add_parser("file", help="OCR a single PDF or image file")
    file_parser.add_argument("input", help="Input PDF or image file")
    file_parser.add_argument("--output", "-o", help="Output file or directory")
    file_parser.add_argument("--format", "-f", choices=["pdf", "text"], default="pdf",
                           help="Output format (pdf or text)")
    file_parser.add_argument("--engine", "-e", help="OCR engine to use")
    file_parser.add_argument("--language", "-l", default="eng", 
                           help="OCR language(s), comma-separated (e.g., 'eng,fra')")
    file_parser.set_defaults(func=ocr_file_command)
    
    # Directory OCR command
    dir_parser = subparsers.add_parser("directory", 
                                     help="Process all PDFs and images in a directory")
    dir_parser.add_argument("input", help="Input directory")
    dir_parser.add_argument("--output", "-o", required=True, help="Output directory")
    dir_parser.add_argument("--format", "-f", choices=["pdf", "text"], default="pdf",
                          help="Output format (pdf or text)")
    dir_parser.add_argument("--engine", "-e", help="OCR engine to use")
    dir_parser.add_argument("--language", "-l", default="eng", 
                          help="OCR language(s), comma-separated (e.g., 'eng,fra')")
    dir_parser.add_argument("--workers", "-w", type=int, default=1, 
                          help="Number of worker processes")
    dir_parser.add_argument("--recursive", "-r", action="store_true", 
                          help="Process subdirectories recursively")
    dir_parser.add_argument("--extensions", help="Comma-separated list of file extensions to process")
    dir_parser.set_defaults(func=process_directory_command)
    
    # Parse arguments
    args = parser.parse_args(argv)
    
    # Set up logging
    setup_logging(args.verbose)
    
    # Execute command
    if hasattr(args, 'func'):
        return args.func(args)
    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main()) 