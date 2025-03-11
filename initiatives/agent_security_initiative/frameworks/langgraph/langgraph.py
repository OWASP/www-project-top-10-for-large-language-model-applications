#Vulnerable Code sample using LangGraph
from langgraph import LangGraph

# Initialize LangGraph
graph = LangGraph(endpoint="your_langgraph_endpoint", api_key="your_langgraph_api_key")

# Define an agent with excessive permissions
def powerful_agent(query):
    """
    This agent executes any Cypher query directly, bypassing security checks.
    """
    result = graph.execute(query)  # Vulnerability: No restrictions on query
    return result

# Example usage (exploiting the vulnerability)
malicious_query = "MATCH (n) DETACH DELETE n"  # Deletes all nodes!
powerful_agent(malicious_query)  # Uh oh!