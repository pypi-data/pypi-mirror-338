#!/usr/bin/env python3
"""
Example script demonstrating the OCR capabilities of llamasearch-pdf.

This script shows how to use the OCR module to extract text from 
PDF documents and images, and how to batch process files.
"""

import os
import sys
import argparse
from pathlib import Path
import logging

# Add the parent directory to the Python path to allow importing llamasearch_pdf
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from llamasearch_pdf.ocr import (
    ocr_pdf, 
    ocr_image, 
    process_directory, 
    OCRProcessor,
    get_available_engines
)


def setup_logging(verbose):
    """Set up logging configuration."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )


def main():
    """Run the OCR example."""
    parser = argparse.ArgumentParser(description="OCR example for llamasearch-pdf")
    
    # Input options
    parser.add_argument("--input", "-i", type=str, help="Input file or directory")
    parser.add_argument("--output", "-o", type=str, help="Output file or directory")
    parser.add_argument("--format", "-f", type=str, choices=["pdf", "text"], default="pdf",
                      help="Output format (pdf or text)")
    
    # OCR engine options
    parser.add_argument("--engine", "-e", type=str, help="OCR engine to use (tesseract, ocrmypdf, huggingface)")
    parser.add_argument("--language", "-l", type=str, default="eng", 
                      help="OCR language(s), comma-separated (e.g., 'eng,fra')")
    
    # Processing options
    parser.add_argument("--workers", "-w", type=int, default=1, 
                      help="Number of worker processes for batch processing")
    parser.add_argument("--recursive", "-r", action="store_true", 
                      help="Process directories recursively")
    parser.add_argument("--verbose", "-v", action="store_true", 
                      help="Enable verbose output")
    
    # Command selection
    parser.add_argument("--list-engines", action="store_true", 
                      help="List available OCR engines and exit")
    
    args = parser.parse_args()
    
    # Set up logging
    setup_logging(args.verbose)
    
    # List available engines if requested
    if args.list_engines:
        print("Available OCR engines:")
        engines = get_available_engines()
        if not engines:
            print("  No OCR engines available. Please install tesseract-ocr, ocrmypdf, or transformers.")
        else:
            for name, description in engines.items():
                print(f"  - {name}: {description}")
        return
    
    # Check for required arguments
    if not args.input:
        parser.error("--input is required")
    
    input_path = Path(args.input)
    
    # Prepare engine options
    engine_options = {}
    if args.language:
        engine_options['lang'] = args.language
    
    # Process based on input type
    if input_path.is_file():
        output_path = args.output
        
        # If output is a directory, create a default filename
        if output_path and Path(output_path).is_dir():
            if args.format == "pdf":
                output_path = Path(output_path) / f"{input_path.stem}_ocr.pdf"
            else:
                output_path = Path(output_path) / f"{input_path.stem}.txt"
        
        # Process PDF or image
        if input_path.suffix.lower() == '.pdf':
            print(f"Processing PDF: {input_path}")
            result = ocr_pdf(
                input_path, 
                output_path, 
                output_format=args.format,
                engine=args.engine,
                engine_options=engine_options,
                verbose=args.verbose
            )
            
            if args.format == "text" and not output_path:
                # Print extracted text to console
                print("\nExtracted Text:")
                print("-" * 40)
                print(result)
            else:
                print(f"Output saved to: {result}")
                
        else:
            # Assume it's an image
            print(f"Processing image: {input_path}")
            result = ocr_image(
                input_path, 
                output_path,
                engine=args.engine,
                engine_options=engine_options,
                verbose=args.verbose
            )
            
            if not output_path:
                # Print extracted text to console
                print("\nExtracted Text:")
                print("-" * 40)
                print(result)
            else:
                print(f"Output saved to: {output_path}")
    
    elif input_path.is_dir():
        # Process directory
        if not args.output:
            parser.error("--output directory is required when processing a directory")
        
        output_dir = Path(args.output)
        
        print(f"Processing directory: {input_path}")
        print(f"Output directory: {output_dir}")
        print(f"Output format: {args.format}")
        
        results = process_directory(
            input_path,
            output_dir,
            output_format=args.format,
            engine=args.engine,
            engine_options=engine_options,
            num_workers=args.workers,
            recursive=args.recursive,
            verbose=args.verbose
        )
        
        print(f"Processed {len(results)} files.")
    
    else:
        print(f"Error: {args.input} does not exist or is not a file or directory.")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main()) 