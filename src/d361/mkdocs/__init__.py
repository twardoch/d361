"""MkDocs export functionality for d361.

This module provides comprehensive Document360 → MkDocs conversion capabilities,
including support for Material theme, popular plugins, and modern MkDocs features.
"""
# this_file: external/int_folders/d361/src/d361/mkdocs/__init__.py

# Exporters
from d361.mkdocs.exporters.config_generator import ConfigGenerator
from d361.mkdocs.exporters.mkdocs_exporter import MkDocsExporter
from d361.mkdocs.exporters.navigation_builder import NavigationBuilder
from d361.mkdocs.exporters.theme_optimizer import ThemeOptimizer
from d361.mkdocs.processors.accessibility_optimizer import (
    AccessibilityIssue,
    AccessibilityOptimizer,
    AccessibilityReport,
    ContrastRatio,
    WCAGLevel,
)
from d361.mkdocs.processors.asset_manager import (
    AssetManager,
    AssetReference,
    OptimizationResult,
)
from d361.mkdocs.processors.content_enhancer import ContentEnhancer
from d361.mkdocs.processors.cross_reference_resolver import (
    AnchorReference,
    CrossReferenceResolver,
    LinkReference,
)

# Processors
from d361.mkdocs.processors.markdown_processor import MarkdownProcessor

# Phase 3: Plugin Ecosystem Integration
from d361.mkdocs.processors.plugin_manager import (
    MarkdownExtensionManager,
    PluginConfig,
    PluginManager,
    PluginSet,
)
from d361.mkdocs.processors.seo_optimizer import (
    SEOMetadata,
    SEOOptimizer,
    StructuredData,
)

__all__ = [
    "AccessibilityIssue",
    # Phase 3: Accessibility Enhancement
    "AccessibilityOptimizer",
    "AccessibilityReport",
    "AnchorReference",
    "AssetManager",
    "AssetReference",
    "ConfigGenerator",
    "ContentEnhancer",
    "ContrastRatio",
    "CrossReferenceResolver",
    "LinkReference",
    "MarkdownExtensionManager",
    # Core Processors (Phase 1 & 2)
    "MarkdownProcessor",
    # Exporters
    "MkDocsExporter",
    "NavigationBuilder",
    "OptimizationResult",
    "PluginConfig",
    # Phase 3: Plugin Management
    "PluginManager",
    "PluginSet",
    "SEOMetadata",
    # Phase 3: SEO Optimization
    "SEOOptimizer",
    "StructuredData",
    "ThemeOptimizer",
    "WCAGLevel",
]
