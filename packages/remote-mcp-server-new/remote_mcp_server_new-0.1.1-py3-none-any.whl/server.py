from typing import Callable, Any, Dict
from .config import Config, ResourceModel, Tool, PromptModel, ToolCall, PromptRequest, ArgumentModel
from mcp.types import Resource, ReadResourceResult, ListPromptsResult, Prompt, PromptArgument, PromptMessage, ServerCapabilities, TextContent, TextResourceContents
from fastapi import FastAPI
from .logger import get_logger

logger = get_logger(__name__)

class MCPServer:
    """
    Server implementation for Model Control Protocol (MCP).
    Manages tools, resources, and prompts with a FastAPI interface.
    """
    def __init__(self, config: Config):
        """Initialize the MCP server with configuration."""
        self.tools: Dict[str, Tool] = {}
        self.resources: Dict[str, ResourceModel] = {}
        self.prompts: Dict[str, PromptModel] = {}
        self.config = config
        logger.info(f"Initializing MCP server with name: {config.name}, version: {config.version}")
        self.app = FastAPI()

    def add_tool(self, name: str, description: str, input_schema: dict[str, Any], fn: Callable[..., Any]) -> Tool:
        """
        Register a tool with the server.
        
        Args:
            name: Tool name
            description: Tool description
            input_schema: JSON schema for tool input
            fn: Function to execute when tool is called
        """
        existing = self.tools.get(name)
        if existing:
            if self.config.warn_on_duplicates:
                logger.warning(f"Tool already exists: {name}")
            return existing

        tool = Tool(name=name, description=description, input_schema=input_schema, fn=fn)
        self.tools[name] = tool
        logger.info(f"Added tool: {name}")
        return tool

    def list_tools(self) -> list[Tool]:
        """Get all registered tools."""
        logger.debug(f"Listing {len(self.tools)} tools")
        return list(self.tools.values())

    async def call_tool(self, name: str, arguments: Dict[str, Any]) -> Any:
        """
        Execute a tool with the given arguments.
        
        Args:
            name: Tool name to call
            arguments: Arguments to pass to the tool
        """
        tool = self.tools.get(name)
        if not tool:
            logger.error(f"Unknown tool requested: {name}")
            raise Exception(f"Unknown Tool: {name}")

        logger.info(f"Calling tool: {name}")
        try:
            result = await tool.fn(**arguments)
            logger.debug(f"Tool {name} executed successfully")
            return result
        except Exception as e:
            logger.error(f"Error executing tool {name}: {e}")
            raise

    def add_resource(self, resource: ResourceModel):
        """
        Register a resource with the server.
        
        Args:
            resource: Resource model to register
        """
        existing = self.resources.get(resource.uri)
        if existing:
            if self.config.warn_on_duplicates:
                logger.warning(f"Resource already exists: {resource.uri}")
            return existing
        
        self.resources[resource.uri] = resource
        logger.info(f"Added resource: {resource.name} ({resource.uri})")
        return resource

    def list_resources(self) -> list[Resource]:
        """Get all registered resources."""
        resources: list[Resource] = []

        for r in self.resources.values():
            resources.extend(r.list_fn())

        logger.debug(f"Listing {len(resources)} resources")
        return resources
    
    async def read_sources(self, uri: str) -> list[ReadResourceResult]:
        """
        Read a resource by URI.
        
        Args:
            uri: Resource URI to read
        """
        resource = self.resources.get(uri)
        if not resource:
            logger.error(f"Resource not found: {uri}")
            raise ValueError(f"Resource doesn't exist: {uri}")
        
        logger.info(f"Reading resource: {uri}")
        try:
            result = await resource.read_fn(uri)
            logger.debug(f"Resource {uri} read successfully")
            return result
        except Exception as e:
            logger.error(f"Error reading resource {uri}: {e}")
            raise
    
    def add_prompt(self, prompt: PromptModel):
        """
        Register a prompt with the server.
        
        Args:
            prompt: Prompt model to register
        """
        existing = self.prompts.get(prompt.name)
        if existing:
            if self.config.warn_on_duplicates:
                logger.warning(f"Prompt already exists: {prompt.name}")
            return existing
        
        self.prompts[prompt.name] = prompt
        logger.info(f"Added prompt: {prompt.name}")
        return prompt
    
    def list_prompts(self) -> ListPromptsResult:
        """Get all registered prompts."""
        prompts = [
            Prompt(
                name=p.name,
                description=p.description,
                arguments=[
                    PromptArgument(
                        name=a.name,
                        description=a.description,
                        required=a.required
                    ) for a in p.arguments
                ]
            ) for p in self.prompts.values()
        ]
        
        logger.debug(f"Listing {len(prompts)} prompts")
        return ListPromptsResult(prompts=prompts)

    def get_prompt(self, name: str, arguments: Dict[str, str]) -> list[PromptMessage]:
        """
        Get a prompt with the given arguments.
        
        Args:
            name: Prompt name
            arguments: Arguments to pass to the prompt
        """
        prompt = self.prompts.get(name)
        if not prompt:
            logger.error(f"Prompt not found: {name}")
            raise ValueError(f"Prompt doesn't exist: {name}")
        
        logger.info(f"Getting prompt: {name}")
        try:
            updated_prompt = prompt.prompt_fn(arguments)
            logger.debug(f"Generated prompt {name} with {len(updated_prompt)} messages")
            return updated_prompt
        except Exception as e:
            logger.error(f"Error generating prompt {name}: {e}")
            raise
    
    def start_server(self):
        """Configure and start the FastAPI server."""
        logger.info("Starting MCP server")
        
        @self.app.get("/tools/list")
        def list_tools():
            """API endpoint to list tools."""
            logger.info("API: List tools request")
            res = self.list_tools()
            return {
                "data": [r.model_dump(exclude={"fn": True}) for r in res]
            }
        
        @self.app.post("/tools/call")
        async def call_tool(data: ToolCall):
            """API endpoint to call a tool."""
            logger.info(f"API: Call tool request for {data.name}")
            res = await self.call_tool(data.name, data.arguments)
            return {
                "data": res
            }
        
        @self.app.get("/resources/list")
        def list_resources():
            """API endpoint to list resources."""
            logger.info("API: List resources request")
            res = self.list_resources()
            return {
                "data": [r.model_dump() for r in res]
            }
        
        @self.app.get("/resources/read")
        async def read_sources(uri: str):
            """API endpoint to read a resource."""
            logger.info(f"API: Read resource request for {uri}")
            res = await self.read_sources(uri)
            return {
                "data": [r.model_dump() for r in res]
            }
        
        @self.app.get("/prompts/list")
        def list_prompts():
            """API endpoint to list prompts."""
            logger.info("API: List prompts request")
            res = self.list_prompts()
            return {
                "data": res.model_dump()
            }
        
        @self.app.post("/prompts/get")
        def get_prompt(data: PromptRequest):
            """API endpoint to get a prompt."""
            logger.info(f"API: Get prompt request for {data.name}")
            res = self.get_prompt(data.name, data.arguments)
            logger.debug(f"Prompt result: {res}")
            return {
                "data": [r.model_dump() for r in res]
            }
        
        logger.info("MCP server endpoints configured")
        return self.app