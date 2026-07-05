# this_file: external/int_folders/d361/src/d361/config/__init__.py
"""
Configuration and secrets management package.

This package provides comprehensive configuration management with support for
multiple environments, secrets management, and security hardening for the d361 system.
"""

from .environment import (
    ConfigFileHandler,
    # Environment Loading
    EnvironmentLoader,
)
from .loader import (
    # Configuration Loading
    ConfigLoader,
    ConfigValidator,
    # Global Functions
    get_config_loader,
    reset_config_loader,
    set_config_loader,
)
from .schema import (
    ApiConfig,
    # Configuration Models
    AppConfig,
    ArchiveConfig,
    CacheConfig,
    CacheEvictionPolicy,
    # Enums
    Environment,
    LogLevel,
    MonitoringConfig,
    ScrapingConfig,
    SecretProvider,
    SecurityConfig,
    # Global Configuration Functions
    get_config,
    reset_config,
    set_config,
)
from .secrets import (
    # Provider Registry
    PROVIDER_REGISTRY,
    # Concrete Providers
    EnvironmentSecretsProvider,
    HashiCorpVaultProvider,
    LocalFileSecretsProvider,
    SecretMetadata,
    # Provider Base Class
    SecretsProvider,
    # Secret Types and Models
    SecretType,
    SecretValue,
    create_secrets_provider,
)
from .secrets_manager import (
    # Secrets Management
    SecretsManager,
    # Global Functions
    get_secrets_manager,
    reset_secrets_manager,
    set_secrets_manager,
)

# Public API
__all__ = [
    "PROVIDER_REGISTRY",
    "ApiConfig",
    # Configuration Models
    "AppConfig",
    "ArchiveConfig",
    "CacheConfig",
    "CacheEvictionPolicy",
    "ConfigFileHandler",
    # Configuration Loading & Validation
    "ConfigLoader",
    "ConfigValidator",
    # Enums
    "Environment",
    # Environment Loading
    "EnvironmentLoader",
    "EnvironmentSecretsProvider",
    "HashiCorpVaultProvider",
    "LocalFileSecretsProvider",
    "LogLevel",
    "MonitoringConfig",
    "ScrapingConfig",
    # Secrets Management
    "SecretMetadata",
    "SecretProvider",
    "SecretType",
    "SecretValue",
    "SecretsManager",
    "SecretsProvider",
    "SecurityConfig",
    "create_secrets_provider",
    # Global Functions
    "get_config",
    "get_config_loader",
    "get_secrets_manager",
    "reset_config",
    "reset_config_loader",
    "reset_secrets_manager",
    "set_config",
    "set_config_loader",
    "set_secrets_manager",
]
