# Contributing to LlamaSearch PDF

Thank you for your interest in contributing to LlamaSearch PDF! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before contributing.

## Ways to Contribute

There are many ways to contribute to LlamaSearch PDF:

1. **Report bugs**: Create an issue to report a bug or unexpected behavior
2. **Suggest features**: Propose new features or improvements
3. **Write documentation**: Improve existing documentation or add new sections
4. **Submit code changes**: Fix bugs, add features, or improve performance
5. **Review code**: Review pull requests from other contributors

## Development Environment Setup

1. **Fork the repository** on GitHub
2. **Clone your fork** to your local machine
```bash
git clone https://github.com/your-username/llamasearch-pdf.git
cd llamasearch-pdf
```
3. **Set up the development environment**
```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package in development mode with all extras
pip install -e ".[dev,docs,all]"

# Install pre-commit hooks
pre-commit install
```

## Development Workflow

1. **Create a new branch** for your changes
```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes**: Implement your bug fix or feature

3. **Run the tests** to make sure everything works
```bash
pytest
```

4. **Format your code** using black and isort
```bash
black .
isort .
```

5. **Run type checking** with mypy
```bash
mypy src
```

6. **Commit your changes** with a descriptive commit message
```bash
git add .
git commit -m "Add feature X" or "Fix bug Y"
```

7. **Push to your fork**
```bash
git push origin feature/your-feature-name
```

8. **Create a pull request** from your branch to the main repository

## Pull Request Guidelines

1. **Describe your changes** in detail
2. **Reference any related issues** using the GitHub issue number
3. **Include tests** for any new functionality
4. **Update documentation** if needed
5. **Make sure all tests pass**
6. **Keep your PR focused** on a single issue or feature

## Code Style Guidelines

We follow these guidelines for code style:

1. **Python Code Style**: We use [Black](https://github.com/psf/black) with a line length of 100 characters
2. **Import Ordering**: We use [isort](https://pycqa.github.io/isort/) with the Black profile
3. **Type Annotations**: All new code should include type annotations
4. **Documentation**: All public functions, classes, and methods should have docstrings
5. **Comments**: Add comments for complex logic, but prefer writing readable code

## Documentation Guidelines

Documentation is written using Markdown and built with MkDocs:

1. **API Documentation**: Generated from docstrings
2. **Code Examples**: Include practical examples
3. **Building Documentation**: Use `mkdocs serve` to preview locally
4. **Documentation Structure**: Follow the existing structure

## Testing Guidelines

1. **Test Coverage**: Aim for high test coverage for new code
2. **Test Types**:
   - **Unit Tests**: Test individual functions and classes
   - **Integration Tests**: Test interactions between components
   - **Functional Tests**: Test end-to-end workflows
3. **Test Organization**: Place tests in the `tests/` directory with a structure that mirrors the package
4. **Running Tests**: Use `pytest` to run the test suite

## Releasing (For Maintainers)

1. **Update Version**: Version is managed by setuptools_scm based on git tags
2. **Update Changelog**: Make sure CHANGELOG.md is up to date
3. **Create a Release**: Create a new release on GitHub with a version tag
4. **PyPI Release**: The CI system will build and upload to PyPI

## License

By contributing to LlamaSearch PDF, you agree that your contributions will be licensed under the [MIT License](LICENSE).

## Questions?

If you have any questions about contributing, feel free to open an issue or reach out to the maintainers.

Thank you for your contributions! 