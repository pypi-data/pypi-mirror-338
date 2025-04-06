"""
Command-line interface for text extraction operations.

This module provides a CLI for extracting and processing text from PDF documents.
"""

import os
import sys
import argparse
import logging
from pathlib import Path
from typing import List, Optional

from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn
from rich.logging import RichHandler

from ..core import extract_text, TextExtractor


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


def extract_text_command(args):
    """
    Extract text from a PDF document.
    
    Args:
        args: Command-line arguments
    """
    console = Console()
    
    # Get input file path
    input_path = Path(args.input)
    if not input_path.exists():
        console.print(f"[red]Error:[/red] File not found: {input_path}")
        return 1
    
    # Determine output path
    output_path = args.output
    if not output_path and not args.stdout:
        # If no output path and not printing to stdout, create default output path
        output_path = input_path.with_suffix('.txt')
    
    # Set up extractor options
    preserve_layout = not args.flow_text
    
    try:
        # Extract text
        if args.pages:
            try:
                # Parse page ranges (e.g., "1-3,5,7-9")
                page_numbers = []
                for part in args.pages.split(','):
                    if '-' in part:
                        start, end = map(int, part.split('-'))
                        # Convert to 0-based indexing
                        page_numbers.extend(range(start - 1, end))
                    else:
                        # Convert to 0-based indexing
                        page_numbers.append(int(part) - 1)
            except ValueError:
                console.print(f"[red]Error:[/red] Invalid page range: {args.pages}")
                return 1
        else:
            page_numbers = None
        
        # Extract text
        console.print(f"Extracting text from: [cyan]{input_path}[/cyan]")
        
        result = extract_text(
            input_path,
            output_path=None if args.stdout else output_path,
            page_numbers=page_numbers,
            preserve_layout=preserve_layout,
            verbose=args.verbose
        )
        
        # If output is sent to stdout, print it
        if args.stdout:
            if isinstance(result, dict):
                for page_num, text in sorted(result.items()):
                    console.print(f"[bold cyan]=== Page {page_num + 1} ===[/bold cyan]")
                    console.print(text)
                    console.print("")
        else:
            console.print(f"Extracted text saved to: [green]{result}[/green]")
        
        return 0
        
    except Exception as e:
        console.print(f"[red]Error extracting text:[/red] {str(e)}")
        if args.verbose:
            console.print_exception()
        return 1


def batch_extract_command(args):
    """
    Extract text from multiple PDF documents.
    
    Args:
        args: Command-line arguments
    """
    console = Console()
    
    # Get input directory
    input_dir = Path(args.input_dir)
    if not input_dir.is_dir():
        console.print(f"[red]Error:[/red] Directory not found: {input_dir}")
        return 1
    
    # Get or create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Set up extractor options
    preserve_layout = not args.flow_text
    
    # Find PDF files
    pdf_files = []
    glob_pattern = "**/*.pdf" if args.recursive else "*.pdf"
    for pdf_path in input_dir.glob(glob_pattern):
        if pdf_path.is_file():
            pdf_files.append(pdf_path)
    
    if not pdf_files:
        console.print(f"[yellow]No PDF files found in {input_dir}[/yellow]")
        return 0
    
    console.print(f"Found [cyan]{len(pdf_files)}[/cyan] PDF files to process")
    
    # Create TextExtractor instance
    extractor = TextExtractor(
        preserve_layout=preserve_layout,
        remove_hyphenation=True,
        normalize_whitespace=True,
        fallback_to_ocr=args.fallback_ocr
    )
    
    # Process files with progress tracking
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console
    ) as progress:
        # Create top-level task
        overall_task = progress.add_task(f"Processing {len(pdf_files)} files", total=len(pdf_files))
        
        for pdf_path in pdf_files:
            try:
                # Determine output path
                rel_path = pdf_path.relative_to(input_dir).with_suffix('.txt')
                out_path = output_dir / rel_path
                out_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Extract text
                progress.update(overall_task, description=f"Processing {pdf_path.name}")
                text_dict = extractor.extract_text_from_pdf(pdf_path, progress=progress)
                
                # Write text to output file
                with open(out_path, 'w', encoding='utf-8') as f:
                    for page_num, text in sorted(text_dict.items()):
                        f.write(f"=== Page {page_num + 1} ===\n\n")
                        f.write(text)
                        f.write("\n\n")
                
                progress.update(overall_task, advance=1)
                
            except Exception as e:
                console.print(f"[red]Error processing {pdf_path}:[/red] {str(e)}")
                if args.verbose:
                    console.print_exception()
                progress.update(overall_task, advance=1)
    
    console.print(f"[green]Text extraction complete. Results saved to: {output_dir}[/green]")
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    """
    Main entry point for the text extraction CLI.
    
    Args:
        argv: Command-line arguments
        
    Returns:
        Exit code (0 for success, non-zero for errors)
    """
    parser = argparse.ArgumentParser(
        description="LlamaSearch PDF Text Extraction Tool",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    # Global options
    parser.add_argument("--verbose", "-v", action="store_true", 
                        help="Enable verbose output")
    
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Single file text extraction
    extract_parser = subparsers.add_parser("extract", 
                                          help="Extract text from a single PDF")
    extract_parser.add_argument("input", help="Input PDF file")
    extract_parser.add_argument("--output", "-o", help="Output text file (default: input file with .txt extension)")
    extract_parser.add_argument("--pages", "-p", help="Pages to extract (comma-separated, ranges allowed: e.g., '1-3,5,7-9')")
    extract_parser.add_argument("--flow-text", "-f", action="store_true",
                               help="Treat text as a continuous flow, ignoring layout")
    extract_parser.add_argument("--stdout", "-s", action="store_true",
                               help="Print extracted text to stdout")
    extract_parser.set_defaults(func=extract_text_command)
    
    # Batch text extraction
    batch_parser = subparsers.add_parser("batch",
                                        help="Extract text from multiple PDFs")
    batch_parser.add_argument("input_dir", help="Input directory containing PDFs")
    batch_parser.add_argument("output_dir", help="Output directory for extracted text files")
    batch_parser.add_argument("--recursive", "-r", action="store_true",
                             help="Recursively process subdirectories")
    batch_parser.add_argument("--flow-text", "-f", action="store_true",
                             help="Treat text as a continuous flow, ignoring layout")
    batch_parser.add_argument("--fallback-ocr", action="store_true",
                             help="Fall back to OCR for PDFs with no extractable text")
    batch_parser.set_defaults(func=batch_extract_command)
    
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