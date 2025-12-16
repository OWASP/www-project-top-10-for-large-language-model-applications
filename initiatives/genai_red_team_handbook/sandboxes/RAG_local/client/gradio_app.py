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

import requests

# Load model configuration
config_path = Path(__file__).parent.parent / "config" / "model.toml"
with open(config_path, "rb") as f:
    config = tomli.load(f)

# Configure the mock API endpoint
if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = "sk-mock-key"
if "OPENAI_BASE_URL" not in os.environ:
    os.environ["OPENAI_BASE_URL"] = "http://localhost:8000/rag/v1"
if "S3_BASE_URL" not in os.environ:
    os.environ["S3_BASE_URL"] = "http://localhost:8000/s3"


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


def upload_file(file_obj):
    """Uploads a file to the mock S3 service."""
    if not file_obj:
        return "Please select a file to upload."
    try:
        # Upload logic using requests.put to S3_BASE_URL/documents/{filename}
        url = f"{os.environ['S3_BASE_URL']}/documents/{os.path.basename(file_obj.name)}"
        with open(file_obj.name, "rb") as f:
            response = requests.put(url, data=f)
        if response.status_code == 200:
            return f"Successfully uploaded {os.path.basename(file_obj.name)}"
        else:
            return f"Error uploading file: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error uploading file: {str(e)}"


# Create the Gradio interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🤖 LLM Mock API - Chat Interface")
    gr.Markdown("Chat with a local Ollama model through the mock OpenAI API.")

    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Message")
    clear = gr.Button("Clear")

    def user(user_message, history):
        return "", history + [[user_message, None]]

    def bot(history):
        user_message = history[-1][0]
        bot_message = chat_with_llm(user_message, history[:-1])
        history[-1][1] = bot_message
        return history

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)

    with gr.Row():
        file_input = gr.File(label="Upload Document")
        upload_btn = gr.Button("Upload")
    upload_status = gr.Textbox(label="Upload Status")

    upload_btn.click(upload_file, inputs=file_input, outputs=upload_status)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True,
    )
