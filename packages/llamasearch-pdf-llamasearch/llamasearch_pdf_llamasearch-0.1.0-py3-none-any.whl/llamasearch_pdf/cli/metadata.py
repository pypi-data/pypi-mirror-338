"""
Command-line interface for PDF metadata operations.

This module provides command-line tools for extracting, updating, and
manipulating metadata in PDF documents.
"""

import os
import sys
import argparse
import json
import logging
from pathlib import Path
from typing import Optional, Dict, Any, List

from rich.console import Console
from rich.table import Table
from rich.progress import Progress

from ..core.metadata import (
    MetadataManager, 
    extract_metadata, 
    update_metadata,
    create_basic_metadata
)
from ..core.text import extract_text


def setup_logging(verbosity: int) -> None:
    """
    Configure logging based on verbosity level.
    
    Args:
        verbosity: Verbosity level (0=errors only, 1=warnings, 2=info, 3=debug)
    """
    log_levels = {
        0: logging.ERROR,
        1: logging.WARNING,
        2: logging.INFO,
        3: logging.DEBUG
    }
    
    level = log_levels.get(verbosity, logging.INFO)
    logging.basicConfig(
        level=level,
        format='%(levelname)s: %(message)s'
    )


def extract_command(args: argparse.Namespace) -> None:
    """
    Handle the 'extract' subcommand to extract metadata from PDFs.
    
    Args:
        args: Command line arguments
    """
    console = Console()
    
    # Validate input
    pdf_path = Path(args.input)
    if not pdf_path.exists():
        console.print(f"[red]Error: PDF file not found: {pdf_path}[/red]")
        sys.exit(1)
    
    # Determine output path
    output_path = None
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Extract metadata
    console.print(f"Extracting metadata from: {pdf_path}")
    
    try:
        metadata = extract_metadata(pdf_path, strict=not args.non_strict)
        
        # Display metadata in a nice table if not exporting to file
        if args.format == 'table' or (not output_path and not args.format):
            table = Table(title=f"Metadata for {pdf_path.name}")
            table.add_column("Field", style="cyan")
            table.add_column("Value", style="green")
            
            # Add standard metadata fields
            standard_fields = [
                'title', 'author', 'subject', 'keywords', 'creator', 
                'producer', 'creation_date', 'modification_date'
            ]
            
            for field in standard_fields:
                # Try different variations of the field name
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
            
            # Add other fields that aren't in the standard list
            other_fields = set(metadata.keys()) - set(standard_fields) - {'page_count', 'page_sizes', 'xmp'}
            for field in sorted(other_fields):
                value = metadata[field]
                # Skip complex objects or very long strings
                if not isinstance(value, (dict, list)) and not (isinstance(value, str) and len(value) > 100):
                    table.add_row(field, str(value))
            
            console.print(table)
            
            # Show XMP metadata if available
            if 'xmp' in metadata and metadata['xmp'] and args.detailed:
                console.print("\n[bold]XMP Metadata:[/bold]")
                xmp_table = Table()
                xmp_table.add_column("Field", style="cyan")
                xmp_table.add_column("Value", style="green")
                
                for key, value in metadata['xmp'].items():
                    xmp_table.add_row(key, str(value))
                
                console.print(xmp_table)
        
        # Export metadata if an output path is provided
        if output_path:
            def json_serializer(obj):
                if hasattr(obj, 'isoformat'):
                    return obj.isoformat()
                raise TypeError(f"Type {type(obj)} not serializable")
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, default=json_serializer)
            
            console.print(f"[green]Metadata exported to: {output_path}[/green]")
        
        # If format is json and no output file, print to stdout
        elif args.format == 'json':
            def json_serializer(obj):
                if hasattr(obj, 'isoformat'):
                    return obj.isoformat()
                raise TypeError(f"Type {type(obj)} not serializable")
            
            json_output = json.dumps(metadata, indent=2, default=json_serializer)
            console.print(json_output)
        
    except Exception as e:
        console.print(f"[red]Error extracting metadata: {e}[/red]")
        if args.verbose >= 2:
            import traceback
            console.print(traceback.format_exc())
        sys.exit(1)


def update_command(args: argparse.Namespace) -> None:
    """
    Handle the 'update' subcommand to update metadata in PDFs.
    
    Args:
        args: Command line arguments
    """
    console = Console()
    
    # Validate input
    pdf_path = Path(args.input)
    if not pdf_path.exists():
        console.print(f"[red]Error: PDF file not found: {pdf_path}[/red]")
        sys.exit(1)
    
    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_dir = pdf_path.parent
        output_path = output_dir / f"{pdf_path.stem}_updated.pdf"
    
    # Create output directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Create metadata dict
    metadata = {}
    
    # Process metadata from file if provided
    if args.metadata_file:
        try:
            with open(args.metadata_file, 'r', encoding='utf-8') as f:
                metadata_from_file = json.load(f)
                
                # Convert keys to PDF format with leading slash if needed
                for key, value in metadata_from_file.items():
                    if not key.startswith('/'):
                        metadata[f"/{key.capitalize()}"] = value
                    else:
                        metadata[key] = value
                
        except Exception as e:
            console.print(f"[red]Error reading metadata file: {e}[/red]")
            sys.exit(1)
    
    # Add individual fields if provided
    if args.title:
        metadata['/Title'] = args.title
    if args.author:
        metadata['/Author'] = args.author
    if args.subject:
        metadata['/Subject'] = args.subject
    if args.keywords:
        metadata['/Keywords'] = args.keywords
    if args.creator:
        metadata['/Creator'] = args.creator
    if args.producer:
        metadata['/Producer'] = args.producer
    
    # If no metadata was provided, show error
    if not metadata:
        console.print("[red]Error: No metadata provided. Use --title, --author, etc. or --metadata-file.[/red]")
        sys.exit(1)
    
    # Update the PDF
    console.print(f"Updating metadata in: {pdf_path}")
    console.print(f"Saving to: {output_path}")
    
    try:
        update_metadata(pdf_path, output_path, metadata, strict=not args.non_strict)
        console.print("[green]Metadata updated successfully![/green]")
        
        # Show the updated metadata if requested
        if args.show_result:
            console.print("\n[bold]Updated Metadata:[/bold]")
            updated_metadata = extract_metadata(output_path)
            
            table = Table(title=f"Updated Metadata for {output_path.name}")
            table.add_column("Field", style="cyan")
            table.add_column("Value", style="green")
            
            for key, value in updated_metadata.items():
                if not isinstance(value, (dict, list)) and not (isinstance(value, str) and len(str(value)) > 100):
                    table.add_row(key, str(value))
            
            console.print(table)
    
    except Exception as e:
        console.print(f"[red]Error updating metadata: {e}[/red]")
        if args.verbose >= 2:
            import traceback
            console.print(traceback.format_exc())
        sys.exit(1)


def batch_extract_command(args: argparse.Namespace) -> None:
    """
    Handle the 'batch-extract' subcommand to extract metadata from multiple PDFs.
    
    Args:
        args: Command line arguments
    """
    console = Console()
    
    # Validate input directory
    input_dir = Path(args.input_dir)
    if not input_dir.is_dir():
        console.print(f"[red]Error: Input directory not found: {input_dir}[/red]")
        sys.exit(1)
    
    # Setup output directory
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = input_dir / "metadata"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Find all PDF files in the input directory
    pdf_files = list(input_dir.glob("**/*.pdf")) if args.recursive else list(input_dir.glob("*.pdf"))
    
    if not pdf_files:
        console.print(f"[yellow]No PDF files found in {input_dir}[/yellow]")
        sys.exit(0)
    
    console.print(f"Found {len(pdf_files)} PDF files in {input_dir}")
    
    # Extract metadata from each PDF
    results = []
    failed_files = []
    
    with Progress() as progress:
        task = progress.add_task("Extracting metadata...", total=len(pdf_files))
        
        for pdf_file in pdf_files:
            try:
                # Extract metadata
                metadata = extract_metadata(pdf_file, strict=not args.non_strict)
                
                # Add file information
                metadata['file_name'] = pdf_file.name
                metadata['file_path'] = str(pdf_file.relative_to(input_dir))
                metadata['file_size'] = pdf_file.stat().st_size
                
                results.append(metadata)
                
                # Save individual metadata file if requested
                if args.individual:
                    output_file = output_dir / f"{pdf_file.stem}_metadata.json"
                    
                    def json_serializer(obj):
                        if hasattr(obj, 'isoformat'):
                            return obj.isoformat()
                        raise TypeError(f"Type {type(obj)} not serializable")
                    
                    with open(output_file, 'w', encoding='utf-8') as f:
                        json.dump(metadata, f, indent=2, default=json_serializer)
            
            except Exception as e:
                logging.error(f"Error processing {pdf_file}: {e}")
                failed_files.append((str(pdf_file), str(e)))
            
            progress.update(task, advance=1)
    
    # Save combined results
    if results:
        summary_file = output_dir / "metadata_summary.json"
        
        def json_serializer(obj):
            if hasattr(obj, 'isoformat'):
                return obj.isoformat()
            raise TypeError(f"Type {type(obj)} not serializable")
        
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, default=json_serializer)
        
        console.print(f"[green]Metadata summary saved to: {summary_file}[/green]")
        
        # Print summary table
        if not args.quiet:
            table = Table(title="Metadata Summary")
            table.add_column("File", style="cyan")
            table.add_column("Pages", style="green")
            table.add_column("Title", style="green")
            table.add_column("Author", style="green")
            
            for result in results:
                file_name = result.get('file_name', '')
                pages = result.get('page_count', '')
                
                # Try to get title and author with various key formats
                title = result.get('title', 
                         result.get('Title',
                         result.get('/Title', '')))
                
                author = result.get('author',
                          result.get('Author',
                          result.get('/Author', '')))
                
                table.add_row(file_name, str(pages), str(title), str(author))
            
            console.print(table)
    
    # Report failures
    if failed_files:
        console.print(f"[yellow]Failed to process {len(failed_files)} files:[/yellow]")
        for file_path, error in failed_files:
            console.print(f"  - {file_path}: {error}")


def text_metadata_command(args: argparse.Namespace) -> None:
    """
    Handle the 'text-metadata' subcommand to extract metadata from PDF text content.
    
    Args:
        args: Command line arguments
    """
    console = Console()
    
    # Validate input
    pdf_path = Path(args.input)
    if not pdf_path.exists():
        console.print(f"[red]Error: PDF file not found: {pdf_path}[/red]")
        sys.exit(1)
    
    # Determine output path
    output_path = None
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
    
    console.print(f"Extracting text and analyzing metadata from: {pdf_path}")
    
    try:
        # Extract text from the PDF
        text_result = extract_text(pdf_path, preserve_layout=True)
        
        # Combine text from all pages
        full_text = "\n".join(text_result.values())
        
        # Extract potential metadata from text
        manager = MetadataManager()
        text_metadata = manager.extract_text_metadata(full_text)
        
        # Display results
        if text_metadata:
            console.print("[green]Potential metadata found in text content:[/green]")
            
            table = Table()
            table.add_column("Field", style="cyan")
            table.add_column("Value", style="green")
            
            for field, value in text_metadata.items():
                if isinstance(value, list):
                    table.add_row(field, ", ".join(value))
                else:
                    table.add_row(field, str(value))
            
            console.print(table)
            
            # Extract normal metadata and combine results if requested
            if args.combine:
                console.print("\n[bold]Combining with standard metadata...[/bold]")
                
                # Get standard metadata
                std_metadata = extract_metadata(pdf_path)
                
                # Create combined metadata
                combined = std_metadata.copy()
                combined['text_extracted'] = text_metadata
                
                # Apply text metadata to standard fields if they're empty
                if 'title_candidate' in text_metadata and not any(k in std_metadata for k in ['/Title', 'Title', 'title']):
                    combined['/Title'] = text_metadata['title_candidate']
                
                if 'author_candidates' in text_metadata and not any(k in std_metadata for k in ['/Author', 'Author', 'author']):
                    combined['/Author'] = text_metadata['author_candidates'][0]
                
                # Save or display combined metadata
                if output_path:
                    def json_serializer(obj):
                        if hasattr(obj, 'isoformat'):
                            return obj.isoformat()
                        raise TypeError(f"Type {type(obj)} not serializable")
                    
                    with open(output_path, 'w', encoding='utf-8') as f:
                        json.dump(combined, f, indent=2, default=json_serializer)
                    
                    console.print(f"[green]Combined metadata saved to: {output_path}[/green]")
                
                # If format is json and no output file, print to stdout
                elif args.format == 'json':
                    def json_serializer(obj):
                        if hasattr(obj, 'isoformat'):
                            return obj.isoformat()
                        raise TypeError(f"Type {type(obj)} not serializable")
                    
                    json_output = json.dumps(combined, indent=2, default=json_serializer)
                    console.print(json_output)
            
            # Save text metadata only if not combining
            elif output_path:
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(text_metadata, f, indent=2)
                
                console.print(f"[green]Text metadata saved to: {output_path}[/green]")
            
            # If format is json and no output file, print to stdout
            elif args.format == 'json':
                json_output = json.dumps(text_metadata, indent=2)
                console.print(json_output)
        
        else:
            console.print("[yellow]No metadata patterns detected in text content.[/yellow]")
    
    except Exception as e:
        console.print(f"[red]Error extracting text metadata: {e}[/red]")
        if args.verbose >= 2:
            import traceback
            console.print(traceback.format_exc())
        sys.exit(1)


def main() -> None:
    """Entry point for the metadata CLI."""
    parser = argparse.ArgumentParser(
        description="LlamaSearch PDF Metadata Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("--verbose", "-v", action="count", default=0,
                        help="Increase verbosity (can be used multiple times)")
    parser.add_argument("--non-strict", action="store_true",
                        help="Use non-strict mode for PDF parsing (more lenient)")
    
    subparsers = parser.add_subparsers(title="commands", dest="command")
    
    # Extract metadata command
    extract_parser = subparsers.add_parser("extract", help="Extract metadata from a PDF")
    extract_parser.add_argument("input", help="Input PDF file")
    extract_parser.add_argument("--output", "-o", help="Output JSON file for metadata")
    extract_parser.add_argument("--format", "-f", choices=["table", "json"],
                                help="Output format (default: table if no output file, json if output file)")
    extract_parser.add_argument("--detailed", "-d", action="store_true",
                                help="Show detailed metadata including XMP")
    extract_parser.set_defaults(func=extract_command)
    
    # Update metadata command
    update_parser = subparsers.add_parser("update", help="Update metadata in a PDF")
    update_parser.add_argument("input", help="Input PDF file")
    update_parser.add_argument("--output", "-o", help="Output PDF file")
    update_parser.add_argument("--metadata-file", "-m", help="JSON file containing metadata")
    update_parser.add_argument("--title", help="Document title")
    update_parser.add_argument("--author", help="Document author")
    update_parser.add_argument("--subject", help="Document subject")
    update_parser.add_argument("--keywords", help="Document keywords")
    update_parser.add_argument("--creator", help="Document creator")
    update_parser.add_argument("--producer", help="Document producer")
    update_parser.add_argument("--show-result", "-s", action="store_true",
                              help="Show the updated metadata after processing")
    update_parser.set_defaults(func=update_command)
    
    # Batch extract command
    batch_parser = subparsers.add_parser("batch", help="Batch extract metadata from multiple PDFs")
    batch_parser.add_argument("input_dir", help="Input directory containing PDF files")
    batch_parser.add_argument("--output-dir", "-o", help="Output directory for metadata files")
    batch_parser.add_argument("--recursive", "-r", action="store_true",
                             help="Search for PDFs recursively in subdirectories")
    batch_parser.add_argument("--individual", "-i", action="store_true",
                             help="Save individual metadata files for each PDF")
    batch_parser.add_argument("--quiet", "-q", action="store_true",
                             help="Don't display summary table")
    batch_parser.set_defaults(func=batch_extract_command)
    
    # Text metadata command
    text_parser = subparsers.add_parser("text", help="Extract metadata from PDF text content")
    text_parser.add_argument("input", help="Input PDF file")
    text_parser.add_argument("--output", "-o", help="Output JSON file for metadata")
    text_parser.add_argument("--format", "-f", choices=["table", "json"],
                            help="Output format (default: table if no output file, json if output file)")
    text_parser.add_argument("--combine", "-c", action="store_true",
                            help="Combine with standard metadata")
    text_parser.set_defaults(func=text_metadata_command)
    
    args = parser.parse_args()
    
    # Setup logging based on verbosity
    setup_logging(args.verbose)
    
    # If no command was specified, show help and exit
    if not hasattr(args, 'func'):
        parser.print_help()
        sys.exit(1)
    
    # Execute the command function
    args.func(args) 