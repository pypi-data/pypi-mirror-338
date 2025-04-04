from .config import ClientConfig
from .helper import _convert_to_content, _convert_to_prompt_message_content, _convert_to_read_resource
from mcp.server.lowlevel.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, Prompt, Resource, PromptMessage, PromptArgument, GetPromptResult
from mcp.server.lowlevel.helper_types import ReadResourceContents
from typing import Any, Optional
import requests
import json
import logging

class MCPClient:
    """
    Client for communicating with an MCP server over HTTP.
    Handles serialization and deserialization of MCP protocol objects.
    """
    
    def __init__(self, config: ClientConfig, logger: Optional[logging.Logger] = None):
        """
        Initialize the MCP client.
        
        Args:
            config: Configuration for the client
            logger: Optional logger instance for logging
        """
        self.config = config
        self.logger = logger or logging.getLogger(__name__)
        self.server = Server("Remote MCP Client")
        self.setup_handlers()
        self.logger.info(f"Initialized MCP client for server: {self.config.get('server_url')}")

    async def run(self):
        """Start the client and connect to the stdio server."""
        self.logger.info("Starting MCP client")
        try:
            async with stdio_server() as (read_stream, write_stream):
                self.logger.info("Connected to stdio server")
                await self.server.run(
                    read_stream,
                    write_stream,
                    self.server.create_initialization_options(),
                )
        except Exception as e:
            self.logger.error(f"Error running MCP client: {e}")
            raise

    def setup_handlers(self):
        """Register handlers for MCP protocol operations."""
        self.logger.debug("Setting up protocol handlers")
        self.server.list_tools()(self.list_tools)
        self.server.call_tool()(self.call_tool)
        self.server.list_resources()(self.list_resources)
        self.server.list_prompts()(self.list_prompts)
        self.server.read_resource()(self.read_resource)
        self.server.get_prompt()(self.get_prompt)

    def _call_get_api(self, slug) -> Any:
        """
        Make a GET request to the MCP server.
        
        Args:
            slug: API endpoint path
            
        Returns:
            Parsed JSON response
        """
        url = f"{self.config.get('server_url')}{slug}"
        self.logger.debug(f"GET request to: {url}")
        try:
            res = requests.get(url)
            res.raise_for_status()
            return res.json()
        except requests.RequestException as e:
            self.logger.error(f"API request failed: {e}")
            raise
    
    def _call_post_api(self, slug: str, data: Any) -> Any:
        """
        Make a POST request to the MCP server.
        
        Args:
            slug: API endpoint path
            data: Request payload
            
        Returns:
            Parsed JSON response
        """
        url = f"{self.config.get('server_url')}{slug}"
        self.logger.debug(f"POST request to: {url}")
        try:
            res = requests.post(
                url, 
                data=data, 
                headers={"content-type": "application/json"}
            )
            res.raise_for_status()
            return res.json()
        except requests.RequestException as e:
            self.logger.error(f"API request failed: {e}")
            raise

    async def list_tools(self) -> list[Tool]:
        """Get available tools from the server."""
        self.logger.info("Listing available tools")
        try:
            response = self._call_get_api("/tools/list")
            tools = [
                Tool(
                    name=r["name"],
                    description=r["description"],
                    inputSchema=r["input_schema"]
                )
                for r in response["data"]
            ]
            self.logger.info(f"Found {len(tools)} tools")
            return tools
        except Exception as e:
            self.logger.error(f"Error listing tools: {e}")
            raise
    
    async def call_tool(self, name: str, arguments: dict[str, Any]) -> Any:
        """
        Call a tool on the server with arguments.
        
        Args:
            name: Tool name
            arguments: Tool arguments
            
        Returns:
            Tool execution result
        """
        self.logger.info(f"Calling tool: {name}")
        try:
            response = self._call_post_api(
                "/tools/call", 
                data=json.dumps({
                    "name": name,
                    "arguments": arguments
                })
            )
            self.logger.debug(f"Tool response received")
            return _convert_to_content(response["data"])
        except Exception as e:
            self.logger.error(f"Error calling tool {name}: {e}")
            raise
    
    async def list_resources(self) -> list[Resource]:
        """Get available resources from the server."""
        self.logger.info("Listing available resources")
        try:
            response = self._call_get_api("/resources/list")
            resources = [
                Resource(
                    name=r["name"],
                    description=r["description"],
                    uri=r["uri"],
                    mimeType=r["mimeType"],
                    size=r["size"]
                )
                for r in response["data"]
            ]
            self.logger.info(f"Found {len(resources)} resources")
            return resources
        except Exception as e:
            self.logger.error(f"Error listing resources: {e}")
            raise
    
    async def read_resource(self, uri: str) -> list[ReadResourceContents]:
        """
        Read a resource from the server.
        
        Args:
            uri: Resource URI
            
        Returns:
            Resource contents
        """
        self.logger.info(f"Reading resource: {uri}")
        try:
            response = self._call_get_api(f"/resources/read?uri={uri}")
            resources = [
                item
                for r in response["data"]
                for resource in r["contents"]
                for item in _convert_to_read_resource(resource)
            ]
            self.logger.debug(f"Received {len(resources)} resource items")
            return resources
        except Exception as e:
            self.logger.error(f"Error reading resource {uri}: {e}")
            raise
    
    async def list_prompts(self) -> list[Prompt]:
        """Get available prompts from the server."""
        self.logger.info("Listing available prompts")
        try:
            response = self._call_get_api("/prompts/list")
            prompts = [
                Prompt(
                    name=r["name"],
                    description=r["description"],
                    arguments=[
                        PromptArgument(
                            name=arg["name"],
                            description=arg["description"],
                            required=arg["required"],
                        )
                        for arg in (r["arguments"] or [])
                    ]
                )
                for r in response["data"]["prompts"]
            ]
            self.logger.info(f"Found {len(prompts)} prompts")
            return prompts
        except Exception as e:
            self.logger.error(f"Error listing prompts: {e}")
            raise
    
    async def get_prompt(self, name: str, arguments: dict[str, Any]) -> GetPromptResult:
        """
        Get a prompt from the server.
        
        Args:
            name: Prompt name
            arguments: Prompt arguments
            
        Returns:
            Prompt messages
        """
        self.logger.info(f"Getting prompt: {name}")
        try:
            response = self._call_post_api(
                "/prompts/get", 
                json.dumps({
                    "name": name,
                    "arguments": arguments
                })
            )
            prompts = [
                PromptMessage(
                    role=r["role"],
                    content=_convert_to_prompt_message_content(r["content"])
                )
                for r in response["data"]
            ]
            self.logger.debug(f"Received {len(prompts)} prompt messages")
            return GetPromptResult(messages=prompts)
        except Exception as e:
            self.logger.error(f"Error getting prompt {name}: {e}")
            raise