# this_file: external/int_folders/d361/src/d361/providers/mock_provider.py
"""
Mock provider for testing and development.

This module provides a mock implementation of the DataProvider protocol
for use in testing, development, and demonstration scenarios.
"""

from __future__ import annotations

import asyncio
import random
from collections.abc import AsyncIterator
from datetime import datetime, timezone
from typing import Any

from ..api.errors import Document360Error, ErrorCategory, ErrorSeverity
from ..core.models import Article, Category, ProjectVersion, PublishStatus


class MockProvider:
    """Mock provider for testing and development.

    This provider implements the DataProvider protocol with predictable,
    configurable mock data for testing and development purposes.

    Article IDs are strings of the form ``"mock-article-{n}"`` and category
    IDs are ``"mock-category-{n}"`` (1-indexed).
    """

    def __init__(
        self,
        simulate_delays: bool = False,
        delay_ms: int = 100,
        fail_probability: float = 0.0,
        num_articles: int = 10,
        num_categories: int = 5,
        include_content: bool = True,
        seed: int | None = None,
        **kwargs: Any,
    ) -> None:
        """Initialize the mock provider.

        Args:
            simulate_delays: Whether to simulate network delays
            delay_ms: Delay in milliseconds for simulated operations
            fail_probability: Probability of operations failing (0.0-1.0)
            num_articles: Number of mock articles to generate
            num_categories: Number of mock categories to generate
            include_content: Whether generated articles include body content
            seed: Random seed for reproducible data generation
            **kwargs: Additional configuration options
        """
        self.simulate_delays = simulate_delays
        self.delay_ms = delay_ms
        self.fail_probability = fail_probability
        self.num_articles = num_articles
        self.num_categories = num_categories
        self.include_content = include_content
        self.seed = seed

        if seed is not None:
            random.seed(seed)

        # Generate mock data
        self._mock_articles = self._generate_mock_articles()
        self._mock_categories = self._generate_mock_categories()
        self._mock_project = self._generate_mock_project()

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _article_id(self, n: int) -> str:
        return f"mock-article-{n}"

    def _category_id(self, n: int) -> str:
        return f"mock-category-{n}"

    def _make_article(self, n: int) -> Article:
        """Create a single mock article with 1-based index *n*."""
        now = datetime.now(timezone.utc)
        content = (
            f"<h1>Mock Article {n}</h1><p>Content for mock article {n}.</p>"
            if self.include_content
            else ""
        )
        content_markdown = (
            f"# Mock Article {n}\n\nContent for mock article {n}."
            if self.include_content
            else ""
        )
        cat_idx = (n - 1) % max(1, self.num_categories) + 1
        return Article(
            id=self._article_id(n),
            title=f"Mock Article {n}",
            slug=f"mock-article-{n}",
            content=content,
            content_markdown=content_markdown,
            excerpt=f"Excerpt for mock article {n}",
            category_id=self._category_id(cat_idx),
            status=PublishStatus.PUBLISHED,
            created_at=now,
            updated_at=now,
            author_name=f"Author {n}",
            author_email=f"author{n}@example.com",
            tags=[f"tag-{n}"],
        )

    def _make_category(self, n: int) -> Category:
        """Create a single mock category with 1-based index *n*."""
        now = datetime.now(timezone.utc)
        return Category(
            id=self._category_id(n),
            name=f"Mock Category {n}",
            slug=f"mock-category-{n}",
            parent_id=None,
            order=n,
            level=0,
            path=f"Mock Category {n}",
            description=f"Description for mock category {n}",
            is_public=True,
            status=PublishStatus.PUBLISHED,
            created_at=now,
            updated_at=now,
            article_count=0,
            subcategory_count=0,
        )

    def _generate_mock_articles(self) -> list[Article]:
        """Generate ``self.num_articles`` mock articles."""
        return [self._make_article(i + 1) for i in range(self.num_articles)]

    def _generate_mock_categories(self) -> list[Category]:
        """Generate ``self.num_categories`` mock categories."""
        return [self._make_category(i + 1) for i in range(self.num_categories)]

    def _generate_mock_project(self) -> ProjectVersion:
        """Generate mock project version data."""
        now = datetime.now(timezone.utc)
        return ProjectVersion(
            id="mock-project-1",
            name="Main Documentation",
            version_number="1.0.0",
            is_default=True,
            project_id="mock-project",
            project_name="Mock Documentation Project",
            project_slug="mock-docs",
            created_at=now,
            updated_at=now,
            published_at=now,
            language_code="en",
            timezone="UTC",
            is_public=True,
            site_title="Mock Documentation",
            site_description="Mock documentation site for testing",
            total_articles=self.num_articles,
            total_categories=self.num_categories,
        )

    async def _simulate_operation(self) -> None:
        """Simulate operation delays and failures if configured."""
        if self.simulate_delays:
            await asyncio.sleep(self.delay_ms / 1000)
        if self.fail_probability > 0:
            if random.random() < self.fail_probability:
                raise Document360Error(
                    "Simulated operation failure",
                    category=ErrorCategory.NETWORK,
                    severity=ErrorSeverity.HIGH,
                )

    # ------------------------------------------------------------------
    # DataProvider protocol
    # ------------------------------------------------------------------

    async def get_article(self, article_id: Any, **kwargs: Any) -> Article:
        """Fetch a mock article by ID.

        Args:
            article_id: Article identifier (string ``"mock-article-{n}"``)
            **kwargs: Additional parameters

        Returns:
            Article: Mock article data

        Raises:
            Document360Error: If article not found in mock data
        """
        await self._simulate_operation()
        for article in self._mock_articles:
            if str(article.id) == str(article_id):
                return article
        raise Document360Error(
            f"Article '{article_id}' not found in mock data",
            category=ErrorCategory.NOT_FOUND,
            severity=ErrorSeverity.LOW,
        )

    async def list_articles(
        self,
        category_id: Any = None,
        status: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        **kwargs: Any,
    ) -> list[Article]:
        """List mock articles with optional filtering and pagination.

        Args:
            category_id: Filter by category ID
            status: Filter by status string
            limit: Maximum number of articles to return
            offset: Number of articles to skip
            **kwargs: Additional parameters

        Returns:
            list[Article]: Filtered and paginated mock articles
        """
        await self._simulate_operation()

        articles: list[Article] = list(self._mock_articles)

        if category_id is not None:
            articles = [a for a in articles if str(a.category_id) == str(category_id)]
        if status is not None:
            articles = [a for a in articles if a.status.value == status]

        if offset is not None:
            articles = articles[offset:]
        if limit is not None:
            articles = articles[:limit]

        return articles

    async def stream_articles(self, **kwargs: Any) -> AsyncIterator[Article]:
        """Stream mock articles.

        Args:
            **kwargs: Additional parameters

        Yields:
            Article: Individual mock articles
        """
        await self._simulate_operation()
        for article in self._mock_articles:
            if self.simulate_delays:
                await asyncio.sleep(self.delay_ms / 1000)
            yield article

    async def search_articles(self, query: str, **kwargs: Any) -> list[Article]:
        """Search mock articles by title/content substring.

        Args:
            query: Search query string
            **kwargs: Additional parameters

        Returns:
            list[Article]: Matching articles
        """
        await self._simulate_operation()
        q = query.lower()
        return [
            a
            for a in self._mock_articles
            if q in a.title.lower() or q in (a.content or "").lower()
        ]

    async def get_category(self, category_id: Any, **kwargs: Any) -> Category:
        """Fetch a mock category by ID.

        Args:
            category_id: Category identifier (string ``"mock-category-{n}"``)
            **kwargs: Additional parameters

        Returns:
            Category: Mock category data

        Raises:
            Document360Error: If category not found in mock data
        """
        await self._simulate_operation()
        for category in self._mock_categories:
            if str(category.id) == str(category_id):
                return category
        raise Document360Error(
            f"Category '{category_id}' not found in mock data",
            category=ErrorCategory.NOT_FOUND,
            severity=ErrorSeverity.LOW,
        )

    async def list_categories(self, **kwargs: Any) -> list[Category]:
        """List all mock categories.

        Args:
            **kwargs: Additional parameters

        Returns:
            list[Category]: All mock categories
        """
        await self._simulate_operation()
        return list(self._mock_categories)

    async def list_project_versions(self, **kwargs: Any) -> list[ProjectVersion]:
        """Get list of mock project versions.

        Args:
            **kwargs: Additional parameters

        Returns:
            list[ProjectVersion]: Mock project versions (single default version)
        """
        await self._simulate_operation()
        return [self._mock_project]

    async def get_project_version(self, **kwargs: Any) -> ProjectVersion:
        """Get mock project version.

        Args:
            **kwargs: Additional parameters

        Returns:
            ProjectVersion: Mock project version
        """
        await self._simulate_operation()
        return self._mock_project

    async def get_articles(self, **kwargs: Any) -> list[Article]:
        """Get all articles (MkDocsExporter interface alias).

        Args:
            **kwargs: Additional parameters

        Returns:
            list[Article]: All mock articles
        """
        return await self.list_articles(**kwargs)

    async def get_categories(self, **kwargs: Any) -> list[Category]:
        """Get all categories (MkDocsExporter interface alias).

        Args:
            **kwargs: Additional parameters

        Returns:
            list[Category]: All mock categories
        """
        return await self.list_categories(**kwargs)
