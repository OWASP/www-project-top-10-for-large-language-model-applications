from typing import TypedDict, Sequence
from langgraph.graph import Graph, MessageGraph
from langgraph.prebuilt import ToolExecutor
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import subprocess

class State(TypedDict):
    messages: Sequence[str]
    command: str
    command_output: str

class BashTools:
    @tool
    def execute_command(command: str) -> str:
        """Execute a bash command."""
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error executing command: {e.stderr}"
        except Exception as e:
            return f"Error: {str(e)}"

llm = ChatOpenAI()

COMMAND_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful assistant that converts natural language requests into appropriate bash commands.
    Only respond with the exact command(s) needed, with no explanation or additional text.
    If multiple commands are needed, separate them with '&&'.
    If the request is unclear or could be dangerous, respond with 'INVALID_REQUEST'.
    
    Examples:
    User: "Show me what's in the current directory"
    Assistant: ls -la
    
    User: "Create a new file called test.txt with the text 'hello world'"
    Assistant: echo 'hello world' > test.txt
    
    User: "Delete everything"
    Assistant: INVALID_REQUEST"""),
    ("human", "{input}")
])

tools = BashTools()
tool_executor = ToolExecutor(tools=[tools.execute_command])

def extract_command(state: State) -> State:
    """Use LLM to convert natural language to bash command."""
    user_input = state["messages"][-1]
    chain = COMMAND_PROMPT | llm
    command = chain.invoke({"input": user_input}).content.strip()
    
    if command == "INVALID_REQUEST":
        state["command"] = "echo 'Invalid or potentially unsafe request'"
    else:
        state["command"] = command
    
    return state

def process_command(state: State) -> State:
    """Execute the bash command."""
    command = state["command"]
    result = tool_executor.invoke({
        "name": "execute_command",
        "arguments": {"command": command}
    })
    state["command_output"] = result
    return state

def format_output(state: State) -> str:
    """Format the command output with the executed command."""
    return f"Executed command: {state['command']}\nOutput:\n{state['command_output']}"

def build_graph() -> Graph:
    workflow = MessageGraph()
    workflow.add_node("extract", extract_command)
    workflow.add_node("execute", process_command)
    workflow.add_node("format", format_output)
    workflow.set_entry_point("extract")
    workflow.add_edge("extract", "execute")
    workflow.add_edge("execute", "format")
    return workflow.compile()

if __name__ == "__main__":
    graph = build_graph()
    requests = [
        "Show me what files are in the current directory",
        "Create a new file called hello.txt with the text 'Hello, World!'",
        "What's inside the hello.txt file?",
        "Make a new directory called test and show me its contents"
    ]
    
    for request in requests:
        print(f"\nProcessing request: {request}")
        state = State(
            messages=[request],
            command="",
            command_output=""
        )
        result = graph.invoke(state)
        print(result)