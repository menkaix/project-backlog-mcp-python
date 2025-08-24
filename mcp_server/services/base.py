"""Base service class with common functionality."""

from abc import ABC
from typing import Any, Callable, TypeVar
from mcp_server.client.hypermanager import hypermanager_client
from mcp_server.core.logging import get_logger

T = TypeVar('T')


class BaseService(ABC):
    """Base service class with common functionality."""
    
    def __init__(self):
        """Initialize the base service."""
        self.client = hypermanager_client
        self.logger = get_logger(self.__class__.__name__)
    
    def execute_api_call(self, operation_name: str, operation_func: Callable[..., T], *args, **kwargs) -> T:
        """
        Execute an API call with standardized error handling and logging.
        
        Args:
            operation_name: Name of the operation for logging
            operation_func: API function to execute
            *args: Positional arguments for the function
            **kwargs: Keyword arguments for the function
            
        Returns:
            Result of the API call
        """
        return self.client.execute_with_error_handling(
            operation_name=operation_name,
            operation_func=operation_func,
            *args,
            **kwargs
        )
