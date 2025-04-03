# Copyright (c) 2023-2024 Datalayer, Inc.
#
# BSD 3-Clause License

from pathlib import Path

import pyjson5 as json5

from typing import TypedDict, Optional, Any


class LLMConfig(TypedDict):
    """Type definition for LLM configuration."""
    model_provider: str
    model: Optional[str]
    temperature: Optional[float]
    system_prompt: Optional[str]


class ConfigError(Exception):
    """Base exception for configuration related errors."""
    pass


class ConfigFileNotFoundError(ConfigError):
    """Raised when the configuration file cannot be found."""
    pass


class ConfigValidationError(ConfigError):
    """Raised when the configuration fails validation."""
    pass


def load_config(config_path: str):
    """Load and validate configuration from JSON5 file."""
    config_file = Path(config_path)
    if not config_file.exists():
        raise ConfigFileNotFoundError(f"Config file {config_path} not found")
    with open(config_file, 'r', encoding='utf-8') as f:
        config: dict[str, Any] = json5.load(f)
    return config
