from zagen.agent import OpenAIAgent, OpenAIAgentConfig
from zagen.mcp import MCPServer
from zagen.mcp.server import NativeLambdaMCPServer


from typing import Literal
import asyncio


def get_weather(loc: str) -> Literal["Sunny", "Cloudy", "Rainy"]:
    """Get the weather of current locations"""
    return "Sunny: " + loc


triage_agent = OpenAIAgent(
    name="Triage Agent",
    instructions="""
    You are the Triage Agent. Your role is to assist customers by identifying their needs and routing them to the correct agent:
    - **Food Ordering** (`to_food_order`): For menu recommendations, adding/removing items, viewing or modifying the cart.
    - **Payment** (`to_payment`): For payments, payment method queries, receipts, or payment issues.
    - **Feedback** (`to_feedback`): For reviews, ratings, comments, or complaints.
    If unsure, guide customers by explaining options (ordering, payment, feedback). For multi-step needs, start with the immediate priority and redirect after.
    Always ensure clear, polite, and accurate communication during handoffs.
    """,
    mcp={
        "weather": MCPServer(
            type="lambda",
            function=[get_weather],
        ),
    },
    config=OpenAIAgentConfig(
        model="",
        base_url="",
        api_key="",
    ),
)


async def main():
    await triage_agent.connect_to_mcp_servers()
    x = triage_agent.multi_mcp_clients
    print(x)


asyncio.run(main())
