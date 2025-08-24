"""Optimized story management service with real API calls."""

from typing import Any, Dict, Optional
from mcp_server.services.optimized_base import OptimizedBaseServiceWithMixins
from mcp_server.generated_client.hypermanager_ia_gemini_integration_client.api.default import (
    get_story_tree, update_story
)
from mcp_server.generated_client.hypermanager_ia_gemini_integration_client.models import (
    UpdateStoryBody
)


class OptimizedStoryService(OptimizedBaseServiceWithMixins):
    """Optimized service for story management operations."""
    
    def get_story_tree(self, story_id: str) -> Any:
        """
        Get the story tree by story ID.
        
        Args:
            story_id: Story ID
            
        Returns:
            Story tree data
        """
        if not story_id or not isinstance(story_id, str):
            raise ValueError("Story ID must be a non-empty string")
        
        return self.execute_api_call(
            "get_story_tree",
            get_story_tree.sync,
            client=self.client.client,
            story_id=story_id.strip()
        )
    
    def update_story(self, story_data: Dict[str, Any]) -> Any:
        """
        Update a story with validation.
        
        Args:
            story_data: Story data to update
            
        Returns:
            Updated story data
        """
        if not story_data or not isinstance(story_data, dict):
            raise ValueError("Story data must be a non-empty dictionary")
        
        # Validate that we have some data to update
        if not any(story_data.values()):
            raise ValueError("Story data cannot be empty")
        
        # Create the request body
        body = UpdateStoryBody(**story_data)
        
        return self.execute_api_call(
            "update_story",
            update_story.sync,
            client=self.client.client,
            json_body=body
        )
    
    # Note: The following methods are placeholders for API endpoints that don't exist yet
    # in the generated client. They return informative messages instead of null.
    
    def get_story_features(self, story_id: str) -> Any:
        """
        Get features of a story.
        
        Args:
            story_id: Story ID
            
        Returns:
            List of story features or informative message
        """
        if not story_id or not isinstance(story_id, str):
            raise ValueError("Story ID must be a non-empty string")
        
        # This endpoint doesn't exist in the generated client yet
        return {
            "status": "endpoint_not_implemented",
            "message": f"GET /story-command/{story_id}/features endpoint is not yet available in the API client",
            "requested_story_id": story_id.strip(),
            "suggestion": "This endpoint needs to be implemented in the API client"
        }
    
    def get_story(self, story_id: str) -> Any:
        """
        Get a story by ID.
        
        Args:
            story_id: Story ID
            
        Returns:
            Story data or informative message
        """
        if not story_id or not isinstance(story_id, str):
            raise ValueError("Story ID must be a non-empty string")
        
        # This endpoint doesn't exist in the generated client yet
        return {
            "status": "endpoint_not_implemented",
            "message": f"GET /story-command/{story_id} endpoint is not yet available in the API client",
            "requested_story_id": story_id.strip(),
            "suggestion": "Use get_story_tree() to get story information, or implement this endpoint in the API client"
        }
    
    def delete_story(self, story_id: str) -> Any:
        """
        Delete a story.
        
        Args:
            story_id: Story ID
            
        Returns:
            Deletion result or informative message
        """
        if not story_id or not isinstance(story_id, str):
            raise ValueError("Story ID must be a non-empty string")
        
        # This endpoint doesn't exist in the generated client yet
        return {
            "status": "endpoint_not_implemented",
            "message": f"DELETE /story-command/{story_id} endpoint is not yet available in the API client",
            "requested_story_id": story_id.strip(),
            "suggestion": "This endpoint needs to be implemented in the API client"
        }
    
    def move_story(self, story_id: str, new_actor_id: str) -> Any:
        """
        Move a story to another actor.
        
        Args:
            story_id: Story ID to move
            new_actor_id: ID of the new actor
            
        Returns:
            Move operation result or informative message
        """
        if not story_id or not isinstance(story_id, str):
            raise ValueError("Story ID must be a non-empty string")
        
        if not new_actor_id or not isinstance(new_actor_id, str):
            raise ValueError("New actor ID must be a non-empty string")
        
        # This endpoint doesn't exist in the generated client yet
        return {
            "status": "endpoint_not_implemented",
            "message": f"POST /story-command/{story_id}/move endpoint is not yet available in the API client",
            "requested_story_id": story_id.strip(),
            "requested_new_actor_id": new_actor_id.strip(),
            "suggestion": "This endpoint needs to be implemented in the API client"
        }


# Global optimized service instance
optimized_story_service = OptimizedStoryService()
