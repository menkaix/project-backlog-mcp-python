import os
from fastapi import FastAPI, Request, HTTPException, Security
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from mcp_server import tools
from mcp_server.mcp_handlers import MCPHandlers
from mcp import types
import uvicorn
import json

# Charger les variables d'environnement
load_dotenv()

# Initialiser l'application FastAPI
app = FastAPI(
    title="MCP Server",
    description="Serveur pour exécuter des outils via une API HTTP sécurisée.",
    version="1.0.0"
)

# Configuration CORS pour MCP Inspector
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration de la sécurité par clé API
API_KEY = os.getenv("API_KEY")
API_KEY_NAME = "x-mcp-key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

# Initialiser les handlers MCP
mcp_handlers = MCPHandlers()

async def get_api_key(api_key_header: str = Security(api_key_header)):
    """Vérifie si la clé API fournie est valide."""
    if api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=403,
            detail="Could not validate credentials"
        )

@app.post("/tool/{tool_name}")
async def execute_tool(tool_name: str, request: Request, api_key: str = Security(get_api_key)):
    """
    Exécute un outil spécifié avec les paramètres fournis dans le corps de la requête.
    """
    try:
        params = await request.json()
    except Exception:
        params = {}

    if hasattr(tools, tool_name):
        tool_func = getattr(tools, tool_name)
        try:
            result = tool_func(**params)
            return {"result": result}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    else:
        raise HTTPException(status_code=404, detail=f"Tool '{tool_name}' not found.")

# ===== ENDPOINTS MCP =====

@app.post("/mcp")
async def mcp_main_endpoint(request: Request, api_key: str = Security(get_api_key)):
    """
    Endpoint principal MCP pour le transport HTTP streamable.
    Compatible avec MCP Inspector et autres clients MCP officiels.
    """
    try:
        body = await request.json()
        method = body.get("method")
        params = body.get("params", {})
        request_id = body.get("id")
        
        # Gestion des différents messages MCP
        if method == "initialize":
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "tools": {}
                    },
                    "serverInfo": {
                        "name": "project-backlog-mcp-server",
                        "version": "1.0.0"
                    }
                }
            }
        
        elif method == "notifications/initialized":
            # Notification d'initialisation - pas de réponse requise
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

@app.post("/mcp/list-tools")
async def mcp_list_tools(api_key: str = Security(get_api_key)):
    """
    Endpoint MCP pour lister les outils disponibles.
    Compatible avec MCP Inspector via transport HTTP streamable.
    """
    try:
        result = mcp_handlers.list_tools()
        return {
            "jsonrpc": "2.0",
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
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "jsonrpc": "2.0",
                "error": {
                    "code": -32603,
                    "message": "Internal error",
                    "data": str(e)
                }
            }
        )

@app.post("/mcp/call-tool")
async def mcp_call_tool(request: Request, api_key: str = Security(get_api_key)):
    """
    Endpoint MCP pour exécuter un outil.
    Compatible avec MCP Inspector via transport HTTP streamable.
    """
    try:
        body = await request.json()
        tool_name = body.get("params", {}).get("name")
        arguments = body.get("params", {}).get("arguments", {})
        
        if not tool_name:
            return JSONResponse(
                status_code=400,
                content={
                    "jsonrpc": "2.0",
                    "error": {
                        "code": -32602,
                        "message": "Invalid params",
                        "data": "Tool name is required"
                    }
                }
            )
        
        result = mcp_handlers.call_tool(tool_name, arguments)
        
        return {
            "jsonrpc": "2.0",
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
        
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "jsonrpc": "2.0",
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
    Endpoint d'information MCP pour MCP Inspector.
    Pas d'authentification requise pour les informations de base.
    """
    return {
        "name": "project-backlog-mcp-server",
        "version": "1.0.0",
        "description": "Serveur MCP pour la gestion des projets et diagrammes via HyperManager API",
        "transport": "http",
        "capabilities": {
            "tools": True,
            "resources": False
        }
    }

@app.get("/debug/api-key")
async def debug_api_key():
    """Endpoint de debug pour vérifier l'API_KEY chargée."""
    return {
        "api_key_loaded": API_KEY,
        "api_key_length": len(API_KEY) if API_KEY else 0
    }

@app.post("/debug/auth-test")
async def debug_auth_test(request: Request):
    """Endpoint de debug pour tester l'authentification."""
    headers = dict(request.headers)
    api_key_from_header = headers.get("x-mcp-key", "NOT_PROVIDED")
    
    return {
        "expected_api_key": API_KEY,
        "received_api_key": api_key_from_header,
        "match": api_key_from_header == API_KEY,
        "all_headers": headers
    }

def start():
    """Lance le serveur FastAPI avec uvicorn."""
    uvicorn.run("mcp_server.main:app", host="0.0.0.0", port=5000, reload=True)

if __name__ == "__main__":
    start()
