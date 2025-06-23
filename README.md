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

Install using pip:
```bash
pip install d361
```
Or, using [uv](https://github.com/astral-sh/uv) (a fast Python package installer):
```bash
uv pip install d361
```

## Usage

### Command Line Interface

The package provides a command-line interface `d361-offline` with several operations:

```bash
# Prepare phase: Extract sitemap and navigation
d361-offline prep --map-url=https://docs.example.com/sitemap.xml --output-dir=my_docs

# Fetch phase: Download content from all URLs
d361-offline fetch --prep-file=my_docs/prep.json --output-dir=my_docs

# Build phase: Generate documentation files
d361-offline build --fetch-file=my_docs/fetch.json --output-dir=my_docs --style=my_style.css

# Run all phases in sequence
d361-offline all --map-url=https://docs.example.com/sitemap.xml --output-dir=my_docs
```
For a full list of options for each command, use `d361-offline <command> --help`.

### Python API

```python
import asyncio
from pathlib import Path
from d361.offline.config import Config # Updated import
from d361.offline.d361_offline import D361Offline

async def generate_offline_docs():
    config = Config(
        map_url="https://docs.example.com/sitemap.xml", # Changed from url to map_url
        output_dir=Path("my_docs"), # output_dir is a Path object
        css_file=Path("my_style.css"), # css_file is a Path object
        max_concurrent=5 # This is a default, can be customized
    )
    
    d361_offline = D361Offline(config) # Renamed variable for clarity
    
    # Run all phases
    await d361_offline.all()
    
    # Or run individual phases
    # prep_data = await d361_offline.prep()
    # fetch_data = await d361_offline.fetch(prep_file_path=config.prep_file) # Assuming prep_file path from config
    # await d361_offline.build(fetch_file_path=config.fetch_file) # Assuming fetch_file path from config

# Run the async function
asyncio.run(generate_offline_docs())
```

## Configuration Options

The behavior of `d361-offline` is controlled by the `Config` model (see `src/d361/offline/config.py`). Key options include:

| Option (`Config` field) | CLI Argument    | Description                                           | Default (from `Config`) |
|-------------------------|-----------------|-------------------------------------------------------|-------------------------|
| `map_url`               | `--map-url`     | URL of the sitemap (e.g., sitemap.xml)                | None (Required for most ops) |
| `nav_url`               | `--nav-url`     | URL of a page to extract navigation from (optional)   | None                    |
| `output_dir`            | `--output-dir`  | Directory to store output files                       | Current working directory / domain |
| `css_file`              | `--style` (build) | Path to custom CSS file for styling HTML output       | None                    |
| `effort`                | `--effort` (prep)| Try harder to map all sitemap links in navigation     | `False`                 |
| `max_concurrent`        | `--parallel`    | Maximum number of concurrent download requests        | 5                       |
| `retries`               | `--retries`     | Number of retry attempts for failed requests          | 3                       |
| `timeout`               | `--timeout`     | Request timeout in seconds for page loads             | 60                      |
| `verbose`               | `--verbose`     | Enable verbose (DEBUG level) logging                  | `False`                 |
| `test`                  | `--test` (prep) | Test mode: process only a few items                   | `False`                 |
| `pause`                 | `--wait` (prep) | Pause during navigation extraction (for debugging)    | `False`                 |

*Note: CLI arguments may vary slightly per command. Refer to `--help` for each command.*

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

This project uses [Hatch](https://hatch.pypa.io/) for development workflow management. Hatch environments use [uv](https://github.com/astral-sh/uv) by default if it's available, which significantly speeds up dependency management.

### Setup Development Environment

1.  **Install Hatch and uv**:
    It's recommended to install `uv` first, then use it to install `hatch`.
    ```bash
    # Install uv (refer to official uv documentation for preferred method)
    # Example:
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # Then install Hatch using uv
    uv pip install hatch
    ```

2.  **Activate Hatch Environment**:
    Navigate to the project root directory and run:
    ```bash
    hatch shell
    ```
    This command creates an isolated virtual environment (if it doesn't exist), installs all project dependencies (including development dependencies like `pytest`, `ruff`, `mypy`), and activates the environment. You can also use `uv activate` if you prefer, after `hatch env create`.

3.  **Running Tasks**:
    Once the environment is active, you can use Hatch scripts defined in `pyproject.toml` to run common tasks:

    *   **Run tests with coverage**:
        ```bash
        hatch run test:test-cov
        ```
        (The `test:test-cov` script runs pytest with coverage.)
        To run tests without coverage: `hatch run test:test`

    *   **Run linters and formatters**:
        The project uses Ruff for linting and formatting, and MyPy for type checking.
        ```bash
        # Run all linting and type checking (style, format check, type check)
        hatch run lint:all

        # Auto-format code
        hatch run lint:fmt

        # Just check style
        hatch run lint:style

        # Just run type checking
        hatch run lint:typing
        ```
        Refer to the `[tool.hatch.envs.lint.scripts]` section in `pyproject.toml` for all available linting scripts.

### Codebase Structure

The core logic of the offline documentation generator resides in the `src/d361/offline/` directory:

*   `config.py`: Defines the Pydantic `Config` model that holds all configuration parameters for the generation process. It includes logic for path resolution and default values.
*   `d361_offline.py`: Contains the main `D361Offline` class, which orchestrates the entire process (preparation, fetching, building).
*   `browser.py`: Handles interactions with web pages using Playwright, primarily for extracting sitemap data and JavaScript-rendered navigation structures.
*   `content.py`: Responsible for fetching content from URLs (using `aiohttp`), extracting relevant article content, and converting it to Markdown or processing HTML.
*   `navigation.py`: Deals with parsing, processing, and structuring navigation data extracted from the documentation site.
*   `parser.py`: Includes various parsing utilities, e.g., for XML sitemaps and HTML content, using tools like BeautifulSoup and lxml.
*   `generator.py`: Contains logic for generating the final output files (combined HTML/Markdown, individual files, navigation files).
*   `__main__.py`: Provides the command-line interface (CLI) entry point using `python-fire`, allowing users to run the generator from the terminal.
*   `__init__.py`: Makes the `d361.offline` package and its main components importable.

The `src/d361/__init__.py` and `src/d361/__version__.py` handle package-level initialization and versioning (via `hatch-vcs`).

## Contributing

Contributions are welcome! Please follow these guidelines:

1.  **Branching**: Create a new branch for each feature or bug fix.
2.  **Coding Standards**:
    *   Code is formatted using **Ruff** and linted with **Ruff**. Configuration is in `pyproject.toml`. Run `hatch run lint:fmt` to format and `hatch run lint:style` to check.
    *   Type checking is done with **MyPy**. Configuration is in `pyproject.toml`. Run `hatch run lint:typing` to check types.
    *   Ensure all pre-commit hooks pass before committing. Install hooks with `pre-commit install`.
3.  **Commit Messages**:
    *   Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification. For example: `feat: add support for XYZ format` or `fix: resolve issue with navigation parsing`.
4.  **Testing**:
    *   Write tests for new features and bug fixes using `pytest`.
    *   Ensure all tests pass by running `hatch run test:test-cov`. Aim for high test coverage.
5.  **Pull Requests**:
    *   Submit a pull request (PR) to the `main` branch.
    *   Ensure your PR includes a clear description of the changes and why they were made.
    *   Link any relevant issues.
    *   Ensure GitHub Actions CI checks pass for your PR.

## License

MIT License