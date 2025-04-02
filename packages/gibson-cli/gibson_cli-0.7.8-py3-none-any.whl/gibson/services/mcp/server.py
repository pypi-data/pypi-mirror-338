import os

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("GibsonAI")

# Note: Resources are not yet supported by Cursor, everything must be implemented as a tool


@mcp.tool()
def get_project_name() -> str:
    """Get the gibson project name"""
    return os.environ.get("GIBSONAI_PROJECT")
