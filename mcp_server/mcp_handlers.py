import json
from typing import Any, Dict, List, Optional
from mcp import types
from mcp_server import tools

class MCPHandlers:
    """Gestionnaire des requêtes MCP pour les outils du serveur."""
    
    def __init__(self):
        self.tools_registry = {
            "list_projects": {
                "name": "list_projects",
                "description": "Récupère la liste des projets depuis l'API HyperManager",
                "inputSchema": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            },
            "create_diagram": {
                "name": "create_diagram",
                "description": "Crée un nouveau diagramme avec un nom et une définition",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Nom du diagramme"
                        },
                        "definition": {
                            "type": "string",
                            "description": "Définition du diagramme"
                        }
                    },
                    "required": ["name", "definition"]
                }
            },
            "list_diagrams": {
                "name": "list_diagrams",
                "description": "Récupère la liste des diagrammes",
                "inputSchema": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        }
    
    def list_tools(self) -> types.ListToolsResult:
        """Retourne la liste des outils disponibles."""
        tools_list = []
        for tool_info in self.tools_registry.values():
            tools_list.append(types.Tool(
                name=tool_info["name"],
                description=tool_info["description"],
                inputSchema=tool_info["inputSchema"]
            ))
        
        return types.ListToolsResult(tools=tools_list)
    
    def call_tool(self, name: str, arguments: Optional[Dict[str, Any]] = None) -> types.CallToolResult:
        """Exécute un outil spécifié avec les arguments fournis."""
        if arguments is None:
            arguments = {}
            
        try:
            if name == "list_projects":
                result = tools.list_projects()
                return types.CallToolResult(
                    content=[
                        types.TextContent(
                            type="text",
                            text=json.dumps(result, indent=2, ensure_ascii=False)
                        )
                    ]
                )
            
            elif name == "create_diagram":
                if "name" not in arguments or "definition" not in arguments:
                    return types.CallToolResult(
                        content=[
                            types.TextContent(
                                type="text",
                                text="Erreur: Les paramètres 'name' et 'definition' sont requis"
                            )
                        ],
                        isError=True
                    )
                
                result = tools.create_diagram(
                    name=arguments["name"],
                    definition=arguments["definition"]
                )
                return types.CallToolResult(
                    content=[
                        types.TextContent(
                            type="text",
                            text=json.dumps(result, indent=2, ensure_ascii=False)
                        )
                    ]
                )
            
            elif name == "list_diagrams":
                result = tools.list_diagrams()
                return types.CallToolResult(
                    content=[
                        types.TextContent(
                            type="text",
                            text=json.dumps(result, indent=2, ensure_ascii=False)
                        )
                    ]
                )
            
            else:
                return types.CallToolResult(
                    content=[
                        types.TextContent(
                            type="text",
                            text=f"Outil '{name}' non trouvé"
                        )
                    ],
                    isError=True
                )
                
        except Exception as e:
            return types.CallToolResult(
                content=[
                    types.TextContent(
                        type="text",
                        text=f"Erreur lors de l'exécution de l'outil '{name}': {str(e)}"
                    )
                ],
                isError=True
            )
