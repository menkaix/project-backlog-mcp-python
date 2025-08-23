from mcp_server.client import client
from mcp_server.generated_client.hypermanager_ia_gemini_integration_client.api.default import get_list_projects, add_diagram, get_list_diagrams
from mcp_server.generated_client.hypermanager_ia_gemini_integration_client.models import AddDiagramBody

def list_projects():
    """
    Récupère la liste des projets depuis l'API HyperManager.
    """
    return get_list_projects.sync(client=client)

def create_diagram(name: str, definition: str):
    """
    Crée un nouveau diagramme.
    """
    body = AddDiagramBody(name=name, definition=definition)
    return add_diagram.sync(client=client, json_body=body)

def list_diagrams():
    """
    Récupère la liste des diagrammes.
    """
    return get_list_diagrams.sync(client=client)