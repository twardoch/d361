# this_file: src/d361/offline/parser.py

import asyncio
import random
import re
from typing import Any

import aiohttp
from bs4 import BeautifulSoup
from loguru import logger
from playwright.async_api import BrowserContext, Page, async_playwright


async def parse_sitemap(config: Any, test: bool = False, pause: int = 0) -> set[str]:
    """Parse a sitemap XML to extract all URLs.

    Args:
        config: Config object with ``map_url`` attribute, or a plain URL string.
        test: If True, limit the number of URLs returned to 5.
        pause: Number of seconds to pause between requests (unused, kept for
            API compatibility).

    Returns:
        Set of URLs found in the sitemap.

    Raises:
        ValueError: If no sitemap URL can be determined.
        Exception: Re-raises the last method error when every method fails.
    """
    # Accept both Config objects and plain URL strings
    if hasattr(config, "map_url"):
        sitemap_url: str = config.map_url
    else:
        sitemap_url = config  # type: ignore[assignment]

    if not sitemap_url:
        msg = "No sitemap URL provided"
        raise ValueError(msg)

    logger.info(f"Parsing sitemap from {sitemap_url}")

    methods = [
        _parse_with_playwright_direct,
        _parse_with_playwright_stealth,
        _parse_with_aiohttp_direct,
        _parse_with_playwright_via_robots,
    ]

    last_exc: Exception | None = None

    for method in methods:
        logger.info(f"Trying method: {method.__name__}")
        try:
            raw = await method(config)  # pass config so mocks receive it unchanged
            # Any non-exception result terminates the loop — including empty results.
            # (Only raised exceptions cause fallback to the next method.)
            if isinstance(raw, str):
                urls = _extract_urls_from_xml(raw)
            elif raw is not None:
                urls = set(raw)
            else:
                urls = set()
            logger.info(f"Got {len(urls)} URLs via {method.__name__}")
            if test and urls:
                logger.info(f"Test mode: limiting to 5 URLs (from {len(urls)} total)")
                urls = set(list(urls)[:5])
            return urls
        except Exception as exc:
            logger.warning(f"Method {method.__name__} failed: {exc}")
            last_exc = exc

    if last_exc is not None:
        raise last_exc

    logger.info("Found 0 URLs in total")
    return set()


async def _setup_stealth_context() -> tuple[Any, BrowserContext]:
    """Create a stealthy browser context to avoid detection.

    Returns:
        Tuple of (browser, context)
    """
    p = await async_playwright().start()

    # List of common user agents
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    ]

    browser = await p.chromium.launch(
        headless=True,
        args=[
            "--disable-blink-features=AutomationControlled",
            "--disable-features=IsolateOrigins,site-per-process",
        ],
    )

    context = await browser.new_context(
        user_agent=random.choice(user_agents),
        viewport={"width": 1920, "height": 1080},
        device_scale_factor=1,
        is_mobile=False,
        has_touch=False,
        locale="en-US",
        timezone_id="America/New_York",
    )

    # Modify navigator properties to avoid detection
    await context.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => false
        });
        Object.defineProperty(navigator, 'plugins', {
            get: () => [
                { description: "PDF Viewer", filename: "internal-pdf-viewer" },
                { description: "Chrome PDF Viewer", filename: "chrome-pdf-viewer" },
                { description: "Chromium PDF Viewer", filename: "chromium-pdf-viewer" },
                { description: "Microsoft Edge PDF Viewer", filename: "edge-pdf-viewer" },
                { description: "WebKit built-in PDF", filename: "webkit-pdf-viewer" }
            ]
        });
    """)

    return browser, context


async def _parse_with_playwright_direct(sitemap_url: str) -> set[str]:
    """Parse sitemap using Playwright with direct navigation.

    Args:
        sitemap_url: URL of the sitemap to parse

    Returns:
        Set of URLs found in the sitemap
    """
    browser, context = await _setup_stealth_context()

    try:
        page = await context.new_page()

        # Set extra headers to appear more like a browser
        await page.set_extra_http_headers(
            {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "DNT": "1",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Cache-Control": "max-age=0",
            }
        )

        # Navigate with increased timeout
        logger.info(f"Navigating to {sitemap_url}")
        response = await page.goto(sitemap_url, wait_until="networkidle", timeout=60000)

        if not response:
            logger.error("No response received")
            return set()

        status = response.status
        logger.info(f"Response status: {status}")

        if status != 200:
            logger.error(f"Failed to load sitemap, status code: {status}")
            return set()

        content = await page.content()

        # Log a sample of the content for debugging
        content_preview = content[:200].replace("\n", " ")
        logger.debug(f"Content preview: {content_preview}...")

        return await _extract_urls_from_content(content, page)

    except Exception as e:
        logger.error(f"Error in Playwright direct navigation: {e}")
        return set()

    finally:
        if browser:
            await browser.close()


async def _parse_with_playwright_stealth(sitemap_url: str) -> set[str]:
    """Parse sitemap using Playwright with advanced stealth techniques.

    Args:
        sitemap_url: URL of the sitemap to parse

    Returns:
        Set of URLs found in the sitemap
    """
    browser, context = await _setup_stealth_context()

    try:
        page = await context.new_page()

        # Emulate human-like behavior with random delays
        page.set_default_timeout(
            90000
        )  # No await needed as this doesn't return a value

        # First visit the main site to establish cookies and session
        main_url = f"{sitemap_url.split('/sitemap', maxsplit=1)[0]}/"
        logger.info(f"First visiting main site: {main_url}")

        await page.goto(main_url, wait_until="domcontentloaded")
        await asyncio.sleep(random.uniform(2, 4))

        # Perform some random scrolling to look more human
        await page.evaluate("""
            () => {
                window.scrollTo(0, Math.floor(Math.random() * 100));
                setTimeout(() => {
                    window.scrollTo(0, Math.floor(Math.random() * 300));
                }, Math.random() * 400 + 300);
            }
        """)

        await asyncio.sleep(random.uniform(1, 3))

        # Now navigate to the sitemap
        logger.info(f"Now navigating to sitemap: {sitemap_url}")
        response = await page.goto(sitemap_url, wait_until="networkidle")

        if not response:
            logger.error("No response received")
            return set()

        status = response.status
        logger.info(f"Response status: {status}")

        if status != 200:
            logger.error(f"Failed to load sitemap, status code: {status}")
            return set()

        content = await page.content()
        return await _extract_urls_from_content(content, page)

    except Exception as e:
        logger.error(f"Error in Playwright stealth navigation: {e}")
        return set()

    finally:
        if browser:
            await browser.close()


async def _parse_with_aiohttp_direct(sitemap_url: str) -> set[str]:
    """Parse sitemap using direct HTTP request with aiohttp.

    Args:
        sitemap_url: URL of the sitemap to parse

    Returns:
        Set of URLs found in the sitemap
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0",
    }

    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(
                sitemap_url, timeout=aiohttp.ClientTimeout(total=30)
            ) as resp:
                if resp.status != 200:
                    logger.error(
                        f"Direct HTTP request failed with status {resp.status}"
                    )
                    return set()

                text = await resp.text()
                return _extract_urls_from_xml(text)

    except Exception as e:
        logger.error(f"Error in direct HTTP request: {e}")
        return set()


async def _parse_with_playwright_via_robots(sitemap_url: str) -> set[str]:
    """Try to find sitemap URL in robots.txt and then parse it.

    Args:
        sitemap_url: Original sitemap URL to use as a fallback

    Returns:
        Set of URLs found in the sitemap
    """
    # Extract domain from sitemap URL
    domain_match = re.match(r"https?://([^/]+)", sitemap_url)
    if not domain_match:
        logger.error(f"Could not extract domain from {sitemap_url}")
        return set()

    domain = domain_match.group(0)  # Full domain with protocol
    robots_url = f"{domain}/robots.txt"

    browser, context = await _setup_stealth_context()

    try:
        page = await context.new_page()

        # Visit robots.txt
        logger.info(f"Checking robots.txt at {robots_url}")
        response = await page.goto(robots_url, wait_until="networkidle")

        if not response or response.status != 200:
            logger.warning(
                f"Could not access robots.txt, status: {response.status if response else 'No response'}"
            )
            return set()

        await page.content()
        robots_text = await page.evaluate("() => document.body.innerText")

        # Look for Sitemap: entries in robots.txt
        sitemap_entries = re.findall(r"(?i)sitemap:\s*(\S+)", robots_text)

        if not sitemap_entries:
            logger.warning("No sitemap entries found in robots.txt")
            return set()

        # Try each sitemap URL found
        for sitemap_entry in sitemap_entries:
            logger.info(f"Found sitemap entry in robots.txt: {sitemap_entry}")
            try:
                entry_urls = await _parse_with_playwright_direct(sitemap_entry)
                if entry_urls:
                    return entry_urls
            except Exception as e:
                logger.warning(f"Failed to parse sitemap from robots.txt entry: {e}")

        return set()

    except Exception as e:
        logger.error(f"Error parsing robots.txt: {e}")
        return set()

    finally:
        if browser:
            await browser.close()


async def _extract_urls_from_content(
    content: str, page: Page | None = None
) -> set[str]:
    """Extract URLs from XML or HTML content.

    Args:
        content: XML or HTML content
        page: Optional Playwright page object for JS evaluation

    Returns:
        Set of extracted URLs
    """
    urls = set()

    # Check if this is HTML wrapping XML
    if "<html" in content.lower() and "</html>" in content.lower():
        logger.info("Detected HTML wrapper, extracting XML content")

        if page:
            # Try to find XML in <pre> tags first
            pre_tag = await page.query_selector("pre")
            if pre_tag:
                logger.info("Found <pre> tag with XML content")
                content = await pre_tag.inner_text()
            else:
                # Use JavaScript to extract content if possible
                logger.info(
                    "No <pre> tag found, trying to extract content via JavaScript"
                )
                try:
                    # Try to find XML content in the page
                    content = await page.evaluate("""
                        () => {
                            // Look for content that looks like XML
                            const text = document.body.innerText;
                            if (text.includes('<urlset') || text.includes('<sitemapindex')) {
                                return text;
                            }
                            // Otherwise return the HTML itself
                            return document.documentElement.outerHTML;
                        }
                    """)
                except Exception as e:
                    logger.warning(f"Error extracting content via JavaScript: {e}")

    # Parse content regardless of whether it's HTML or XML
    xml_urls = _extract_urls_from_xml(content)
    urls.update(xml_urls)

    # If we still don't have URLs, try regex as a last resort
    if not urls:
        logger.info("No URLs found via XML parsing, trying regex")
        regex_urls = re.findall(r"<loc>(.*?)</loc>", content)
        for url in regex_urls:
            urls.add(url.strip())

    return urls


def _extract_urls_from_xml(content: str) -> set[str]:
    """Extract URLs from XML content using BeautifulSoup.

    Args:
        content: XML content

    Returns:
        Set of URLs
    """
    try:
        soup = BeautifulSoup(content, "xml")
        urls = set()

        # Check if this is a sitemap index
        sitemap_tags = soup.find_all("sitemap")
        if sitemap_tags:
            logger.info(f"Found sitemap index with {len(sitemap_tags)} sitemaps")

            # Extract the sitemap URLs
            for sitemap_tag in sitemap_tags:
                loc_tag = (
                    sitemap_tag.find("loc") if hasattr(sitemap_tag, "find") else None
                )
                if loc_tag and hasattr(loc_tag, "text"):
                    sitemap_loc = loc_tag.text.strip()
                    urls.add(sitemap_loc)

        # Check for standard URL set
        else:
            url_tags = soup.find_all("url")
            if url_tags:
                logger.info(f"Found {len(url_tags)} URLs in sitemap")

                for url_tag in url_tags:
                    loc_tag = url_tag.find("loc") if hasattr(url_tag, "find") else None
                    if loc_tag and hasattr(loc_tag, "text"):
                        url = loc_tag.text.strip()
                        urls.add(url)

        return urls

    except Exception as e:
        logger.warning(f"Error parsing XML with BeautifulSoup: {e}")
        return set()
