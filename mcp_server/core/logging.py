"""Logging configuration for MCP Server."""

import logging
import sys
from typing import Optional
from mcp_server.config.settings import settings


def setup_logging(
    level: Optional[str] = None,
    format_string: Optional[str] = None
) -> logging.Logger:
    """
    Setup structured logging for the application.
    
    Args:
        level: Logging level (defaults to settings.log_level)
        format_string: Log format (defaults to settings.log_format)
    
    Returns:
        Configured logger instance
    """
    log_level = level or settings.log_level
    log_format = format_string or settings.log_format
    
    # Configure root logger
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Create application logger
    logger = logging.getLogger("mcp_server")
    logger.setLevel(getattr(logging, log_level.upper()))
    
    return logger


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger instance for a specific module.
    
    Args:
        name: Logger name (usually __name__)
    
    Returns:
        Logger instance
    """
    return logging.getLogger(f"mcp_server.{name}")


# Global logger instance
logger = setup_logging()
