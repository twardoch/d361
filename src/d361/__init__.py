# this_file: external/int_folders/d361/src/d361/__init__.py
"""
d361 - Document360 Unified Toolkit

A comprehensive Python library for interacting with Document360 documentation platforms.
Built on hexagonal architecture principles with support for API integration, offline
archive processing, web scraping, and plugin-based content conversion.

Key Features:
- Multi-provider data access (API, archives, web scraping)
- Enterprise-grade API client with token rotation and rate limiting
- Plugin-based content conversion system
- Modern CLI with rich terminal output
- Comprehensive testing and observability

Examples:
    >>> from d361 import MockProvider
    >>> provider = MockProvider()
    >>> articles = await provider.list_articles()

    >>> from d361 import PluginManager
    >>> pm = PluginManager()
    >>> converted = pm.convert(content, "html", "markdown")
"""

from importlib.metadata import PackageNotFoundError, version

# Version information
try:
    __version__ = version("d361")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

# Core models and interfaces
# API client
from .api import (
    ApiConfig,
    ApiError,
    ApiMetrics,
    ApiUpdater,
    ApiUpdaterConfig,
    AuthenticationError,
    BulkOperationConfig,
    BulkOperationManager,
    BulkOperationResult,
    ChangeRecord,
    ChangeType,
    ChunkedDownloader,
    ChunkStatus,
    CircuitBreaker,
    CircuitBreakerConfig,
    CircuitBreakerError,
    CircuitBreakerRegistry,
    CircuitMetrics,
    CircuitState,
    ContentFingerprint,
    DataSyncManager,
    DeduplicationStrategy,
    Document360ApiClient,
    Document360Error,
    DownloadChunk,
    DownloadConfig,
    DownloadProgress,
    DownloadState,
    DownloadStatus,
    ErrorHandler,
    GenerationResult,
    MetricPoint,
    MetricsConfig,
    MetricSeries,
    MetricType,
    ModelGenerationConfig,
    ModelGenerator,
    NotFoundError,
    OpenApiConfig,
    OpenApiIntegration,
    OpenApiSpec,
    OperationRequest,
    OperationType,
    RateLimiter,
    RateLimitError,
    ServerError,
    SmartBulkProcessor,
    SyncConfig,
    SyncState,
    SyncStrategy,
    TimeWindow,
    TokenManager,
    TokenStats,
    UpdateEvent,
    UpdateStatus,
    UpdateTrigger,
    circuit_breaker,
    configure_metrics,
    create_updater,
    generate_models_cli,
    get_circuit_breaker,
    get_metrics,
    get_registry,
    run_one_time_update,
)
from .api import (
    ValidationError as ApiValidationError,
)

# Archive processing
from .archive import (
    ArchiveMetadata,
    ArchiveParser,
    ArchiveParserConfig,
    ArchiveSchema,
    CacheConfig,
    CacheEntry,
    CacheStats,
    ParsedArchive,
    SqliteCache,
    create_archive_schema,
    migrate_archive_schema,
)

# Configuration and secrets management
from .config import (
    PROVIDER_REGISTRY,
    AppConfig,
    CacheEvictionPolicy,
    ConfigFileHandler,
    ConfigLoader,
    ConfigValidator,
    Environment,
    EnvironmentLoader,
    EnvironmentSecretsProvider,
    HashiCorpVaultProvider,
    LocalFileSecretsProvider,
    MonitoringConfig,
    SecretMetadata,
    SecretProvider,
    SecretsManager,
    SecretsProvider,
    SecretType,
    SecretValue,
    SecurityConfig,
    create_secrets_provider,
    get_config,
    get_config_loader,
    get_secrets_manager,
    reset_config,
    reset_config_loader,
    reset_secrets_manager,
    set_config,
    set_config_loader,
    set_secrets_manager,
)
from .config import (
    ApiConfig as ConfigApiConfig,
)
from .config import (
    ArchiveConfig as ConfigArchiveConfig,
)
from .config import (
    CacheConfig as ConfigCacheConfig,
)
from .config import (
    LogLevel as ConfigLogLevel,
)
from .config import (
    ScrapingConfig as ConfigScrapingConfig,
)
from .core.interfaces import ConvertedContent, ConverterPlugin, DataProvider
from .core.models import Article, Category, ContentType, ProjectVersion, PublishStatus
from .core.transformers import ModelTransformer

# HTTP client
from .http import HttpResponse, RetryConfig, UnifiedHttpClient, create_http_client

# MkDocs export functionality
from .mkdocs import (
    AnchorReference,
    AssetManager,
    AssetReference,
    ConfigGenerator,
    ContentEnhancer,
    CrossReferenceResolver,
    LinkReference,
    MarkdownProcessor,
    MkDocsExporter,
    NavigationBuilder,
    OptimizationResult,
    ThemeOptimizer,
)

# Plugin system
from .plugins import PluginManager

# Providers
from .providers import ApiProvider, ArchiveProvider, HybridProvider, MockProvider

# Web scraping and content processing
from .scraping import (
    BrowserType,
    ContentBlock,
    ContentDeduplicator,
    ContentExtractor,
    ConversionConfig,
    ConversionResult,
    ConversionStats,
    DeduplicationConfig,
    Document360MarkdownConverter,
    Document360Scraper,
    DuplicateGroup,
    DuplicateStatus,
    ExtractedContent,
    ExtractionConfig,
    ExtractionQuality,
    LinkHandling,
    MarkdownConverter,
    MarkdownStyle,
    ScrapedPage,
    ScrapingConfig,
    ScrapingMode,
    ScrapingSession,
    SimilarityAlgorithm,
    SimilarityScore,
    UserAgent,
)
from .scraping import (
    ContentType as ScrapingContentType,
)

# Utilities and infrastructure
from .utils import (
    LogContext,
    LogFormat,
    LoggingManager,
    LogLevel,
    PerformanceOptimizer,
    ServiceContainer,
    ServiceLifecycle,
    ValidatedBaseModel,
    ValidationHelper,
    async_cache,
    batch_processor,
    get_container,
    get_logger,
    get_logging_manager,
    get_optimizer,
    injectable,
    performance_monitor,
    register_scoped,
    register_singleton,
    register_transient,
    resolve,
    setup_development_logging,
    setup_logging,
    setup_production_logging,
    validate_function_inputs,
)

__all__ = [
    "PROVIDER_REGISTRY",
    "AnchorReference",
    "ApiConfig",
    "ApiError",
    "ApiMetrics",
    # Providers
    "ApiProvider",
    "ApiUpdater",
    "ApiUpdaterConfig",
    "ApiValidationError",
    "AppConfig",
    "ArchiveMetadata",
    # Archive processing
    "ArchiveParser",
    "ArchiveParserConfig",
    "ArchiveProvider",
    "ArchiveSchema",
    # Core models
    "Article",
    "AssetManager",
    "AssetReference",
    "AuthenticationError",
    "BrowserType",
    "BulkOperationConfig",
    "BulkOperationManager",
    "BulkOperationResult",
    "CacheConfig",
    "CacheEntry",
    "CacheEvictionPolicy",
    "CacheStats",
    "Category",
    "ChangeRecord",
    "ChangeType",
    "ChunkStatus",
    "ChunkedDownloader",
    "CircuitBreaker",
    "CircuitBreakerConfig",
    "CircuitBreakerError",
    "CircuitBreakerRegistry",
    "CircuitMetrics",
    "CircuitState",
    "ConfigApiConfig",
    "ConfigArchiveConfig",
    "ConfigCacheConfig",
    "ConfigFileHandler",
    "ConfigGenerator",
    "ConfigLoader",
    "ConfigLogLevel",
    "ConfigScrapingConfig",
    "ConfigValidator",
    "ContentBlock",
    "ContentDeduplicator",
    "ContentEnhancer",
    "ContentExtractor",
    "ContentFingerprint",
    "ContentType",
    "ConversionConfig",
    "ConversionResult",
    "ConversionStats",
    "ConvertedContent",
    "ConverterPlugin",
    "CrossReferenceResolver",
    # Core interfaces
    "DataProvider",
    "DataSyncManager",
    "DeduplicationConfig",
    "DeduplicationStrategy",
    # API client
    "Document360ApiClient",
    "Document360Error",
    "Document360MarkdownConverter",
    # Web scraping and content processing
    "Document360Scraper",
    "DownloadChunk",
    "DownloadConfig",
    "DownloadProgress",
    "DownloadState",
    "DownloadStatus",
    "DuplicateGroup",
    "DuplicateStatus",
    # Configuration and secrets management
    "Environment",
    "EnvironmentLoader",
    "EnvironmentSecretsProvider",
    "ErrorHandler",
    "ExtractedContent",
    "ExtractionConfig",
    "ExtractionQuality",
    "GenerationResult",
    "HashiCorpVaultProvider",
    "HttpResponse",
    "HybridProvider",
    "LinkHandling",
    "LinkReference",
    "LocalFileSecretsProvider",
    "LogContext",
    "LogFormat",
    "LogLevel",
    # Logging and utilities
    "LoggingManager",
    "MarkdownConverter",
    "MarkdownProcessor",
    "MarkdownStyle",
    "MetricPoint",
    "MetricSeries",
    "MetricType",
    "MetricsConfig",
    # MkDocs export functionality
    "MkDocsExporter",
    "MockProvider",
    "ModelGenerationConfig",
    "ModelGenerator",
    # Transformers
    "ModelTransformer",
    "MonitoringConfig",
    "NavigationBuilder",
    "NotFoundError",
    "OpenApiConfig",
    "OpenApiIntegration",
    "OpenApiSpec",
    "OperationRequest",
    "OperationType",
    "OptimizationResult",
    "ParsedArchive",
    # Performance optimization
    "PerformanceOptimizer",
    # Plugin system
    "PluginManager",
    "ProjectVersion",
    "PublishStatus",
    "RateLimitError",
    "RateLimiter",
    "RetryConfig",
    "ScrapedPage",
    "ScrapingConfig",
    "ScrapingContentType",
    "ScrapingMode",
    "ScrapingSession",
    "SecretMetadata",
    "SecretProvider",
    "SecretType",
    "SecretValue",
    "SecretsManager",
    "SecretsProvider",
    "SecurityConfig",
    "ServerError",
    "ServiceContainer",
    # Dependency injection
    "ServiceLifecycle",
    "SimilarityAlgorithm",
    "SimilarityScore",
    "SmartBulkProcessor",
    "SqliteCache",
    "SyncConfig",
    "SyncState",
    "SyncStrategy",
    "ThemeOptimizer",
    "TimeWindow",
    "TokenManager",
    "TokenStats",
    # HTTP client
    "UnifiedHttpClient",
    "UpdateEvent",
    "UpdateStatus",
    "UpdateTrigger",
    "UserAgent",
    "ValidatedBaseModel",
    # Validation and migration
    "ValidationHelper",
    # Version
    "__version__",
    "async_cache",
    "batch_processor",
    "circuit_breaker",
    "configure_metrics",
    "create_archive_schema",
    "create_http_client",
    "create_secrets_provider",
    "create_updater",
    "generate_models_cli",
    "get_circuit_breaker",
    "get_config",
    "get_config_loader",
    "get_container",
    "get_logger",
    "get_logging_manager",
    "get_metrics",
    "get_optimizer",
    "get_registry",
    "get_secrets_manager",
    "injectable",
    "migrate_archive_schema",
    "performance_monitor",
    "register_scoped",
    "register_singleton",
    "register_transient",
    "reset_config",
    "reset_config_loader",
    "reset_secrets_manager",
    "resolve",
    "run_one_time_update",
    "set_config",
    "set_config_loader",
    "set_secrets_manager",
    "setup_development_logging",
    "setup_logging",
    "setup_production_logging",
    "validate_function_inputs",
]
