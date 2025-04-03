from mcp import ClientSession, StdioServerParameters, Tool
from typing import Literal, Callable
from contextlib import AsyncExitStack
from mcp.client.stdio import stdio_client
from mcp.client.sse import sse_client
from dataclasses import dataclass
from zagen.mcp.server import NativeLambdaMCPServer


@dataclass
class MCPServer:
    """Configuration options for the MCP server"""

    type: Literal["lambda", "sse", "stdio"]
    """Connection type to MCP server."""

    command: str | None = None
    """(For `stdio` type) The command or executable to run to start the MCP server."""

    args: list[str] | None = None
    """(For `stdio` type) Command line arguments to pass to the `command`."""

    url: str | None = None
    """(For `websocket` or `sse` type) The URL to connect to the MCP server."""

    function: list[Callable] | None = None
    """(For `lambda` type) The function to call."""


class MCPClient:
    def __init__(self):
        self.session: ClientSession | None = None
        self.exit_stack = AsyncExitStack()

    async def connect_to_server(self, config: MCPServer):
        """Connect to an MCP server"""

        if config.type == "lambda":
            self.session = NativeLambdaMCPServer(config.function)
        elif config.type == "stdio":
            params = StdioServerParameters(command=config.command, args=config.args)
            stdio_transport = await self.exit_stack.enter_async_context(
                stdio_client(params)
            )
            self.stdio, self.write = stdio_transport
            self.session = await self.exit_stack.enter_async_context(
                ClientSession(self.stdio, self.write)
            )
            await self.session.initialize()
        else:
            stdio_transport = await self.exit_stack.enter_async_context(
                sse_client(config.url)
            )
            self.sse, self.write = stdio_transport
            self.session = await self.exit_stack.enter_async_context(
                ClientSession(self.sse, self.write)
            )
            await self.session.initialize()

    async def cleanup(self):
        """Clean up resources"""
        await self.exit_stack.aclose()


@dataclass
class MultiMCPClient:
    """Result from initialising MCP servers"""

    clients: dict[str, MCPClient] | None = None
    """A dictionary mapping server names to their corresponding `MCPClient` instances."""

    tools: dict[str, Tool] | None = None
    """A dictionary mapping tool names to `Tool` instances registered with the MCP servers."""

    tool_client_mapping: dict[str, str] | None = None
    """A dictionary mapping tool names to the corresponding MCP server names."""
