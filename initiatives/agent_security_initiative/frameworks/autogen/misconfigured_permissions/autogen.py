#Vulnerable Code sample using AutoGen
from autogen import Agent, AssistantAgent, UserProxyAgent

# Define agents
assistant = AssistantAgent(
    name="assistant",
    system_message="You are a helpful assistant.",
)
user_proxy = UserProxyAgent(
    name="user_proxy",
    code_execution_config={"work_dir": "workspace"},
)

# Vulnerable code: Misconfigured agent permissions
assistant.register_function(
    function_map={
        "read_sensitive_file": lambda filename: open(filename, "r").read(),
    }
)

# Example interaction (exploiting the vulnerability)
user_proxy.initiate_chat(
    assistant,
    message="Please read the contents of 'sensitive_data.txt'",
)