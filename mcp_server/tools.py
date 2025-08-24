"""Optimized tools with automatic registration and reduced duplication."""

from typing import Any, Dict, Optional
from mcp_server.mcp.registry import tool_registry
from mcp_server.services.project_service import project_service
from mcp_server.services.diagram_service import diagram_service
from mcp_server.services.story_service import story_service
from mcp_server.services.feature_service import feature_service
from mcp_server.services.actor_service import actor_service
from mcp_server.core.logging import get_logger

logger = get_logger(__name__)

# ===== PROJECT MANAGEMENT TOOLS =====

@tool_registry.register_tool(
    name="list_projects",
    description="Retrieve the list of projects from HyperManager API",
    input_schema={
        "type": "object",
        "properties": {},
        "required": []
    }
)
def list_projects() -> Any:
    """Retrieve the list of projects from HyperManager API."""
    return project_service.list_projects()


@tool_registry.register_tool(
    name="create_project",
    description="Create a new project with name, code, client name and description",
    input_schema={
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "Project name"
            },
            "code": {
                "type": "string",
                "description": "Project code"
            },
            "client_name": {
                "type": "string",
                "description": "Client name (optional)"
            },
            "description": {
                "type": "string",
                "description": "Project description (optional)"
            }
        },
        "required": ["name", "code"]
    }
)
def create_project(name: str, code: str, client_name: Optional[str] = None, description: Optional[str] = None) -> Any:
    """Create a new project."""
    return project_service.create_project(name, code, client_name, description)


@tool_registry.register_tool(
    name="get_projects_tree",
    description="Retrieve the component tree of a project",
    input_schema={
        "type": "object",
        "properties": {
            "project": {
                "type": "string",
                "description": "Project ID"
            }
        },
        "required": ["project"]
    }
)
def get_projects_tree(project: str) -> Any:
    """Retrieve the component tree of a project."""
    return project_service.get_projects_tree(project)


@tool_registry.register_tool(
    name="get_feature_types",
    description="Retrieve the list of feature types",
    input_schema={
        "type": "object",
        "properties": {},
        "required": []
    }
)
def get_feature_types() -> Any:
    """Retrieve the list of feature types."""
    return project_service.get_feature_types()


@tool_registry.register_tool(
    name="refresh_feature_types",
    description="Refresh feature types",
    input_schema={
        "type": "object",
        "properties": {},
        "required": []
    }
)
def refresh_feature_types() -> Any:
    """Refresh feature types."""
    return project_service.refresh_feature_types()


# ===== DIAGRAM MANAGEMENT TOOLS =====

@tool_registry.register_tool(
    name="list_diagrams",
    description="Retrieve the list of diagrams",
    input_schema={
        "type": "object",
        "properties": {},
        "required": []
    }
)
def list_diagrams() -> Any:
    """Retrieve the list of diagrams."""
    return diagram_service.list_diagrams()


@tool_registry.register_tool(
    name="create_diagram",
    description="Create a new diagram with name and definition",
    input_schema={
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "Diagram name"
            },
            "definition": {
                "type": "string",
                "description": "Diagram definition"
            }
        },
        "required": ["name", "definition"]
    }
)
def create_diagram(name: str, definition: str) -> Any:
    """Create a new diagram."""
    return diagram_service.create_diagram(name, definition)


@tool_registry.register_tool(
    name="get_diagram",
    description="Retrieve a diagram by its ID",
    input_schema={
        "type": "object",
        "properties": {
            "id": {
                "type": "string",
                "description": "Diagram ID"
            }
        },
        "required": ["id"]
    }
)
def get_diagram(id: str) -> Any:
    """Retrieve a diagram by its ID."""
    return diagram_service.get_diagram(id)


@tool_registry.register_tool(
    name="update_diagram",
    description="Update a diagram",
    input_schema={
        "type": "object",
        "properties": {
            "id": {
                "type": "string",
                "description": "Diagram ID"
            },
            "name": {
                "type": "string",
                "description": "New diagram name"
            }
        },
        "required": ["id", "name"]
    }
)
def update_diagram(id: str, name: str) -> Any:
    """Update a diagram."""
    return diagram_service.update_diagram(id, name)


@tool_registry.register_tool(
    name="get_png_diagram",
    description="Retrieve a diagram in PNG format",
    input_schema={
        "type": "object",
        "properties": {
            "diagram_name": {
                "type": "string",
                "description": "Diagram name"
            }
        },
        "required": ["diagram_name"]
    }
)
def get_png_diagram(diagram_name: str) -> Any:
    """Retrieve a diagram in PNG format."""
    return diagram_service.get_png_diagram(diagram_name)


@tool_registry.register_tool(
    name="get_plant_url_diagram",
    description="Retrieve the PlantUML URL of a diagram",
    input_schema={
        "type": "object",
        "properties": {
            "diagram_name": {
                "type": "string",
                "description": "Diagram name"
            }
        },
        "required": ["diagram_name"]
    }
)
def get_plant_url_diagram(diagram_name: str) -> Any:
    """Retrieve the PlantUML URL of a diagram."""
    return diagram_service.get_plant_url_diagram(diagram_name)


@tool_registry.register_tool(
    name="get_diagram_definition",
    description="Retrieve the definition of a diagram",
    input_schema={
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "Diagram name"
            }
        },
        "required": ["name"]
    }
)
def get_diagram_definition(name: str) -> Any:
    """Retrieve the definition of a diagram."""
    return diagram_service.get_diagram_definition(name)


@tool_registry.register_tool(
    name="update_diagram_definition",
    description="Update the definition of a diagram",
    input_schema={
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "Diagram name"
            },
            "definition": {
                "type": "string",
                "description": "New diagram definition"
            }
        },
        "required": ["name", "definition"]
    }
)
def update_diagram_definition(name: str, definition: str) -> Any:
    """Update the definition of a diagram."""
    return diagram_service.update_diagram_definition(name, definition)


@tool_registry.register_tool(
    name="update_diagram_graphic",
    description="Update a diagram and return the image",
    input_schema={
        "type": "object",
        "properties": {
            "diagram_name": {
                "type": "string",
                "description": "Diagram name"
            },
            "definition": {
                "type": "string",
                "description": "Diagram definition"
            }
        },
        "required": ["diagram_name", "definition"]
    }
)
def update_diagram_graphic(diagram_name: str, definition: str) -> Any:
    """Update a diagram and return the image."""
    return diagram_service.update_diagram_graphic(diagram_name, definition)


# ===== ADDITIONAL PROJECT TOOLS =====

@tool_registry.register_tool(
    name="normalize_tasks",
    description="Normalize tasks",
    input_schema={
        "type": "object",
        "properties": {},
        "required": []
    }
)
def normalize_tasks() -> Any:
    """Normalize tasks."""
    return project_service.normalize_tasks()


@tool_registry.register_tool(
    name="get_project",
    description="Get a project by ID",
    input_schema={
        "type": "object",
        "properties": {
            "project_id": {
                "type": "string",
                "description": "Project ID"
            }
        },
        "required": ["project_id"]
    }
)
def get_project(project_id: str) -> Any:
    """Get a project by ID."""
    return project_service.get_project(project_id)


@tool_registry.register_tool(
    name="update_project",
    description="Update a project",
    input_schema={
        "type": "object",
        "properties": {
            "project_id": {
                "type": "string",
                "description": "Project ID"
            },
            "project_data": {
                "type": "object",
                "description": "Project data to update",
                "properties": {
                    "name": {"type": "string"},
                    "code": {"type": "string"},
                    "clientName": {"type": "string"},
                    "description": {"type": "string"}
                }
            }
        },
        "required": ["project_id", "project_data"]
    }
)
def update_project(project_id: str, project_data: Dict[str, Any]) -> Any:
    """Update a project."""
    return project_service.update_project(project_id, project_data)


@tool_registry.register_tool(
    name="delete_project",
    description="Delete a project",
    input_schema={
        "type": "object",
        "properties": {
            "project_id": {
                "type": "string",
                "description": "Project ID"
            }
        },
        "required": ["project_id"]
    }
)
def delete_project(project_id: str) -> Any:
    """Delete a project."""
    return project_service.delete_project(project_id)


@tool_registry.register_tool(
    name="get_all_project_actors",
    description="Get all actors of a project",
    input_schema={
        "type": "object",
        "properties": {
            "project_id": {
                "type": "string",
                "description": "Project ID"
            }
        },
        "required": ["project_id"]
    }
)
def get_all_project_actors(project_id: str) -> Any:
    """Get all actors of a project."""
    return project_service.get_all_project_actors(project_id)


@tool_registry.register_tool(
    name="get_project_stories",
    description="Get all stories of a project",
    input_schema={
        "type": "object",
        "properties": {
            "project_id": {
                "type": "string",
                "description": "Project ID"
            }
        },
        "required": ["project_id"]
    }
)
def get_project_stories(project_id: str) -> Any:
    """Get all stories of a project."""
    return project_service.get_project_stories(project_id)


@tool_registry.register_tool(
    name="get_project_features",
    description="Get all features of a project",
    input_schema={
        "type": "object",
        "properties": {
            "project_id": {
                "type": "string",
                "description": "Project ID"
            }
        },
        "required": ["project_id"]
    }
)
def get_project_features(project_id: str) -> Any:
    """Get all features of a project."""
    return project_service.get_project_features(project_id)


# ===== ADDITIONAL DIAGRAM TOOLS =====

@tool_registry.register_tool(
    name="export_diagram",
    description="Export a diagram in various formats",
    input_schema={
        "type": "object",
        "properties": {
            "diagram_id": {
                "type": "string",
                "description": "Diagram ID"
            },
            "format": {
                "type": "string",
                "description": "Export format (png, svg, pdf)",
                "enum": ["png", "svg", "pdf"],
                "default": "png"
            }
        },
        "required": ["diagram_id"]
    }
)
def export_diagram(diagram_id: str, format: str = "png") -> Any:
    """Export a diagram in various formats."""
    return diagram_service.export_diagram(diagram_id, format)


@tool_registry.register_tool(
    name="clone_diagram",
    description="Clone a diagram",
    input_schema={
        "type": "object",
        "properties": {
            "diagram_id": {
                "type": "string",
                "description": "Diagram ID to clone"
            },
            "name": {
                "type": "string",
                "description": "Name for the cloned diagram"
            }
        },
        "required": ["diagram_id", "name"]
    }
)
def clone_diagram(diagram_id: str, name: str) -> Any:
    """Clone a diagram."""
    return diagram_service.clone_diagram(diagram_id, name)


# ===== STORY MANAGEMENT TOOLS =====

@tool_registry.register_tool(
    name="get_story_tree",
    description="Get the story tree by story ID",
    input_schema={
        "type": "object",
        "properties": {
            "story_id": {
                "type": "string",
                "description": "Story ID"
            }
        },
        "required": ["story_id"]
    }
)
def get_story_tree(story_id: str) -> Any:
    """Get the story tree by story ID."""
    return story_service.get_story_tree(story_id)


@tool_registry.register_tool(
    name="update_story",
    description="Update a story",
    input_schema={
        "type": "object",
        "properties": {
            "story_data": {
                "type": "object",
                "description": "Story data to update"
            }
        },
        "required": ["story_data"]
    }
)
def update_story(story_data: Dict[str, Any]) -> Any:
    """Update a story."""
    return story_service.update_story(story_data)


@tool_registry.register_tool(
    name="get_story_features",
    description="Get features of a story",
    input_schema={
        "type": "object",
        "properties": {
            "story_id": {
                "type": "string",
                "description": "Story ID"
            }
        },
        "required": ["story_id"]
    }
)
def get_story_features(story_id: str) -> Any:
    """Get features of a story."""
    return story_service.get_story_features(story_id)


@tool_registry.register_tool(
    name="get_story",
    description="Get a story by ID",
    input_schema={
        "type": "object",
        "properties": {
            "story_id": {
                "type": "string",
                "description": "Story ID"
            }
        },
        "required": ["story_id"]
    }
)
def get_story(story_id: str) -> Any:
    """Get a story by ID."""
    return story_service.get_story(story_id)


@tool_registry.register_tool(
    name="delete_story",
    description="Delete a story",
    input_schema={
        "type": "object",
        "properties": {
            "story_id": {
                "type": "string",
                "description": "Story ID"
            }
        },
        "required": ["story_id"]
    }
)
def delete_story(story_id: str) -> Any:
    """Delete a story."""
    return story_service.delete_story(story_id)


@tool_registry.register_tool(
    name="move_story",
    description="Move a story to another actor",
    input_schema={
        "type": "object",
        "properties": {
            "story_id": {
                "type": "string",
                "description": "Story ID to move"
            },
            "new_actor_id": {
                "type": "string",
                "description": "ID of the new actor"
            }
        },
        "required": ["story_id", "new_actor_id"]
    }
)
def move_story(story_id: str, new_actor_id: str) -> Any:
    """Move a story to another actor."""
    return story_service.move_story(story_id, new_actor_id)


# ===== FEATURE MANAGEMENT TOOLS =====

@tool_registry.register_tool(
    name="add_feature_to_story",
    description="Add a feature to a story",
    input_schema={
        "type": "object",
        "properties": {
            "story_id": {
                "type": "string",
                "description": "Story ID"
            },
            "feature_data": {
                "type": "object",
                "description": "Feature data to add"
            }
        },
        "required": ["story_id", "feature_data"]
    }
)
def add_feature_to_story(story_id: str, feature_data: Dict[str, Any]) -> Any:
    """Add a feature to a story."""
    return feature_service.add_feature_to_story(story_id, feature_data)


@tool_registry.register_tool(
    name="add_child_feature",
    description="Add a child feature to a parent feature",
    input_schema={
        "type": "object",
        "properties": {
            "parent_id": {
                "type": "string",
                "description": "Parent feature ID"
            },
            "feature_data": {
                "type": "object",
                "description": "Child feature data to add"
            }
        },
        "required": ["parent_id", "feature_data"]
    }
)
def add_child_feature(parent_id: str, feature_data: Dict[str, Any]) -> Any:
    """Add a child feature to a parent feature."""
    return feature_service.add_child_feature(parent_id, feature_data)


@tool_registry.register_tool(
    name="adopt_child_feature",
    description="Adopt a child feature",
    input_schema={
        "type": "object",
        "properties": {
            "parent_id": {
                "type": "string",
                "description": "Parent feature ID"
            },
            "child_id": {
                "type": "string",
                "description": "Child feature ID"
            }
        },
        "required": ["parent_id", "child_id"]
    }
)
def adopt_child_feature(parent_id: str, child_id: str) -> Any:
    """Adopt a child feature."""
    return feature_service.adopt_child_feature(parent_id, child_id)


@tool_registry.register_tool(
    name="get_feature",
    description="Get a feature by ID",
    input_schema={
        "type": "object",
        "properties": {
            "feature_id": {
                "type": "string",
                "description": "Feature ID"
            }
        },
        "required": ["feature_id"]
    }
)
def get_feature(feature_id: str) -> Any:
    """Get a feature by ID."""
    return feature_service.get_feature(feature_id)


@tool_registry.register_tool(
    name="update_feature",
    description="Update a feature",
    input_schema={
        "type": "object",
        "properties": {
            "feature_id": {
                "type": "string",
                "description": "Feature ID"
            },
            "feature_data": {
                "type": "object",
                "description": "Feature data to update"
            }
        },
        "required": ["feature_id", "feature_data"]
    }
)
def update_feature(feature_id: str, feature_data: Dict[str, Any]) -> Any:
    """Update a feature."""
    return feature_service.update_feature(feature_id, feature_data)


@tool_registry.register_tool(
    name="delete_feature",
    description="Delete a feature",
    input_schema={
        "type": "object",
        "properties": {
            "feature_id": {
                "type": "string",
                "description": "Feature ID"
            }
        },
        "required": ["feature_id"]
    }
)
def delete_feature(feature_id: str) -> Any:
    """Delete a feature."""
    return feature_service.delete_feature(feature_id)


@tool_registry.register_tool(
    name="get_feature_children",
    description="Get children features of a feature",
    input_schema={
        "type": "object",
        "properties": {
            "feature_id": {
                "type": "string",
                "description": "Feature ID"
            }
        },
        "required": ["feature_id"]
    }
)
def get_feature_children(feature_id: str) -> Any:
    """Get children features of a feature."""
    return feature_service.get_feature_children(feature_id)


@tool_registry.register_tool(
    name="move_feature",
    description="Move a feature to another parent",
    input_schema={
        "type": "object",
        "properties": {
            "feature_id": {
                "type": "string",
                "description": "Feature ID to move"
            },
            "new_parent_id": {
                "type": "string",
                "description": "ID of the new parent feature or story"
            }
        },
        "required": ["feature_id", "new_parent_id"]
    }
)
def move_feature(feature_id: str, new_parent_id: str) -> Any:
    """Move a feature to another parent."""
    return feature_service.move_feature(feature_id, new_parent_id)


# ===== ACTOR MANAGEMENT TOOLS =====

@tool_registry.register_tool(
    name="add_actor",
    description="Add an actor to a project",
    input_schema={
        "type": "object",
        "properties": {
            "project_id": {
                "type": "string",
                "description": "Project ID"
            },
            "actor_data": {
                "type": "object",
                "description": "Actor data to add"
            }
        },
        "required": ["project_id", "actor_data"]
    }
)
def add_actor(project_id: str, actor_data: Dict[str, Any]) -> Any:
    """Add an actor to a project."""
    return actor_service.add_actor(project_id, actor_data)


@tool_registry.register_tool(
    name="add_story_to_actor",
    description="Add a story to an actor",
    input_schema={
        "type": "object",
        "properties": {
            "project_id": {
                "type": "string",
                "description": "Project ID"
            },
            "actor_name": {
                "type": "string",
                "description": "Actor name"
            },
            "story_data": {
                "type": "object",
                "description": "Story data to add"
            }
        },
        "required": ["project_id", "actor_name", "story_data"]
    }
)
def add_story_to_actor(project_id: str, actor_name: str, story_data: Dict[str, Any]) -> Any:
    """Add a story to an actor."""
    return actor_service.add_story_to_actor(project_id, actor_name, story_data)


@tool_registry.register_tool(
    name="get_project_actors",
    description="Get actors of a project",
    input_schema={
        "type": "object",
        "properties": {
            "project_id": {
                "type": "string",
                "description": "Project ID"
            }
        },
        "required": ["project_id"]
    }
)
def get_project_actors(project_id: str) -> Any:
    """Get actors of a project."""
    return actor_service.get_project_actors(project_id)


@tool_registry.register_tool(
    name="get_actor",
    description="Get an actor by ID",
    input_schema={
        "type": "object",
        "properties": {
            "project_id": {
                "type": "string",
                "description": "Project ID"
            },
            "actor_id": {
                "type": "string",
                "description": "Actor ID"
            }
        },
        "required": ["project_id", "actor_id"]
    }
)
def get_actor(project_id: str, actor_id: str) -> Any:
    """Get an actor by ID."""
    return actor_service.get_actor(project_id, actor_id)


@tool_registry.register_tool(
    name="update_actor",
    description="Update an actor",
    input_schema={
        "type": "object",
        "properties": {
            "project_id": {
                "type": "string",
                "description": "Project ID"
            },
            "actor_id": {
                "type": "string",
                "description": "Actor ID"
            },
            "actor_data": {
                "type": "object",
                "description": "Actor data to update"
            }
        },
        "required": ["project_id", "actor_id", "actor_data"]
    }
)
def update_actor(project_id: str, actor_id: str, actor_data: Dict[str, Any]) -> Any:
    """Update an actor."""
    return actor_service.update_actor(project_id, actor_id, actor_data)


@tool_registry.register_tool(
    name="delete_actor",
    description="Delete an actor",
    input_schema={
        "type": "object",
        "properties": {
            "project_id": {
                "type": "string",
                "description": "Project ID"
            },
            "actor_id": {
                "type": "string",
                "description": "Actor ID"
            }
        },
        "required": ["project_id", "actor_id"]
    }
)
def delete_actor(project_id: str, actor_id: str) -> Any:
    """Delete an actor."""
    return actor_service.delete_actor(project_id, actor_id)


@tool_registry.register_tool(
    name="get_actor_stories",
    description="Get stories of an actor",
    input_schema={
        "type": "object",
        "properties": {
            "project_id": {
                "type": "string",
                "description": "Project ID"
            },
            "actor_id": {
                "type": "string",
                "description": "Actor ID"
            }
        },
        "required": ["project_id", "actor_id"]
    }
)
def get_actor_stories(project_id: str, actor_id: str) -> Any:
    """Get stories of an actor."""
    return actor_service.get_actor_stories(project_id, actor_id)


logger.info(f"Registered {len(tool_registry.get_tool_names())} tools")
