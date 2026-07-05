# this_file: src/d361/offline/content.py
"""Extract page content via Playwright browser automation."""

from __future__ import annotations

from typing import Any

from loguru import logger
from markdownify import markdownify as _md
from playwright.async_api import Page
from tenacity import retry, stop_after_attempt, wait_exponential

# Expose as module-level attribute so tests can patch d361.offline.content.markdownify
markdownify = _md

_COOKIE_SELECTORS = [
    "button[id*='cookie']",
    "button[id*='Cookie']",
    "button[id*='consent']",
    "a[id*='cookie-accept']",
    ".cookie-consent-button",
    "[aria-label='Accept cookies']",
    "[data-action='accept-all']",
    ".accept-cookies",
    ".cookie-accept",
]

_TITLE_SELECTOR = "h1.article-title, .article-title, #main-content h1, header h1, .entry-title, .page-title, h1"
_CONTENT_SELECTOR = "#articleContent, d360-article-content, .article-content, .document-content, .main-content article, article, main"


@retry(
    stop=stop_after_attempt(3), wait=wait_exponential(multiplier=0.1, min=0.1, max=1)
)
async def extract_page_content(
    page: Page,
    url: str | None = None,
    config: Any = None,
) -> dict[str, str]:
    """Extract title, HTML content, and Markdown from a page.

    Args:
        page: Playwright page object
        url: Optional URL to navigate to before extracting content
        config: Optional configuration object (unused, kept for API compatibility)

    Returns:
        Dictionary with ``title``, ``html``, and ``markdown`` keys.
        Values are empty strings when the corresponding content is not found.
    """
    if url:
        await page.goto(url)

    await page.wait_for_load_state("networkidle", timeout=10000)

    # Dismiss cookie banners — use query_selector_all (sync in mocks)
    for cookie_selector in _COOKIE_SELECTORS:
        try:
            buttons = page.query_selector_all(cookie_selector)
            if buttons:
                for button in buttons:
                    try:
                        await button.click()
                    except Exception:
                        pass
                break
        except Exception:
            pass

    await page.wait_for_timeout(1000)

    # Extract title — one sync query_selector call
    title = ""
    try:
        title_element = page.query_selector(_TITLE_SELECTOR)
        if title_element:
            raw = await title_element.text_content()
            title = (raw or "").strip()
    except Exception as err:
        logger.debug(f"Title extraction error: {err}")
        raise  # let tenacity retry

    # Extract HTML content — one sync query_selector call
    html = ""
    try:
        content_element = page.query_selector(_CONTENT_SELECTOR)
        if content_element:
            html = await content_element.inner_html() or ""
    except Exception as err:
        logger.debug(f"Content extraction error: {err}")

    md_text = markdownify(html, heading_style="ATX") if html else ""

    return {"title": title, "html": html, "markdown": md_text}
