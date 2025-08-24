"""Optimized base service class with enhanced functionality."""

from abc import ABC
from typing import Any, Callable, TypeVar, Dict, Optional
from mcp_server.client.optimized_hypermanager import optimized_hypermanager_client
from mcp_server.core.logging import get_logger

T = TypeVar('T')


class OptimizedBaseService(ABC):
    """Optimized base service class with enhanced functionality."""
    
    def __init__(self):
        """Initialize the optimized base service."""
        self.client = optimized_hypermanager_client
        self.logger = get_logger(self.__class__.__name__)
    
    def execute_api_call(self, operation_name: str, operation_func: Callable[..., T], *args, **kwargs) -> T:
        """
        Execute an API call with optimized error handling and caching.
        
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
    
    def get_service_metrics(self) -> Dict[str, Any]:
        """Get service-specific metrics."""
        return {
            'service_name': self.__class__.__name__,
            'client_metrics': self.client.get_metrics()
        }
    
    def clear_cache(self) -> None:
        """Clear the service cache."""
        self.client.clear_cache()
        self.logger.info(f"{self.__class__.__name__} cache cleared")
    
    def health_check(self) -> Dict[str, Any]:
        """Perform a health check for this service."""
        try:
            client_health = self.client.health_check()
            return {
                'service': self.__class__.__name__,
                'status': 'healthy' if client_health['status'] == 'healthy' else 'unhealthy',
                'client_health': client_health
            }
        except Exception as e:
            return {
                'service': self.__class__.__name__,
                'status': 'unhealthy',
                'error': str(e)
            }


class CRUDMixin:
    """Mixin providing generic CRUD operations."""
    
    def _create_resource(self, resource_name: str, create_func: Callable, data: Dict[str, Any]) -> Any:
        """Generic create operation."""
        operation_name = f"create_{resource_name}"
        self.logger.info(f"Creating {resource_name} with data: {data}")
        return self.execute_api_call(operation_name, create_func, **data)
    
    def _get_resource(self, resource_name: str, get_func: Callable, resource_id: str) -> Any:
        """Generic get operation."""
        operation_name = f"get_{resource_name}"
        self.logger.debug(f"Getting {resource_name} with ID: {resource_id}")
        return self.execute_api_call(operation_name, get_func, id=resource_id)
    
    def _update_resource(self, resource_name: str, update_func: Callable, resource_id: str, data: Dict[str, Any]) -> Any:
        """Generic update operation."""
        operation_name = f"update_{resource_name}"
        self.logger.info(f"Updating {resource_name} {resource_id} with data: {data}")
        return self.execute_api_call(operation_name, update_func, id=resource_id, **data)
    
    def _delete_resource(self, resource_name: str, delete_func: Callable, resource_id: str) -> Any:
        """Generic delete operation."""
        operation_name = f"delete_{resource_name}"
        self.logger.info(f"Deleting {resource_name} with ID: {resource_id}")
        return self.execute_api_call(operation_name, delete_func, id=resource_id)
    
    def _list_resources(self, resource_name: str, list_func: Callable, **filters) -> Any:
        """Generic list operation."""
        operation_name = f"list_{resource_name}"
        self.logger.debug(f"Listing {resource_name} with filters: {filters}")
        return self.execute_api_call(operation_name, list_func, **filters)


class ValidationMixin:
    """Mixin providing input validation."""
    
    def _validate_required_fields(self, data: Dict[str, Any], required_fields: list) -> None:
        """Validate that required fields are present."""
        missing_fields = [field for field in required_fields if field not in data or data[field] is None]
        if missing_fields:
            raise ValueError(f"Missing required fields: {missing_fields}")
    
    def _validate_field_types(self, data: Dict[str, Any], field_types: Dict[str, type]) -> None:
        """Validate field types."""
        for field, expected_type in field_types.items():
            if field in data and data[field] is not None:
                if not isinstance(data[field], expected_type):
                    raise TypeError(f"Field '{field}' must be of type {expected_type.__name__}")
    
    def _sanitize_string_fields(self, data: Dict[str, Any], string_fields: list) -> Dict[str, Any]:
        """Sanitize string fields by stripping whitespace."""
        sanitized_data = data.copy()
        for field in string_fields:
            if field in sanitized_data and isinstance(sanitized_data[field], str):
                sanitized_data[field] = sanitized_data[field].strip()
        return sanitized_data


class OptimizedBaseServiceWithMixins(OptimizedBaseService, CRUDMixin, ValidationMixin):
    """Optimized base service with all mixins included."""
    pass
