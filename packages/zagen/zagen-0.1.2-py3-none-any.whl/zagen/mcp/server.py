from abc import ABC, abstractmethod
from mcp import Tool, types
from typing import Any, Callable
from zagen.mcp.utils import function_to_json, function_to_tool


class NativeMCPServer(ABC):
    @abstractmethod
    async def list_tools(self) -> types.ListToolsResult:
        pass

    @abstractmethod
    async def call_tool(
        self, name: str, arguments: dict[str, Any] | None = None
    ) -> types.CallToolResult:
        pass


class NativeLambdaMCPServer(NativeMCPServer):
    def __init__(self, function: list[Callable]) -> None:
        self.func = [function_to_json(fn) for fn in function]
        self.tools: list[Tool] = [function_to_tool(fn) for fn in function]
        self.tools_map = {
            fn["function"]["name"]: fn["function"]["call"] for fn in self.func
        }

    async def list_tools(self) -> types.ListToolsResult:
        return types.ListToolsResult(tools=self.tools)

    async def call_tool(
        self, name: str, arguments: dict[str, Any] | None = None
    ) -> types.CallToolResult:
        try:
            return types.CallToolResult(
                content=[
                    types.TextContent(
                        type="text",
                        text=str(self.tools_map[name](**arguments)),
                    )
                ],
            )
        except Exception as e:
            return types.CallToolResult(
                content=[
                    types.TextContent(
                        type="text",
                        text=str(e),
                    )
                ],
                isError=True,
            )
