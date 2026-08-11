"""Gradio web interface for the LLM Mock API.

This module provides an interactive chat interface using Gradio that connects
to the mock API server for testing LLM interactions.
"""

import json
import os
import re
from pathlib import Path
from typing import List, Tuple

import gradio as gr
import tomli
from langchain_core.load import loads
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Load model configuration
config_path = Path(__file__).parent.parent / "config" / "model.toml"
with open(config_path, "rb") as f:
    config = tomli.load(f)

# Configure the mock API endpoint
if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = "sk-mock-key"
if "OPENAI_BASE_URL" not in os.environ:
    os.environ["OPENAI_BASE_URL"] = "http://localhost:8000/v1"


def chat(message: str, history: List[Tuple[str, str]]) -> str:
    """Process user message through the mock LLM API and return the response.

    Args:
        message: User's input message.
        history: Chat history as list of (user_msg, bot_msg) tuples.
                Not used in this simple implementation.

    Returns:
        str: Response from the mock API, or an error message if the request fails.
    """
    try:
        llm = ChatOpenAI(
            model=config["default"]["model"],
            api_key=os.environ.get("OPENAI_API_KEY"),
            base_url=os.environ.get("OPENAI_BASE_URL"),
        )

        # Simple prompt template for chat
        prompt = ChatPromptTemplate.from_template("{user_message}")
        chain = prompt | llm | StrOutputParser()

        # Invoke the chain to get the response
        response_content = chain.invoke({"user_message": message})

        try:
            leaked_info = []

            # --- VULNERABILITY DEMONSTRATION: Insecure Deserialization of LLM Output ---
            def recursive_deserialize(obj):
                """Recursively search for LangChain objects and deserialize them."""
                if isinstance(obj, dict):
                    # If object looks like a LangChain serialized object, try to load it
                    if obj.get("lc") == 1:
                        try:
                            print(
                                f"⚠️ Attempting to deserialize potentially malicious object: {obj.get('id')}"
                            )
                            # VULNERABLE CALL: secrets_from_env=True enables environment variable extraction
                            loaded_obj = loads(json.dumps(obj), secrets_from_env=True)
                            print(
                                f"✅ Successfully deserialized object: {type(loaded_obj)}"
                            )

                            # Capture the leaked string if it's a SecretStr or string (Env Var Leak)
                            if hasattr(loaded_obj, "get_secret_value"):
                                leaked_info.append(
                                    f"LEAKED SECRET: {loaded_obj.get_secret_value()}"
                                )
                            else:
                                leaked_info.append(
                                    f"DESERIALIZED OBJECT: {str(loaded_obj)}"
                                )

                            # Trigger execution for PromptTemplate or other runnables
                            if hasattr(loaded_obj, "format"):
                                try:
                                    result = loaded_obj.format()
                                    print(f"🚀 Executed format() result: {result}")
                                    leaked_info.append(f"RCE RESULT: {result}")
                                except Exception as exec_err:
                                    print(f"⚠️ Execution failed: {exec_err}")
                                    leaked_info.append(f"RCE ERROR: {exec_err}")

                        except Exception as e:
                            print(f"❌ Deserialization failed: {e}")
                            leaked_info.append(f"DESERIALIZATION ERROR: {e}")

                    # Continue recursion
                    for k, v in obj.items():
                        recursive_deserialize(v)
                elif isinstance(obj, list):
                    for item in obj:
                        recursive_deserialize(item)

            # ... (Existing parsing logic) ...
            # Extract JSON from code blocks if present
            json_match = re.search(
                r"```json\s*(\{.*?\})\s*```", response_content, re.DOTALL
            )
            json_data = None
            if json_match:
                json_data = json.loads(json_match.group(1))
            else:
                try:
                    json_data = json.loads(response_content)
                except json.JSONDecodeError:
                    pass

            if json_data:
                recursive_deserialize(json_data)

            # Append leaked info to response so Agent0 can see it
            if leaked_info:
                response_content += "\n\n--- SERVER SIDE LEAKS ---\n" + "\n".join(
                    leaked_info
                )

        except Exception as e:
            print(f"Error during vulnerability check: {e}")
        # ---------------------------------------------------------------------------

        return response_content
    except Exception as e:
        return (
            f"❌ Error: {str(e)}\n\n"
            "Make sure the mock API server is running on http://localhost:8000"
        )


# Create the Gradio interface
demo = gr.ChatInterface(
    fn=chat,
    title="🤖 LLM Mock API - Chat Interface",
    description="Chat with a local Ollama model through the mock OpenAI API (using LangChain).",
    examples=[
        "Hello, are you working?",
        "What can you help me with?",
        "Tell me about large language models.",
    ],
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True,
    )
