#!/usr/bin/env python3
"""Test script to count registered MCP tools."""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from mcp_server.tools import tool_registry
    
    tool_names = tool_registry.get_tool_names()
    print(f"Total tools registered: {len(tool_names)}")
    print("\nRegistered tools:")
    for i, tool_name in enumerate(sorted(tool_names), 1):
        print(f"{i:2d}. {tool_name}")
        
except Exception as e:
    print(f"Error importing tools: {e}")
    sys.exit(1)
