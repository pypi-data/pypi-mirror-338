"""
Core functionality for gandula.

Provides configuration and logging capabilities.
"""

from .config import configure, get_config_value, get_data_dir, get_temp_dir
from .logging import configure_logging, get_logger

__all__ = [
    'configure',
    'get_config_value',
    'get_data_dir',
    'get_temp_dir',
    'configure_logging',
    'get_logger',
]
