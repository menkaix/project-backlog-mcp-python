"""Optimized diagram management service with real API calls."""

from typing import Any, Dict, Optional
from mcp_server.services.optimized_base import OptimizedBaseServiceWithMixins
from mcp_server.generated_client.hypermanager_ia_gemini_integration_client.api.default import (
    get_list_diagrams, add_diagram, get_diagram, update_diagram,
    get_png_diagram, get_plant_url_diagram, get_diagram_definition,
    update_diagram_definition, update_diagram_graphic
)
from mcp_server.generated_client.hypermanager_ia_gemini_integration_client.models import (
    AddDiagramBody, UpdateDiagramBody
)


class OptimizedDiagramService(OptimizedBaseServiceWithMixins):
    """Optimized service for diagram management operations."""
    
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
        Create a new diagram with validation.
        
        Args:
            name: Diagram name
            definition: Diagram definition
            
        Returns:
            Created diagram data
        """
        # Validate input data
        diagram_data = {'name': name, 'definition': definition}
        
        # Validate required fields
        self._validate_required_fields(diagram_data, ['name', 'definition'])
        
        # Validate field types
        field_types = {'name': str, 'definition': str}
        self._validate_field_types(diagram_data, field_types)
        
        # Sanitize string fields
        diagram_data = self._sanitize_string_fields(diagram_data, ['name', 'definition'])
        
        # Additional validation for diagram definition
        if not diagram_data['definition'].strip():
            raise ValueError("Diagram definition cannot be empty")
        
        # Create the request body
        body = AddDiagramBody(
            name=diagram_data['name'],
            definition=diagram_data['definition']
        )
        
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
        if not diagram_id or not isinstance(diagram_id, str):
            raise ValueError("Diagram ID must be a non-empty string")
        
        return self.execute_api_call(
            "get_diagram",
            get_diagram.sync,
            client=self.client.client,
            id=diagram_id.strip()
        )
    
    def update_diagram(self, diagram_id: str, name: str) -> Any:
        """
        Update a diagram name.
        
        Args:
            diagram_id: Diagram ID
            name: New diagram name
            
        Returns:
            Updated diagram data
        """
        if not diagram_id or not isinstance(diagram_id, str):
            raise ValueError("Diagram ID must be a non-empty string")
        
        if not name or not isinstance(name, str):
            raise ValueError("Diagram name must be a non-empty string")
        
        # Create the request body
        body = UpdateDiagramBody(name=name.strip())
        
        return self.execute_api_call(
            "update_diagram",
            update_diagram.sync,
            client=self.client.client,
            id=diagram_id.strip(),
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
        if not diagram_name or not isinstance(diagram_name, str):
            raise ValueError("Diagram name must be a non-empty string")
        
        return self.execute_api_call(
            "get_png_diagram",
            get_png_diagram.sync,
            client=self.client.client,
            diagram_name=diagram_name.strip()
        )
    
    def get_plant_url_diagram(self, diagram_name: str) -> Any:
        """
        Retrieve the PlantUML URL of a diagram.
        
        Args:
            diagram_name: Diagram name
            
        Returns:
            PlantUML URL
        """
        if not diagram_name or not isinstance(diagram_name, str):
            raise ValueError("Diagram name must be a non-empty string")
        
        return self.execute_api_call(
            "get_plant_url_diagram",
            get_plant_url_diagram.sync,
            client=self.client.client,
            diagram_name=diagram_name.strip()
        )
    
    def get_diagram_definition(self, name: str) -> Any:
        """
        Retrieve the definition of a diagram.
        
        Args:
            name: Diagram name
            
        Returns:
            Diagram definition
        """
        if not name or not isinstance(name, str):
            raise ValueError("Diagram name must be a non-empty string")
        
        return self.execute_api_call(
            "get_diagram_definition",
            get_diagram_definition.sync,
            client=self.client.client,
            name=name.strip()
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
        if not name or not isinstance(name, str):
            raise ValueError("Diagram name must be a non-empty string")
        
        if not definition or not isinstance(definition, str):
            raise ValueError("Diagram definition must be a non-empty string")
        
        return self.execute_api_call(
            "update_diagram_definition",
            update_diagram_definition.sync,
            client=self.client.client,
            name=name.strip(),
            json_body=definition.strip()
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
        if not diagram_name or not isinstance(diagram_name, str):
            raise ValueError("Diagram name must be a non-empty string")
        
        if not definition or not isinstance(definition, str):
            raise ValueError("Diagram definition must be a non-empty string")
        
        return self.execute_api_call(
            "update_diagram_graphic",
            update_diagram_graphic.sync,
            client=self.client.client,
            diagram_name=diagram_name.strip(),
            json_body=definition.strip()
        )
    
    # Note: The following methods are placeholders for API endpoints that don't exist yet
    # in the generated client. They return informative messages instead of null.
    
    def export_diagram(self, diagram_id: str, format: str = "png") -> Any:
        """
        Export a diagram in various formats.
        
        Args:
            diagram_id: Diagram ID
            format: Export format (png, svg, pdf)
            
        Returns:
            Export result or informative message
        """
        if not diagram_id or not isinstance(diagram_id, str):
            raise ValueError("Diagram ID must be a non-empty string")
        
        valid_formats = ["png", "svg", "pdf"]
        if format not in valid_formats:
            raise ValueError(f"Format must be one of: {valid_formats}")
        
        # This endpoint doesn't exist in the generated client yet
        return {
            "status": "endpoint_not_implemented",
            "message": f"GET /diagrams/{diagram_id}/export endpoint is not yet available in the API client",
            "requested_diagram_id": diagram_id.strip(),
            "requested_format": format,
            "suggestion": "Use get_png_diagram() for PNG format, or implement this endpoint in the API client"
        }
    
    def clone_diagram(self, diagram_id: str, name: str) -> Any:
        """
        Clone a diagram.
        
        Args:
            diagram_id: Diagram ID to clone
            name: Name for the cloned diagram
            
        Returns:
            Clone result or informative message
        """
        if not diagram_id or not isinstance(diagram_id, str):
            raise ValueError("Diagram ID must be a non-empty string")
        
        if not name or not isinstance(name, str):
            raise ValueError("Clone name must be a non-empty string")
        
        # This endpoint doesn't exist in the generated client yet
        return {
            "status": "endpoint_not_implemented",
            "message": f"POST /diagrams/{diagram_id}/clone endpoint is not yet available in the API client",
            "requested_diagram_id": diagram_id.strip(),
            "requested_clone_name": name.strip(),
            "suggestion": "Get the original diagram definition and create a new diagram with the same definition"
        }
    
    def get_diagram_by_name(self, name: str) -> Any:
        """
        Get a diagram by name (helper method).
        
        Args:
            name: Diagram name
            
        Returns:
            Diagram data or None if not found
        """
        if not name or not isinstance(name, str):
            raise ValueError("Diagram name must be a non-empty string")
        
        try:
            # Get all diagrams and find by name
            diagrams = self.list_diagrams()
            
            # If diagrams is a list, search for the diagram by name
            if isinstance(diagrams, list):
                for diagram in diagrams:
                    if isinstance(diagram, dict) and diagram.get('name') == name.strip():
                        return diagram
            
            return None
        except Exception as e:
            self.logger.error(f"Error searching for diagram by name '{name}': {str(e)}")
            raise
    
    def delete_diagram(self, diagram_id: str) -> Any:
        """
        Delete a diagram (placeholder).
        
        Args:
            diagram_id: Diagram ID
            
        Returns:
            Informative message
        """
        if not diagram_id or not isinstance(diagram_id, str):
            raise ValueError("Diagram ID must be a non-empty string")
        
        # This endpoint doesn't exist in the generated client yet
        return {
            "status": "endpoint_not_implemented",
            "message": f"DELETE /diagrams/{diagram_id} endpoint is not yet available in the API client",
            "requested_diagram_id": diagram_id.strip(),
            "suggestion": "This endpoint needs to be implemented in the API client"
        }


# Global optimized service instance
optimized_diagram_service = OptimizedDiagramService()
