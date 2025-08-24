"""Optimized FastAPI application with clean architecture."""

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from mcp_server.config.settings import settings
from mcp_server.core.logging import setup_logging, get_logger
from mcp_server.core.security import create_auth_dependency
from mcp_server.core.exceptions import MCPServerError
from mcp_server.mcp.handlers import mcp_handlers
import mcp_server.optimized_tools  # Import to register optimized tools
import uvicorn

# Setup logging
logger = setup_logging()
app_logger = get_logger(__name__)

# Initialize FastAPI application
app = FastAPI(
    title="MCP Server",
    description=settings.server_description,
    version=settings.server_version
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=settings.cors_credentials,
    allow_methods=settings.cors_methods,
    allow_headers=settings.cors_headers,
)

# Authentication dependency
auth_dependency = create_auth_dependency()


@app.exception_handler(MCPServerError)
async def mcp_server_error_handler(request: Request, exc: MCPServerError):
    """Handle MCP server errors."""
    app_logger.error(f"MCP Server Error: {exc.message}")
    return JSONResponse(
        status_code=500,
        content={
            "jsonrpc": "2.0",
            "error": {
                "code": exc.code,
                "message": exc.message,
                "data": exc.data
            }
        }
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Handle HTTP exceptions."""
    app_logger.warning(f"HTTP Exception: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )


# ===== MCP ENDPOINTS =====

@app.post("/mcp")
async def mcp_main_endpoint(request: Request, _: str = auth_dependency):
    """
    Main MCP endpoint for HTTP streamable transport.
    Compatible with MCP Inspector and other official MCP clients.
    """
    try:
        body = await request.json()
        method = body.get("method")
        params = body.get("params", {})
        request_id = body.get("id")
        
        app_logger.debug(f"MCP request: method={method}, id={request_id}")
        
        if method == "initialize":
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "protocolVersion": settings.mcp_protocol_version,
                    "capabilities": {"tools": {}},
                    "serverInfo": {
                        "name": settings.server_name,
                        "version": settings.server_version
                    }
                }
            }
        
        elif method == "notifications/initialized":
            return {"jsonrpc": "2.0"}
        
        elif method == "tools/list":
            result = mcp_handlers.list_tools()
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "tools": [
                        {
                            "name": tool.name,
                            "description": tool.description,
                            "inputSchema": tool.inputSchema
                        }
                        for tool in result.tools
                    ]
                }
            }
        
        elif method == "tools/call":
            tool_name = params.get("name")
            arguments = params.get("arguments", {})
            
            if not tool_name:
                return {
                    "jsonrpc": "2.0",
                    "id": request_id,
                    "error": {
                        "code": -32602,
                        "message": "Invalid params",
                        "data": "Tool name is required"
                    }
                }
            
            result = mcp_handlers.call_tool(tool_name, arguments)
            
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "content": [
                        {
                            "type": content.type,
                            "text": content.text
                        }
                        for content in result.content
                    ],
                    "isError": getattr(result, 'isError', False)
                }
            }
        
        else:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {
                    "code": -32601,
                    "message": "Method not found",
                    "data": f"Unknown method: {method}"
                }
            }
            
    except Exception as e:
        app_logger.error(f"Error in MCP endpoint: {e}")
        return JSONResponse(
            status_code=500,
            content={
                "jsonrpc": "2.0",
                "id": body.get("id") if 'body' in locals() else None,
                "error": {
                    "code": -32603,
                    "message": "Internal error",
                    "data": str(e)
                }
            }
        )


@app.get("/mcp/info")
async def mcp_info():
    """
    MCP information endpoint for MCP Inspector.
    No authentication required for basic information.
    """
    return {
        "name": settings.server_name,
        "version": settings.server_version,
        "description": settings.server_description,
        "transport": "http",
        "capabilities": {
            "tools": True,
            "resources": False
        }
    }


# ===== LEGACY TOOL ENDPOINTS =====

@app.post("/tool/{tool_name}")
async def execute_tool(tool_name: str, request: Request, _: str = auth_dependency):
    """
    Execute a tool by name (legacy endpoint).
    """
    try:
        params = await request.json()
    except Exception:
        params = {}

    try:
        result = mcp_handlers.call_tool(tool_name, params)
        
        if getattr(result, 'isError', False):
            raise HTTPException(status_code=500, detail=result.content[0].text)
        
        # Parse JSON result for legacy compatibility
        import json
        result_data = json.loads(result.content[0].text)
        return {"result": result_data}
        
    except Exception as e:
        app_logger.error(f"Error executing tool {tool_name}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# ===== DEBUG ENDPOINTS =====

@app.get("/debug/api-key")
async def debug_api_key():
    """Debug endpoint to check API key configuration."""
    return {
        "api_key_loaded": bool(settings.api_key),
        "api_key_length": len(settings.api_key) if settings.api_key else 0
    }


@app.post("/debug/auth-test")
async def debug_auth_test(request: Request):
    """Debug endpoint to test authentication."""
    headers = dict(request.headers)
    api_key_from_header = headers.get(settings.api_key_header_name, "NOT_PROVIDED")
    
    return {
        "expected_api_key": settings.api_key,
        "received_api_key": api_key_from_header,
        "match": api_key_from_header == settings.api_key,
        "all_headers": headers
    }


# ===== HEALTH CHECK =====

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "server": settings.server_name,
        "version": settings.server_version
    }


def start():
    """Start the FastAPI server with uvicorn."""
    app_logger.info(f"Starting {settings.server_name} v{settings.server_version}")
    uvicorn.run(
        "mcp_server.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload
    )


if __name__ == "__main__":
    start()
