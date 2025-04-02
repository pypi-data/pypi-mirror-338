from dataclasses import dataclass
from typing import Literal


@dataclass
class AgentToolCallFunction:
    arguments: str
    """String representation of the arguments for the tool call function."""

    name: str
    """The name of the tool call function."""


@dataclass
class AgentToolCall:
    id: str
    """Unique identifier of the tool call."""

    function: AgentToolCallFunction
    """Function that the model called."""

    type: str = "function"
    """The type of the tool."""

    index: int | None = None
    """Identifies which function call the delta is for."""

    def __post_init__(self):
        if isinstance(self.function, dict):
            self.function = AgentToolCallFunction(**self.function)


@dataclass
class AgentResponse:
    """Response object from generating response from model."""

    type: Literal["text", "tool"]
    """Specify if it is a natural language or a tool call response."""

    content: str | None = None
    """String output from the model"""

    tool_calls: list[AgentToolCall] | None = None
    """List of tool call objects."""

    def __post_init__(self):
        if self.tool_calls:
            self.tool_calls = [
                (
                    tool_call
                    if isinstance(tool_call, AgentToolCall)
                    else AgentToolCall(**tool_call)
                )
                for tool_call in self.tool_calls
            ]
