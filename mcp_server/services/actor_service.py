"""Actor management service."""

from typing import Any, Dict, Optional
from mcp_server.services.base import BaseService
from mcp_server.generated_client.hypermanager_ia_gemini_integration_client.api.default import (
    add_actor, add_story_to_actor
)
from mcp_server.generated_client.hypermanager_ia_gemini_integration_client.models import (
    AddActorBody, AddStoryToActorBody
)


class ActorService(BaseService):
    """Service for actor management operations."""
    
    def add_actor(self, project_id: str, actor_data: Dict[str, Any]) -> Any:
        """
        Add an actor to a project.
        
        Args:
            project_id: Project ID
            actor_data: Actor data to add
            
        Returns:
            Created actor data
        """
        body = AddActorBody(**actor_data)
        
        return self.execute_api_call(
            "add_actor",
            add_actor.sync,
            client=self.client.client,
            project=project_id,
            json_body=body
        )
    
    def add_story_to_actor(self, project_id: str, actor_name: str, story_data: Dict[str, Any]) -> Any:
        """
        Add a story to an actor.
        
        Args:
            project_id: Project ID
            actor_name: Actor name
            story_data: Story data to add
            
        Returns:
            Created story data
        """
        body = AddStoryToActorBody(**story_data)
        
        return self.execute_api_call(
            "add_story_to_actor",
            add_story_to_actor.sync,
            client=self.client.client,
            project=project_id,
            name=actor_name,
            json_body=body
        )
    
    def get_project_actors(self, project_id: str) -> Any:
        """
        Get actors of a project.
        
        Args:
            project_id: Project ID
            
        Returns:
            List of project actors
        """
        # This would need to be implemented in the API client
        return self.execute_api_call(
            "get_project_actors",
            lambda client, **kwargs: f"Actors of project {project_id} - API not yet implemented",
            client=self.client.client,
            project_id=project_id
        )
    
    def get_actor(self, project_id: str, actor_id: str) -> Any:
        """
        Get an actor by ID.
        
        Args:
            project_id: Project ID
            actor_id: Actor ID
            
        Returns:
            Actor data
        """
        # This would need to be implemented in the API client
        return self.execute_api_call(
            "get_actor",
            lambda client, **kwargs: f"Actor {actor_id} in project {project_id} - API not yet implemented",
            client=self.client.client,
            project_id=project_id,
            actor_id=actor_id
        )
    
    def update_actor(self, project_id: str, actor_id: str, actor_data: Dict[str, Any]) -> Any:
        """
        Update an actor.
        
        Args:
            project_id: Project ID
            actor_id: Actor ID
            actor_data: Actor data to update
            
        Returns:
            Updated actor data
        """
        # This would need to be implemented in the API client
        return self.execute_api_call(
            "update_actor",
            lambda client, **kwargs: f"Updated actor {actor_id} in project {project_id} - API not yet implemented",
            client=self.client.client,
            project_id=project_id,
            actor_id=actor_id,
            actor_data=actor_data
        )
    
    def delete_actor(self, project_id: str, actor_id: str) -> Any:
        """
        Delete an actor.
        
        Args:
            project_id: Project ID
            actor_id: Actor ID
            
        Returns:
            Deletion result
        """
        # This would need to be implemented in the API client
        return self.execute_api_call(
            "delete_actor",
            lambda client, **kwargs: f"Deleted actor {actor_id} from project {project_id} - API not yet implemented",
            client=self.client.client,
            project_id=project_id,
            actor_id=actor_id
        )
    
    def get_actor_stories(self, project_id: str, actor_id: str) -> Any:
        """
        Get stories of an actor.
        
        Args:
            project_id: Project ID
            actor_id: Actor ID
            
        Returns:
            List of actor stories
        """
        # This would need to be implemented in the API client
        return self.execute_api_call(
            "get_actor_stories",
            lambda client, **kwargs: f"Stories of actor {actor_id} in project {project_id} - API not yet implemented",
            client=self.client.client,
            project_id=project_id,
            actor_id=actor_id
        )


# Global service instance
actor_service = ActorService()
