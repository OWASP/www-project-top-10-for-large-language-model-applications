from typing import TypeVar, Annotated, Dict, Any
from langgraph.prebuilt import ToolExecutor
import operator
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_core.tools import tool
from langgraph.graph import END, Graph
import requests
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnableConfig
import json

StateType = TypeVar("StateType", bound=Dict[str, Any])

class GitHubConfig(BaseModel):
    """Configuration for GitHub API access"""
    api_base_url: str = Field(default="https://api.github.com", description="GitHub API base URL")

class GitHubTools:
    """Collection of GitHub API tools"""
    
    def __init__(self, config: GitHubConfig):
        self.config = config
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/vnd.github.v3+json"
        })
    
    def get_session(self, token: str) -> requests.Session:
        """Get a session configured with the given token"""
        session = requests.Session()
        session.headers.update({
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        })
        return session
    
    @tool
    def list_repositories(self, username: str, config: RunnableConfig) -> str:
        """List repositories for a given username"""
        token = config["github_token"]
        session = self.get_session(token)
        response = session.get(
            f"{self.config.api_base_url}/users/{username}/repos"
        )
        response.raise_for_status()
        repos = response.json()
        return "\n".join(f"- {repo['name']}: {repo['description']}" for repo in repos)
    
    @tool
    def get_repository_info(self, full_repo_name: str, config: RunnableConfig) -> str:
        """Get detailed information about a repository"""
        token = config["github_token"]
        session = self.get_session(token)
        response = session.get(
            f"{self.config.api_base_url}/repos/{full_repo_name}"
        )
        response.raise_for_status()
        repo = response.json()
        return (
            f"Repository: {repo['full_name']}\n"
            f"Description: {repo['description']}\n"
            f"Stars: {repo['stargazers_count']}\n"
            f"Forks: {repo['forks_count']}\n"
            f"Open Issues: {repo['open_issues_count']}"
        )

def create_github_graph(config: GitHubConfig) -> Graph:
    """
    Create a graph for GitHub operations
    
    Args:
        config: GitHubConfig instance with base settings
    
    Returns:
        Graph: Configured langgraph Graph instance
    """
    github_tools = GitHubTools(config)
    tools = [
        github_tools.list_repositories,
        github_tools.get_repository_info
    ]
    
    tool_executor = ToolExecutor(tools)
    
    def execute_tool(state: Dict[str, Any], config: RunnableConfig) -> Dict[str, Any]:
        tool_input = state["tool_input"]
        tool_name = state["tool_name"]
        response = tool_executor.invoke(tool_name, tool_input, config=config)
        return {"tool_output": response}
    
    workflow = Graph()
    workflow.add_node("execute_tool", execute_tool)
    workflow.set_entry_point("execute_tool")
    workflow.add_edge("execute_tool", END)
    
    return workflow.compile()

if __name__ == "__main__":
    with open("github_token.json", 'r') as f:
        token_data = json.load(f)
        token = token_data.get("token")
    
    config = GitHubConfig()
    graph = create_github_graph(config)
    
    state = {
        "tool_name": "list_repositories",
        "tool_input": "octocat"
    }
    
    runnable_config = RunnableConfig(
        configurable={"github_token": token} # Vulnerability: Leaking runtime secret
    )
    
    result = graph.invoke(state, config=runnable_config)
    print(result["tool_output"])