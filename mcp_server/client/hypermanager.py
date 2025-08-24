"""HyperManager API client with error handling and logging."""

from typing import Any, Optional
from mcp_server.generated_client.hypermanager_ia_gemini_integration_client import Client
from mcp_server.config.settings import settings
from mcp_server.core.exceptions import HyperManagerAPIError
from mcp_server.core.logging import get_logger

logger = get_logger(__name__)


class HyperManagerClient:
    """Enhanced HyperManager API client with error handling."""
    
    def __init__(self):
        """Initialize the HyperManager client."""
        self._client = Client(
            base_url=settings.base_url,
            headers={"x-api-key": settings.google_api_key}
        )
        logger.info(f"HyperManager client initialized with base URL: {settings.base_url}")
    
    @property
    def client(self) -> Client:
        """Get the underlying client instance."""
        return self._client
    
    def execute_with_error_handling(self, operation_name: str, operation_func, *args, **kwargs) -> Any:
        """
        Execute an API operation with standardized error handling.
        
        Args:
            operation_name: Name of the operation for logging
            operation_func: Function to execute
            *args: Positional arguments for the function
            **kwargs: Keyword arguments for the function
            
        Returns:
            Result of the operation
            
        Raises:
            HyperManagerAPIError: If the API call fails
        """
        try:
            logger.debug(f"Executing {operation_name} with args: {args}, kwargs: {kwargs}")
            result = operation_func(*args, **kwargs)
            logger.debug(f"{operation_name} completed successfully")
            return result
        except Exception as e:
            error_msg = f"Failed to execute {operation_name}: {str(e)}"
            logger.error(error_msg)
            raise HyperManagerAPIError(error_msg) from e


# Global client instance
hypermanager_client = HyperManagerClient()
