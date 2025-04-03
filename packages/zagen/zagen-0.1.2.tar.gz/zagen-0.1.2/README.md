![zagen](./asset/zagen.png)

Accessible and customizable agent components that you can copy and paste into your apps. Free. Open Source. Use this to build your own agentic workflows.

### 👉 Getting Started

#### Install using uv:

```bash
uv add zagen
```

#### Install using pip:

```bash
pip install zagen
```

### 🤩 Feel The Magic

```python
from zagen.agent import OpenAIAgent, OpenAIAgentConfig
from zagen.mcp import MCPServer

def get_weather(loc: str) -> Literal["Sunny", "Cloudy", "Rainy"]:
    """Get the weather of current locations"""
    return "Sunny"

triage_agent = OpenAIAgent(
    name="Triage Agent",
    instructions="""You are the Triage Agent.
    """,
    mcp={
        "weather": MCPServer(
            type="lambda",
            function=[get_weather],
        ),
        "slack": MCPServer(
            type="sse",
            url="https://"
        ),
    },
    config=OpenAIAgentConfig(
        model="gpt-4o",
        base_url="",
        api_key="",
    ),
)
```
