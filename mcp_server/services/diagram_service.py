"""Diagram management service."""

from typing import Any
from mcp_server.services.base import BaseService
from mcp_server.generated_client.hypermanager_ia_gemini_integration_client.api.default import (
    get_list_diagrams, add_diagram, get_diagram, update_diagram,
    get_png_diagram, get_plant_url_diagram, get_diagram_definition,
    update_diagram_definition, update_diagram_graphic
)
from mcp_server.generated_client.hypermanager_ia_gemini_integration_client.models import (
    AddDiagramBody, UpdateDiagramBody
)


class DiagramService(BaseService):
    """Service for diagram management operations."""
    
    def list_diagrams(self) -> Any:
        """
        Retrieve the list of diagrams.
        
        Returns:
            List of diagrams
        """
        return self.execute_api_call(
            "list_diagrams",
            get_list_diagrams.sync,
            client=self.client.client
        )
    
    def create_diagram(self, name: str, definition: str) -> Any:
        """
        Create a new diagram.
        
        Args:
            name: Diagram name
            definition: Diagram definition
            
        Returns:
            Created diagram data
        """
        body = AddDiagramBody(name=name, definition=definition)
        
        return self.execute_api_call(
            "create_diagram",
            add_diagram.sync,
            client=self.client.client,
            json_body=body
        )
    
    def get_diagram(self, diagram_id: str) -> Any:
        """
        Retrieve a diagram by its ID.
        
        Args:
            diagram_id: Diagram ID
            
        Returns:
            Diagram data
        """
        return self.execute_api_call(
            "get_diagram",
            get_diagram.sync,
            client=self.client.client,
            id=diagram_id
        )
    
    def update_diagram(self, diagram_id: str, name: str) -> Any:
        """
        Update a diagram.
        
        Args:
            diagram_id: Diagram ID
            name: New diagram name
            
        Returns:
            Updated diagram data
        """
        body = UpdateDiagramBody(name=name)
        
        return self.execute_api_call(
            "update_diagram",
            update_diagram.sync,
            client=self.client.client,
            id=diagram_id,
            json_body=body
        )
    
    def get_png_diagram(self, diagram_name: str) -> Any:
        """
        Retrieve a diagram in PNG format.
        
        Args:
            diagram_name: Diagram name
            
        Returns:
            PNG diagram data
        """
        return self.execute_api_call(
            "get_png_diagram",
            get_png_diagram.sync,
            client=self.client.client,
            diagram_name=diagram_name
        )
    
    def get_plant_url_diagram(self, diagram_name: str) -> Any:
        """
        Retrieve the PlantUML URL of a diagram.
        
        Args:
            diagram_name: Diagram name
            
        Returns:
            PlantUML URL
        """
        return self.execute_api_call(
            "get_plant_url_diagram",
            get_plant_url_diagram.sync,
            client=self.client.client,
            diagram_name=diagram_name
        )
    
    def get_diagram_definition(self, name: str) -> Any:
        """
        Retrieve the definition of a diagram.
        
        Args:
            name: Diagram name
            
        Returns:
            Diagram definition
        """
        return self.execute_api_call(
            "get_diagram_definition",
            get_diagram_definition.sync,
            client=self.client.client,
            name=name
        )
    
    def update_diagram_definition(self, name: str, definition: str) -> Any:
        """
        Update the definition of a diagram.
        
        Args:
            name: Diagram name
            definition: New diagram definition
            
        Returns:
            Update result
        """
        return self.execute_api_call(
            "update_diagram_definition",
            update_diagram_definition.sync,
            client=self.client.client,
            name=name,
            json_body=definition
        )
    
    def update_diagram_graphic(self, diagram_name: str, definition: str) -> Any:
        """
        Update a diagram and return the image.
        
        Args:
            diagram_name: Diagram name
            definition: Diagram definition
            
        Returns:
            Updated diagram image
        """
        return self.execute_api_call(
            "update_diagram_graphic",
            update_diagram_graphic.sync,
            client=self.client.client,
            diagram_name=diagram_name,
            json_body=definition
        )
    
    def export_diagram(self, diagram_id: str, format: str = "png") -> Any:
        """
        Export a diagram in various formats.
        
        Args:
            diagram_id: Diagram ID
            format: Export format (png, svg, pdf)
            
        Returns:
            Exported diagram data
        """
        # This would need to be implemented in the API client
        return self.execute_api_call(
            "export_diagram",
            lambda client, **kwargs: f"Exported diagram {diagram_id} as {format} - API not yet implemented",
            client=self.client.client,
            diagram_id=diagram_id,
            format=format
        )
    
    def clone_diagram(self, diagram_id: str, name: str) -> Any:
        """
        Clone a diagram.
        
        Args:
            diagram_id: Diagram ID to clone
            name: Name for the cloned diagram
            
        Returns:
            Cloned diagram data
        """
        # This would need to be implemented in the API client
        return self.execute_api_call(
            "clone_diagram",
            lambda client, **kwargs: f"Cloned diagram {diagram_id} as {name} - API not yet implemented",
            client=self.client.client,
            diagram_id=diagram_id,
            name=name
        )


# Global service instance
diagram_service = DiagramService()
