import inspect
from mcp.types import Tool
from typing import Callable


def mcp_to_openai_tool(tool: Tool) -> dict[str, any]:
    """Convert MCP tool to openai format.

    Args:
        tool (Tool): MCP Tool object.

    Returns:
        dict[str, any]: A dictionary representing tool in JSON format.
    """
    return {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description,
            "parameters": tool.inputSchema,
        },
    }


def function_to_json(func: Callable) -> dict:
    """
    Converts a Python function into a JSON-serializable dictionary
    that describes the function's signature, including its name,
    description, and parameters.

    Compatible with OpenAI tool definition.

    Args:
        func: The function to be converted.

    Returns:
        A dictionary representing the function's signature in JSON format.
    """
    type_map = {
        str: "string",
        int: "integer",
        float: "number",
        bool: "boolean",
        list: "array",
        dict: "object",
        type(None): "null",
    }

    try:
        signature = inspect.signature(func)
    except ValueError as e:
        raise ValueError(
            f"Failed to get signature for function {func.__name__}: {str(e)}"
        )

    parameters = {}
    for param in signature.parameters.values():
        try:
            param_type = type_map.get(param.annotation, "string")
        except KeyError as e:
            raise KeyError(
                f"Unknown type annotation {param.annotation} for parameter {param.name}: {str(e)}"
            )
        parameters[param.name] = {"type": param_type}

    required = [
        param.name
        for param in signature.parameters.values()
        if param.default == inspect._empty
    ]

    return {
        "type": "function",
        "function": {
            "call": func,
            "name": func.__name__,
            "description": func.__doc__ or "",
            "parameters": {
                "type": "object",
                "properties": parameters,
                "required": required,
            },
        },
    }


def function_to_tool(func: Callable) -> Tool:
    fn = function_to_json(func)["function"]
    return Tool(
        name=fn["name"], description=fn["description"], inputSchema=fn["parameters"]
    )
