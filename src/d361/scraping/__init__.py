# this_file: external/int_folders/d361/src/d361/scraping/__init__.py
"""
Scraping package - Document360 web scraping and content extraction.

This package provides comprehensive web scraping capabilities including
browser automation, content extraction, HTML-to-Markdown conversion,
and intelligent deduplication for Document360 websites.
"""

from .content_processor import ContentProcessor, Document360ContentProcessor
from .converter import (
    ConversionConfig,
    ConversionResult,
    ConversionStats,
    Document360MarkdownConverter,
    LinkHandling,
    MarkdownConverter,
    MarkdownStyle,
)
from .deduplicator import (
    ContentDeduplicator,
    DeduplicationConfig,
    DuplicateGroup,
    DuplicateStatus,
    SimilarityAlgorithm,
    SimilarityScore,
)
from .extractor import (
    ContentBlock,
    ContentExtractor,
    ContentType,
    ExtractedContent,
    ExtractionConfig,
    ExtractionQuality,
)
from .scraper import (
    BrowserType,
    Document360Scraper,
    ScrapedPage,
    ScrapingConfig,
    ScrapingMode,
    ScrapingSession,
    UserAgent,
)

__all__ = [
    "BrowserType",
    "ContentBlock",
    # Deduplication
    "ContentDeduplicator",
    # Content extraction
    "ContentExtractor",
    # Content processing
    "ContentProcessor",
    "ContentType",
    "ConversionConfig",
    "ConversionResult",
    "ConversionStats",
    "DeduplicationConfig",
    "Document360ContentProcessor",
    "Document360MarkdownConverter",
    # Web scraping
    "Document360Scraper",
    "DuplicateGroup",
    "DuplicateStatus",
    "ExtractedContent",
    "ExtractionConfig",
    "ExtractionQuality",
    "LinkHandling",
    # Markdown conversion
    "MarkdownConverter",
    "MarkdownStyle",
    "ScrapedPage",
    "ScrapingConfig",
    "ScrapingMode",
    "ScrapingSession",
    "SimilarityAlgorithm",
    "SimilarityScore",
    "UserAgent",
]
