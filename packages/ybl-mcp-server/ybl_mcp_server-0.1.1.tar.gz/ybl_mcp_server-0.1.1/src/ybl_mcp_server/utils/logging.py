"""Logging utilities for the ybl-mcp server."""

import logging
import sys

from ybl_mcp_server.constants import MCP_SERVER_NAME


def setup_logging(
    name: str = MCP_SERVER_NAME, level: str | None = None
) -> logging.Logger:
    """
    Configure and return a logger with the specified name and level.

    Args:
        name: The logger name
        level: The logging level (overrides config if provided)

    Returns:
        A configured logger instance
    """
    log_level = level or "INFO"
    numeric_level = getattr(logging, log_level.upper(), logging.INFO)

    logger = logging.getLogger(name)
    logger.setLevel(numeric_level)

    # Avoid duplicate handlers
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stderr)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


logger = setup_logging()
