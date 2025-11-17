import json
import os
from typing import Any, Dict, TypeVar

import requests
from langchain_aws import ChatBedrockConverse
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool

# from langchain_openai import ChatOpenAI
from langgraph.graph import END, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode
from pydantic import BaseModel, Field

StateType = TypeVar("StateType", bound=Dict[str, Any])


class GitHubConfig(BaseModel):
    """Configuration for GitHub API access"""

    api_base_url: str = Field(
        default="https://api.github.com", description="GitHub API base URL"
    )


def get_session(token: str) -> requests.Session:
    """Get a session configured with the given token"""
    session = requests.Session()
    session.headers.update(
        {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
        }
    )
    return session


@tool
def github_graphql(query: str, config: RunnableConfig) -> str:
    """Execute a GraphQL query against the GitHub API.
    The query parameter should be a valid GraphQL query string.
    Example query: {
        viewer {
            login
            repositories(first: 3) {
                nodes {
                    name
                    description
                }
            }
        }
    }"""
    token = config["configurable"]["__github_token"]
    session = get_session(token)

    response = session.post("https://api.github.com/graphql", json={"query": query})
    response.raise_for_status()

    result = response.json()
    if "errors" in result:
        return f"GraphQL Error: {json.dumps(result['errors'], indent=2)}"
    return json.dumps(result["data"], indent=2)


def create_github_graph(llm: ChatBedrockConverse) -> StateGraph:
    """
    Create a graph for GitHub operations using ReAct pattern

    Args:
        llm: Language model for reasoning

    Returns:
        Graph: Configured langgraph Graph instance
    """
    tools = [github_graphql]
    tool_node = ToolNode(tools=tools)

    llm_with_tools = llm.bind_tools(tools)

    def should_continue(state: MessagesState):
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools"
        return END

    def agent(state: MessagesState, config: RunnableConfig) -> MessagesState:
        messages = state["messages"]
        response = llm_with_tools.invoke(messages, config=config)
        return {"messages": messages + [response]}

    workflow = StateGraph(MessagesState)

    workflow.add_node("agent", agent)
    workflow.add_node("tools", tool_node)

    workflow.set_entry_point("agent")
    workflow.add_conditional_edges("agent", should_continue, ["tools", END])
    workflow.add_edge("tools", "agent")

    return workflow.compile()


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print('Usage: python agent.py "your question about GitHub"')
        sys.exit(1)

    with open("github_token.json", "r") as f:
        token_data = json.load(f)
        token = token_data.get("token")

    config = GitHubConfig()
    llm = ChatBedrockConverse(
        model_id=os.getenv("MODEL_ID"),
        region_name=os.getenv("REGION_NAME"),
        credentials_profile_name=os.getenv("CREDENTIALS_PROFILE_NAME"),
    )
    graph = create_github_graph(llm)

    state = {"messages": [HumanMessage(content=sys.argv[1])]}

    runnable_config = RunnableConfig(configurable={"__github_token": token})

    result = graph.invoke(state, config=runnable_config)
    for message in result["messages"]:
        if isinstance(message, (AIMessage, HumanMessage)):
            print(f"{type(message).__name__}: {message.content}\n")
