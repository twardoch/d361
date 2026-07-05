# this_file: external/int_folders/d361/src/d361/api/__init__.py
"""
API package - Document360 API client and related utilities.

This package contains the enterprise-grade Document360 API client with
token management, rate limiting, and advanced features for robust
API interactions.
"""

from .api_updater import (
    ApiUpdater,
    ApiUpdaterConfig,
    UpdateEvent,
    UpdateStatus,
    UpdateTrigger,
    create_updater,
    run_one_time_update,
)
from .bulk_operations import (
    BulkOperationConfig,
    BulkOperationManager,
    BulkOperationResult,
    OperationRequest,
    OperationType,
    SmartBulkProcessor,
)
from .chunked_download import (
    ChunkedDownloader,
    ChunkStatus,
    DownloadChunk,
    DownloadConfig,
    DownloadProgress,
    DownloadState,
    DownloadStatus,
)
from .circuit_breaker import (
    CircuitBreaker,
    CircuitBreakerConfig,
    CircuitBreakerError,
    CircuitBreakerRegistry,
    CircuitMetrics,
    CircuitState,
    circuit_breaker,
    get_circuit_breaker,
    get_registry,
)
from .client import ApiConfig, Document360ApiClient
from .data_sync import (
    ChangeRecord,
    ChangeType,
    ContentFingerprint,
    DataSyncManager,
    DeduplicationStrategy,
    SyncConfig,
    SyncState,
    SyncStrategy,
)
from .errors import (
    ApiError,
    AuthenticationError,
    Document360Error,
    ErrorHandler,
    NotFoundError,
    RateLimitError,
    ServerError,
    ValidationError,
)
from .generate_models import (
    GenerationResult,
    ModelGenerationConfig,
    ModelGenerator,
    generate_models_cli,
)
from .metrics import (
    ApiMetrics,
    MetricPoint,
    MetricsConfig,
    MetricSeries,
    MetricType,
    TimeWindow,
    configure_metrics,
    get_metrics,
)
from .openapi_integration import (
    OpenApiConfig,
    OpenApiIntegration,
    OpenApiSpec,
)
from .token_manager import RateLimiter, TokenManager, TokenStats

__all__ = [
    "ApiConfig",
    "ApiError",
    # Metrics and observability
    "ApiMetrics",
    # API updater
    "ApiUpdater",
    "ApiUpdaterConfig",
    "AuthenticationError",
    "BulkOperationConfig",
    # Bulk operations
    "BulkOperationManager",
    "BulkOperationResult",
    "ChangeRecord",
    "ChangeType",
    "ChunkStatus",
    # Chunked downloads
    "ChunkedDownloader",
    # Circuit breaker
    "CircuitBreaker",
    "CircuitBreakerConfig",
    "CircuitBreakerError",
    "CircuitBreakerRegistry",
    "CircuitMetrics",
    "CircuitState",
    "ContentFingerprint",
    # Data synchronization
    "DataSyncManager",
    "DeduplicationStrategy",
    # Main API client
    "Document360ApiClient",
    # Error handling
    "Document360Error",
    "DownloadChunk",
    "DownloadConfig",
    "DownloadProgress",
    "DownloadState",
    "DownloadStatus",
    "ErrorHandler",
    "GenerationResult",
    "MetricPoint",
    "MetricSeries",
    "MetricType",
    "MetricsConfig",
    "ModelGenerationConfig",
    # Model generation
    "ModelGenerator",
    "NotFoundError",
    "OpenApiConfig",
    # OpenAPI integration
    "OpenApiIntegration",
    "OpenApiSpec",
    "OperationRequest",
    "OperationType",
    "RateLimitError",
    "RateLimiter",
    "ServerError",
    "SmartBulkProcessor",
    "SyncConfig",
    "SyncState",
    "SyncStrategy",
    "TimeWindow",
    # Token management
    "TokenManager",
    "TokenStats",
    "UpdateEvent",
    "UpdateStatus",
    "UpdateTrigger",
    "ValidationError",
    "circuit_breaker",
    "configure_metrics",
    "create_updater",
    "generate_models_cli",
    "get_circuit_breaker",
    "get_metrics",
    "get_registry",
    "run_one_time_update",
]
