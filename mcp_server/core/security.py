"""Security utilities for MCP Server."""

from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader
from mcp_server.config.settings import settings
from mcp_server.core.exceptions import AuthenticationError
from mcp_server.core.logging import get_logger

logger = get_logger(__name__)

# API Key header security
api_key_header = APIKeyHeader(name=settings.api_key_header_name, auto_error=True)


async def verify_api_key(api_key: str = Security(api_key_header)) -> str:
    """
    Verify the provided API key against the configured key.
    
    Args:
        api_key: API key from request header
        
    Returns:
        The validated API key
        
    Raises:
        HTTPException: If API key is invalid
    """
    if api_key != settings.api_key:
        logger.warning(f"Invalid API key attempt: {api_key[:8]}...")
        raise HTTPException(
            status_code=403,
            detail="Could not validate credentials"
        )
    
    logger.debug("API key validated successfully")
    return api_key


def create_auth_dependency():
    """
    Create an authentication dependency for FastAPI routes.
    
    Returns:
        FastAPI dependency function
    """
    return Security(verify_api_key)
