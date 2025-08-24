#!/usr/bin/env python3
"""Simple script to test MCP tools endpoint."""

import requests
import json

def test_mcp_tools():
    """Test the MCP tools/list endpoint."""
    url = "http://localhost:5000/mcp"
    headers = {
        "Content-Type": "application/json",
        "x-mcp-key": "test_api_key_123"
    }
    
    payload = {
        "method": "tools/list",
        "id": 1
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        result = response.json()
        
        if "result" in result and "tools" in result["result"]:
            tools = result["result"]["tools"]
            print(f"✅ Found {len(tools)} tools:")
            
            # Group tools by category
            categories = {
                "Project Management": [],
                "Diagram Management": [],
                "Story Management": [],
                "Feature Management": [],
                "Actor Management": [],
                "Utility Tools": []
            }
            
            for tool in tools:
                name = tool["name"]
                if any(x in name for x in ["project", "feature_types", "normalize"]):
                    categories["Project Management"].append(name)
                elif "diagram" in name:
                    categories["Diagram Management"].append(name)
                elif "story" in name:
                    categories["Story Management"].append(name)
                elif "feature" in name:
                    categories["Feature Management"].append(name)
                elif "actor" in name:
                    categories["Actor Management"].append(name)
                else:
                    categories["Utility Tools"].append(name)
            
            for category, tool_names in categories.items():
                if tool_names:
                    print(f"\n📁 {category} ({len(tool_names)} tools):")
                    for tool_name in sorted(tool_names):
                        print(f"   • {tool_name}")
        else:
            print("❌ Unexpected response format")
            print(json.dumps(result, indent=2))
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
    except json.JSONDecodeError as e:
        print(f"❌ JSON decode error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    test_mcp_tools()
