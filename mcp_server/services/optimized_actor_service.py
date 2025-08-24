"""Optimized actor management service with real API calls."""

from typing import Any, Dict, Optional
from mcp_server.services.optimized_base import OptimizedBaseServiceWithMixins
from mcp_server.generated_client.hypermanager_ia_gemini_integration_client.api.default import (
    add_actor, add_story_to_actor
)
from mcp_server.generated_client.hypermanager_ia_gemini_integration_client.models import (
    AddActorBody, AddStoryToActorBody
)


class OptimizedActorService(OptimizedBaseServiceWithMixins):
    """Optimized service for actor management operations."""
    
    def add_actor(self, project_id: str, actor_data: Dict[str, Any]) -> Any:
        """
        Add an actor to a project with validation.
        
        Args:
            project_id: Project ID
            actor_data: Actor data to add
            
        Returns:
            Created actor data
        """
        if not project_id or not isinstance(project_id, str):
            raise ValueError("Project ID must be a non-empty string")
        
        if not actor_data or not isinstance(actor_data, dict):
            raise ValueError("Actor data must be a non-empty dictionary")
        
        # Validate that we have some data to create the actor
        if not any(actor_data.values()):
            raise ValueError("Actor data cannot be empty")
        
        # Create the request body
        body = AddActorBody(**actor_data)
        
        return self.execute_api_call(
            "add_actor",
            add_actor.sync,
            client=self.client.client,
            project=project_id.strip(),
            json_body=body
        )
    
    def add_story_to_actor(self, project_id: str, actor_name: str, story_data: Dict[str, Any]) -> Any:
        """
        Add a story to an actor with validation.
        
        Args:
            project_id: Project ID
            actor_name: Actor name
            story_data: Story data to add
            
        Returns:
            Created story data
        """
        if not project_id or not isinstance(project_id, str):
            raise ValueError("Project ID must be a non-empty string")
        
        if not actor_name or not isinstance(actor_name, str):
            raise ValueError("Actor name must be a non-empty string")
        
        if not story_data or not isinstance(story_data, dict):
            raise ValueError("Story data must be a non-empty dictionary")
        
        # Validate that we have some data to create the story
        if not any(story_data.values()):
            raise ValueError("Story data cannot be empty")
        
        # Create the request body
        body = AddStoryToActorBody(**story_data)
        
        return self.execute_api_call(
            "add_story_to_actor",
            add_story_to_actor.sync,
            client=self.client.client,
            project=project_id.strip(),
            name=actor_name.strip(),
            json_body=body
        )
    
    # Note: The following methods are placeholders for API endpoints that don't exist yet
    # in the generated client. They return informative messages instead of null.
    
    def get_project_actors(self, project_id: str) -> Any:
        """
        Get actors of a project.
        
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
            "message": f"GET /actor-command/{project_id} endpoint is not yet available in the API client",
            "requested_project_id": project_id.strip(),
            "suggestion": "This endpoint needs to be implemented in the API client"
        }
    
    def get_actor(self, project_id: str, actor_id: str) -> Any:
        """
        Get an actor by ID.
        
        Args:
            project_id: Project ID
            actor_id: Actor ID
            
        Returns:
            Actor data or informative message
        """
        if not project_id or not isinstance(project_id, str):
            raise ValueError("Project ID must be a non-empty string")
        
        if not actor_id or not isinstance(actor_id, str):
            raise ValueError("Actor ID must be a non-empty string")
        
        # This endpoint doesn't exist in the generated client yet
        return {
            "status": "endpoint_not_implemented",
            "message": f"GET /actor-command/{project_id}/{actor_id} endpoint is not yet available in the API client",
            "requested_project_id": project_id.strip(),
            "requested_actor_id": actor_id.strip(),
            "suggestion": "This endpoint needs to be implemented in the API client"
        }
    
    def update_actor(self, project_id: str, actor_id: str, actor_data: Dict[str, Any]) -> Any:
        """
        Update an actor.
        
        Args:
            project_id: Project ID
            actor_id: Actor ID
            actor_data: Actor data to update
            
        Returns:
            Updated actor data or informative message
        """
        if not project_id or not isinstance(project_id, str):
            raise ValueError("Project ID must be a non-empty string")
        
        if not actor_id or not isinstance(actor_id, str):
            raise ValueError("Actor ID must be a non-empty string")
        
        if not actor_data or not isinstance(actor_data, dict):
            raise ValueError("Actor data must be a non-empty dictionary")
        
        # Validate that we have some data to update
        if not any(actor_data.values()):
            raise ValueError("Actor data cannot be empty")
        
        # This endpoint doesn't exist in the generated client yet
        return {
            "status": "endpoint_not_implemented",
            "message": f"PATCH /actor-command/{project_id}/{actor_id} endpoint is not yet available in the API client",
            "requested_project_id": project_id.strip(),
            "requested_actor_id": actor_id.strip(),
            "requested_updates": actor_data,
            "suggestion": "This endpoint needs to be implemented in the API client"
        }
    
    def delete_actor(self, project_id: str, actor_id: str) -> Any:
        """
        Delete an actor.
        
        Args:
            project_id: Project ID
            actor_id: Actor ID
            
        Returns:
            Deletion result or informative message
        """
        if not project_id or not isinstance(project_id, str):
            raise ValueError("Project ID must be a non-empty string")
        
        if not actor_id or not isinstance(actor_id, str):
            raise ValueError("Actor ID must be a non-empty string")
        
        # This endpoint doesn't exist in the generated client yet
        return {
            "status": "endpoint_not_implemented",
            "message": f"DELETE /actor-command/{project_id}/{actor_id} endpoint is not yet available in the API client",
            "requested_project_id": project_id.strip(),
            "requested_actor_id": actor_id.strip(),
            "suggestion": "This endpoint needs to be implemented in the API client"
        }
    
    def get_actor_stories(self, project_id: str, actor_id: str) -> Any:
        """
        Get stories of an actor.
        
        Args:
            project_id: Project ID
            actor_id: Actor ID
            
        Returns:
            List of actor stories or informative message
        """
        if not project_id or not isinstance(project_id, str):
            raise ValueError("Project ID must be a non-empty string")
        
        if not actor_id or not isinstance(actor_id, str):
            raise ValueError("Actor ID must be a non-empty string")
        
        # This endpoint doesn't exist in the generated client yet
        return {
            "status": "endpoint_not_implemented",
            "message": f"GET /actor-command/{project_id}/{actor_id}/stories endpoint is not yet available in the API client",
            "requested_project_id": project_id.strip(),
            "requested_actor_id": actor_id.strip(),
            "suggestion": "This endpoint needs to be implemented in the API client"
        }


# Global optimized service instance
optimized_actor_service = OptimizedActorService()
