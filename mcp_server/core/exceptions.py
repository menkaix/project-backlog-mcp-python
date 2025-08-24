"""Custom exceptions for MCP Server."""

from typing import Any, Dict, Optional


class MCPServerError(Exception):
    """Base exception for MCP Server errors."""
    
    def __init__(
        self,
        message: str,
        code: int = -32603,
        data: Optional[Dict[str, Any]] = None
    ):
        self.message = message
        self.code = code
        self.data = data or {}
        super().__init__(self.message)


class ValidationError(MCPServerError):
    """Exception raised when parameter validation fails."""
    
    def __init__(self, message: str, missing_params: Optional[list] = None):
        super().__init__(
            message=message,
            code=-32602,
            data={"missing_params": missing_params or []}
        )


class ToolNotFoundError(MCPServerError):
    """Exception raised when a tool is not found."""
    
    def __init__(self, tool_name: str):
        super().__init__(
            message=f"Tool '{tool_name}' not found",
            code=-32601,
            data={"tool_name": tool_name}
        )


class AuthenticationError(MCPServerError):
    """Exception raised when authentication fails."""
    
    def __init__(self, message: str = "Authentication failed"):
        super().__init__(
            message=message,
            code=403,
            data={"type": "authentication_error"}
        )


class HyperManagerAPIError(MCPServerError):
    """Exception raised when HyperManager API calls fail."""
    
    def __init__(self, message: str, status_code: Optional[int] = None):
        super().__init__(
            message=f"HyperManager API error: {message}",
            code=-32603,
            data={
                "type": "api_error",
                "status_code": status_code
            }
        )


class MethodNotFoundError(MCPServerError):
    """Exception raised when MCP method is not found."""
    
    def __init__(self, method: str):
        super().__init__(
            message=f"Method not found: {method}",
            code=-32601,
            data={"method": method}
        )
