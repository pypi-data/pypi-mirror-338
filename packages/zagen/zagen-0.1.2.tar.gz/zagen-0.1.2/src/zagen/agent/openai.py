from dataclasses import dataclass, field
from openai import NotGiven, OpenAI
from zagen.agent.types import AgentToolCall, AgentResponse
from zagen.mcp import MCPServer, MCPClient, MultiMCPClient, mcp_to_openai_tool
from zagen.types import ConversationMessage
from mcp.types import Tool, TextContent
from typing import Any
import json


@dataclass
class OpenAIAgentConfig:
    model: str | None = None
    """model: model name required to pass into openai package model"""

    api_key: str | None = None
    """api_key: api_key required to pass into openai package api_key"""

    base_url: str = "https://api.openai.com"
    """base_url: base_url required to pass into openai package base_url"""

    inference_config: dict[str, Any] = field(
        default_factory=lambda: {
            "max_tokens": 1000,
            "temperature": 0.0,
            "top_p": 0.9,
            "stop_sequences": [],
            "yolo": False,
        }
    )


@dataclass
class OpenAIAgentChatParam:
    inference_config: dict[str, Any] | None = None
    """Additional configurations for the inference."""

    parallel_tool_calls: bool = True
    """Whether model should perform multiple tool calls together."""

    tool_choice: Any | None = None
    """The tool choice for the agent, if any."""


class OpenAIAgent:
    """OpenAIAgent - agent connected with mcp tools

    Args:
        - name: str = "Agent Name"
        - instructions: list[str] = list of instructions inserted as role: system on top of the prompt

    Example:
    triage_agent = OpenAIAgent(
        name="Triage Agent",
        instructions=[
            "You are a friendly assistant",
            "Answer users' query"
        ],
        mcp={
            "jira": MCPServer("sse", url="https://mcp.com/mcp/jira/sse"),
            "slack": MCPServer("stdio", command="uvx ..."),
            "local_toolset": MCPServer("func", functions=[
                get_weather,
                get_calendar_events,
                get_recent_deployments,
            ])
        },
        config=OpenAIAgentConfig(
            model="gpt-4o",
            base_url="",
            api_key="",
        )
    )
    """

    def __init__(
        self,
        name: str,
        instructions: list[str],
        mcp: dict[str, MCPServer],
        config: OpenAIAgentConfig,
    ) -> None:
        self.name = name
        self.instructions = instructions
        self.model = config.model
        self.inference_config = config.inference_config
        self.client = OpenAI(api_key=config.api_key, base_url=config.base_url)
        self.mcp_servers = mcp
        self.multi_mcp_clients = MultiMCPClient()
        self.tools: list[dict[str, any]] = []

        self.messages: list[ConversationMessage] = [
            ConversationMessage(role="system", content=instruction)
            for instruction in instructions
        ]

    async def connect_to_mcp_servers(self) -> None:
        """Initialise MCP servers.

        Args:
            servers (dict[str, MCPServer]): List of MCP servers.

        Returns:
            tuple[dict[str, MCPClient], dict[str, Tool], dict[str, str]]: Response as tuple.
        """
        mcp_clients: dict[str, MCPClient] = {}
        mcp_tools: dict[str, Tool] = {}
        tool_client_mapping: dict[str, str] = {}
        for server_name, config in self.mcp_servers.items():
            try:
                mcp_client = MCPClient()
                await mcp_client.connect_to_server(config)
                list_tools_result = await mcp_client.session.list_tools()
                mcp_clients[server_name] = mcp_client
                for tool in list_tools_result.tools:
                    toolname = server_name + "_" + tool.name
                    mcp_tools[toolname] = tool
                    tool_client_mapping[toolname] = server_name
            except Exception as e:
                print(f"Unable to connect to MCP server. Skipping. Error: {e}")
        self.multi_mcp_clients = MultiMCPClient(
            mcp_clients, mcp_tools, tool_client_mapping
        )
        self.tools = [
            mcp_to_openai_tool(tool) for tool in self.multi_mcp_clients.tools.values()
        ]
        if mcp_tools:
            print(f"MCP tools loaded: {list(mcp_tools.keys())}")

    async def cleanup_mcp(self):
        """Cleanup MCP connections."""
        for client in list(self.multi_mcp_clients.clients.values())[::-1]:
            await client.cleanup()

    def add_message(self, message: ConversationMessage) -> None:
        self.messages.append(message)

    async def approve(self) -> AgentResponse:
        """Approve function calling to MCP servers"""
        tool_calls = self.messages[-1].tool_calls
        if len(tool_calls) > 0:
            res = []
            for tool_call in tool_calls:
                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)
                server_name = self.multi_mcp_clients.tool_client_mapping[name]
                client = self.multi_mcp_clients.clients[server_name]
                response = await client.session.call_tool(name, args)
                texts = []
                for content in response.content:
                    if isinstance(content, TextContent):
                        texts.append(content.text)
                res.append(
                    AgentResponse(
                        type="tool",
                        content="\n".join(texts),
                    )
                )
                self.add_message(
                    role="tool",
                    content="\n".join(texts),
                    tool_call_id=tool_call.id,
                    sender=self.name,
                )
            return res
        else:
            return AgentResponse(
                type="text", content="No tool executions at the moment."
            )

    async def chat(self, message: str, params: OpenAIAgentChatParam) -> AgentResponse:
        """Add message to the historical conversations"""
        self.add_message(ConversationMessage(role="user", content=message))

        """Update inference config if needed"""
        if params.inference_config:
            self.inference_config = {**self.inference_config, **params.inference_config}

        """Call LLM api"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            tools=self.tools or None,
            tool_choice=params.tool_choice,
            parallel_tool_calls=(
                params.parallel_tool_calls if self.tools else NotGiven()
            ),
            max_tokens=self.inference_config["max_tokens"],
            temperature=self.inference_config["temperature"],
            top_p=self.inference_config["top_p"],
            stop=self.inference_config["stop_sequences"],
        )

        """Convert model response to AgentResponse"""
        message = response.choices[0].message
        if message.tool_calls:
            tool_calls = [
                AgentToolCall(**dict(tool_call)) for tool_call in message.tool_calls
            ]
            self.add_message(
                ConversationMessage(
                    role="assistant",
                    content=message.content,
                    tool_calls=tool_calls,
                    sender=self.name,
                )
            )
            return AgentResponse(
                content=message.content,
                tool_calls=tool_calls,
                type="tool",
            )
        elif message.content:
            self.add_message(
                ConversationMessage(
                    role="assistant",
                    content=message.content,
                    sender=self.name,
                )
            )
            return AgentResponse(content=message.content, type="text")
        else:
            raise ValueError("Unknown message type")
