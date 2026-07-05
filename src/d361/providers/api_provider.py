# this_file: external/int_folders/d361/src/d361/providers/api_provider.py
"""
Document360 API provider implementation.

This module provides the primary adapter for interacting with Document360's REST API,
implementing enterprise-grade features like token rotation, rate limiting, and
bulk operations.
"""

from __future__ import annotations

from collections.abc import AsyncIterator
from datetime import datetime
from typing import Any

from loguru import logger

from ..api.client import Document360ApiClient
from ..api.token_manager import TokenManager
from ..core.models import Article, Category, ProjectVersion
from ..http.client import UnifiedHttpClient


class ApiProvider:
    """API provider for Document360 REST API access.

    This provider implements the DataProvider protocol and provides enterprise-grade
    features including:
    - Multi-token rotation for high throughput
    - Intelligent rate limiting (60 calls/min per token)
    - Automatic retries with exponential backoff
    - Bulk operations and streaming support
    - Circuit breaker pattern for resilience
    """

    def __init__(
        self,
        tokens: list[str] | None = None,
        base_url: str = "https://apidocs.document360.com",
        rate_limit: int = 60,
        client: Any = None,
        enable_cache: bool = False,
        **kwargs: Any,
    ) -> None:
        """Initialize the API provider.

        Args:
            tokens: List of API tokens for rotation (optional when *client* provided)
            base_url: Base API URL
            rate_limit: Calls per minute per token
            client: Pre-built API client (e.g. a mock for testing).  When
                supplied *tokens* is ignored and no internal clients are created.
            enable_cache: Enable response caching
            **kwargs: Additional configuration options
        """
        self.enable_cache = enable_cache

        if client is not None:
            # Use provided client directly (e.g. for testing)
            self.client = client
            self.tokens = tokens or []
            self.base_url = base_url.rstrip("/")
            self.rate_limit = rate_limit
            self.token_manager = None
            self.http_client = None
            self.api_client = None
        else:
            if not tokens:
                raise ValueError("Either 'tokens' or 'client' must be provided")
            self.tokens = tokens
            self.base_url = base_url.rstrip("/")
            self.rate_limit = rate_limit
            self.client = None

            # Initialize token manager for intelligent rotation
            self.token_manager = TokenManager(tokens, rate_limit)

            # Initialize HTTP client
            self.http_client = UnifiedHttpClient(
                base_url=base_url,
                timeout=kwargs.get("timeout", 30.0),
                retry_config=kwargs.get("retry_config"),
                **kwargs,
            )

            # Initialize API client with token management
            self.api_client = Document360ApiClient(
                tokens=tokens,
                base_url=base_url,
                rate_limit=rate_limit,
                **kwargs,
            )

            logger.info(
                "Initialized API provider",
                base_url=base_url,
                token_count=len(tokens),
                rate_limit=rate_limit,
            )

    def _dict_to_article(
        self, data: dict | Article, fallback_id: Any = None
    ) -> Article:
        """Convert a raw dict (or pass-through Article) to an Article model."""
        if isinstance(data, Article):
            return data
        from datetime import datetime, timezone

        _now = datetime.now(timezone.utc)
        cat_id = data.get("category_id") or (
            data["category"]["id"]
            if "category" in data and isinstance(data["category"], dict)
            else None
        )
        return Article(
            id=data.get("id", fallback_id),
            title=data.get("title", ""),
            slug=data.get("slug", ""),
            content=data.get("content") or data.get("body", ""),
            content_markdown=data.get("content_markdown", ""),
            excerpt=data.get("excerpt", ""),
            category_id=cat_id,
            order=data.get("order", 0),
            status=data.get("status", "draft"),
            created_at=self._parse_datetime(
                data.get("created_at") or data.get("created_date")
            )
            or _now,
            updated_at=self._parse_datetime(data.get("updated_at")) or _now,
            published_at=self._parse_datetime(data.get("published_at")),
            author_id=data.get("author_id"),
            author_name=data.get("author_name", ""),
            author_email=data.get("author_email", ""),
            meta_title=data.get("meta_title", ""),
            meta_description=data.get("meta_description", ""),
            tags=data.get("tags", []),
            version_id=data.get("version_id"),
            language_code=data.get("language_code", "en"),
            is_public=data.get("is_public", True),
            metadata=data.get("metadata", {}),
            custom_fields=data.get("custom_fields", {}),
        )

    async def get_article(self, article_id: Any, **kwargs: Any) -> Article:
        """Fetch a single article by ID.

        Args:
            article_id: Article identifier
            **kwargs: Additional parameters

        Returns:
            Article: The requested article
        """
        try:
            logger.debug(f"Fetching article {article_id}")
            source = self.client if self.client is not None else self.api_client
            article_data = await source.get_article(article_id, **kwargs)
            article = self._dict_to_article(article_data, fallback_id=article_id)
            logger.debug(f"Successfully fetched article {article_id}: {article.title}")
            return article
        except Exception as e:
            logger.error(f"Failed to fetch article {article_id}: {e}")
            raise

    async def list_articles(
        self,
        category_id: int | None = None,
        status: str | None = None,
        **kwargs: Any,
    ) -> list[Article]:
        """List articles with filtering.

        Args:
            category_id: Filter by category
            status: Filter by status
            **kwargs: Additional parameters

        Returns:
            list[Article]: Filtered articles
        """
        try:
            logger.debug(
                f"Listing articles (category_id={category_id}, status={status})"
            )

            params: dict[str, Any] = {}
            if category_id is not None:
                params["category_id"] = category_id
            if status is not None:
                params["status"] = status
            params.update(kwargs)

            source = self.client if self.client is not None else self.api_client
            articles_data = await source.list_articles(**params)

            articles = [self._dict_to_article(d) for d in articles_data]
            logger.debug(f"Successfully listed {len(articles)} articles")
            return articles

        except Exception as e:
            logger.error(f"Failed to list articles: {e}")
            raise

    async def stream_articles(self, **kwargs: Any) -> AsyncIterator[Article]:
        """Stream all articles efficiently.

        Args:
            **kwargs: Additional parameters

        Yields:
            Article: Individual articles
        """
        try:
            logger.debug("Starting to stream articles")

            # Get paginated results and stream them
            page = 1
            per_page = kwargs.get("per_page", 100)
            total_yielded = 0

            while True:
                # Fetch a page of articles
                page_params = {"page": page, "per_page": per_page}
                page_params.update(kwargs)

                articles = await self.list_articles(**page_params)

                if not articles:
                    break

                # Yield each article
                for article in articles:
                    yield article
                    total_yielded += 1

                # If we got fewer articles than per_page, we're done
                if len(articles) < per_page:
                    break

                page += 1

            logger.debug(f"Successfully streamed {total_yielded} articles")

        except Exception as e:
            logger.error(f"Failed to stream articles: {e}")
            raise

    async def get_category(self, category_id: int, **kwargs: Any) -> Category:
        """Fetch a single category by ID.

        Args:
            category_id: Category identifier
            **kwargs: Additional parameters

        Returns:
            Category: The requested category
        """
        try:
            logger.debug(f"Fetching category {category_id}")

            # Use the Document360ApiClient to fetch category data
            category_data = await self.api_client.get_category(category_id, **kwargs)

            # Convert API response to canonical Category model
            category = Category(
                id=category_data.get("id", category_id),
                name=category_data.get("name", ""),
                slug=category_data.get("slug", ""),
                description=category_data.get("description", ""),
                parent_id=category_data.get("parent_id"),
                order=category_data.get("order", 0),
                is_public=category_data.get("is_public", True),
                created_at=self._parse_datetime(category_data.get("created_at")),
                updated_at=self._parse_datetime(category_data.get("updated_at")),
                icon=category_data.get("icon", ""),
                metadata=category_data.get("metadata", {}),
                custom_fields=category_data.get("custom_fields", {}),
            )

            logger.debug(
                f"Successfully fetched category {category_id}: {category.name}"
            )
            return category

        except Exception as e:
            logger.error(f"Failed to fetch category {category_id}: {e}")
            raise

    async def list_categories(
        self, parent_id: int | None = None, **kwargs: Any
    ) -> list[Category]:
        """List categories with optional parent filtering.

        Args:
            parent_id: Filter by parent category
            **kwargs: Additional parameters

        Returns:
            list[Category]: Filtered categories
        """
        try:
            logger.debug(f"Listing categories (parent_id={parent_id})")

            # Build query parameters
            params = {}
            if parent_id is not None:
                params["parent_id"] = parent_id

            # Merge with additional parameters
            params.update(kwargs)

            # Use the Document360ApiClient to fetch categories
            categories_data = await self.api_client.list_categories(**params)

            # Convert API response to canonical Category models
            categories = []
            for category_data in categories_data:
                category = Category(
                    id=category_data.get("id", 0),
                    name=category_data.get("name", ""),
                    slug=category_data.get("slug", ""),
                    description=category_data.get("description", ""),
                    parent_id=category_data.get("parent_id"),
                    order=category_data.get("order", 0),
                    is_public=category_data.get("is_public", True),
                    created_at=self._parse_datetime(category_data.get("created_at")),
                    updated_at=self._parse_datetime(category_data.get("updated_at")),
                    icon=category_data.get("icon", ""),
                    metadata=category_data.get("metadata", {}),
                    custom_fields=category_data.get("custom_fields", {}),
                )
                categories.append(category)

            logger.debug(f"Successfully listed {len(categories)} categories")
            return categories

        except Exception as e:
            logger.error(f"Failed to list categories: {e}")
            raise

    async def get_project_version(self, **kwargs: Any) -> ProjectVersion:
        """Get project version information.

        Args:
            **kwargs: Additional parameters

        Returns:
            ProjectVersion: Project version details
        """
        try:
            logger.debug("Fetching project version")

            # Use the Document360ApiClient to fetch project version data
            version_data = await self.api_client.get_project_version(**kwargs)

            # Convert API response to canonical ProjectVersion model
            version = ProjectVersion(
                id=version_data.get("id", 0),
                name=version_data.get("name", ""),
                slug=version_data.get("slug", ""),
                description=version_data.get("description", ""),
                is_default=version_data.get("is_default", False),
                is_public=version_data.get("is_public", True),
                created_at=self._parse_datetime(version_data.get("created_at")),
                updated_at=self._parse_datetime(version_data.get("updated_at")),
                project_id=version_data.get("project_id", 0),
                language_code=version_data.get("language_code", "en"),
                metadata=version_data.get("metadata", {}),
                custom_fields=version_data.get("custom_fields", {}),
            )

            logger.debug(f"Successfully fetched project version: {version.name}")
            return version

        except Exception as e:
            logger.error(f"Failed to fetch project version: {e}")
            raise

    def _parse_datetime(self, date_str: str | None) -> datetime | None:
        """Parse datetime string from API response.

        Args:
            date_str: ISO format datetime string

        Returns:
            datetime: Parsed datetime or None if invalid
        """
        if not date_str:
            return None

        try:
            # Handle common ISO formats from Document360 API
            if date_str.endswith("Z"):
                # UTC timezone
                return datetime.fromisoformat(date_str[:-1] + "+00:00")
            elif "+" in date_str or date_str.endswith(("GMT", "UTC")):
                # Has timezone info
                return datetime.fromisoformat(
                    date_str.replace("GMT", "+00:00").replace("UTC", "+00:00")
                )
            else:
                # Assume UTC if no timezone
                return datetime.fromisoformat(date_str).replace(tzinfo=None)

        except (ValueError, TypeError) as e:
            logger.warning(f"Failed to parse datetime '{date_str}': {e}")
            return None

    async def get_statistics(self) -> dict[str, Any]:
        """Get provider statistics and health information.

        Returns:
            dict: Provider statistics
        """
        try:
            token_stats = self.token_manager.get_statistics()

            return {
                "provider_type": "api",
                "base_url": self.base_url,
                "token_count": len(self.tokens),
                "rate_limit": self.rate_limit,
                "token_stats": token_stats,
                "http_client_stats": await self._get_http_stats(),
                "has_content": True,
                "supports_streaming": True,
                "supports_search": True,
            }

        except Exception as e:
            logger.error(f"Failed to get API provider statistics: {e}")
            return {"provider_type": "api", "error": str(e)}

    async def _get_http_stats(self) -> dict[str, Any]:
        """Get HTTP client statistics.

        Returns:
            dict: HTTP client statistics
        """
        try:
            # Get basic stats from HTTP client if available
            return {
                "total_requests": getattr(self.http_client, "total_requests", 0),
                "successful_requests": getattr(
                    self.http_client, "successful_requests", 0
                ),
                "failed_requests": getattr(self.http_client, "failed_requests", 0),
                "average_response_time": getattr(
                    self.http_client, "avg_response_time", 0.0
                ),
            }
        except Exception:
            return {}
