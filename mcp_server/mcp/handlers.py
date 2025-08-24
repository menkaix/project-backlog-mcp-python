"""Optimized MCP handlers with reduced duplication."""

import json
from typing import Any, Dict, Optional
from mcp import types
from mcp_server.mcp.registry import tool_registry
from mcp_server.core.exceptions import MCPServerError, ValidationError, ToolNotFoundError
from mcp_server.core.logging import get_logger

logger = get_logger(__name__)


class MCPHandlers:
    """Optimized MCP handlers with centralized logic."""
    
    def __init__(self):
        """Initialize MCP handlers."""
        logger.info("MCP handlers initialized")
    
    def list_tools(self) -> types.ListToolsResult:
        """
        Return the list of available tools.
        
        Returns:
            List of available tools
        """
        try:
            tools = tool_registry.list_tools()
            logger.debug(f"Listed {len(tools)} tools")
            return types.ListToolsResult(tools=tools)
        except Exception as e:
            logger.error(f"Error listing tools: {e}")
            raise MCPServerError(f"Failed to list tools: {str(e)}") from e
    
    def call_tool(self, name: str, arguments: Optional[Dict[str, Any]] = None) -> types.CallToolResult:
        """
        Execute a tool with the provided arguments.
        
        Args:
            name: Tool name
            arguments: Tool arguments
            
        Returns:
            Tool execution result
        """
        if arguments is None:
            arguments = {}
        
        try:
            logger.debug(f"Calling tool '{name}' with arguments: {arguments}")
            
            # Validate parameters
            tool_registry.validate_parameters(name, arguments)
            
            # Get tool definition and execute
            tool_def = tool_registry.get_tool(name)
            result = tool_def.handler(**arguments)
            
            logger.debug(f"Tool '{name}' executed successfully")
            return self._create_success_result(result)
            
        except (ValidationError, ToolNotFoundError) as e:
            logger.warning(f"Tool execution failed: {e}")
            return self._create_error_result(str(e))
        except Exception as e:
            logger.error(f"Unexpected error executing tool '{name}': {e}")
            return self._create_error_result(f"Tool execution failed: {str(e)}")
    
    def _create_success_result(self, result: Any) -> types.CallToolResult:
        """
        Create a success result for a tool call.
        
        Args:
            result: Tool execution result
            
        Returns:
            MCP CallToolResult
        """
        return types.CallToolResult(
            content=[
                types.TextContent(
                    type="text",
                    text=json.dumps(result, indent=2, ensure_ascii=False)
                )
            ]
        )
    
    def _create_error_result(self, error_message: str) -> types.CallToolResult:
        """
        Create an error result for a tool call.
        
        Args:
            error_message: Error message
            
        Returns:
            MCP CallToolResult with error
        """
        return types.CallToolResult(
            content=[
                types.TextContent(
                    type="text",
                    text=error_message
                )
            ],
            isError=True
        )


# Global handlers instance
mcp_handlers = MCPHandlers()
