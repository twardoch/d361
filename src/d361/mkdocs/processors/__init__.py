"""Content processors for MkDocs export functionality."""
# this_file: external/int_folders/d361/src/d361/mkdocs/processors/__init__.py

from d361.mkdocs.processors.accessibility_optimizer import (
    AccessibilityIssue,
    AccessibilityOptimizer,
    AccessibilityReport,
    ContrastRatio,
    WCAGLevel,
)
from d361.mkdocs.processors.asset_manager import AssetManager
from d361.mkdocs.processors.content_enhancer import ContentEnhancer
from d361.mkdocs.processors.cross_reference_resolver import CrossReferenceResolver
from d361.mkdocs.processors.markdown_processor import MarkdownProcessor

# Phase 3: Plugin Ecosystem Integration components
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
    "AssetManager",
    "ContentEnhancer",
    "ContrastRatio",
    "CrossReferenceResolver",
    "MarkdownExtensionManager",
    # Phase 1 & 2 components
    "MarkdownProcessor",
    "PluginConfig",
    # Phase 3: Plugin Management
    "PluginManager",
    "PluginSet",
    "SEOMetadata",
    # Phase 3: SEO Optimization
    "SEOOptimizer",
    "StructuredData",
    "WCAGLevel",
]
