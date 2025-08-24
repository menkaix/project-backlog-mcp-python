"""Optimized HyperManager API client with advanced features."""

import asyncio
import time
from typing import Any, Optional, Dict, Callable
from functools import wraps
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import requests
from mcp_server.generated_client.hypermanager_ia_gemini_integration_client import Client
from mcp_server.config.settings import settings
from mcp_server.core.exceptions import HyperManagerAPIError
from mcp_server.core.logging import get_logger

logger = get_logger(__name__)


class CircuitBreaker:
    """Circuit breaker pattern implementation."""
    
    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = 'CLOSED'  # CLOSED, OPEN, HALF_OPEN
    
    def call(self, func: Callable, *args, **kwargs):
        """Execute function with circuit breaker protection."""
        if self.state == 'OPEN':
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = 'HALF_OPEN'
            else:
                raise HyperManagerAPIError("Circuit breaker is OPEN")
        
        try:
            result = func(*args, **kwargs)
            if self.state == 'HALF_OPEN':
                self.state = 'CLOSED'
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()
            
            if self.failure_count >= self.failure_threshold:
                self.state = 'OPEN'
            
            raise e


class APICache:
    """Simple in-memory cache for API responses."""
    
    def __init__(self, default_ttl: int = 300):  # 5 minutes default
        self.cache: Dict[str, Dict] = {}
        self.default_ttl = default_ttl
    
    def get(self, key: str) -> Optional[Any]:
        """Get cached value if not expired."""
        if key in self.cache:
            entry = self.cache[key]
            if time.time() < entry['expires']:
                logger.debug(f"Cache hit for key: {key}")
                return entry['value']
            else:
                del self.cache[key]
                logger.debug(f"Cache expired for key: {key}")
        return None
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """Set cached value with TTL."""
        ttl = ttl or self.default_ttl
        self.cache[key] = {
            'value': value,
            'expires': time.time() + ttl
        }
        logger.debug(f"Cached value for key: {key}, TTL: {ttl}s")
    
    def clear(self) -> None:
        """Clear all cached values."""
        self.cache.clear()
        logger.debug("Cache cleared")


def retry_on_failure(max_retries: int = 3, backoff_factor: float = 0.3):
    """Decorator for automatic retry on API failures."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_retries:
                        wait_time = backoff_factor * (2 ** attempt)
                        logger.warning(f"Attempt {attempt + 1} failed, retrying in {wait_time}s: {str(e)}")
                        time.sleep(wait_time)
                    else:
                        logger.error(f"All {max_retries + 1} attempts failed")
            raise last_exception
        return wrapper
    return decorator


class OptimizedHyperManagerClient:
    """Optimized HyperManager API client with advanced features."""
    
    def __init__(self):
        """Initialize the optimized client."""
        self._client = self._create_optimized_client()
        self.cache = APICache()
        self.circuit_breaker = CircuitBreaker()
        self.metrics = {
            'total_calls': 0,
            'successful_calls': 0,
            'failed_calls': 0,
            'cache_hits': 0,
            'average_response_time': 0.0
        }
        logger.info(f"Optimized HyperManager client initialized with base URL: {settings.base_url}")
    
    def _create_optimized_client(self) -> Client:
        """Create client with optimized HTTP session."""
        # Create a session with connection pooling and retry strategy
        session = requests.Session()
        
        # Configure retry strategy
        retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS", "POST", "PUT", "PATCH", "DELETE"],
            backoff_factor=0.3
        )
        
        # Configure HTTP adapter with connection pooling
        adapter = HTTPAdapter(
            max_retries=retry_strategy,
            pool_connections=10,
            pool_maxsize=20
        )
        
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        # Set default headers
        session.headers.update({
            "x-api-key": settings.google_api_key,
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Accept-Encoding": "gzip, deflate"
        })
        
        # Create client with optimized session
        client = Client(
            base_url=settings.base_url,
            headers={"x-api-key": settings.google_api_key}
        )
        
        return client
    
    @property
    def client(self) -> Client:
        """Get the underlying client instance."""
        return self._client
    
    def _generate_cache_key(self, operation_name: str, *args, **kwargs) -> str:
        """Generate cache key for operation."""
        # Create a simple cache key from operation name and parameters
        key_parts = [operation_name]
        key_parts.extend(str(arg) for arg in args)
        key_parts.extend(f"{k}={v}" for k, v in sorted(kwargs.items()))
        return "|".join(key_parts)
    
    def _is_cacheable_operation(self, operation_name: str) -> bool:
        """Check if operation results should be cached."""
        # Cache read operations but not write operations
        cacheable_operations = {
            'list_projects', 'get_project', 'get_projects_tree',
            'list_diagrams', 'get_diagram', 'get_diagram_definition',
            'get_feature_types', 'get_story_tree', 'get_story',
            'get_feature', 'get_actor', 'get_story_features',
            'get_feature_children', 'get_actor_stories'
        }
        return operation_name in cacheable_operations
    
    @retry_on_failure(max_retries=3)
    def execute_with_error_handling(self, operation_name: str, operation_func, *args, **kwargs) -> Any:
        """
        Execute an API operation with advanced error handling and optimizations.
        
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
        start_time = time.time()
        self.metrics['total_calls'] += 1
        
        try:
            # Check cache for read operations
            if self._is_cacheable_operation(operation_name):
                cache_key = self._generate_cache_key(operation_name, *args, **kwargs)
                cached_result = self.cache.get(cache_key)
                if cached_result is not None:
                    self.metrics['cache_hits'] += 1
                    return cached_result
            
            # Execute with circuit breaker protection
            logger.debug(f"Executing {operation_name} with args: {args}, kwargs: {kwargs}")
            
            def api_call():
                return operation_func(*args, **kwargs)
            
            result = self.circuit_breaker.call(api_call)
            
            # Cache the result if it's a cacheable operation
            if self._is_cacheable_operation(operation_name):
                cache_key = self._generate_cache_key(operation_name, *args, **kwargs)
                # Cache for different durations based on operation type
                ttl = 300 if 'list' in operation_name else 60  # 5min for lists, 1min for single items
                self.cache.set(cache_key, result, ttl)
            
            # Update metrics
            response_time = time.time() - start_time
            self.metrics['successful_calls'] += 1
            self._update_average_response_time(response_time)
            
            logger.debug(f"{operation_name} completed successfully in {response_time:.3f}s")
            return result
            
        except Exception as e:
            self.metrics['failed_calls'] += 1
            error_msg = f"Failed to execute {operation_name}: {str(e)}"
            logger.error(error_msg)
            raise HyperManagerAPIError(error_msg) from e
    
    def _update_average_response_time(self, response_time: float) -> None:
        """Update average response time metric."""
        total_successful = self.metrics['successful_calls']
        current_avg = self.metrics['average_response_time']
        
        # Calculate new average
        new_avg = ((current_avg * (total_successful - 1)) + response_time) / total_successful
        self.metrics['average_response_time'] = new_avg
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get client performance metrics."""
        success_rate = (
            (self.metrics['successful_calls'] / self.metrics['total_calls'] * 100)
            if self.metrics['total_calls'] > 0 else 0
        )
        
        cache_hit_rate = (
            (self.metrics['cache_hits'] / self.metrics['total_calls'] * 100)
            if self.metrics['total_calls'] > 0 else 0
        )
        
        return {
            **self.metrics,
            'success_rate_percent': round(success_rate, 2),
            'cache_hit_rate_percent': round(cache_hit_rate, 2),
            'circuit_breaker_state': self.circuit_breaker.state
        }
    
    def clear_cache(self) -> None:
        """Clear the API cache."""
        self.cache.clear()
        logger.info("API cache cleared")
    
    def health_check(self) -> Dict[str, Any]:
        """Perform a health check of the API."""
        try:
            # Try a simple API call to check connectivity
            from mcp_server.generated_client.hypermanager_ia_gemini_integration_client.api.default import get_list_projects
            
            start_time = time.time()
            result = get_list_projects.sync(client=self.client)
            response_time = time.time() - start_time
            
            return {
                'status': 'healthy',
                'response_time_ms': round(response_time * 1000, 2),
                'circuit_breaker_state': self.circuit_breaker.state,
                'timestamp': time.time()
            }
        except Exception as e:
            return {
                'status': 'unhealthy',
                'error': str(e),
                'circuit_breaker_state': self.circuit_breaker.state,
                'timestamp': time.time()
            }


# Global optimized client instance
optimized_hypermanager_client = OptimizedHyperManagerClient()
