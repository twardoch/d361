# D361: Robust Offline Documentation Generator

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/d361.svg)](https://badge.fury.io/py/d361)
[![Python Versions](https://img.shields.io/pypi/pyversions/d361.svg)](https://pypi.org/project/d361/)
[![Code style: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with MyPy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Tests Passing](https://github.com/twardoch/d361/actions/workflows/push.yml/badge.svg)](https://github.com/twardoch/d361/actions/workflows/push.yml)

## 🚀 **TL;DR**

D361 is a robust, enterprise-grade Python package that creates comprehensive offline versions of Document360 knowledge bases and other sitemap-based documentation sites. It's the **generic, reusable foundation** of the Document360 unified toolkit, designed for reliability, performance, and seamless integration.

**Quick Start:**
```bash
# Install and generate offline docs in one command
pip install d361 && playwright install chromium
d361-offline all --map-url="https://docs.example.com/sitemap-en.xml" --output-dir="offline_docs"

# Or use the standalone binary (no Python required)
curl -L -o d361-offline https://github.com/twardoch/d361/releases/latest/download/d361-offline-ubuntu-latest
chmod +x d361-offline && ./d361-offline all --map-url="https://docs.example.com/sitemap-en.xml"
```

**Key Features:**
- 🎯 **Complete Documentation Capture** - Intelligently extracts entire documentation structures
- 🚀 **Multi-Strategy Parsing** - Robust sitemap parsing with multiple fallback mechanisms
- 🤖 **Browser Automation** - Playwright-based extraction with stealth techniques for dynamic content
- 📱 **Multi-Format Output** - HTML, Markdown, and combined documentation files
- ⚡ **Performance Optimized** - Concurrent downloads with intelligent retry logic
- 🔄 **Navigation Preservation** - Maintains original site structure for intuitive offline browsing

---

## 📦 **What is D361?**

D361 is the **robust offline documentation generator** that serves as the foundational component of the Document360 unified toolkit. As a standalone package, it specializes in extracting, processing, and organizing documentation content for offline access, with enterprise-grade reliability and performance.

**Core Purpose:**
D361 automates the complete process of downloading entire Document360 sites (or other sitemap-based documentation) and converting them into comprehensive, browsable offline formats. It's designed to handle the complexities of modern documentation sites, including dynamic content, virtual scrolling, and complex navigation structures.

**The D361 Workflow:**

1. **🔍 Multi-Strategy Discovery** - Advanced sitemap parsing with multiple fallback mechanisms
2. **🗺️  Dynamic Structure Extraction** - Intelligently maps navigation hierarchies from live sites  
3. **⚡ Concurrent Content Fetching** - High-performance parallel downloading with retry logic
4. **🔄 Multi-Format Processing** - Converts content to HTML, Markdown, and combined formats
5. **📁 Intelligent Organization** - Creates structured offline archives with preserved navigation

**Result:** A complete, self-contained documentation snapshot that works entirely offline.

## 🎯 **Who Uses D361?**

**Enterprise Documentation Teams:**
- **Technical Writers** - Archive documentation versions, perform offline reviews, and create distribution packages
- **DevOps Engineers** - Integrate offline documentation into deployment pipelines and container images
- **Support Engineers** - Access knowledge bases instantly in customer support scenarios
- **Compliance Teams** - Create immutable documentation snapshots for regulatory requirements

**Development & Integration:**
- **Software Developers** - Bundle documentation with applications for offline environments
- **System Integrators** - Deploy documentation in air-gapped or restricted network environments  
- **CI/CD Pipelines** - Automated documentation processing and archival as part of build processes
- **Documentation Toolkit Builders** - Use D361 as a foundational component (like in `vexy-help`)

**Specialized Use Cases:**
- **Industrial/Manufacturing** - Offline documentation access on factory floors and production environments
- **Healthcare/Government** - Secure, compliant documentation in regulated environments
- **Field Service** - Technical documentation for remote locations with limited connectivity
- **Training & Education** - Portable documentation packages for distributed learning

## 🚀 **Why Choose D361?**

**🔧 Technical Excellence:**
- **Robust Architecture** - Handles complex modern documentation sites with dynamic content
- **Enterprise Performance** - Concurrent processing with intelligent retry mechanisms and error handling
- **Multiple Fallback Strategies** - Ensures successful content extraction even with challenging sites
- **Format Flexibility** - Outputs HTML, Markdown, and combined formats for different use cases

**🌐 Real-World Reliability:**
- **Production-Tested** - Successfully processes large-scale documentation sites with thousands of pages
- **Stealth Browser Automation** - Advanced Playwright techniques to handle cookie banners, virtual scrolling, and dynamic loading
- **Content Preservation** - Maintains original navigation structure, styling, and cross-references
- **Error Resilience** - Comprehensive error handling ensures partial success even with network issues

**🔄 Integration-Friendly:**
- **Standalone Operation** - Works independently without external dependencies on other toolkit components
- **API-First Design** - Clean programmatic interface for integration into larger workflows
- **Container-Ready** - Docker-friendly with minimal resource requirements
- **Cross-Platform** - Native support for Linux, macOS, and Windows environments

## ⚡ **Core Features & Capabilities**

### 🎯 **Complete Documentation Extraction**
D361 employs sophisticated techniques to capture entire documentation ecosystems:

```python
# Advanced content discovery with multiple fallback strategies
from d361.offline.parser import parse_sitemap

# Strategy 1: Direct sitemap parsing
urls = await parse_sitemap("https://docs.example.com/sitemap-en.xml")

# Strategy 2: Robots.txt discovery + parsing  
urls = await parse_sitemap("https://docs.example.com/robots.txt", strategy="robots")

# Strategy 3: Stealth browser automation for protected sites
urls = await parse_sitemap("https://docs.example.com", strategy="stealth")
```

**What gets captured:**
- 📄 All article content (HTML + converted Markdown)
- 🗺️ Complete navigation hierarchy with nested categories
- 🖼️ Referenced images and media files
- 🔗 Cross-references and internal links  
- 🎨 Original styling and CSS (optional)

### 🚀 **Multi-Strategy Sitemap Parsing**
Robust discovery mechanisms ensure content extraction even from challenging sites:

```python
from d361.offline.d361_offline import D361Offline
from d361.offline.config import Config

config = Config(
    map_url="https://docs.example.com/sitemap-en.xml",
    # Fallback strategies automatically attempted if primary fails
    effort=True,  # Enable additional discovery strategies
    max_concurrent=8,  # Concurrent parsing attempts
    retries=3  # Per-strategy retry attempts
)

offline_gen = D361Offline(config)
await offline_gen.prep()  # Intelligent sitemap discovery and parsing
```

**Parsing Strategies:**
1. **Direct Navigation** - Standard HTTP GET to sitemap URL
2. **Stealth Browser** - Playwright with human-like behavior patterns
3. **HTTP Direct** - aiohttp-based lightweight parsing
4. **Robots.txt Discovery** - Automatic sitemap URL discovery
5. **Google Cache** - Last resort via cached versions

### 🤖 **Advanced Browser Automation**
Playwright-powered content extraction handles modern web complexity:

```python
from d361.offline.browser import setup_browser, expand_all_items

# Configure stealth browser with realistic parameters
browser_config = {
    'headless': True,
    'user_agent': 'Mozilla/5.0 (compatible; D361 Documentation Archiver)',
    'viewport': {'width': 1920, 'height': 1080},
    'extra_http_headers': {
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br'
    }
}

async with setup_browser(**browser_config) as browser:
    page = await browser.new_page()
    await page.goto("https://docs.example.com")
    
    # Handle dynamic content loading
    navigation_tree = await page.locator('#left-panel d360-data-list-tree-view').first
    await expand_all_items(navigation_tree, page)  # Recursively expand all navigation
    
    # Extract complete navigation structure
    nav_data = await extract_tree_structure(navigation_tree)
```

**Browser Automation Capabilities:**
- 🍪 **Cookie Banner Dismissal** - Automatically handles consent dialogs  
- 📜 **Virtual Scrolling** - Loads all content from virtually rendered lists
- 🌳 **Dynamic Tree Expansion** - Recursively expands navigation hierarchies
- ⏱️ **Network Idle Detection** - Waits for complete content loading
- 🔄 **Retry Logic** - Handles intermittent failures gracefully

### 📱 **Multi-Format Output Generation**
Flexible output formats for different consumption needs:

```python
# Configure output formats and customization
config = Config(
    map_url="https://docs.example.com/sitemap-en.xml",
    output_dir=Path("./offline_docs"),
    css_file=Path("./custom-styling.css"),  # Custom CSS for HTML output
    
    # File naming patterns
    all_docs_html_filename="complete_documentation.html",
    all_docs_md_filename="complete_documentation.md",
    
    # Processing options
    test=False,  # Process all content (not just test subset)
    verbose=True  # Detailed logging
)

offline_gen = D361Offline(config)
await offline_gen.all()  # Generate all formats
```

**Generated Output Structure:**
```
offline_docs/docs.example.com/
├── prep.json              # Sitemap discovery metadata
├── fetch.json             # Content extraction results  
├── nav.json               # Navigation structure data
├── nav.html               # Standalone navigation menu
├── nav.md                 # Markdown navigation index
├── all_docs.html          # Complete HTML with embedded navigation
├── all_docs.md            # Complete Markdown with TOC
├── html/                  # Individual HTML pages
│   ├── getting-started.html
│   ├── api-reference.html
│   └── ...
└── md/                    # Individual Markdown pages
    ├── getting-started.md
    ├── api-reference.md
    └── ...
```

### ⚡ **Performance-Optimized Processing**
Enterprise-grade performance with intelligent resource management:

```python
from d361.offline.config import Config

# Performance-tuned configuration
config = Config(
    map_url="https://docs.example.com/sitemap-en.xml",
    max_concurrent=12,        # Concurrent page fetching
    timeout=60,              # Per-page timeout (seconds)
    retries=5,               # Retry attempts for failed pages  
    pause=0,                 # No artificial delays (max speed)
)

# Monitor performance during processing
offline_gen = D361Offline(config)

start_time = time.time()
result = await offline_gen.all()
processing_time = time.time() - start_time

print(f"Processed {len(result['content'])} pages in {processing_time:.2f}s")
print(f"Average: {processing_time/len(result['content']):.3f}s per page")
```

**Performance Features:**
- 🚀 **Concurrent Downloads** - Configurable parallel processing (default: 5 concurrent)
- 🔄 **Exponential Backoff** - Intelligent retry delays with `tenacity` library
- 💾 **Memory Efficient** - Streaming content processing to minimize memory usage
- 📊 **Progress Tracking** - Real-time processing status and performance metrics
- ⚡ **Network Optimization** - Connection pooling and keep-alive for HTTP efficiency

### Installation

D361 can be installed in multiple ways depending on your needs:

#### Quick Installation (Recommended)

```bash
# One-line installation script
curl -sSL https://raw.githubusercontent.com/twardoch/d361/main/scripts/install.sh | bash
```

#### Manual Installation

**Via pip:**
```bash
pip install d361
playwright install chromium
```

**Via uv (faster):**
```bash
uv pip install d361
playwright install chromium
```

**Binary Download (No Python required):**
```bash
# Linux
curl -L -o d361-offline https://github.com/twardoch/d361/releases/latest/download/d361-offline-ubuntu-latest
chmod +x d361-offline

# macOS
curl -L -o d361-offline https://github.com/twardoch/d361/releases/latest/download/d361-offline-macos-latest
chmod +x d361-offline

# Windows
curl -L -o d361-offline.exe https://github.com/twardoch/d361/releases/latest/download/d361-offline-windows-latest.exe
```

#### Installation Options

The installation script supports various options:

```bash
# Install specific version
./scripts/install.sh --version 1.0.0

# Install via specific method
./scripts/install.sh --method binary

# Install with Playwright browsers
./scripts/install.sh --install-browsers

# Install to custom directory
./scripts/install.sh --install-dir ~/.local/bin

# See all options
./scripts/install.sh --help
```

### Command Line Usage

The package provides a command-line interface `d361-offline` with several operations. The main commands are `prep`, `fetch`, `build`, and `all`.

**1. `all` (Recommended for most users):**
Runs the entire process: preparation, fetching, and building.
```bash
d361-offline all --map-url="https://docs.example.com/sitemap-en.xml" --output-dir="my_offline_docs"
```
*   `--map-url`: (Required) The URL to your Document360 sitemap (usually ends with `sitemap-en.xml` or similar).
*   `--output-dir`: (Optional) The directory where offline documentation will be saved. Defaults to a folder named after the domain in the current directory (e.g., `./docs.example.com/`).
*   `--style`: (Optional) Path to a custom CSS file to style the HTML output.
*   `--nav-url`: (Optional) URL of a specific page to extract navigation from. If not provided, uses the first URL from the sitemap.

**2. Individual Steps (for advanced control):**

*   **`prep`**: Parses the sitemap and extracts the navigation structure.
    ```bash
    d361-offline prep --map-url="https://docs.example.com/sitemap-en.xml" --output-dir="my_docs"
    ```
    This creates a `prep.json` file in the output directory.

*   **`fetch`**: Downloads the content for all URLs found in the `prep` phase.
    ```bash
    d361-offline fetch --prep-file="my_docs/prep.json" --output-dir="my_docs"
    ```
    This creates a `fetch.json` file and saves individual HTML/Markdown pages.

*   **`build`**: Generates the final combined documentation files from the fetched content.
    ```bash
    d361-offline build --fetch-file="my_docs/fetch.json" --output-dir="my_docs" --style="path/to/custom.css"
    ```

**Getting Help:**
For a full list of options for each command, use `d361-offline <command> --help`.
For example: `d361-offline all --help`.

### Programmatic Usage

You can also use D361 from your Python scripts:

```python
import asyncio
from pathlib import Path
from d361.offline.config import Config
from d361.offline.d361_offline import D361Offline

async def generate_my_docs():
    # Configure the generator
    # Ensure map_url is provided
    sitemap_url = "https://docs.example.com/sitemap-en.xml" # Replace with actual sitemap URL
    if not sitemap_url:
        raise ValueError("map_url must be set for Config")

    config = Config(
        map_url=sitemap_url,
        output_dir=Path("custom_offline_docs"),  # Output will be in ./custom_offline_docs/docs.example.com/
        css_file=Path("styles/my_custom_style.css") if Path("styles/my_custom_style.css").exists() else None,
        max_concurrent=5,  # Number of parallel downloads
        retries=3,         # Number of retries for failed requests
        timeout=60,        # Timeout for page loads in seconds
        verbose=False,     # Set to True for detailed logging
        test=False         # Set to True to process only a few items for testing
    )

    # Create an instance of the offline generator
    offline_generator = D361Offline(config)

    try:
        print(f"Starting offline generation for {config.map_url}...")
        print(f"Output will be saved to: {config.output_dir.resolve()}")

        # Run the entire process: prep, fetch, and build
        await offline_generator.all()

        # Alternatively, run individual phases:
        # print("Running prep phase...")
        # prep_data = await offline_generator.prep()
        # print(f"Prep phase complete. Data saved to {config.prep_file}")

        # print("Running fetch phase...")
        # fetch_data = await offline_generator.fetch(prep_file=config.prep_file)
        # print(f"Fetch phase complete. Data saved to {config.fetch_file}")

        # print("Running build phase...")
        # await offline_generator.build(fetch_file=config.fetch_file)
        # print("Build phase complete.")

        print("Offline documentation generated successfully!")
        print(f"Combined HTML: {config.output_dir / config.all_docs_html_filename}")
        print(f"Combined Markdown: {config.output_dir / config.all_docs_md_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # Ensure Playwright browsers are installed:
    # Run `playwright install` in your terminal if you haven't already.
    asyncio.run(generate_my_docs())
```

### Configuration Options

The behavior of `d361-offline` is controlled by the `Config` model (see `src/d361/offline/config.py`). Key options include:

| Option (`Config` field) | CLI Argument    | Description                                           | Default (from `Config`) |
|-------------------------|-----------------|-------------------------------------------------------|-------------------------|
| `map_url`               | `--map-url`     | URL of the sitemap (e.g., sitemap.xml)                | **Required** (None by default, must be set) |
| `nav_url`               | `--nav-url`     | URL of a page to extract navigation from (optional)   | None                    |
| `output_dir`            | `--output-dir`  | Base directory for output. A subfolder named after the domain will be created here. | Current working directory |
| `css_file`              | `--style` (build)| Path to custom CSS file for styling HTML output       | None                    |
| `effort`                | `--effort` (prep)| Try harder to map all sitemap links in navigation     | `False`                 |
| `max_concurrent`        | `--parallel`    | Maximum number of concurrent download requests        | 5                       |
| `retries`               | `--retries`     | Number of retry attempts for failed requests          | 3                       |
| `timeout`               | `--timeout`     | Request timeout in seconds for page loads             | 60                      |
| `verbose`               | `--verbose`     | Enable verbose (DEBUG level) logging                  | `False`                 |
| `test`                  | `--test` (prep, fetch) | Test mode: process only a few items (typically 5)  | `False`                 |
| `pause`                 | `--wait` (prep) | Pause during navigation extraction (for debugging browser) | `False` (numeric value for seconds in CLI) |

*Note: Default `output_dir` behavior: If `map_url` is `https://docs.example.com/...` and `output_dir` is `my_docs` (or not set, defaulting to current dir), the actual output path will be `my_docs/docs.example.com/`.*

### Output Structure

The generated offline documentation will be organized as follows in your specified output directory (e.g., `output_dir/your_domain_com/`):

```
output_dir/your_domain_com/
├── prep.json          # Intermediate data from preparation phase (URLs, navigation)
├── fetch.json         # Intermediate data from fetch phase (content map)
├── nav.json           # Navigation structure in JSON format
├── nav.html           # Standalone HTML version of the navigation menu
├── nav.md             # Markdown version of the navigation menu
├── all_docs.html      # Combined HTML documentation with navigation and styling
├── all_docs.md        # Combined Markdown documentation with a table of contents
├── html/              # Directory for individual HTML page files
│   ├── page-slug-1.html
│   ├── page-slug-2.html
│   └── ...
└── md/                # Directory for individual Markdown page files
    ├── page-slug-1.md
    ├── page-slug-2.md
    └── ...
```
If a custom CSS file is used, it will be copied into `html/assets/` and linked in `all_docs.html`.

## Part 2: Technical Deep-Dive

This section describes how D361 works internally, its architecture, and guidelines for contributors.

### How the Code Works

D361 operates in a three-phase workflow: **Prep**, **Fetch**, and **Build**. All operations are asynchronous using Python's `asyncio` library for efficient I/O and concurrency.

**Core Workflow:**

1.  **Prep Phase:**
    *   Parses the sitemap (`map_url`) to get a list of all unique page URLs.
    *   Extracts the navigation structure (table of contents) from a specified page (`nav_url` or the first sitemap URL).
    *   Saves this information (`urls`, `navigation`, `config`) into `prep.json`.
    *   Generates `nav.json`, `nav.html`, and `nav.md`.

2.  **Fetch Phase:**
    *   Reads `prep.json`.
    *   For each URL, fetches the page content (title, HTML body, Markdown version).
    *   Saves individual page content as `html/<slug>.html` and `md/<slug>.md`.
    *   Saves all fetched content mapped by URL, along with the navigation structure and config, into `fetch.json`.

3.  **Build Phase:**
    *   Reads `fetch.json`.
    *   Generates `all_docs.html`: A single HTML file containing all articles, prepended with the navigation menu and linked to the specified CSS.
    *   Generates `all_docs.md`: A single Markdown file containing all articles, with a generated table of contents at the top.

**Key Components and Processes:**

*   **Configuration (`src/d361/offline/config.py`):**
    *   The `Config` class (Pydantic model) manages all settings. It validates inputs, computes default values (like `output_dir` based on the domain), and provides paths for various output files.

*   **Main Orchestrator (`src/d361/offline/d361_offline.py`):**
    *   The `D361Offline` class is the heart of the generator. It takes a `Config` object and has methods for `prep()`, `fetch()`, `build()`, and `all()`.
    *   It coordinates interactions between other modules.

*   **Command Line Interface (`src/d361/offline/__main__.py`):**
    *   Uses the `fire` library to expose `D361Offline` methods and configuration options to the command line as `d361-offline prep`, `fetch`, `build`, `all`.

*   **Sitemap Parsing (`src/d361/offline/parser.py`):**
    *   The `parse_sitemap` function is responsible for fetching and extracting URLs from the `sitemap.xml`.
    *   It employs multiple strategies for robustness:
        1.  Direct Playwright navigation (`_parse_with_playwright_direct`).
        2.  Playwright with enhanced stealth techniques (`_parse_with_playwright_stealth`) to mimic human browsing.
        3.  Direct HTTP GET request using `aiohttp` (`_parse_with_aiohttp_direct`).
        4.  Checking `robots.txt` for sitemap directives and then parsing found URLs (`_parse_with_playwright_via_robots`).
        5.  As a last resort, it can try Google's web cache of the sitemap.
    *   Uses `BeautifulSoup` (with `lxml` parser) to parse XML content and extract `<loc>` tags.

*   **Navigation Extraction (`src/d361/offline/navigation.py`):**
    *   The `extract_navigation` function uses Playwright to load the `nav_url`.
    *   This is one ofthe most complex interactions due to Document360's dynamic UI:
        *   **Cookie/Consent Handling:** Attempts to detect and dismiss various cookie consent banners.
        *   **Tree Expansion:** Locates the main navigation tree element (e.g., `#left-panel ... d360-data-list-tree-view`). It then calls `expand_navigation_tree` which uses `browser.expand_all_items`.
        *   `expand_all_items` (in `browser.py`) repeatedly scrolls the navigation pane (to load virtually rendered items via `scroll_to_bottom`) and clicks on collapsed item indicators (e.g., triangle icons) until all navigation nodes are visible.
        *   **Structure Parsing:** `extract_tree_structure` then iterates over the DOM elements of the expanded tree to rebuild the hierarchical navigation data (titles, links, children).
    *   Includes fallback mechanisms if standard Document360 selectors are not found.

*   **Content Fetching and Processing (`src/d361/offline/content.py`, `D361Offline.process_url`):**
    *   For each URL, `D361Offline.process_url` launches a Playwright page.
    *   `extract_page_content` (in `content.py`) is called:
        *   Navigates to the URL.
        *   Attempts to dismiss cookie banners.
        *   Waits for network idle and content to render.
        *   Extracts the page title (trying common selectors like `h1.article-title`).
        *   Extracts the main article HTML content (trying selectors like `#articleContent`, `.article-content`).
        *   Converts the extracted HTML to Markdown using the `markdownify` library.
    *   The `D361Offline` class then saves this content to `html/<slug>.html` and `md/<slug>.md`. Slugs are generated from URLs.

*   **Browser Automation (`src/d361/offline/browser.py`):**
    *   `setup_browser`: Configures and launches Playwright (Chromium by default) with specific arguments to appear more like a regular browser and handle various environments.
    *   `scroll_to_bottom`: Handles scrolling within elements that use virtual scrolling (common in Document360 navigation) to ensure all items are loaded into the DOM.
    *   `expand_all_items`: A sophisticated function to recursively find and click "expand" icons in a tree structure, dealing with items that might only appear after scrolling or previous expansions. It uses multiple selector strategies.

*   **Output Generation (`D361Offline._generate_combined_files`, `src/d361/offline/generator.py`):**
    *   `D361Offline._generate_combined_files` is responsible for creating `all_docs.html` and `all_docs.md`.
    *   For `all_docs.html`:
        *   It includes a navigation section generated from `nav.json`.
        *   It appends the HTML content of each article, ordered by the navigation structure.
        *   It embeds the custom CSS (if provided) or a default style.
    *   For `all_docs.md`:
        *   It generates a Table of Contents based on the navigation and article titles.
        *   It appends the Markdown content of each article.
    *   The `generator.py` module contains helper functions for creating directories and was initially intended for more granular file generation, though much of that logic is now within `D361Offline`.

*   **Error Handling and Retries:**
    *   The `tenacity` library is used in `content.extract_page_content` to automatically retry page content extraction on failure, using exponential backoff.
    *   Individual URL processing errors are logged but generally don't stop the entire batch, allowing the tool to fetch as much content as possible.

### Development Environment

This project uses [Hatch](https://hatch.pypa.io/) for managing dependencies, virtual environments, and running development tasks. Hatch leverages [uv](https://github.com/astral-sh/uv) if available, which significantly speeds up environment setup and package installation.

**Setup:**

1.  **Install Hatch and uv**:
    It's recommended to install `uv` first, then use it to install `hatch`.
    ```bash
    # Install uv (refer to official uv documentation for your OS)
    # Example for Linux/macOS:
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # Then install Hatch using uv
    uv pip install hatch
    ```

2.  **Create/Activate Hatch Environment**:
    Navigate to the project root directory and run:
    ```bash
    hatch shell
    ```
    This command:
    *   Creates an isolated virtual environment (e.g., in `.hatch/`) if one doesn't exist.
    *   Installs all project dependencies, including development tools (`pytest`, `ruff`, `mypy`, etc.), using `uv` if available.
    *   Activates the environment in your current shell.

3.  **Install Playwright Browsers**:
    After activating the environment, install the necessary browser binaries for Playwright:
    ```bash
    playwright install
    ```
    This typically installs Chromium, Firefox, and WebKit. D361 primarily uses Chromium.

**Running Tasks with Hatch:**

Hatch scripts are defined in `pyproject.toml` under `[tool.hatch.envs.*.scripts]`.

*   **Run Tests**:
    The project uses `pytest`.
    ```bash
    # Run tests with coverage report
    hatch run test:test-cov

    # Run tests without coverage
    hatch run test:test
    ```

*   **Linting and Formatting**:
    The project uses [Ruff](https://github.com/astral-sh/ruff) for super-fast linting and formatting, and [MyPy](http://mypy-lang.org/) for static type checking.
    ```bash
    # Format code and fix lint issues (where possible)
    hatch run lint:fix  # Or an alias: hatch run fix

    # Check for linting and formatting issues
    hatch run lint:style # Or an alias: hatch run lint

    # Run static type checking
    hatch run lint:typing # Or an alias: hatch run type-check

    # Run all checks (style, format, types)
    hatch run lint:all
    ```

*   **Pre-commit Hooks**:
    The project is configured with pre-commit hooks (see `.pre-commit-config.yaml`). Install them to automatically run checks before each commit:
    ```bash
    pre-commit install
    ```

### Coding and Contribution Guidelines

Contributions are highly welcome! Please adhere to the following guidelines:

1.  **Branching Strategy**:
    *   Create new branches from `main` for features or bug fixes (e.g., `feat/add-new-exporter`, `fix/navigation-parsing-bug`).

2.  **Code Style & Quality**:
    *   **Formatting**: Code is formatted with Ruff. Run `hatch run lint:fix` before committing.
    *   **Linting**: Code is linted with Ruff. Ensure `hatch run lint:style` passes.
    *   **Type Checking**: All code should pass MyPy checks. Run `hatch run lint:typing`.
    *   **Pythonic Code**: Write clear, readable, and idiomatic Python.
    *   **Docstrings and Comments**: Add docstrings to all public modules, classes, and functions. Use comments for complex logic.

3.  **Commit Messages**:
    *   Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.
    *   Examples:
        *   `feat: add support for Confluence sitemap parsing`
        *   `fix: improve resilience of cookie banner dismissal`
        *   `docs: update README with advanced usage examples`
        *   `refactor: simplify content extraction logic`
        *   `test: add unit tests for slug generation`

4.  **Testing**:
    *   Write tests for all new features and bug fixes using `pytest`.
    *   Place tests in the `tests/` directory, mirroring the structure of `src/d361/`.
    *   Aim for high test coverage. Check coverage with `hatch run test:test-cov`.
    *   Ensure all tests pass locally before submitting a Pull Request.

5.  **Pull Requests (PRs)**:
    *   Submit PRs against the `main` branch.
    *   Provide a clear and descriptive title and summary for your PR.
    *   Explain the "what" and "why" of your changes. Link to any relevant issues.
    *   Ensure all GitHub Actions CI checks (tests, linting, type checking) pass on your PR.
    *   Be responsive to feedback and code reviews.

6.  **Dependencies**:
    *   Minimize new dependencies. If adding one, justify its need.
    *   Add new dependencies to `pyproject.toml` under `[project.dependencies]` or `[project.optional-dependencies.dev]`.

### Releases

D361 follows [Semantic Versioning](https://semver.org/) and provides multiple distribution formats:

- **PyPI Package**: Available on [PyPI](https://pypi.org/project/d361/) for `pip` and `uv` installation
- **Binary Releases**: Pre-built executables for Linux, macOS, and Windows
- **Source Code**: Available on [GitHub](https://github.com/twardoch/d361)

Each release includes:
- Source distribution (`.tar.gz`)
- Wheel distribution (`.whl`)
- Standalone binaries for all platforms
- Automated testing across Python 3.10-3.12 and multiple operating systems

#### Release Process

New releases are automatically created when version tags are pushed:

```bash
# Create and push a new release tag
git tag v1.0.0
git push origin v1.0.0
```

This triggers the CI/CD pipeline which:
1. Runs comprehensive tests on all platforms
2. Builds Python packages and binaries
3. Publishes to PyPI
4. Creates GitHub release with binary artifacts

For development and contribution guidelines, see [DEVELOPMENT.md](DEVELOPMENT.md).

### License

D361 is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.