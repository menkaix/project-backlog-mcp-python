"""Project management service."""

from typing import Any, Dict, Optional
from mcp_server.services.base import BaseService
from mcp_server.generated_client.hypermanager_ia_gemini_integration_client.api.default import (
    get_list_projects, add_project, get_projects_tree, get_list_feature_types, refresh_feature_types,
    normalize_tasks
)
from mcp_server.generated_client.hypermanager_ia_gemini_integration_client.models import AddProjectBody


class ProjectService(BaseService):
    """Service for project management operations."""
    
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
        Create a new project.
        
        Args:
            name: Project name
            code: Project code
            client_name: Client name (optional)
            description: Project description (optional)
            
        Returns:
            Created project data
        """
        body = AddProjectBody(
            name=name,
            code=code,
            client_name=client_name,
            description=description
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
        return self.execute_api_call(
            "get_projects_tree",
            get_projects_tree.sync,
            client=self.client.client,
            project=project
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
    
    def get_project(self, project_id: str) -> Any:
        """
        Get a project by ID.
        
        Args:
            project_id: Project ID
            
        Returns:
            Project data
        """
        # This would need to be implemented in the API client
        return self.execute_api_call(
            "get_project",
            lambda client, **kwargs: f"Project {project_id} - API not yet implemented",
            client=self.client.client,
            project_id=project_id
        )
    
    def update_project(self, project_id: str, project_data: Dict[str, Any]) -> Any:
        """
        Update a project.
        
        Args:
            project_id: Project ID
            project_data: Project data to update
            
        Returns:
            Updated project data
        """
        # This would need to be implemented in the API client
        return self.execute_api_call(
            "update_project",
            lambda client, **kwargs: f"Updated project {project_id} - API not yet implemented",
            client=self.client.client,
            project_id=project_id,
            project_data=project_data
        )
    
    def delete_project(self, project_id: str) -> Any:
        """
        Delete a project.
        
        Args:
            project_id: Project ID
            
        Returns:
            Deletion result
        """
        # This would need to be implemented in the API client
        return self.execute_api_call(
            "delete_project",
            lambda client, **kwargs: f"Deleted project {project_id} - API not yet implemented",
            client=self.client.client,
            project_id=project_id
        )
    
    def get_all_project_actors(self, project_id: str) -> Any:
        """
        Get all actors of a project.
        
        Args:
            project_id: Project ID
            
        Returns:
            List of all project actors
        """
        # This would need to be implemented in the API client
        return self.execute_api_call(
            "get_all_project_actors",
            lambda client, **kwargs: f"All actors of project {project_id} - API not yet implemented",
            client=self.client.client,
            project_id=project_id
        )
    
    def get_project_stories(self, project_id: str) -> Any:
        """
        Get all stories of a project.
        
        Args:
            project_id: Project ID
            
        Returns:
            List of project stories
        """
        # This would need to be implemented in the API client
        return self.execute_api_call(
            "get_project_stories",
            lambda client, **kwargs: f"Stories of project {project_id} - API not yet implemented",
            client=self.client.client,
            project_id=project_id
        )
    
    def get_project_features(self, project_id: str) -> Any:
        """
        Get all features of a project.
        
        Args:
            project_id: Project ID
            
        Returns:
            List of project features
        """
        # This would need to be implemented in the API client
        return self.execute_api_call(
            "get_project_features",
            lambda client, **kwargs: f"Features of project {project_id} - API not yet implemented",
            client=self.client.client,
            project_id=project_id
        )


# Global service instance
project_service = ProjectService()
