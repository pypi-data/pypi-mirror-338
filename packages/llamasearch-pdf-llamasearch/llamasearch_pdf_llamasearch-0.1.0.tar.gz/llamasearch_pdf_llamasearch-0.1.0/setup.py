"""
Setup script for llamasearch-pdf package.
"""

import os
from setuptools import setup, find_packages

# Read the contents of README.md
this_directory = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "PDF processing tools for document processing workflows"

# Dependencies
install_requires = [
    "PyPDF2>=3.0.0",
    "Pillow>=9.0.0",
    "pytesseract>=0.3.9",
    "pdf2image>=1.16.0",
    "rich>=12.0.0",
]

# Optional dependencies
extras_require = {
    "ocrmypdf": ["ocrmypdf>=14.0.0"],
    "huggingface": ["transformers>=4.20.0", "torch>=1.10.0"],
    "search": ["reportlab>=3.6.0"],  # For creating test PDFs in examples
    "dev": [
        "pytest>=7.0.0",
        "pytest-cov>=4.0.0",
        "flake8>=6.0.0",
        "black>=23.0.0",
        "isort>=5.10.0",
        "reportlab>=3.6.0",  # For creating test PDFs in tests
    ],
    "docs": [
        "sphinx>=5.0.0",
        "sphinx-rtd-theme>=1.0.0",
    ],
}

# All extras combined
extras_require["all"] = sorted(
    set(pkg for group in extras_require.values() for pkg in group)
)

setup(
    name="llamasearch-pdf-llamasearch",
    version="0.1.0",
    description="PDF processing tools for document processing workflows",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="LlamaSearch AI",
    author_email="nikjois@llamasearch.ai",
    url="https://llamasearch.ai",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=install_requires,
    extras_require=extras_require,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    entry_points={
        "console_scripts": [
            "llamasearch-pdf=llamasearch_pdf.cli:main",
        ],
    },
) 