"""Optimized project management service with real API calls."""

from typing import Any, Dict, Optional
from mcp_server.services.optimized_base import OptimizedBaseServiceWithMixins
from mcp_server.generated_client.hypermanager_ia_gemini_integration_client.api.default import (
    get_list_projects, add_project, get_projects_tree, get_list_feature_types, 
    refresh_feature_types, normalize_tasks
)
from mcp_server.generated_client.hypermanager_ia_gemini_integration_client.models import AddProjectBody


class OptimizedProjectService(OptimizedBaseServiceWithMixins):
    """Optimized service for project management operations."""
    
    def list_projects(self) -> Any:
        """
        Retrieve the list of projects from HyperManager API.
        
        Returns:
            List of projects
        """
        return self.execute_api_call(
            "list_projects",
            get_list_projects.sync,
            client=self.client.client
        )
    
    def create_project(
        self,
        name: str,
        code: str,
        client_name: Optional[str] = None,
        description: Optional[str] = None
    ) -> Any:
        """
        Create a new project with validation.
        
        Args:
            name: Project name
            code: Project code
            client_name: Client name (optional)
            description: Project description (optional)
            
        Returns:
            Created project data
        """
        # Validate input data
        project_data = {
            'name': name,
            'code': code,
            'client_name': client_name,
            'description': description
        }
        
        # Validate required fields
        self._validate_required_fields(project_data, ['name', 'code'])
        
        # Validate field types
        field_types = {
            'name': str,
            'code': str,
            'client_name': str,
            'description': str
        }
        self._validate_field_types(project_data, field_types)
        
        # Sanitize string fields
        project_data = self._sanitize_string_fields(
            project_data, 
            ['name', 'code', 'client_name', 'description']
        )
        
        # Create the request body
        body = AddProjectBody(
            name=project_data['name'],
            code=project_data['code'],
            client_name=project_data.get('client_name'),
            description=project_data.get('description')
        )
        
        return self.execute_api_call(
            "create_project",
            add_project.sync,
            client=self.client.client,
            json_body=body
        )
    
    def get_projects_tree(self, project: str) -> Any:
        """
        Retrieve the component tree of a project.
        
        Args:
            project: Project ID
            
        Returns:
            Project component tree
        """
        if not project or not isinstance(project, str):
            raise ValueError("Project ID must be a non-empty string")
        
        return self.execute_api_call(
            "get_projects_tree",
            get_projects_tree.sync,
            client=self.client.client,
            project=project.strip()
        )
    
    def get_feature_types(self) -> Any:
        """
        Retrieve the list of feature types.
        
        Returns:
            List of feature types
        """
        return self.execute_api_call(
            "get_feature_types",
            get_list_feature_types.sync,
            client=self.client.client
        )
    
    def refresh_feature_types(self) -> Any:
        """
        Refresh feature types.
        
        Returns:
            Refresh operation result
        """
        return self.execute_api_call(
            "refresh_feature_types",
            refresh_feature_types.sync,
            client=self.client.client
        )
    
    def normalize_tasks(self) -> Any:
        """
        Normalize tasks.
        
        Returns:
            Normalization result
        """
        return self.execute_api_call(
            "normalize_tasks",
            normalize_tasks.sync,
            client=self.client.client
        )
    
    # Note: The following methods are placeholders for API endpoints that don't exist yet
    # in the generated client. They return informative messages instead of null.
    # These should be replaced with real API calls when the endpoints are available.
    
    def get_project(self, project_id: str) -> Any:
        """
        Get a project by ID.
        
        Args:
            project_id: Project ID
            
        Returns:
            Project data or informative message
        """
        if not project_id or not isinstance(project_id, str):
            raise ValueError("Project ID must be a non-empty string")
        
        # This endpoint doesn't exist in the generated client yet
        # Return an informative response instead of null
        return {
            "status": "endpoint_not_implemented",
            "message": f"GET /project-command/{project_id} endpoint is not yet available in the API client",
            "requested_project_id": project_id.strip(),
            "suggestion": "Use list_projects() to get all projects, then filter by ID"
        }
    
    def update_project(self, project_id: str, project_data: Dict[str, Any]) -> Any:
        """
        Update a project.
        
        Args:
            project_id: Project ID
            project_data: Project data to update
            
        Returns:
            Update result or informative message
        """
        if not project_id or not isinstance(project_id, str):
            raise ValueError("Project ID must be a non-empty string")
        
        if not project_data or not isinstance(project_data, dict):
            raise ValueError("Project data must be a non-empty dictionary")
        
        # Validate and sanitize the update data
        allowed_fields = ['name', 'code', 'clientName', 'description']
        sanitized_data = {k: v for k, v in project_data.items() if k in allowed_fields}
        
        if not sanitized_data:
            raise ValueError(f"No valid fields provided. Allowed fields: {allowed_fields}")
        
        # This endpoint doesn't exist in the generated client yet
        return {
            "status": "endpoint_not_implemented",
            "message": f"PATCH /project-command/{project_id} endpoint is not yet available in the API client",
            "requested_project_id": project_id.strip(),
            "requested_updates": sanitized_data,
            "suggestion": "This endpoint needs to be implemented in the API client"
        }
    
    def delete_project(self, project_id: str) -> Any:
        """
        Delete a project.
        
        Args:
            project_id: Project ID
            
        Returns:
            Deletion result or informative message
        """
        if not project_id or not isinstance(project_id, str):
            raise ValueError("Project ID must be a non-empty string")
        
        # This endpoint doesn't exist in the generated client yet
        return {
            "status": "endpoint_not_implemented",
            "message": f"DELETE /project-command/{project_id} endpoint is not yet available in the API client",
            "requested_project_id": project_id.strip(),
            "suggestion": "This endpoint needs to be implemented in the API client"
        }
    
    def get_all_project_actors(self, project_id: str) -> Any:
        """
        Get all actors of a project.
        
        Args:
            project_id: Project ID
            
        Returns:
            List of project actors or informative message
        """
        if not project_id or not isinstance(project_id, str):
            raise ValueError("Project ID must be a non-empty string")
        
        # This endpoint doesn't exist in the generated client yet
        return {
            "status": "endpoint_not_implemented",
            "message": f"GET /project-command/{project_id}/actors endpoint is not yet available in the API client",
            "requested_project_id": project_id.strip(),
            "suggestion": "This endpoint needs to be implemented in the API client"
        }
    
    def get_project_stories(self, project_id: str) -> Any:
        """
        Get all stories of a project.
        
        Args:
            project_id: Project ID
            
        Returns:
            List of project stories or informative message
        """
        if not project_id or not isinstance(project_id, str):
            raise ValueError("Project ID must be a non-empty string")
        
        # This endpoint doesn't exist in the generated client yet
        return {
            "status": "endpoint_not_implemented",
            "message": f"GET /project-command/{project_id}/stories endpoint is not yet available in the API client",
            "requested_project_id": project_id.strip(),
            "suggestion": "This endpoint needs to be implemented in the API client"
        }
    
    def get_project_features(self, project_id: str) -> Any:
        """
        Get all features of a project.
        
        Args:
            project_id: Project ID
            
        Returns:
            List of project features or informative message
        """
        if not project_id or not isinstance(project_id, str):
            raise ValueError("Project ID must be a non-empty string")
        
        # This endpoint doesn't exist in the generated client yet
        return {
            "status": "endpoint_not_implemented",
            "message": f"GET /project-command/{project_id}/features endpoint is not yet available in the API client",
            "requested_project_id": project_id.strip(),
            "suggestion": "This endpoint needs to be implemented in the API client"
        }


# Global optimized service instance
optimized_project_service = OptimizedProjectService()
