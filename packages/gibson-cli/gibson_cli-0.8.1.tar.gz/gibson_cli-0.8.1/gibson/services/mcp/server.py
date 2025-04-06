from typing import Dict, List

from mcp.server.fastmcp import FastMCP

from gibson.api.ProjectApi import ProjectApi
from gibson.core.Configuration import Configuration

mcp = FastMCP("GibsonAI")

project_api = ProjectApi(Configuration())

# Note: Resources are not yet supported by Cursor, everything must be implemented as a tool
# See https://docs.cursor.com/context/model-context-protocol#limitations


@mcp.tool()
def get_projects() -> List[Dict]:
    """Get all GibsonAI projects"""
    return project_api.list()


@mcp.tool()
def create_project() -> Dict:
    """Create a new GibsonAI project"""
    return project_api.create()


@mcp.tool()
def get_project_details(uuid: str) -> Dict:
    """Get a GibsonAI project's details"""
    return project_api.lookup(uuid=uuid)


@mcp.tool()
def get_project_hosted_api_details(uuid: str) -> str:
    """
    Get a GibsonAI project's hosted API details
    This includes necessary context for an LLM to understand and generate API calls related to fetching or modifying the project's data
    """
    return project_api.mcp(uuid=uuid)


@mcp.tool()
def update_project(uuid: str, project_name: str) -> Dict:
    """
    Update a GibsonAI project's details
    This currently only updates the project's name
    Returns the updated project details
    """
    return project_api.update(uuid=uuid, name=project_name)


@mcp.tool()
def submit_data_modeling_request(uuid: str, data_modeling_request: str) -> Dict:
    """
    Submit a data modeling request for a GibsonAI project
    This tool fully handles all data modeling, you should provide the user's request as-is
    Returns the response from the LLM
    """
    return project_api.submit_message(uuid=uuid, message=data_modeling_request)


@mcp.tool()
def deploy_project(uuid: str) -> None:
    """
    Deploy a GibsonAI project's hosted databases
    This deploys both the development and production databases simultaneously and automatically handles the migrations
    """
    project_api.deploy(uuid=uuid)


@mcp.tool()
def get_project_schema(uuid: str) -> str:
    """
    Get the schema for a GibsonAI project
    This includes any changes made to the schema since the last deployment
    """
    return project_api.schema(uuid=uuid)


@mcp.tool()
def get_deployed_schema(uuid: str) -> str:
    """
    Get the deployed schema for a GibsonAI project
    This is the schema that is currently live on the project's hosted databases
    """
    return project_api.database_schema(uuid=uuid)
