"""
Command-line interface for the LlamaSearch PDF toolkit.

This module provides CLI commands for:
- OCR operations
- PDF conversion
- PDF optimization
- Text extraction
- Metadata extraction and management
- PDF search and indexing
- Batch processing
- Interactive mode
"""

import sys
from typing import List, Optional

from .ocr import main as ocr_main
from .text import main as text_main
from .metadata import main as metadata_main
from .search import main as search_main


def main(argv: Optional[List[str]] = None) -> int:
    """
    Main entry point for the LlamaSearch PDF CLI.
    
    Args:
        argv: Command-line arguments
        
    Returns:
        Exit code (0 for success, non-zero for errors)
    """
    if argv is None:
        argv = sys.argv[1:]
    
    # Check if a command is specified
    if not argv or argv[0].startswith('-'):
        # Display help if no command or only flags are provided
        print("LlamaSearch PDF Command-Line Tool")
        print("=================================")
        print("Available commands:")
        print("  ocr         - OCR operations for PDFs and images")
        print("  text        - Extract and process text from PDFs")
        print("  metadata    - Extract and manage PDF metadata")
        print("  search      - Search and index PDF content")
        # Add more commands as they become available
        print("\nFor help on a specific command, use: llamasearch-pdf COMMAND --help")
        return 0
    
    # Route to appropriate command handler
    command = argv[0]
    remaining_args = argv[1:]
    
    if command == "ocr":
        return ocr_main(remaining_args)
    elif command == "text":
        return text_main(remaining_args)
    elif command == "metadata":
        return metadata_main(remaining_args)
    elif command == "search":
        return search_main(remaining_args)
    else:
        print(f"Unknown command: {command}")
        print("Available commands: ocr, text, metadata, search")
        return 1


if __name__ == "__main__":
    sys.exit(main()) 