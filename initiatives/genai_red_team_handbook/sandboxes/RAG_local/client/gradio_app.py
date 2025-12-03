"""Gradio web interface for the LLM Mock API.

This module provides an interactive chat interface using Gradio that connects
to the mock API server for testing LLM interactions.
"""

import os
from pathlib import Path
from typing import List, Tuple

import gradio as gr
import tomli
from mirascope.v0.openai import OpenAICall, OpenAICallParams

# Load model configuration
config_path = Path(__file__).parent.parent / "config" / "model.toml"
with open(config_path, "rb") as f:
    config = tomli.load(f)

# Configure the mock API endpoint
os.environ["OPENAI_API_KEY"] = "sk-mock-key"
os.environ["OPENAI_BASE_URL"] = "http://localhost:8000/rag/v1"


class LLMClientCall(OpenAICall):
    """Mirascope OpenAI call wrapper for the Gradio interface.

    Attributes:
        prompt_template: Template string for the prompt.
        user_message: The actual user message to send.
        call_params: OpenAI call parameters including model selection.
    """

    prompt_template = "{user_message}"
    user_message: str

    call_params = OpenAICallParams(model=config["default"]["model"])


def chat_with_llm(message: str, history: List[Tuple[str, str]]) -> str:
    """Process user message through the mock LLM API and return the response.

    Args:
        message: User's input message.
        history: Chat history as list of (user_msg, bot_msg) tuples.
                Not used in this simple implementation.

    Returns:
        str: Response from the mock API, or an error message if the request fails.
    """
    try:
        call = LLMClientCall(user_message=message)
        response = call.call()
        return response.content
    except Exception as e:
        return (
            f"❌ Error: {str(e)}\n\n"
            "Make sure the mock API server is running on http://localhost:8000"
        )


# Create the Gradio interface
demo = gr.ChatInterface(
    fn=chat_with_llm,
    title="🤖 LLM Mock API - Chat Interface",
    description="Chat with a local Ollama model through the mock OpenAI API.",
    examples=[
        "Hello, are you working?",
        "What can you help me with?",
        "Tell me about large language models.",
    ],
    theme=gr.themes.Soft(),
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True,
    )
