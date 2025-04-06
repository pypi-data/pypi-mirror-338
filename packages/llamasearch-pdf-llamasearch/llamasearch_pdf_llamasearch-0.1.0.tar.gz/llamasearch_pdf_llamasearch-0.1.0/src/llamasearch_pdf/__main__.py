"""
Main entry point for the LlamaSearch PDF command-line tool.

This module allows the package to be executed as a module:
    python -m llamasearch_pdf

It serves as the primary entry point for the command-line interface,
routing to the appropriate subcommands.
"""

import sys
from .cli import main

if __name__ == "__main__":
    sys.exit(main()) 