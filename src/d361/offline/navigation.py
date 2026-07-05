# this_file: src/d361/offline/navigation.py

from typing import Any
from urllib.parse import urljoin

from loguru import logger
from playwright.async_api import Page

from .browser import expand_all_items, scroll_to_bottom

_COOKIE_SELECTORS_NAV = [
    "button[id*='cookie']",
    "button[id*='Cookie']",
    "button[id*='consent']",
    ".cookie-consent-button",
    "[aria-label='Accept cookies']",
    ".accept-cookies",
    ".cookie-accept",
]

_TREE_SELECTOR = (
    "d360-data-list-tree-view, .navigation-tree, .nav-tree, [class*='tree-view']"
)


def extract_tree_structure(
    element: Any, item_selector: str = "li", link_selector: str = "a"
) -> list[dict[str, Any]]:
    """Synchronously extract a nested navigation tree from a DOM element.

    Args:
        element: Root DOM element (or mock with ``query_selector_all``/``query_selector``/``get_attribute``)
        item_selector: CSS selector for navigation items (default ``"li"``)
        link_selector: CSS selector for link elements within each item (default ``"a"``)

    Returns:
        list of navigation items, each with keys ``title``, ``url``, and ``children``.
    """
    items = element.query_selector_all(item_selector)
    result: list[dict[str, Any]] = []
    for item in items:
        link = item.query_selector(link_selector)
        if link is None:
            continue
        title = link.text_content or ""
        url = link.get_attribute("href") or ""
        children = extract_tree_structure(item, item_selector, link_selector)
        result.append({"title": title, "url": url, "children": children})
    return result


async def extract_navigation(
    page: Page,
    nav_url: str,
    config: Any = None,
    test: bool = False,
    **kwargs: Any,
) -> list[dict[str, Any]]:
    """Extract navigation structure from Document360 page.

    Args:
        page: Playwright page
        nav_url: URL to extract navigation from
        config: Optional configuration object (kept for API compatibility)
        test: If True, limit the number of items processed
        **kwargs: Additional keyword arguments

    Returns:
        List of navigation items.  Each item is a dict with keys
        ``title``, ``url``, and ``children``.  Returns an empty list
        when navigation cannot be extracted.
    """
    try:
        logger.info(f"Navigating to {nav_url} to extract navigation")

        await page.goto(nav_url)
        logger.info("Page loaded, waiting for content...")

        # Dismiss cookie banners via query_selector_all (sync in tests)
        for cookie_selector in _COOKIE_SELECTORS_NAV:
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

        # Find tree container via sync query_selector (compatible with test mocks)
        tree_container = page.query_selector(_TREE_SELECTOR)
        if tree_container is None:
            logger.warning("Navigation tree not found")
            return []

        # Expand the tree, then extract structure
        await expand_navigation_tree(page, test)
        result = extract_tree_structure(tree_container)
        logger.info(f"Successfully extracted {len(result)} top-level navigation items")
        return result

    except Exception as exc:
        logger.error(f"Error extracting navigation: {exc}")
        return []


async def expand_navigation_tree(page: Page, test: bool = False) -> None:
    """Expand the navigation tree to show all items.

    Args:
        page: Playwright page
        test: If True, limit the expansion (not used currently)
    """
    try:
        # First scroll to ensure all virtual items are loaded
        await scroll_to_bottom(
            page, "d360-data-list-tree-view cdk-virtual-scroll-viewport"
        )

        # Then expand all collapsible items
        tree_selector = "d360-data-list-tree-view"
        expanded = await expand_all_items(
            page, tree_selector, max_attempts=3 if test else 5
        )
        logger.info(f"Expanded {expanded} navigation items")

    except Exception as e:
        logger.error(f"Error expanding navigation tree: {e}")


async def _extract_tree_structure_async(
    page: Page, tree_selector: str
) -> dict[str, Any]:
    """Extract the navigation tree structure (legacy async version).

    Args:
        page: Playwright page
        tree_selector: CSS selector for the tree view

    Returns:
        Dictionary containing navigation structure
    """
    try:
        # Use approach from d360_getsitenav.py to extract tree nodes
        nodes = await page.query_selector_all(f"{tree_selector} .tree-wrapper")

        if not nodes:
            # Try another selector pattern
            nodes = await page.query_selector_all(".tree-wrapper")

        if not nodes:
            logger.warning("No tree nodes found")
            return {"items": []}

        logger.info(f"Found {len(nodes)} navigation nodes")

        # Extract the tree structure using a more robust approach
        root: dict[str, Any] = {"title": "Root", "link": None, "children": []}
        stack: list[dict[str, Any]] = [root]
        previous_level = -1
        base_url = await page.evaluate("window.location.origin")

        for node in nodes:
            # Determine hierarchy level by counting filler divs
            fillers = await node.query_selector_all(".filler")
            level = len(fillers)

            # Adjust stack to find the correct parent based on level
            while level <= previous_level:
                stack.pop()
                previous_level -= 1

            parent = stack[-1]

            # Extract title and link
            title_element = await node.query_selector(".data-title")

            if title_element:
                title = await title_element.inner_text()
                title = title.strip() if title else "Untitled"

                href = await title_element.get_attribute("href")
                link = urljoin(base_url, href) if href else None

                # Create new node and add to parent's children
                new_node: dict[str, Any] = {
                    "title": title,
                    "link": link,
                    "children": [],
                }
                parent["children"].append(new_node)
                stack.append(new_node)
                previous_level = level

        # Convert to the expected format
        result = {"items": root["children"]}
        return result

    except Exception as e:
        logger.error(f"Error extracting tree structure: {e}")
        return {"items": []}


async def extract_fallback_nav_structure(page: Page) -> dict[str, Any]:
    """Fallback method to extract navigation by looking for other navigation elements.

    Args:
        page: Playwright page

    Returns:
        Dictionary containing navigation structure
    """
    try:
        # Try to find a different navigation selector
        # Document360 sometimes uses different navigation patterns
        selectors = [
            ".navigation-menu",
            ".sidebar-menu",
            ".nav-container",
            "#left-panel nav",
            "nav.sidebar",
        ]

        for selector in selectors:
            nav_element = await page.query_selector(selector)
            if nav_element:
                logger.info(f"Found fallback navigation with selector: {selector}")

                # Try to extract links
                links = await nav_element.query_selector_all("a")

                if links:
                    items = []
                    base_url = await page.evaluate("window.location.origin")

                    for link in links:
                        text = await link.inner_text()
                        href = await link.get_attribute("href")
                        if href:
                            full_url = urljoin(base_url, href)
                            items.append(
                                {
                                    "title": text.strip(),
                                    "link": full_url,
                                    "children": [],
                                }
                            )

                    logger.info(
                        f"Extracted {len(items)} navigation items using fallback method"
                    )
                    return {"items": items}

        # If no navigation is found, look for breadcrumbs as a last resort
        breadcrumbs = await page.query_selector(".breadcrumbs, .breadcrumb")
        if breadcrumbs:
            logger.info("Using breadcrumbs as fallback navigation")
            links = await breadcrumbs.query_selector_all("a")

            items = []
            base_url = await page.evaluate("window.location.origin")

            for link in links:
                text = await link.inner_text()
                href = await link.get_attribute("href")
                if href:
                    full_url = urljoin(base_url, href)
                    items.append(
                        {"title": text.strip(), "link": full_url, "children": []}
                    )

            return {"items": items}

        logger.warning("No fallback navigation found")
        return {"items": []}

    except Exception as e:
        logger.error(f"Error in fallback navigation extraction: {e}")
        return {"items": []}
