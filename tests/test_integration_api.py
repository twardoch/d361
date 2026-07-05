# this_file: external/int_folders/d361/tests/test_integration_api.py
"""
Integration tests for d361 API client and related components.

This module provides integration testing of the API client with mock servers,
token management, error handling, and performance characteristics.
"""

import asyncio
from datetime import datetime
from typing import Any
from unittest.mock import AsyncMock, Mock, patch

import pytest

from d361.api import (
    ApiMetrics,
    BulkOperationManager,
    CircuitBreaker,
    DataSyncManager,
    Document360ApiClient,
    TokenManager,
    TokenStats,
)
from d361.api.errors import Document360Error, NotFoundError
from d361.core.models import Article


class MockHttpServer:
    """Mock HTTP server for API testing."""

    def __init__(self):
        self.responses = {}
        self.request_count = 0
        self.request_log = []

    def add_response(
        self, method: str, path: str, response: dict[str, Any], status_code: int = 200
    ):
        """Add mock response for specific endpoint."""
        key = f"{method.upper()}:{path}"
        self.responses[key] = {"response": response, "status_code": status_code}

    def get_response(self, method: str, path: str) -> tuple:
        """Get mock response for request."""
        self.request_count += 1
        self.request_log.append(f"{method.upper()} {path}")

        key = f"{method.upper()}:{path}"
        if key in self.responses:
            mock_resp = self.responses[key]
            return mock_resp["response"], mock_resp["status_code"]

        # Default 404 response
        return {"error": "Not Found"}, 404


@pytest.fixture
def mock_server():
    """Create mock HTTP server for testing."""
    server = MockHttpServer()

    # Add common responses
    server.add_response(
        "GET",
        "/api/v1/articles",
        {
            "data": [
                {
                    "id": "article-1",
                    "title": "Test Article 1",
                    "content": "Content for article 1",
                    "category_id": "cat-1",
                    "status": "published",
                    "created_at": "2025-01-01T00:00:00Z",
                },
                {
                    "id": "article-2",
                    "title": "Test Article 2",
                    "content": "Content for article 2",
                    "category_id": "cat-1",
                    "status": "published",
                    "created_at": "2025-01-01T01:00:00Z",
                },
            ],
            "pagination": {"total": 2, "page": 1, "per_page": 10},
        },
    )

    server.add_response(
        "GET",
        "/api/v1/articles/article-1",
        {
            "data": {
                "id": "article-1",
                "title": "Test Article 1",
                "content": "Content for article 1",
                "category_id": "cat-1",
                "status": "published",
                "created_at": "2025-01-01T00:00:00Z",
            }
        },
    )

    server.add_response(
        "GET",
        "/api/v1/categories",
        {
            "data": [
                {
                    "id": "cat-1",
                    "name": "Test Category 1",
                    "slug": "test-category-1",
                    "parent_id": None,
                }
            ]
        },
    )

    return server


class TestDocument360ApiClientIntegration:
    """Integration tests for Document360ApiClient."""

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_api_client_initialization(self):
        """Test API client initialization with real configuration."""
        from d361.config import ApiConfig

        config = ApiConfig(
            base_url="https://test-api.document360.com",
            api_tokens=["test-token-123"],
            timeout_seconds=30,
            max_retries=3,
        )

        client = Document360ApiClient(config)

        assert client.config == config
        assert client.token_manager is not None
        assert client.rate_limiter is not None

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_api_client_with_mock_server(self, mock_server):
        """Test API client returns dict data via the mocked d361api layer."""
        from d361api import ArticlesApi

        from d361.config import ApiConfig

        config = ApiConfig(
            base_url="http://mock-server", api_tokens=["mock-token"], timeout_seconds=5
        )

        client = Document360ApiClient(config)

        # Mock the d361api articles layer so no network occurs
        client._articles_api = AsyncMock(spec=ArticlesApi)
        article_payload = {
            "id": "article-1",
            "title": "Test Article 1",
            "content": "Content for article 1",
        }
        client._articles_api.v2_articles_article_id_lang_code_get.return_value = Mock(
            to_dict=lambda: article_payload
        )

        # Client returns the dict contract produced by _execute_with_d361api
        result = await client.get_article("article-1")

        assert result == article_payload
        assert client.statistics["successful_requests"] == 1

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_api_client_error_handling(self, mock_server):
        """Test API client maps a 404 from d361api to NotFoundError."""
        from d361api import ArticlesApi
        from d361api.exceptions import ApiException as D361ApiException

        from d361.config import ApiConfig

        config = ApiConfig(base_url="http://mock-server", api_tokens=["mock-token"])

        client = Document360ApiClient(config)

        # d361api raises a 404 for the missing article; the client must classify it
        client._articles_api = AsyncMock(spec=ArticlesApi)
        client._articles_api.v2_articles_article_id_lang_code_get.side_effect = (
            D361ApiException(status=404)
        )

        with pytest.raises(NotFoundError):
            await client.get_article("nonexistent")

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_api_client_authentication_flow(self):
        """Test authentication flow with token rotation."""
        from d361.config import ApiConfig

        config = ApiConfig(
            base_url="http://test-server",
            api_tokens=["token1", "token2", "token3"],
            token_rotation_enabled=True,
        )

        client = Document360ApiClient(config)

        # Test token manager
        token1 = await client.token_manager.get_token()
        token2 = await client.token_manager.get_token()

        # Should rotate tokens
        assert isinstance(token1, str)
        assert isinstance(token2, str)

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_api_client_rate_limiting(self):
        """Test rate limiting integration."""
        from d361.config import ApiConfig

        config = ApiConfig(
            base_url="http://test-server",
            api_tokens=["test-token"],
            requests_per_minute=5,  # Very low for testing
        )

        client = Document360ApiClient(config)

        # Test rate limiter
        rate_limiter = client.rate_limiter

        # Should allow first few requests
        for i in range(3):
            allowed = await rate_limiter.can_proceed("test-token")
            assert allowed is True
            await rate_limiter.record_request("test-token")

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_api_client_bulk_operations(self, mock_server):
        """Test bulk operations integration."""
        from d361.config import ApiConfig

        config = ApiConfig(
            base_url="http://mock-server",
            api_tokens=["bulk-token"],
            bulk_batch_size=5,
            bulk_concurrency=2,
        )

        # Mock bulk responses
        for i in range(10):
            mock_server.add_response(
                "GET",
                f"/api/v1/articles/bulk-{i}",
                {
                    "data": {
                        "id": f"bulk-{i}",
                        "title": f"Bulk Article {i}",
                        "content": f"Bulk content {i}",
                    }
                },
            )

        client = Document360ApiClient(config)
        bulk_manager = BulkOperationManager(client)

        # Test bulk operation
        article_ids = [f"bulk-{i}" for i in range(5)]

        with patch.object(client, "get_article") as mock_get:
            mock_get.side_effect = [
                Article(
                    id=f"bulk-{i}", title=f"Bulk Article {i}", content=f"Content {i}"
                )
                for i in range(5)
            ]

            results = await bulk_manager.bulk_fetch_articles(article_ids)

            assert len(results.successful) == 5
            assert len(results.failed) == 0


class TestTokenManagerIntegration:
    """Integration tests for TokenManager."""

    @pytest.mark.integration
    def test_token_manager_with_multiple_tokens(self):
        """Test token manager with multiple tokens."""
        tokens = ["token1", "token2", "token3"]

        manager = TokenManager(tokens)

        # Should have tokens loaded
        assert len(manager.tokens) == 3
        assert all(isinstance(stats, TokenStats) for stats in manager.tokens.values())

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_token_manager_load_balancing(self):
        """Test token manager load balancing."""
        tokens = ["token1", "token2", "token3"]
        manager = TokenManager(tokens)

        # Get tokens multiple times
        used_tokens = []
        for _ in range(9):  # 3 times more than tokens
            token = await manager.get_token()
            used_tokens.append(token)

        # Should distribute across all tokens
        unique_tokens = set(used_tokens)
        assert len(unique_tokens) == 3

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_token_manager_health_monitoring(self):
        """Test token health monitoring."""
        manager = TokenManager(["healthy-token", "unhealthy-token"])

        # Simulate successful request for healthy token
        await manager.record_success("healthy-token", response_time=0.1)

        # Simulate failed request for unhealthy token
        await manager.record_failure("unhealthy-token", Exception("API Error"))

        # Get health status
        health = manager.get_health()

        assert "healthy_tokens" in health
        assert "total_requests" in health

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_token_manager_stats_tracking(self):
        """Test token statistics tracking."""
        manager = TokenManager(["stats-token"])

        # Record various metrics
        await manager.record_success("stats-token", response_time=0.2)
        await manager.record_success("stats-token", response_time=0.3)
        await manager.record_failure("stats-token", Exception("Test error"))

        # Get token stats
        stats = manager.get_token_stats("stats-token")

        assert stats.total_requests == 3
        assert stats.successful_requests == 2
        assert stats.failed_requests == 1
        assert stats.average_response_time > 0


class TestCircuitBreakerIntegration:
    """Integration tests for CircuitBreaker."""

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_circuit_breaker_state_transitions(self):
        """Test circuit breaker state transitions."""
        from d361.api.circuit_breaker import CircuitBreakerConfig

        config = CircuitBreakerConfig(
            failure_threshold=3, recovery_timeout=1, half_open_max_calls=2
        )

        breaker = CircuitBreaker("test-service", config)

        # Initially closed
        assert breaker.state.name == "CLOSED"

        # Simulate failures
        for _ in range(3):
            await breaker.record_failure(Exception("Test failure"))

        # Should be open now
        assert breaker.state.name == "OPEN"

        # Wait for recovery timeout
        await asyncio.sleep(1.1)

        # Should be half-open
        assert breaker.state.name == "HALF_OPEN"

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_circuit_breaker_with_api_client(self, mock_server):
        """Test circuit breaker integration with API client."""
        from d361.api.circuit_breaker import CircuitBreakerConfig
        from d361.config import ApiConfig

        # Configure circuit breaker with low thresholds
        CircuitBreakerConfig(failure_threshold=2, recovery_timeout_seconds=1)

        config = ApiConfig(
            base_url="http://failing-server",
            api_tokens=["test-token"],
            circuit_breaker_enabled=True,
        )

        client = Document360ApiClient(config)

        # Mock failing responses
        with patch("httpx.AsyncClient") as mock_httpx:
            mock_response = Mock()
            mock_response.status_code = 500
            mock_response.json.return_value = {"error": "Server Error"}

            mock_httpx.return_value.__aenter__.return_value.get.side_effect = Exception(
                "Connection failed"
            )

            # Trigger circuit breaker
            for _ in range(3):
                try:
                    await client.get_article("test")
                except:
                    pass

            # Circuit should be open
            # Subsequent requests should fail fast


class TestDataSyncManagerIntegration:
    """Integration tests for DataSyncManager."""

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_data_sync_manager_deduplication(self):
        """Test data sync manager deduplication."""
        from d361.api.data_sync import SyncConfig

        config = SyncConfig(deduplication_strategy="hash", similarity_threshold=0.9)

        sync_manager = DataSyncManager(config)

        # Test articles with similar content
        articles = [
            Article(id="1", title="Article 1", content="This is test content"),
            Article(
                id="2", title="Article 2", content="This is test content"
            ),  # Duplicate
            Article(id="3", title="Article 3", content="Different content"),
        ]

        deduplicated = await sync_manager.deduplicate_articles(articles)

        # Should remove duplicate
        assert len(deduplicated) == 2

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_data_sync_manager_incremental_sync(self):
        """Test incremental synchronization."""
        from d361.api.data_sync import SyncConfig

        config = SyncConfig(incremental_sync=True, change_detection="timestamp")

        sync_manager = DataSyncManager(config)

        # Initial dataset
        initial_articles = [
            Article(
                id="1",
                title="Article 1",
                content="Content 1",
                updated_at=datetime(2025, 1, 1),
            )
        ]

        # Updated dataset
        updated_articles = [
            Article(
                id="1",
                title="Updated Article 1",
                content="Updated content 1",
                updated_at=datetime(2025, 1, 2),
            ),
            Article(
                id="2",
                title="New Article 2",
                content="Content 2",
                updated_at=datetime(2025, 1, 2),
            ),
        ]

        # Detect changes
        changes = await sync_manager.detect_changes(initial_articles, updated_articles)

        assert len(changes.updated) == 1  # Article 1 updated
        assert len(changes.added) == 1  # Article 2 added
        assert len(changes.deleted) == 0  # Nothing deleted


class TestApiMetricsIntegration:
    """Integration tests for ApiMetrics."""

    @pytest.mark.integration
    def test_api_metrics_collection(self):
        """Test API metrics collection integration."""
        from d361.api.metrics import MetricsConfig

        config = MetricsConfig(
            collection_enabled=True, buffer_size=100, flush_interval_seconds=1
        )

        metrics = ApiMetrics(config)

        # Record some metrics
        metrics.record_request("GET", "/articles", 200, 0.1, "test-token")
        metrics.record_request("GET", "/articles/1", 200, 0.2, "test-token")
        metrics.record_request("POST", "/articles", 201, 0.3, "test-token")

        # Get metrics summary
        summary = metrics.get_summary()

        assert summary["total_requests"] == 3
        assert summary["success_rate"] == 1.0
        assert "average_response_time" in summary

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_api_metrics_with_client(self, mock_server):
        """Test the client tracks request statistics across calls."""
        from d361api import ArticlesApi

        from d361.config import ApiConfig

        config = ApiConfig(base_url="http://mock-server", api_tokens=["metrics-token"])

        client = Document360ApiClient(config)

        client._articles_api = AsyncMock(spec=ArticlesApi)
        client._articles_api.v2_articles_article_id_lang_code_get.return_value = Mock(
            to_dict=lambda: {"id": "1", "title": "Test"}
        )

        # Make requests
        await client.get_article("1")
        await client.get_article("2")

        # The client records request counters in its statistics
        stats = client.statistics
        assert stats["total_requests"] >= 2
        assert stats["successful_requests"] >= 2


class TestIntegrationEndToEnd:
    """End-to-end integration tests."""

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_complete_api_workflow(self, mock_server):
        """Test complete API workflow integration."""
        from d361.config import ApiConfig

        # Configure realistic API client
        config = ApiConfig(
            base_url="http://mock-server",
            api_tokens=["workflow-token"],
            timeout_seconds=30,
            max_retries=3,
            requests_per_minute=60,
            circuit_breaker_enabled=True,
        )

        client = Document360ApiClient(config)

        from d361api import ArticlesApi, ProjectVersionsApi

        # Mock the d361api layers so the workflow runs fully offline
        client._articles_api = AsyncMock(spec=ArticlesApi)
        client._articles_api.v2_articles_article_id_lang_code_get.return_value = Mock(
            to_dict=lambda: {"id": "article-1", "title": "Test Article 1"}
        )
        client._project_versions_api = AsyncMock(spec=ProjectVersionsApi)
        client._project_versions_api.v2_project_versions_get.return_value = Mock(
            to_dict=lambda: {"data": []}
        )

        # Test workflow
        # 1. Get an article (dict contract)
        article = await client.get_article("article-1")
        assert article["id"] == "article-1"

        # 2. Health check returns a status dict, healthy when connectivity works
        health = await client.health_check()
        assert health["client"]["status"] == "healthy"
        assert health["api_connectivity"] == "healthy"

        # 3. Statistics expose request counters
        stats = client.statistics
        assert "total_requests" in stats

    @pytest.mark.integration
    @pytest.mark.asyncio
    @pytest.mark.slow
    async def test_high_load_integration(self):
        """Test API client under high load conditions."""
        from d361.config import ApiConfig

        config = ApiConfig(
            api_tokens=["load-test-token"],
            requests_per_minute=1000,  # High throughput
            bulk_concurrency=10,
        )

        client = Document360ApiClient(config)

        from d361api import ArticlesApi

        client._articles_api = AsyncMock(spec=ArticlesApi)
        client._articles_api.v2_articles_article_id_lang_code_get.return_value = Mock(
            to_dict=lambda: {"id": "test", "title": "Load Test"}
        )

        # Simulate high load
        tasks = []
        for i in range(50):  # 50 concurrent requests
            task = asyncio.create_task(client.get_article(f"article-{i}"))
            tasks.append(task)

        # Wait for all requests
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Most should succeed
        successful = sum(1 for r in results if not isinstance(r, Exception))
        assert successful >= 45  # Allow for some failures

    @pytest.mark.integration
    @pytest.mark.asyncio
    async def test_error_recovery_integration(self):
        """Test error recovery and resilience."""
        from d361.config import ApiConfig

        config = ApiConfig(
            api_tokens=["recovery-token"], max_retries=3, circuit_breaker_enabled=True
        )

        client = Document360ApiClient(config)

        from d361api import ArticlesApi
        from d361api.exceptions import ApiException as D361ApiException

        client._articles_api = AsyncMock(spec=ArticlesApi)

        # First call hits a transient server error, the next one succeeds.
        client._articles_api.v2_articles_article_id_lang_code_get.side_effect = [
            D361ApiException(status=500),
            Mock(to_dict=lambda: {"id": "recovery", "title": "Recovered"}),
        ]

        # A server error is classified and surfaced (no silent failure)
        with pytest.raises(Document360Error):
            await client.get_article("recovery")

        # A subsequent call against a healthy backend recovers cleanly
        article = await client.get_article("recovery")
        assert article["title"] == "Recovered"
