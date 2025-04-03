"""
Configuration settings for gandula. Sets up logging, paths, and validation settings.
"""

import importlib.resources
import os
import sys
from pathlib import Path
from typing import Any

import yaml


def load_yaml_config() -> dict[str, Any]:
    """
    Load configuration from YAML file.

    Returns:
        Configuration dictionary loaded from the YAML file
    """
    try:
        config_text = (
            importlib.resources.files('gandula').joinpath('config.yaml').read_text()
        )
        config = yaml.safe_load(config_text)

        if not config:
            raise ValueError('Config file is empty or failed to load')
    except (yaml.YAMLError, OSError, ModuleNotFoundError, ImportError, ValueError) as e:
        print(f'Error loading configuration from package: {e}', file=sys.stderr)
        raise

    return config


def load_user_config() -> dict[str, Any]:
    """
    Load user configuration from ~/.config/gandula/config.yaml if it exists.

    Returns:
        User configuration dictionary
    """
    explicit_path = os.environ.get('GANDULA_CONFIG')
    if explicit_path:
        config_path = Path(explicit_path)
        if config_path.exists():
            try:
                with config_path.open() as f:
                    return yaml.safe_load(f) or {}
            except (yaml.YAMLError, OSError) as e:
                print(
                    f'Error loading explicit config from {config_path}: {e}',
                    file=sys.stderr,
                )

    # Check standard user config locations
    user_paths = [
        Path.home() / '.config' / 'gandula' / 'config.yaml',
        Path.home() / '.gandula.config.yaml',
    ]

    for path in user_paths:
        if path.exists():
            try:
                with path.open() as f:
                    user_config = yaml.safe_load(f)
                    if user_config:
                        print(f'Loaded user configuration from {path}', file=sys.stderr)
                        return user_config
            except (yaml.YAMLError, OSError) as e:
                print(
                    f'Error loading user configuration from {path}: {e}',
                    file=sys.stderr,
                )
                raise

    return {}


def merge_configs(
    base_config: dict[str, Any], override_config: dict[str, Any]
) -> dict[str, Any]:
    """
    Deep merge two configuration dictionaries.

    Args:
        base_config: Base configuration
        override_config: Configuration that takes precedence

    Returns:
        Merged configuration dictionary
    """
    merged = base_config.copy()

    for section, values in override_config.items():
        if (
            section in merged
            and isinstance(merged[section], dict)
            and isinstance(values, dict)
        ):
            merged[section] = merge_configs(merged[section], values)
        else:
            merged[section] = values

    return merged


def get_config_value(section: str, key: str | None = None, default: Any = None) -> Any:
    """
    Get a configuration value from the loaded configuration.

    Args:
        section: Configuration section
        key: Configuration key
        default: Default value if not found

    Returns:
        Configuration value or default
    """
    if key is None:
        return CONFIG.get(section, default)

    try:
        return CONFIG[section][key]
    except (KeyError, TypeError):
        return default


def configure(config_updates: dict[str, Any]) -> None:
    """
    Updates the configuration at runtime.

    Allows dynamic modification of the configuration after initial setup.

    Args:
        config_updates: A dictionary containing configuration key-value pairs to update.
            The dictionary should follow the structure of the existing configuration,
            with nested updates supported for complex configuration structures.

    Raises:
        ValueError: If the provided configuration updates are invalid or cannot be
            applied.

    Examples:
        Update a specific data directory path:
        ```python
            import gandula.config

            # Change the data directory
            gandula.config.configure({"paths": {"data_dir": "/new/path"}})

            # Update multiple configuration options
            gandula.config.configure({
                "paths": {
                    "data_dir": "/updated/data/path",
                    "output_dir": "/new/output/path"
                },
                "logging": {
                    "level": "DEBUG"
                }
            })
        ```
    """
    global CONFIG

    CONFIG = merge_configs(CONFIG, config_updates)

    if 'logging' in config_updates:
        # to avoid circular imports
        from .logging import configure_logging

        configure_logging()


def get_data_dir() -> Path:
    """
    Get the data directory path.

    Returns:
        Path to the data directory
    """
    paths_config = CONFIG.get('paths', {})
    data_dir = paths_config.get('data_dir', os.path.join(os.getcwd(), 'data'))

    path = Path(data_dir)

    if not path.exists():
        raise FileNotFoundError(f'Data directory does not exist: {path}')

    return path


def get_temp_dir() -> Path:
    """
    Get the temporary directory path.

    Returns:
        Path to the temporary directory
    """
    import tempfile

    paths_config = CONFIG.get('paths', {})
    temp_dir = paths_config.get('temp_dir')

    if temp_dir:
        path = Path(temp_dir)

        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
        return path

    return Path(tempfile.gettempdir())


package_config = load_yaml_config()
user_config = load_user_config()
CONFIG = merge_configs(package_config, user_config)
