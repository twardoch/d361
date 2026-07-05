# this_file: external/int_folders/d361/src/d361/archive/__init__.py
"""
Archive package - Document360 offline archive processing.

This package provides comprehensive offline archive processing capabilities
including parsing, indexing, and intelligent caching for Document360
documentation archives.
"""

from .cache import CacheConfig, CacheEntry, CacheStats, SqliteCache
from .document360_parser import Document360Parser
from .parser import ArchiveMetadata, ArchiveParser, ArchiveParserConfig, ParsedArchive
from .schema import ArchiveSchema, create_archive_schema, migrate_archive_schema

__all__ = [
    "ArchiveMetadata",
    # Archive parsing
    "ArchiveParser",
    "ArchiveParserConfig",
    # Database schema
    "ArchiveSchema",
    "CacheConfig",
    "CacheEntry",
    "CacheStats",
    # Document360-specific parsing
    "Document360Parser",
    "ParsedArchive",
    # Caching
    "SqliteCache",
    "create_archive_schema",
    "migrate_archive_schema",
]
