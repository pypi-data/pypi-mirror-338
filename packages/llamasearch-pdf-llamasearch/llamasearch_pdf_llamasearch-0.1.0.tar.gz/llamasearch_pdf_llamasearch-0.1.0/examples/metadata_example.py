#!/usr/bin/env python3
"""
Example script demonstrating the metadata capabilities of llamasearch-pdf.

This script shows how to extract, update, and manage metadata in PDF documents.
"""

import os
import sys
import argparse
from pathlib import Path
import json
import logging
from rich.console import Console
from rich.table import Table

# Add the parent directory to the Python path to allow importing llamasearch_pdf
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from llamasearch_pdf.core import MetadataManager, extract_metadata, update_metadata, create_basic_metadata


def example_extract_metadata(pdf_path):
    """
    Example showing how to extract metadata from a PDF.
    
    Args:
        pdf_path: Path to the PDF file
    """
    console = Console()
    console.print("[bold cyan]Metadata Extraction Example[/bold cyan]")
    console.print(f"Extracting metadata from: {pdf_path}")
    
    # Extract metadata using the convenience function
    metadata = extract_metadata(pdf_path)
    
    # Display metadata in a nice table
    table = Table(title="PDF Metadata")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")
    
    # Add standard metadata fields
    standard_fields = [
        'title', 'author', 'subject', 'keywords', 'creator', 
        'producer', 'creation_date', 'modification_date'
    ]
    
    for field in standard_fields:
        # Try with and without leading slash and capitalization
        value = metadata.get(field, 
                metadata.get(field.capitalize(), 
                metadata.get(f"/{field.capitalize()}", None)))
        if value:
            table.add_row(field.replace('_', ' ').title(), str(value))
    
    # Add page count
    if 'page_count' in metadata:
        table.add_row("Page Count", str(metadata['page_count']))
    
    # Add page size if available and consistent
    if 'page_sizes' in metadata and metadata['page_sizes']:
        first_page = metadata['page_sizes'][0]
        if len(set(tuple(p.items()) for p in metadata['page_sizes'])) == 1:
            # All pages same size
            size_str = f"{first_page['width']} × {first_page['height']} {first_page['unit']}"
            table.add_row("Page Size", size_str)
        else:
            # Mixed page sizes
            table.add_row("Page Size", "Mixed (multiple sizes detected)")
    
    console.print(table)
    
    # Show any XMP metadata
    if 'xmp' in metadata and metadata['xmp']:
        console.print("\n[bold]XMP Metadata:[/bold]")
        xmp_table = Table()
        xmp_table.add_column("Field", style="cyan")
        xmp_table.add_column("Value", style="green")
        
        for key, value in metadata['xmp'].items():
            xmp_table.add_row(key, str(value))
        
        console.print(xmp_table)
    
    return metadata


def example_update_metadata(pdf_path, output_path):
    """
    Example showing how to update metadata in a PDF.
    
    Args:
        pdf_path: Path to the input PDF file
        output_path: Path where the updated PDF will be saved
    """
    console = Console()
    console.print("\n[bold cyan]Metadata Update Example[/bold cyan]")
    
    # Create new metadata
    new_metadata = create_basic_metadata(
        title="Updated PDF Document",
        author="LlamaSearch PDF Example"
    )
    
    # Add some additional fields
    new_metadata['/Subject'] = "Metadata Example"
    new_metadata['/Keywords'] = "pdf, metadata, example, llamasearch"
    
    # Update the PDF with the new metadata
    console.print(f"Updating metadata in: {pdf_path}")
    console.print(f"Saving updated PDF to: {output_path}")
    
    # Create output directory if it doesn't exist
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    update_metadata(pdf_path, output_path, new_metadata)
    
    console.print("[green]Metadata updated successfully![/green]")
    
    # Extract and display the updated metadata
    console.print("\n[bold]Updated Metadata:[/bold]")
    updated_metadata = extract_metadata(output_path)
    
    # Display in table format
    table = Table(title="Updated PDF Metadata")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")
    
    for key, value in new_metadata.items():
        # Clean up key for display
        clean_key = key[1:] if key.startswith('/') else key
        table.add_row(clean_key, str(value))
    
    console.print(table)


def example_metadata_from_text(pdf_path):
    """
    Example showing how to extract potential metadata from text content.
    
    Args:
        pdf_path: Path to the PDF file
    """
    console = Console()
    console.print("\n[bold cyan]Metadata from Text Example[/bold cyan]")
    
    # First extract text from the PDF
    from llamasearch_pdf.core import extract_text
    text_result = extract_text(pdf_path, preserve_layout=True)
    
    # Combine all page text
    full_text = "\n".join(text_result.values())
    
    # Create a metadata manager
    manager = MetadataManager()
    
    # Extract potential metadata from text
    text_metadata = manager.extract_text_metadata(full_text)
    
    console.print("[bold]Potential Metadata Detected in Text:[/bold]")
    
    if not text_metadata:
        console.print("[yellow]No metadata patterns detected in text content.[/yellow]")
    else:
        # Display the detected metadata
        table = Table()
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="green")
        
        for field, value in text_metadata.items():
            if isinstance(value, list):
                table.add_row(field, ", ".join(value))
            else:
                table.add_row(field, str(value))
        
        console.print(table)
    
    return text_metadata


def export_metadata_to_json(metadata, output_path):
    """
    Export metadata to a JSON file.
    
    Args:
        metadata: Dictionary of metadata
        output_path: Path where JSON file will be saved
    """
    console = Console()
    
    # Convert datetime objects to strings
    def json_serializer(obj):
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        raise TypeError(f"Type {type(obj)} not serializable")
    
    # Write to JSON file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, default=json_serializer)
    
    console.print(f"[green]Metadata exported to: {output_path}[/green]")


def main():
    """Run the metadata examples."""
    parser = argparse.ArgumentParser(description="Metadata examples for llamasearch-pdf")
    parser.add_argument("--input", "-i", required=True, help="Input PDF file")
    parser.add_argument("--output", "-o", help="Output directory for results")
    parser.add_argument("--all", "-a", action="store_true", help="Run all examples")
    parser.add_argument("--extract", "-e", action="store_true", help="Run metadata extraction example")
    parser.add_argument("--update", "-u", action="store_true", help="Run metadata update example")
    parser.add_argument("--text", "-t", action="store_true", help="Run text-based metadata extraction example")
    parser.add_argument("--export", "-x", action="store_true", help="Export metadata to JSON")
    
    args = parser.parse_args()
    
    # If no specific examples are selected, run them all
    if not (args.extract or args.update or args.text or args.export):
        args.all = True
    
    # Setup output directory
    output_dir = Path(args.output) if args.output else Path.cwd() / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    metadata = None
    
    # Run selected examples
    if args.extract or args.all:
        metadata = example_extract_metadata(args.input)
    
    if args.update or args.all:
        output_pdf = output_dir / f"{Path(args.input).stem}_updated.pdf"
        example_update_metadata(args.input, output_pdf)
    
    if args.text or args.all:
        text_metadata = example_metadata_from_text(args.input)
        if metadata and text_metadata:
            # Merge text metadata into main metadata
            metadata['text_extracted'] = text_metadata
    
    if (args.export or args.all) and metadata:
        json_path = output_dir / f"{Path(args.input).stem}_metadata.json"
        export_metadata_to_json(metadata, json_path)


if __name__ == "__main__":
    main() 