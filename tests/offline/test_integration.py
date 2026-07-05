# this_file: tests/offline/test_integration.py
"""Integration tests for d361.offline module."""

import json
from pathlib import Path
from unittest.mock import AsyncMock, patch

import pytest

from d361.offline.config import Config
from d361.offline.d361_offline import D361Offline


@pytest.fixture
def mock_config(tmp_path: Path) -> Config:
    """Create a mock config for testing."""
    return Config(
        map_url="https://example.com/sitemap.xml",
        output_dir=tmp_path / "test_output",
        test=True,  # Enable test mode
        max_concurrent=2,
        # No retries: keeps tests fast/deterministic and avoids a failing URL's
        # retry attempts consuming mock side_effect entries meant for other URLs.
        retries=0,
    )


@pytest.fixture
def sample_sitemap_urls() -> list[str]:
    """Sample sitemap URLs for testing."""
    return [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3",
    ]


@pytest.fixture
def sample_navigation() -> dict:
    """Sample navigation data for testing.

    Shape matches the real ``extract_navigation()`` contract
    (src/d361/offline/navigation.py): a dict with an "items" list, where each
    item uses "link" (not "url") for its URL.
    """
    return {
        "items": [
            {"title": "Page 1", "link": "https://example.com/page1", "children": []},
            {"title": "Page 2", "link": "https://example.com/page2", "children": []},
        ]
    }


@pytest.fixture
def sample_content() -> dict[str, dict]:
    """Sample content data for testing."""
    return {
        "https://example.com/page1": {
            "title": "Page 1 Title",
            "html": "<h1>Page 1 Title</h1><p>Page 1 content</p>",
            "markdown": "# Page 1 Title\n\nPage 1 content",
        },
        "https://example.com/page2": {
            "title": "Page 2 Title",
            "html": "<h1>Page 2 Title</h1><p>Page 2 content</p>",
            "markdown": "# Page 2 Title\n\nPage 2 content",
        },
    }


def _mock_setup_browser_tuple() -> tuple[AsyncMock, AsyncMock, AsyncMock]:
    """Build a (browser, context, page) AsyncMock triple matching the real
    ``setup_browser() -> tuple[Browser, BrowserContext]`` contract.

    ``d361_offline`` unpacks ``browser, context = await setup_browser(...)``
    and then drives pages via ``context.new_page()`` (not ``browser.new_page()``).
    Using AsyncMock (rather than MagicMock) means every child attribute access
    (``.new_page()``, ``.goto()``, ``.close()``) is itself awaitable by default.
    """
    mock_page = AsyncMock()
    mock_context = AsyncMock()
    mock_context.new_page = AsyncMock(return_value=mock_page)
    mock_browser = AsyncMock()
    return mock_browser, mock_context, mock_page


@pytest.mark.asyncio
async def test_full_workflow_prep_fetch_build(
    mock_config: Config,
    sample_sitemap_urls: list[str],
    sample_navigation: dict,
    sample_content: dict[str, dict],
) -> None:
    """Test the complete workflow: prep -> fetch -> build."""
    offline = D361Offline(mock_config)

    # Mock the individual components
    with (
        patch("d361.offline.d361_offline.parse_sitemap") as mock_parse_sitemap,
        patch("d361.offline.d361_offline.extract_navigation") as mock_extract_nav,
        patch("d361.offline.d361_offline.extract_page_content") as mock_extract_content,
        patch("d361.offline.d361_offline.setup_browser") as mock_setup_browser,
    ):
        # Mock sitemap parsing
        mock_parse_sitemap.return_value = sample_sitemap_urls

        # Mock navigation extraction
        mock_extract_nav.return_value = sample_navigation

        # Mock browser setup: setup_browser() returns (browser, context)
        mock_browser, mock_context, _mock_page = _mock_setup_browser_tuple()
        mock_setup_browser.return_value = (mock_browser, mock_context)

        # Mock content extraction
        mock_extract_content.side_effect = [
            sample_content["https://example.com/page1"],
            sample_content["https://example.com/page2"],
        ]

        # Run the full workflow
        await offline.all()

        # Verify files were created
        assert mock_config.prep_file.exists()
        assert mock_config.fetch_file.exists()
        assert mock_config.nav_json_file.exists()
        assert (mock_config.output_dir / "all_docs.html").exists()
        assert (mock_config.output_dir / "all_docs.md").exists()

        # Verify prep.json content
        with open(mock_config.prep_file) as f:
            prep_data = json.load(f)
            assert prep_data["urls"] == sample_sitemap_urls
            assert prep_data["navigation"] == sample_navigation

        # Verify fetch.json content
        with open(mock_config.fetch_file) as f:
            fetch_data = json.load(f)
            assert len(fetch_data["content"]) == 2
            assert "https://example.com/page1" in fetch_data["content"]
            assert "https://example.com/page2" in fetch_data["content"]


@pytest.mark.asyncio
async def test_prep_phase_only(
    mock_config: Config, sample_sitemap_urls: list[str], sample_navigation: dict
) -> None:
    """Test the prep phase in isolation."""
    offline = D361Offline(mock_config)

    with (
        patch("d361.offline.d361_offline.parse_sitemap") as mock_parse_sitemap,
        patch("d361.offline.d361_offline.extract_navigation") as mock_extract_nav,
        patch("d361.offline.d361_offline.setup_browser") as mock_setup_browser,
    ):
        mock_parse_sitemap.return_value = sample_sitemap_urls
        mock_extract_nav.return_value = sample_navigation

        # Mock browser setup: setup_browser() returns (browser, context)
        mock_browser, mock_context, _mock_page = _mock_setup_browser_tuple()
        mock_setup_browser.return_value = (mock_browser, mock_context)

        # Run prep phase
        result = await offline.prep()

        # Verify results
        assert result["urls"] == sample_sitemap_urls
        assert result["navigation"] == sample_navigation
        assert mock_config.prep_file.exists()
        assert mock_config.nav_json_file.exists()


@pytest.mark.asyncio
async def test_fetch_phase_only(
    mock_config: Config,
    sample_sitemap_urls: list[str],
    sample_navigation: dict,
    sample_content: dict[str, dict],
) -> None:
    """Test the fetch phase in isolation."""
    offline = D361Offline(mock_config)

    # Create prep.json file first
    prep_data = {
        "urls": sample_sitemap_urls,
        "navigation": sample_navigation,
        "config": mock_config.model_dump(),
    }
    mock_config.prep_file.write_text(json.dumps(prep_data))

    with (
        patch("d361.offline.d361_offline.extract_page_content") as mock_extract_content,
        patch("d361.offline.d361_offline.setup_browser") as mock_setup_browser,
    ):
        # Mock browser setup: setup_browser() returns (browser, context)
        mock_browser, mock_context, _mock_page = _mock_setup_browser_tuple()
        mock_setup_browser.return_value = (mock_browser, mock_context)

        # Mock content extraction
        mock_extract_content.side_effect = [
            sample_content["https://example.com/page1"],
            sample_content["https://example.com/page2"],
        ]

        # Run fetch phase
        result = await offline.fetch()

        # Verify results
        assert len(result["content"]) == 2
        assert "https://example.com/page1" in result["content"]
        assert "https://example.com/page2" in result["content"]
        assert mock_config.fetch_file.exists()

        # Verify individual page files were created
        assert (mock_config.html_dir / "page1.html").exists()
        assert (mock_config.html_dir / "page2.html").exists()
        assert (mock_config.md_dir / "page1.md").exists()
        assert (mock_config.md_dir / "page2.md").exists()


@pytest.mark.asyncio
async def test_build_phase_only(
    mock_config: Config, sample_navigation: dict, sample_content: dict[str, dict]
) -> None:
    """Test the build phase in isolation."""
    offline = D361Offline(mock_config)

    # Create fetch.json file first
    fetch_data = {
        "content": sample_content,
        "navigation": sample_navigation,
        "config": mock_config.model_dump(),
    }
    mock_config.fetch_file.write_text(json.dumps(fetch_data))

    # build() assembles the combined Markdown from the per-page .md files that
    # the fetch phase would have written to md_dir (it does not re-derive
    # Markdown from fetch.json's content dict) - see process_url()'s frontmatter
    # format in d361_offline.py. Since this test exercises build() in isolation,
    # write those per-page files ourselves, matching that exact format.
    mock_config.md_dir.mkdir(parents=True, exist_ok=True)
    for url, content in sample_content.items():
        slug = offline._get_slug(url)
        (mock_config.md_dir / f"{slug}.md").write_text(
            f"""---
title: {content["title"]}
url: {url}
---

{content["markdown"]}
"""
        )

    # Run build phase
    await offline.build()

    # Verify combined files were created
    assert (mock_config.output_dir / "all_docs.html").exists()
    assert (mock_config.output_dir / "all_docs.md").exists()

    # Verify content of combined files
    html_content = (mock_config.output_dir / "all_docs.html").read_text()
    assert "Page 1 Title" in html_content
    assert "Page 2 Title" in html_content
    assert "Page 1 content" in html_content
    assert "Page 2 content" in html_content

    md_content = (mock_config.output_dir / "all_docs.md").read_text()
    assert "# Page 1 Title" in md_content
    assert "# Page 2 Title" in md_content
    assert "Page 1 content" in md_content
    assert "Page 2 content" in md_content


@pytest.mark.asyncio
async def test_error_handling_in_fetch(
    mock_config: Config, sample_sitemap_urls: list[str], sample_navigation: dict
) -> None:
    """Test error handling during fetch phase."""
    offline = D361Offline(mock_config)

    # Create prep.json file
    prep_data = {
        "urls": sample_sitemap_urls,
        "navigation": sample_navigation,
        "config": mock_config.model_dump(),
    }
    mock_config.prep_file.write_text(json.dumps(prep_data))

    with (
        patch("d361.offline.d361_offline.extract_page_content") as mock_extract_content,
        patch("d361.offline.d361_offline.setup_browser") as mock_setup_browser,
    ):
        # Mock browser setup: setup_browser() returns (browser, context)
        mock_browser, mock_context, _mock_page = _mock_setup_browser_tuple()
        mock_setup_browser.return_value = (mock_browser, mock_context)

        # Mock content extraction with some failures
        mock_extract_content.side_effect = [
            {"title": "Page 1", "html": "<p>Content 1</p>", "markdown": "Content 1"},
            Exception("Failed to extract page 2"),
            {"title": "Page 3", "html": "<p>Content 3</p>", "markdown": "Content 3"},
        ]

        # Run fetch phase - should handle errors gracefully
        result = await offline.fetch()

        # Should still process successful pages
        assert len(result["content"]) == 2
        assert "https://example.com/page1" in result["content"]
        assert "https://example.com/page3" in result["content"]
        assert "https://example.com/page2" not in result["content"]


@pytest.mark.asyncio
async def test_concurrent_processing(
    mock_config: Config,
    sample_sitemap_urls: list[str],
    sample_navigation: dict,
    sample_content: dict[str, dict],
) -> None:
    """Test concurrent processing of multiple URLs."""
    # Set higher concurrency for this test
    mock_config.max_concurrent = 3
    offline = D361Offline(mock_config)

    # Create prep.json file
    prep_data = {
        "urls": sample_sitemap_urls,
        "navigation": sample_navigation,
        "config": mock_config.model_dump(),
    }
    mock_config.prep_file.write_text(json.dumps(prep_data))

    with (
        patch("d361.offline.d361_offline.extract_page_content") as mock_extract_content,
        patch("d361.offline.d361_offline.setup_browser") as mock_setup_browser,
    ):
        # Mock browser setup: setup_browser() returns (browser, context)
        mock_browser, mock_context, _mock_page = _mock_setup_browser_tuple()
        mock_setup_browser.return_value = (mock_browser, mock_context)

        # Mock content extraction
        mock_extract_content.side_effect = [
            sample_content["https://example.com/page1"],
            sample_content["https://example.com/page2"],
            {"title": "Page 3", "html": "<p>Content 3</p>", "markdown": "Content 3"},
        ]

        # Run fetch phase
        result = await offline.fetch()

        # Should process all URLs
        assert len(result["content"]) == 3
        assert mock_extract_content.call_count == 3
