"""
Command-line interface for PDF search functionality.

This module provides commands for creating search indices, searching PDF documents,
and managing search operations from the command line.
"""

import os
import sys
import json
import argparse
import logging
from pathlib import Path
from typing import List, Optional, Dict, Any, Tuple

# Rich for fancy output
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich import print as rprint

from ..search import SearchIndex, create_index, search_pdfs, SearchResult

# Setup logging
logger = logging.getLogger(__name__)


def setup_logging(verbosity: int) -> None:
    """
    Set up logging based on verbosity level.
    
    Args:
        verbosity: Verbosity level (0-3)
    """
    log_levels = {
        0: logging.ERROR,
        1: logging.WARNING,
        2: logging.INFO,
        3: logging.DEBUG
    }
    
    log_level = log_levels.get(verbosity, logging.INFO)
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def create_index_command(args: argparse.Namespace) -> None:
    """
    Create a search index for a collection of PDF files.
    
    Args:
        args: Command-line arguments
    """
    # Set up logging
    setup_logging(args.verbose)
    
    # Validate input directory
    input_dir = Path(args.input_dir)
    if not input_dir.exists() or not input_dir.is_dir():
        logger.error(f"Input directory not found: {input_dir}")
        sys.exit(1)
    
    # Determine output path
    output_path = args.output_path
    if output_path is None:
        output_path = input_dir / "pdf_index.pkl"
    
    # Create output directory if it doesn't exist
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Set up console for nice output
    console = Console()
    
    # Create the search index
    console.print(f"[bold]Creating search index for PDFs in {input_dir}[/bold]")
    
    # Load stopwords if provided
    stopwords = None
    if args.stopwords:
        try:
            with open(args.stopwords, 'r') as f:
                stopwords = [line.strip() for line in f if line.strip()]
            console.print(f"Loaded {len(stopwords)} stopwords from {args.stopwords}")
        except Exception as e:
            logger.warning(f"Could not load stopwords file: {str(e)}")
    
    # Create index with specified settings
    index = create_index(
        case_sensitive=args.case_sensitive,
        stopwords=stopwords,
        index_path=output_path
    )
    
    # Find PDF files in the directory
    pdf_files = []
    for file_path in input_dir.glob('**/*.pdf'):
        if file_path.is_file():
            pdf_files.append(str(file_path))
    
    if not pdf_files:
        console.print("[yellow]No PDF files found in the specified directory.[/yellow]")
        sys.exit(0)
    
    console.print(f"Found {len(pdf_files)} PDF files to index")
    
    # Add documents to index with progress tracking
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        task = progress.add_task(f"[cyan]Indexing PDF files...", total=len(pdf_files))
        
        for pdf_file in pdf_files:
            try:
                progress.update(task, description=f"[cyan]Indexing {os.path.basename(pdf_file)}...")
                index.add_document(pdf_file)
                progress.advance(task)
            except Exception as e:
                logger.error(f"Failed to index {pdf_file}: {str(e)}")
    
    # Save the index
    try:
        index.save(output_path)
        console.print(f"[green]Index saved to {output_path}[/green]")
        
        # Print index statistics
        stats = index.get_stats()
        table = Table(title="Index Statistics")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        
        for key, value in stats.items():
            key_formatted = key.replace('_', ' ').title()
            table.add_row(key_formatted, str(value))
        
        console.print(table)
        
    except Exception as e:
        logger.error(f"Failed to save index: {str(e)}")
        sys.exit(1)


def search_command(args: argparse.Namespace) -> None:
    """
    Search for content in PDF documents.
    
    Args:
        args: Command-line arguments
    """
    # Set up logging
    setup_logging(args.verbose)
    
    # Set up console for nice output
    console = Console()
    
    # Determine if we're searching using an index or direct files
    if args.index_path:
        # Load the search index
        console.print(f"[bold]Loading search index from {args.index_path}...[/bold]")
        
        try:
            index = create_index(index_path=args.index_path)
            console.print("[green]Search index loaded successfully[/green]")
        except Exception as e:
            logger.error(f"Failed to load index: {str(e)}")
            sys.exit(1)
        
        # Perform the search
        results = index.search(
            args.query, 
            max_results=args.max_results,
            min_score=args.min_score,
            snippet_size=args.snippet_size
        )
    
    elif args.files:
        # Direct search on the specified files
        console.print(f"[bold]Searching {len(args.files)} PDF files...[/bold]")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("[cyan]Indexing files for search...", total=1)
            
            try:
                results = search_pdfs(
                    args.query,
                    args.files,
                    case_sensitive=args.case_sensitive,
                    max_results=args.max_results
                )
                progress.update(task, completed=1)
            except Exception as e:
                logger.error(f"Search failed: {str(e)}")
                sys.exit(1)
    
    else:
        logger.error("Either --index-path or --files must be specified")
        sys.exit(1)
    
    # Display results
    if not results:
        console.print("[yellow]No results found for your query.[/yellow]")
        return
    
    console.print(f"[green]Found {len(results)} results for query: '{args.query}'[/green]\n")
    
    # Output results
    if args.json:
        # Output as JSON
        json_results = []
        for i, result in enumerate(results):
            json_results.append({
                "rank": i + 1,
                "document": result.document_path,
                "page": result.page_number,
                "score": result.score,
                "snippet": result.snippet,
                "metadata": result.metadata
            })
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(json_results, f, indent=2)
            console.print(f"[green]Results saved to {args.output}[/green]")
        else:
            print(json.dumps(json_results, indent=2))
    
    else:
        # Format as table
        table = Table(title=f"Search Results for '{args.query}'")
        table.add_column("#", style="cyan", justify="right")
        table.add_column("Document", style="green")
        table.add_column("Page", style="cyan", justify="right")
        table.add_column("Score", style="green")
        table.add_column("Preview", style="yellow")
        
        for i, result in enumerate(results):
            doc_name = os.path.basename(result.document_path)
            table.add_row(
                str(i + 1),
                doc_name,
                str(result.page_number),
                f"{result.score:.4f}",
                result.snippet
            )
        
        console.print(table)
        
        # Save to file if requested
        if args.output:
            with open(args.output, 'w') as f:
                for i, result in enumerate(results):
                    f.write(f"Result {i+1}:\n")
                    f.write(f"  Document: {result.document_path}\n")
                    f.write(f"  Page: {result.page_number}\n")
                    f.write(f"  Score: {result.score:.4f}\n")
                    f.write(f"  Snippet: {result.snippet}\n\n")
            console.print(f"[green]Results saved to {args.output}[/green]")


def main() -> None:
    """Main entry point for the search CLI."""
    parser = argparse.ArgumentParser(
        description="Search PDF documents and manage search indices"
    )
    
    # Global options
    parser.add_argument("-v", "--verbose", action="count", default=0,
                        help="Increase verbosity (can be used multiple times)")
    
    # Subcommands
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Create index command
    create_parser = subparsers.add_parser("create-index", help="Create a search index for PDF documents")
    create_parser.add_argument("input_dir", help="Directory containing PDF files to index")
    create_parser.add_argument("-o", "--output-path", help="Path to save the search index")
    create_parser.add_argument("--case-sensitive", action="store_true", help="Make search case-sensitive")
    create_parser.add_argument("--stopwords", help="Path to file containing stopwords (one per line)")
    create_parser.set_defaults(func=create_index_command)
    
    # Search command
    search_parser = subparsers.add_parser("search", help="Search for content in PDF documents")
    search_parser.add_argument("query", help="Search query")
    
    # Two mutually exclusive options for search source
    search_source = search_parser.add_mutually_exclusive_group(required=True)
    search_source.add_argument("-i", "--index-path", help="Path to a saved search index")
    search_source.add_argument("-f", "--files", nargs="+", help="PDF files to search")
    
    search_parser.add_argument("-o", "--output", help="Save results to file")
    search_parser.add_argument("--json", action="store_true", help="Output results as JSON")
    search_parser.add_argument("--max-results", type=int, default=10, help="Maximum number of results")
    search_parser.add_argument("--min-score", type=float, default=0.0, help="Minimum score threshold")
    search_parser.add_argument("--snippet-size", type=int, default=100, help="Size of snippets in characters")
    search_parser.add_argument("--case-sensitive", action="store_true", help="Make search case-sensitive")
    search_parser.set_defaults(func=search_command)
    
    # Parse arguments
    args = parser.parse_args()
    
    # Execute the appropriate command
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main() 