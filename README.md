# D361: Document360 Offline Documentation Generator

![License](https://img.shields.io/badge/license-MIT-blue.svg)

D361 is a Python package designed to create comprehensive offline versions of online documentation sites, with primary support for Document360 sites. It extracts, processes, and organizes documentation content for offline access.

## Features

- **Complete Documentation Capture**: Extracts and preserves entire documentation structures
- **Multi-format Output**: Generates both HTML and Markdown versions of documentation
- **Navigation Preservation**: Maintains the original site navigation structure
- **Performance Optimized**:
  - Intelligent caching to avoid redundant downloads
  - Configurable concurrent requests
  - Automatic retries with exponential backoff
- **Combined Output Files**: Creates single-file documentation with embedded navigation
- **Modern Python Implementation**:
  - Type hints and runtime type checking
  - PEP 621 compliant packaging
  - Comprehensive test suite

## Installation

```bash
pip install d361
```

## Usage

### Command Line Interface

The package provides a command-line interface with three main operations:

```bash
# Prepare phase: Extract sitemap and navigation
python -m d361.offline prep --url=https://docs.example.com --output-dir=my_docs

# Fetch phase: Download content from all URLs
python -m d361.offline fetch --prep-file=my_docs/prep.json --output-dir=my_docs

# Build phase: Generate documentation files
python -m d361.offline build --fetch-file=my_docs/fetch.json --output-dir=my_docs --style-file=my_style.css

# Run all phases in sequence
python -m d361.offline all --url=https://docs.example.com --output-dir=my_docs
```

### Python API

```python
import asyncio
from d361.offline import Config, D361Offline

async def generate_offline_docs():
    config = Config(
        url="https://docs.example.com",
        output_dir="my_docs",
        css_file="my_style.css",
        max_concurrent=5
    )
    
    d361 = D361Offline(config)
    
    # Run all phases
    await d361.all()
    
    # Or run individual phases
    # await d361.prep()
    # await d361.fetch()
    # await d361.build()

# Run the async function
asyncio.run(generate_offline_docs())
```

## Configuration Options

| Option | Description | Default |
|--------|-------------|---------|
| `url` | Base URL of the documentation site | Required |
| `output_dir` | Directory to store output files | Required |
| `css_file` | CSS file for styling HTML output | None |
| `max_concurrent` | Maximum number of concurrent requests | 5 |
| `timeout` | Request timeout in seconds | 30 |
| `retries` | Number of retry attempts for failed requests | 3 |
| `test` | Enable test mode (limits processing to a few pages) | False |
| `verbose` | Enable verbose logging | False |

## Output Structure

```
output_dir/
├── prep.json          # Preparation phase data
├── fetch.json         # Fetch phase data
├── nav.json           # Navigation structure
├── nav.html           # HTML version of navigation
├── nav.md             # Markdown version of navigation
├── all_docs.html      # Combined HTML documentation
├── all_docs.md        # Combined Markdown documentation
├── html/              # Individual HTML files
│   ├── page1.html
│   ├── page2.html
│   └── ...
└── md/                # Individual Markdown files
    ├── page1.md
    ├── page2.md
    └── ...
```

## Development

This project uses [Hatch](https://hatch.pypa.io/) for development workflow management.

### Setup Development Environment

```bash
# Install hatch if you haven't already
pip install hatch

# Create and activate development environment
hatch shell

# Run tests
hatch run test

# Run tests with coverage
hatch run test-cov

# Run linting
hatch run lint

# Format code
hatch run format
```

## License

MIT License 