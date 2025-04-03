"""
Logging configuration for gandula.

Provides structured logging capabilities with configurable output formats.
"""

import logging
import sys

import structlog

from .config import get_config_value


def configure_logging(level: str = '', render_json: bool | None = None):
    """
    Configure structlog logging system.

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        render_json: Whether to render logs in JSON format
    """
    log_config = get_config_value(section='logging', default={})
    level = level or log_config.get('level', 'INFO')
    render_json = (
        render_json if render_json is not None else log_config.get('render_json', False)
    )
    log_format = log_config.get('format')

    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        print(f'Invalid log level: {level}, using INFO', file=sys.stderr)
        numeric_level = logging.INFO

    logging.basicConfig(
        format=log_format,
        stream=sys.stdout,
        level=numeric_level,
    )

    processors = [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt='iso'),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
    ]

    if render_json:
        processors.append(structlog.processors.JSONRenderer())
    else:
        processors.append(structlog.dev.ConsoleRenderer())

    structlog.configure(
        processors=processors,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )


def get_logger(name: str = '') -> structlog.stdlib.BoundLogger:
    """
    Get a structured logger.

    Args:
        name: Logger name (defaults to module name if empty)

    Returns:
        A configured structlog logger
    """
    if not name:
        import inspect

        frame = inspect.currentframe()
        if frame:
            try:
                frame = frame.f_back
                if frame:
                    name = frame.f_globals.get('__name__', __name__)
            finally:
                del frame

    return structlog.get_logger(name)
