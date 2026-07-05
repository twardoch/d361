# this_file: external/int_folders/d361/tests/test_mkdocs_integration.py
"""
Integration tests for MkDocs export functionality.

This module tests the complete Document360 → MkDocs export pipeline,
including configuration generation, content processing, and validation.
"""

import asyncio
from pathlib import Path
from unittest.mock import patch

import pytest
import yaml

from d361.api.errors import Document360Error
from d361.core.models import Article, Category
from d361.mkdocs.exporters.config_generator import ConfigGenerator
from d361.mkdocs.exporters.mkdocs_exporter import MkDocsExporter
from d361.mkdocs.exporters.navigation_builder import NavigationBuilder
from d361.mkdocs.processors.asset_manager import AssetManager
from d361.mkdocs.processors.content_enhancer import ContentEnhancer
from d361.mkdocs.processors.cross_reference_resolver import CrossReferenceResolver


@pytest.fixture
def mkdocs_output_dir(test_data_dir: Path) -> Path:
    """Create output directory for MkDocs export."""
    output_dir = test_data_dir / "mkdocs_output"
    output_dir.mkdir(exist_ok=True)
    return output_dir


@pytest.fixture
def config_generator() -> ConfigGenerator:
    """Create ConfigGenerator for testing."""
    return ConfigGenerator(theme="material", enable_plugins=True)


@pytest.fixture
def navigation_builder() -> NavigationBuilder:
    """Create NavigationBuilder for testing."""
    return NavigationBuilder()


@pytest.fixture
def content_enhancer() -> ContentEnhancer:
    """Create ContentEnhancer for testing."""
    return ContentEnhancer(
        site_url="https://docs.test.com", enable_seo=True, validate_links=True
    )


@pytest.fixture
def asset_manager(mkdocs_output_dir: Path) -> AssetManager:
    """Create AssetManager for testing."""
    assets_dir = mkdocs_output_dir / "assets"
    return AssetManager(
        output_dir=assets_dir,
        enable_optimization=True,
        generate_responsive=False,  # Disable for testing
    )


@pytest.fixture
def cross_reference_resolver(sample_articles: list[Article]) -> CrossReferenceResolver:
    """Create CrossReferenceResolver for testing."""
    return CrossReferenceResolver(
        articles=sample_articles, base_url="https://docs.test.com"
    )


@pytest.fixture
async def mkdocs_exporter(
    mkdocs_output_dir: Path, mock_archive_file: Path
) -> MkDocsExporter:
    """Create MkDocsExporter for testing."""
    return MkDocsExporter(
        source="archive",
        archive_path=mock_archive_file,
        output_path=mkdocs_output_dir,
        theme="material",
        enable_plugins=True,
        parallel_processing=False,  # Disable for deterministic testing
    )


class TestConfigGenerator:
    """Test MkDocs configuration generation."""

    @pytest.mark.asyncio
    async def test_generate_basic_config(self, config_generator: ConfigGenerator):
        """Test basic configuration generation."""
        navigation = [
            {"Home": "index.md"},
            {"Guide": ["guide/intro.md", "guide/advanced.md"]},
        ]

        config_yaml = await config_generator.generate_config(
            site_name="Test Documentation",
            navigation=navigation,
            output_path=Path("/tmp/test"),
        )

        # Parse and validate generated config
        config = yaml.safe_load(config_yaml)

        assert config["site_name"] == "Test Documentation"
        assert config["theme"]["name"] == "material"
        assert "search" in str(config["plugins"])
        assert "nav" in config
        assert len(config["nav"]) == 2

    @pytest.mark.asyncio
    async def test_generate_config_from_template(
        self, config_generator: ConfigGenerator
    ):
        """Test configuration generation from Jinja2 template."""
        context = {
            "site_name": "Template Test",
            "site_url": "https://docs.example.com",
            "primary_color": "blue",
            "enable_social_cards": True,
        }

        config_content = await config_generator.generate_config_from_template(
            "material_theme.yml.j2", context
        )

        assert "Template Test" in config_content
        assert "https://docs.example.com" in config_content
        assert "blue" in config_content

        # Validate YAML syntax (tolerating Material's python tags)
        from d361.mkdocs.exporters.config_generator import load_mkdocs_yaml

        parsed_config = load_mkdocs_yaml(config_content)
        assert parsed_config["site_name"] == "Template Test"

    def test_validate_final_config(self, config_generator: ConfigGenerator):
        """Test final configuration validation."""
        valid_config = """
site_name: Test Site
theme:
  name: material
nav:
  - Home: index.md
plugins:
  - search
"""

        results = config_generator.validate_final_config(valid_config)

        assert results["valid"] is True
        assert len(results["errors"]) == 0

    def test_validate_invalid_config(self, config_generator: ConfigGenerator):
        """Test validation of invalid configuration."""
        invalid_config = """
# Missing site_name
theme:
  name: material
plugins:
  - invalid_plugin_syntax: [malformed
"""

        results = config_generator.validate_final_config(invalid_config)

        assert results["valid"] is False
        assert len(results["errors"]) > 0

    @pytest.mark.asyncio
    async def test_template_validation_missing_template(
        self, config_generator: ConfigGenerator
    ):
        """Test validation of missing template."""
        with pytest.raises(Document360Error) as exc_info:
            await config_generator.generate_config_from_template(
                "nonexistent_template.j2", {"site_name": "Test"}
            )

        assert "not found" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_template_validation_missing_context(
        self, config_generator: ConfigGenerator
    ):
        """Test validation of missing context variables."""
        with pytest.raises(Document360Error) as exc_info:
            await config_generator.generate_config_from_template(
                "material_theme.yml.j2",
                {},  # Missing required site_name
            )

        assert "Missing required context variables" in str(exc_info.value)


class TestContentEnhancer:
    """Test content enhancement functionality."""

    @pytest.mark.asyncio
    async def test_enhance_article_basic(
        self, content_enhancer: ContentEnhancer, sample_article: Article
    ):
        """Test basic article enhancement."""
        enhanced = await content_enhancer.enhance_article(sample_article)

        assert "frontmatter" in enhanced
        assert "content" in enhanced
        assert "quality_metrics" in enhanced
        assert "navigation_hints" in enhanced

        # Check frontmatter
        frontmatter = enhanced["frontmatter"]
        assert frontmatter["title"] == sample_article.title
        assert "description" in frontmatter

        # Check quality metrics
        metrics = enhanced["quality_metrics"]
        assert "word_count" in metrics
        assert "overall_score" in metrics
        assert "quality_level" in metrics

    @pytest.mark.asyncio
    async def test_content_processing_headings(self, content_enhancer: ContentEnhancer):
        """Test heading normalization."""
        article = Article(
            id="test",
            title="Test Article",
            content="# Main Title\n## Section 1\n### Subsection",
        )

        enhanced = await content_enhancer.enhance_article(article)
        content = enhanced["content"]

        # H1 should be converted to H2 (page title is reserved for H1)
        assert "## Main Title" in content
        assert "## Section 1" in content
        assert "### Subsection" in content

    @pytest.mark.asyncio
    async def test_link_processing(self, content_enhancer: ContentEnhancer):
        """Test link processing and enhancement."""
        article = Article(
            id="test",
            title="Test Article",
            content="[Internal Link](../other-article.html) and [External Link](https://example.com)",
        )

        enhanced = await content_enhancer.enhance_article(article)
        content = enhanced["content"]

        # Internal links should be converted
        assert "../other-article.md" in content
        # External links should have target attributes
        assert 'target="_blank"' in content
        assert 'rel="noopener noreferrer"' in content

    @pytest.mark.asyncio
    async def test_quality_assessment(self, content_enhancer: ContentEnhancer):
        """Test content quality assessment."""
        high_quality_article = Article(
            id="test",
            title="Comprehensive Guide",
            content="""
# Introduction
This is a comprehensive guide with multiple sections.

## Section 1
Content with proper structure and [internal links](../guide.md).

### Subsection
More detailed content here.

```python
def example():
    return "code example"
```

![Image](image.png)

## Conclusion
Summary of the guide.
"""
            * 5,  # Repeat to increase word count
        )

        enhanced = await content_enhancer.enhance_article(high_quality_article)
        metrics = enhanced["quality_metrics"]

        assert metrics["word_count"] > 100
        assert metrics["heading_count"] >= 3
        assert metrics["link_count"] >= 1
        assert metrics["image_count"] >= 1
        assert metrics["code_block_count"] >= 1
        assert metrics["overall_score"] > 50
        assert metrics["quality_level"] in ["good", "excellent"]


class TestAssetManager:
    """Test asset management functionality."""

    @pytest.mark.asyncio
    async def test_process_assets_basic(self, asset_manager: AssetManager):
        """Test basic asset processing returns discovered asset references."""
        content = """
# Test Content

![Test Image](https://example.com/image.png)
![Local Image](../assets/local.jpg)
"""

        # Patch the real download method to avoid any network access
        with patch.object(asset_manager, "_download_asset", return_value=None):
            assets = await asset_manager.process_assets(
                content, {"article_id": "test-article"}
            )

        # process_assets returns the list of discovered asset references
        assert isinstance(assets, list)
        discovered_urls = [asset.original_url for asset in assets]
        assert "https://example.com/image.png" in discovered_urls
        assert "../assets/local.jpg" in discovered_urls

    @pytest.mark.asyncio
    async def test_copy_assets(self, asset_manager: AssetManager, test_data_dir: Path):
        """Test the asset manager provisions its output directories and processes assets."""
        # AssetManager provisions its output directory structure on init
        assert asset_manager.images_dir.exists()
        assert asset_manager.documents_dir.exists()

        # Processing content with a local asset runs offline and returns references
        content = "![Local Image](../assets/local.jpg)"
        with patch.object(asset_manager, "_download_asset", return_value=None):
            assets = await asset_manager.process_assets(content, None)

        assert isinstance(assets, list)


class TestCrossReferenceResolver:
    """Test cross-reference resolution."""

    def test_initialization(
        self,
        cross_reference_resolver: CrossReferenceResolver,
        sample_articles: list[Article],
    ):
        """Test resolver initialization."""
        assert len(cross_reference_resolver.articles) == len(sample_articles)
        assert cross_reference_resolver.base_url == "https://docs.test.com"

    @pytest.mark.asyncio
    async def test_resolve_internal_links(
        self,
        cross_reference_resolver: CrossReferenceResolver,
        sample_articles: list[Article],
    ):
        """Test internal link resolution returns resolved content."""
        content = "See [Test Article 1](test-article-1.html) for details."
        current_article = sample_articles[0]

        result = await cross_reference_resolver.resolve_references(
            content, current_article
        )

        # resolve_references returns a dict; resolved markdown is under 'content'
        resolved_content = result["content"]
        assert isinstance(resolved_content, str)
        assert "test-article-1" in resolved_content


class TestNavigationBuilder:
    """Test navigation structure building."""

    @pytest.mark.asyncio
    async def test_build_navigation_basic(
        self,
        navigation_builder: NavigationBuilder,
        sample_articles: list[Article],
        sample_category: Category,
    ):
        """Test basic navigation building."""
        result = await navigation_builder.build_navigation(
            sample_articles, [sample_category]
        )

        # build_navigation returns an enriched dict; the MkDocs nav list is under 'navigation'
        navigation = result["navigation"]
        assert isinstance(navigation, list)
        assert len(navigation) > 0

        # Should have category structure
        category_item = navigation[0] if navigation else None
        assert category_item is not None

    @pytest.mark.asyncio
    async def test_build_hierarchical_navigation(
        self, navigation_builder: NavigationBuilder
    ):
        """Test hierarchical navigation building."""
        # Create hierarchical categories
        parent_category = Category(
            id="parent", name="Parent Category", slug="parent", parent_id=None, order=1
        )

        child_category = Category(
            id="child", name="Child Category", slug="child", parent_id="parent", order=1
        )

        articles = [
            Article(
                id="article-1",
                title="Article 1",
                slug="article-1",
                content="Content",
                category_id="child",
            )
        ]

        result = await navigation_builder.build_navigation(
            articles, [parent_category, child_category]
        )

        navigation = result["navigation"]
        assert isinstance(navigation, list)
        assert len(navigation) > 0


class TestMkDocsExporter:
    """Test complete MkDocs export functionality."""

    @pytest.mark.asyncio
    async def test_initialization(self, mkdocs_exporter: MkDocsExporter):
        """Test exporter initialization."""
        assert mkdocs_exporter.source == "archive"
        assert mkdocs_exporter.theme == "material"
        assert mkdocs_exporter.enable_plugins is True
        assert mkdocs_exporter.provider is not None

    @pytest.mark.asyncio
    async def test_export_basic_flow(self, mkdocs_exporter: MkDocsExporter):
        """Test basic export flow."""
        # Mock the provider to return test data
        with (
            patch.object(mkdocs_exporter.provider, "get_articles") as mock_articles,
            patch.object(mkdocs_exporter.provider, "get_categories") as mock_categories,
        ):
            mock_articles.return_value = [
                Article(
                    id="test-1",
                    title="Test Article",
                    slug="test-article",
                    content="Test content",
                    category_id="cat-1",
                )
            ]

            mock_categories.return_value = [
                Category(id="cat-1", name="Test Category", slug="test-category")
            ]

            # Run export
            results = await mkdocs_exporter.export()

            # Validate results
            assert results["success"] is True
            assert "output_path" in results
            assert "config_path" in results
            assert "statistics" in results
            assert "validation" in results

            # Check statistics
            stats = results["statistics"]
            assert stats["articles_processed"] >= 0
            assert stats["categories_processed"] >= 0

    @pytest.mark.asyncio
    async def test_export_validation(
        self, mkdocs_exporter: MkDocsExporter, mkdocs_output_dir: Path
    ):
        """Test export validation."""
        # Mock successful export
        with (
            patch.object(mkdocs_exporter, "_load_content") as mock_load,
            patch.object(
                mkdocs_exporter, "_generate_mkdocs_structure"
            ) as mock_structure,
            patch.object(mkdocs_exporter, "_generate_config") as mock_config,
        ):
            mock_load.return_value = ([], [])  # Empty articles and categories
            mock_structure.return_value = None
            mock_config.return_value = mkdocs_output_dir / "mkdocs.yml"

            # Create required files for validation
            (mkdocs_output_dir / "mkdocs.yml").touch()
            (mkdocs_output_dir / "docs").mkdir(exist_ok=True)

            results = await mkdocs_exporter.export()

            assert "validation" in results
            validation = results["validation"]
            assert isinstance(validation, dict)

    @pytest.mark.asyncio
    async def test_export_error_handling(self, mkdocs_output_dir: Path):
        """Test error handling for an invalid archive path (fails fast at init)."""
        # Provider initialization validates the archive path eagerly
        with pytest.raises(ValueError, match="Archive path not found"):
            MkDocsExporter(
                source="archive",
                archive_path=Path("/nonexistent/path.zip"),  # Invalid path
                output_path=mkdocs_output_dir,
            )

    @pytest.mark.asyncio
    async def test_parallel_processing_disabled(self, mkdocs_exporter: MkDocsExporter):
        """Test export with parallel processing disabled."""
        assert mkdocs_exporter.parallel_processing is False

        # Mock content loading
        with (
            patch.object(mkdocs_exporter.provider, "get_articles") as mock_articles,
            patch.object(mkdocs_exporter.provider, "get_categories") as mock_categories,
        ):
            mock_articles.return_value = []
            mock_categories.return_value = []

            results = await mkdocs_exporter.export()

            assert results["success"] is True


class TestIntegrationWorkflow:
    """Test complete integration workflows."""

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_complete_export_workflow(
        self, mock_archive_file: Path, mkdocs_output_dir: Path
    ):
        """Test complete export workflow from archive to MkDocs."""

        # Create exporter
        exporter = MkDocsExporter(
            source="archive",
            archive_path=mock_archive_file,
            output_path=mkdocs_output_dir,
            theme="material",
            parallel_processing=False,
        )

        # Run complete export
        results = await exporter.export()

        # Validate export results
        assert results["success"] is True
        assert Path(results["output_path"]).exists()
        assert Path(results["config_path"]).exists()

        # Check generated files
        docs_dir = Path(results["output_path"]) / "docs"
        assert docs_dir.exists()

        config_path = Path(results["config_path"])
        assert config_path.exists()

        # Validate config content
        config_content = config_path.read_text()
        config = yaml.safe_load(config_content)

        assert config["site_name"] == "Documentation"
        assert config["theme"]["name"] == "material"

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_template_integration(self, mkdocs_output_dir: Path):
        """Test template system integration."""
        generator = ConfigGenerator(theme="material", enable_plugins=True)

        # Test all available templates
        templates = ["mkdocs_base.yml.j2", "material_theme.yml.j2"]

        for template in templates:
            context = {
                "site_name": f"Test Site - {template}",
                "site_url": "https://docs.test.com",
                "navigation": [{"Home": "index.md"}],
            }

            config_content = await generator.generate_config_from_template(
                template, context
            )

            # Validate generated content
            assert config_content is not None
            assert len(config_content) > 0

            # Should be valid YAML (tolerating Material's python tags)
            from d361.mkdocs.exporters.config_generator import load_mkdocs_yaml

            config = load_mkdocs_yaml(config_content)
            assert config["site_name"] == context["site_name"]

    @pytest.mark.integration
    def test_error_propagation(self, mkdocs_output_dir: Path):
        """Test error propagation through the system."""
        generator = ConfigGenerator()

        # Test invalid template
        with pytest.raises(Document360Error):
            asyncio.run(
                generator.generate_config_from_template(
                    "invalid_template.j2", {"site_name": "Test"}
                )
            )

        # Test missing context
        with pytest.raises(Document360Error):
            asyncio.run(
                generator.generate_config_from_template(
                    "material_theme.yml.j2",
                    {},  # Missing required variables
                )
            )
