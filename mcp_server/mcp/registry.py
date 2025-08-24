"""Tool registry with automatic registration and validation."""

from typing import Any, Dict, List, Optional, Callable
from dataclasses import dataclass
from functools import wraps
from mcp import types
from mcp_server.core.exceptions import ValidationError, ToolNotFoundError
from mcp_server.core.logging import get_logger

logger = get_logger(__name__)


@dataclass
class ToolDefinition:
    """Definition of an MCP tool."""
    name: str
    description: str
    input_schema: Dict[str, Any]
    handler: Callable
    required_params: List[str]


class ToolRegistry:
    """Registry for MCP tools with automatic registration."""
    
    def __init__(self):
        """Initialize the tool registry."""
        self._tools: Dict[str, ToolDefinition] = {}
        logger.info("Tool registry initialized")
    
    def register_tool(
        self,
        name: str,
        description: str,
        input_schema: Dict[str, Any],
        required_params: Optional[List[str]] = None
    ):
        """
        Decorator to register a tool.
        
        Args:
            name: Tool name
            description: Tool description
            input_schema: JSON schema for input validation
            required_params: List of required parameter names
            
        Returns:
            Decorator function
        """
        def decorator(func: Callable) -> Callable:
            # Extract required params from schema if not provided
            if required_params is None:
                schema_required = input_schema.get("required", [])
            else:
                schema_required = required_params
            
            # Register the tool
            tool_def = ToolDefinition(
                name=name,
                description=description,
                input_schema=input_schema,
                handler=func,
                required_params=schema_required
            )
            
            self._tools[name] = tool_def
            logger.debug(f"Registered tool: {name}")
            
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            
            return wrapper
        
        return decorator
    
    def get_tool(self, name: str) -> ToolDefinition:
        """
        Get a tool definition by name.
        
        Args:
            name: Tool name
            
        Returns:
            Tool definition
            
        Raises:
            ToolNotFoundError: If tool is not found
        """
        if name not in self._tools:
            raise ToolNotFoundError(name)
        
        return self._tools[name]
    
    def list_tools(self) -> List[types.Tool]:
        """
        Get list of all registered tools in MCP format.
        
        Returns:
            List of MCP Tool objects
        """
        tools = []
        for tool_def in self._tools.values():
            tools.append(types.Tool(
                name=tool_def.name,
                description=tool_def.description,
                inputSchema=tool_def.input_schema
            ))
        
        return tools
    
    def validate_parameters(self, tool_name: str, arguments: Dict[str, Any]) -> None:
        """
        Validate tool parameters.
        
        Args:
            tool_name: Name of the tool
            arguments: Tool arguments to validate
            
        Raises:
            ToolNotFoundError: If tool is not found
            ValidationError: If required parameters are missing
        """
        tool_def = self.get_tool(tool_name)
        
        missing_params = []
        for param in tool_def.required_params:
            if param not in arguments:
                missing_params.append(param)
        
        if missing_params:
            raise ValidationError(
                f"Missing required parameters for tool '{tool_name}': {missing_params}",
                missing_params=missing_params
            )
    
    def get_tool_names(self) -> List[str]:
        """
        Get list of all registered tool names.
        
        Returns:
            List of tool names
        """
        return list(self._tools.keys())


# Global tool registry instance
tool_registry = ToolRegistry()
