import asyncio
from pprint import pprint
from typing import Any, Dict, List, Optional

from mcp.client.session import ClientSession
from mcp.client.sse import sse_client
from mcp.types import (
    BlobResourceContents,
    EmbeddedResource,
    ImageContent,
    TextContent,
    TextResourceContents,
)

from .tool import Tool
from .tool_registry import ToolRegistry


class MCPToolWrapper:
    """Wrapper class providing both async and sync versions of MCP tool calls."""

    def __init__(self, url: str, name: str, params: Optional[List[str]]) -> None:
        self.url = url
        self.name = name
        self.params = params

    def _process_args(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        """Process positional and keyword arguments.
        Maps positional args to parameter names and validates input.
        Returns processed kwargs.
        """
        if args:
            if not self.params:
                raise ValueError("Tool parameters not initialized")
            if len(args) > len(self.params):
                raise TypeError(
                    f"Expected at most {len(self.params)} positional arguments, got {len(args)}"
                )
            # Map positional args to their corresponding parameter names
            for i, arg in enumerate(args):
                param_name = self.params[i]
                if param_name in kwargs:
                    raise TypeError(
                        f"Parameter '{param_name}' passed both as positional and keyword argument"
                    )
                kwargs[param_name] = arg
        return kwargs

    def call_sync(self, *args: Any, **kwargs: Any) -> Any:
        """Synchronous implementation of MCP tool call.
        Handles both positional and keyword arguments.
        Positional args are mapped to params in order, keyword args are passed directly.
        """
        kwargs = self._process_args(*args, **kwargs)

        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        return loop.run_until_complete(self.call_async(**kwargs))

    async def call_async(self, *args: Any, **kwargs: Any) -> Any:
        """Async implementation of MCP tool call.
        Handles both positional and keyword arguments.
        Positional args are mapped to params in order, keyword args are passed directly.
        """
        kwargs = self._process_args(*args, **kwargs)

        if not self.url or not self.name:
            raise ValueError("URL and name must be set before calling")

        try:
            async with sse_client(self.url) as (read_stream, write_stream):
                async with ClientSession(read_stream, write_stream) as session:
                    await session.initialize()
                    tools = await session.list_tools()
                    tool = next((t for t in tools.tools if t.name == self.name), None)
                    if not tool:
                        raise ValueError(f"Tool {self.name} not found on server")

                    validated_params = {}
                    for param_name, _ in tool.inputSchema.get("properties", {}).items():
                        if param_name in kwargs:
                            validated_params[param_name] = kwargs[param_name]

                    result = await session.call_tool(self.name, validated_params)
                    return self._post_process_result(result)
        except Exception as e:
            print(f"Error calling tool {self.name}: {str(e)}")
            raise

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the wrapper directly callable, using sync version by default."""
        return self.call_sync(*args, **kwargs)

    async def __acall__(self, *args: Any, **kwargs: Any) -> Any:
        """Async version of __call__, allows await wrapper() syntax.
        Simply delegates to call_async which now handles all parameter processing.
        """
        return await self.call_async(*args, **kwargs)

    def _post_process_result(self, result: Any) -> Any:
        """Post-process the result from an MCP tool call.
        If result is not an error and contains content, processes each content item.
        Returns a single value if only one processed output exists, otherwise returns a list.
        """
        if result.isError or not result.content:
            return result

        def process_text(content: TextContent) -> str:
            return content.text

        def process_image(content: ImageContent) -> dict:
            return {
                "type": "image",
                "data": content.data,
                "mimeType": content.mimeType,
            }

        def process_embedded(content: EmbeddedResource) -> Any:
            if isinstance(content.resource, TextResourceContents):
                return content.resource.text
            elif isinstance(content.resource, BlobResourceContents):
                return {
                    "type": "blob",
                    "data": content.resource.blob,
                    "mimeType": content.resource.mimeType,
                }
            return content

        handlers = {
            TextContent: process_text,
            ImageContent: process_image,
            EmbeddedResource: process_embedded,
        }

        processed = [
            handlers.get(type(content), lambda x: x)(content)
            for content in result.content
        ]

        return processed[0] if len(processed) == 1 else processed


class MCPTool(Tool):
    """Wrapper class for MCP tools that preserves original function metadata."""

    @classmethod
    def from_tool_json(
        cls,
        name: str,
        description: str,
        input_schema: Dict[str, Any],
        url: str,
    ) -> "MCPTool":
        """Create an MCPToolWrapper from a function."""
        wrapper = MCPToolWrapper(
            url=url,
            name=name,
            params=(
                list(input_schema.get("properties", {}).keys()) if input_schema else []
            ),
        )
        return cls(
            name=name,
            description=description,
            parameters=input_schema,
            callable=wrapper,
            is_async=False,
        )


class MCPIntegration:
    """Handles integration with MCP server for tool registration."""

    def __init__(self, registry: ToolRegistry):
        self.registry = registry

    async def register_mcp_tools_async(self, server_url: str) -> None:
        """
        Async implementation to register all tools from an MCP server.

        Args:
            server_url (str): URL of the MCP server (e.g. "http://localhost:8000/mcp/sse")
        """
        print(f"Connecting to MCP server at {server_url}")

        async with sse_client(server_url) as (read_stream, write_stream):
            async with ClientSession(read_stream, write_stream) as session:
                print("Connected to server, initializing session...")
                await session.initialize()

                # Get available tools from server
                tools_response = await session.list_tools()
                print(f"Found {len(tools_response.tools)} tools on server")

                # Register each tool with a wrapper function
                for tool in tools_response.tools:
                    # pprint(tool)
                    mcptool_from_json = MCPTool.from_tool_json(
                        name=tool.name,
                        description=tool.description or "",
                        input_schema=tool.inputSchema,
                        url=server_url,
                    )

                    # Register the tool wrapper function
                    self.registry.register(mcptool_from_json)
                    # print(f"Registered tool: {tool.name}")

    def register_mcp_tools(self, server_url: str) -> None:
        """
        Register all tools from an MCP server (synchronous entry point).

        Args:
            server_url (str): URL of the MCP server
        """
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        if loop.is_running():
            # if event loop is already running, use run_coroutine_threadsafe
            future = asyncio.run_coroutine_threadsafe(
                self.register_mcp_tools_async(server_url), loop
            )
            return future.result()
        else:
            return loop.run_until_complete(self.register_mcp_tools_async(server_url))
