#!/usr/bin/env python3
"""
Example script demonstrating the text extraction capabilities of llamasearch-pdf.

This script shows how to use the TextExtractor class and convenience functions
to extract and process text from PDF documents.
"""

import os
import sys
import argparse
from pathlib import Path
import logging
from rich.console import Console
from rich.progress import Progress

# Add the parent directory to the Python path to allow importing llamasearch_pdf
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from llamasearch_pdf.core import TextExtractor, extract_text
from llamasearch_pdf.ocr import ocr_pdf


def example_simple_extraction(pdf_path, output_path=None):
    """
    Simple example using the convenience function.
    
    Args:
        pdf_path: Path to the PDF file
        output_path: Path where extracted text should be saved
    """
    console = Console()
    console.print("[bold cyan]Simple Text Extraction Example[/bold cyan]")
    console.print(f"Extracting text from: {pdf_path}")
    
    # Extract text using the convenience function
    result = extract_text(
        pdf_path,
        output_path=output_path,
        preserve_layout=True,
        verbose=True
    )
    
    if output_path:
        console.print(f"Text saved to: {output_path}")
    else:
        # Print some stats about the extracted text
        console.print(f"Extracted text from {len(result)} pages")
        total_chars = sum(len(text) for text in result.values())
        console.print(f"Total characters extracted: {total_chars}")
        
        # Show a snippet from the first page
        if result:
            first_page = min(result.keys())
            text_snippet = result[first_page][:500] + "..." if len(result[first_page]) > 500 else result[first_page]
            console.print("[bold]Sample text from first page:[/bold]")
            console.print(text_snippet)


def example_advanced_extraction(pdf_path, output_dir=None):
    """
    Advanced example using the TextExtractor class directly.
    
    Args:
        pdf_path: Path to the PDF file
        output_dir: Directory where extracted text should be saved
    """
    console = Console()
    console.print("\n[bold cyan]Advanced Text Extraction Example[/bold cyan]")
    console.print(f"Processing: {pdf_path}")
    
    # Create output directory if needed
    if output_dir:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create a TextExtractor with custom options
    extractor = TextExtractor(
        preserve_layout=True,  # Keep original layout
        remove_hyphenation=True,  # Fix hyphenated words
        normalize_whitespace=True,  # Clean up whitespace
        fallback_to_ocr=True,  # Use OCR if needed
        ocr_engine="tesseract"  # Specify OCR engine
    )
    
    # Extract text with progress tracking
    with Progress() as progress:
        text_dict = extractor.extract_text_from_pdf(
            pdf_path,
            progress=progress
        )
    
    # Process the extracted text
    console.print(f"Extracted text from {len(text_dict)} pages")
    
    # Example: Find pages containing specific keywords
    keyword = "example"
    matching_pages = []
    
    for page_num, text in text_dict.items():
        if keyword.lower() in text.lower():
            matching_pages.append(page_num)
    
    if matching_pages:
        console.print(f"Found keyword '{keyword}' on pages: {[p+1 for p in matching_pages]}")
    else:
        console.print(f"Keyword '{keyword}' not found in document")
    
    # Save to files if output directory is provided
    if output_dir:
        # Save full text
        full_output_path = output_dir / f"{Path(pdf_path).stem}_full.txt"
        with open(full_output_path, 'w', encoding='utf-8') as f:
            for page_num, text in sorted(text_dict.items()):
                f.write(f"=== Page {page_num + 1} ===\n\n")
                f.write(text)
                f.write("\n\n")
        
        # Save matching pages to a separate file
        if matching_pages:
            matches_output_path = output_dir / f"{Path(pdf_path).stem}_matches.txt"
            with open(matches_output_path, 'w', encoding='utf-8') as f:
                f.write(f"Pages containing '{keyword}':\n\n")
                for page_num in matching_pages:
                    f.write(f"=== Page {page_num + 1} ===\n\n")
                    f.write(text_dict[page_num])
                    f.write("\n\n")
            
            console.print(f"Saved matching pages to: {matches_output_path}")
        
        console.print(f"Saved full text to: {full_output_path}")


def example_comparison(pdf_path):
    """
    Compare native extraction with OCR-based extraction.
    
    Args:
        pdf_path: Path to the PDF file
    """
    console = Console()
    console.print("\n[bold cyan]Text Extraction Comparison Example[/bold cyan]")
    
    # Native extraction
    console.print("[bold]Method 1: Native PDF text extraction[/bold]")
    native_extractor = TextExtractor(fallback_to_ocr=False)
    native_text = native_extractor.extract_text_from_pdf(pdf_path)
    
    # OCR-based extraction
    console.print("[bold]Method 2: OCR-based text extraction[/bold]")
    ocr_text = ocr_pdf(pdf_path, output_format='text')
    
    # Compare results
    native_char_count = sum(len(text) for text in native_text.values())
    ocr_char_count = len(ocr_text) if isinstance(ocr_text, str) else 0
    
    console.print(f"Native extraction: {len(native_text)} pages, {native_char_count} characters")
    console.print(f"OCR extraction: {ocr_char_count} characters")
    
    # Determine which method extracted more text
    if native_char_count > ocr_char_count:
        console.print("[green]Native extraction yielded more text[/green]")
    elif ocr_char_count > native_char_count:
        console.print("[green]OCR extraction yielded more text[/green]")
    else:
        console.print("[yellow]Both methods yielded similar amounts of text[/yellow]")


def main():
    """Run the text extraction examples."""
    parser = argparse.ArgumentParser(description="Text extraction examples for llamasearch-pdf")
    parser.add_argument("--input", "-i", required=True, help="Input PDF file")
    parser.add_argument("--output", "-o", help="Output directory for extraction results")
    parser.add_argument("--all", "-a", action="store_true", help="Run all examples")
    parser.add_argument("--simple", "-s", action="store_true", help="Run simple extraction example")
    parser.add_argument("--advanced", "-d", action="store_true", help="Run advanced extraction example")
    parser.add_argument("--compare", "-c", action="store_true", help="Run extraction comparison example")
    
    args = parser.parse_args()
    
    # If no specific examples are selected, run them all
    if not (args.simple or args.advanced or args.compare):
        args.all = True
    
    # Run selected examples
    if args.simple or args.all:
        example_simple_extraction(args.input, args.output)
    
    if args.advanced or args.all:
        example_advanced_extraction(args.input, args.output)
    
    if args.compare or args.all:
        example_comparison(args.input)


if __name__ == "__main__":
    main() 