"""Centralized configuration settings for MCP Server."""

import os
from typing import Optional
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings with validation."""
    
    # API Configuration
    api_key: str = Field(..., env="API_KEY", description="API key for authentication")
    api_key_header_name: str = Field(default="x-mcp-key", description="API key header name")
    
    # HyperManager API Configuration
    google_api_key: str = Field(..., env="GOOGLE_API_KEY", description="Google API key")
    base_url: str = Field(..., env="BASE_URL", description="HyperManager API base URL")
    
    # Server Configuration
    host: str = Field(default="0.0.0.0", description="Server host")
    port: int = Field(default=5000, description="Server port")
    reload: bool = Field(default=True, description="Enable auto-reload in development")
    
    # CORS Configuration
    cors_origins: list[str] = Field(default=["*"], description="Allowed CORS origins")
    cors_credentials: bool = Field(default=True, description="Allow credentials in CORS")
    cors_methods: list[str] = Field(default=["*"], description="Allowed CORS methods")
    cors_headers: list[str] = Field(default=["*"], description="Allowed CORS headers")
    
    # MCP Configuration
    mcp_protocol_version: str = Field(default="2024-11-05", description="MCP protocol version")
    server_name: str = Field(default="project-backlog-mcp-server", description="MCP server name")
    server_version: str = Field(default="1.0.0", description="MCP server version")
    server_description: str = Field(
        default="Serveur MCP pour la gestion des projets et diagrammes via HyperManager API",
        description="MCP server description"
    )
    
    # Logging Configuration
    log_level: str = Field(default="INFO", description="Logging level")
    log_format: str = Field(
        default="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        description="Log format"
    )
    
    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Global settings instance
settings = Settings()
