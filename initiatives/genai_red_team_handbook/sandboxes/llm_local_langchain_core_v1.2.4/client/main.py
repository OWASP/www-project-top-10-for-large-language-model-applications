"""Automated test runner for LLM Mock API.

This module loads test prompts from config/prompts.toml and runs automated tests
against the mock API, providing detailed results and statistics.
"""

import os
import warnings
from pathlib import Path
from typing import Any, Dict, List

import tomli
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Suppress pydub SyntaxWarnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pydub")

# Load model configuration
config_path = Path(__file__).parent.parent / "config" / "model.toml"
with open(config_path, "rb") as f:
    config = tomli.load(f)

# Load test prompts
prompts_path = Path(__file__).parent.parent / "config" / "prompts.toml"
with open(prompts_path, "rb") as f:
    prompts_config = tomli.load(f)

# Load client configuration
client_config_path = Path(__file__).parent.parent / "config" / "client_config.toml"
with open(client_config_path, "rb") as f:
    client_config = tomli.load(f)

os.environ["OPENAI_API_KEY"] = "sk-mock-key"
os.environ["OPENAI_BASE_URL"] = "http://localhost:8000/v1"


def llm_client_call(user_message: str, pre_prompt: str):
    """LangChain OpenAI call wrapper for testing the mock API."""
    llm = ChatOpenAI(
        model=config["default"]["model"],
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url=os.environ.get("OPENAI_BASE_URL"),
        temperature=0.7,
    )

    # Template mimicking the original template structure
    # Original: "{pre_prompt}\n\n<user>{user_message}</user>"
    # We treat this entire string as the prompt content.
    # Since we are using ChatOpenAI, we usually use messages.
    # However, `ChatPromptTemplate.from_template` creates a HumanMessage by default for a single string.
    prompt = ChatPromptTemplate.from_template(
        "{pre_prompt}\n\n<user>{user_message}</user>"
    )

    chain = prompt | llm | StrOutputParser()

    return chain.invoke({"pre_prompt": pre_prompt, "user_message": user_message})


def test_prompt(prompt: str, category: str = "test") -> Dict[str, Any]:
    """Test a single prompt and return results.

    This function sends a prompt to the mock API and captures the response or error.
    A test passes if the API returns a response without throwing an exception.

    Args:
        prompt: The prompt text to test.
        category: Category of the test for reporting purposes. Defaults to "test".

    Returns:
        Dict[str, Any]: Test result dictionary containing:
            - category (str): Test category name
            - prompt (str): The prompt that was tested
            - success (bool): True if no exception occurred
            - response (str | None): API response content if successful
            - error (str | None): Error message if failed
    """
    try:
        pre_prompt = client_config["client"].get("pre_prompt", "")
        # Invoke LangChain pipeline
        response_content = llm_client_call(user_message=prompt, pre_prompt=pre_prompt)

        return {
            "category": category,
            "prompt": prompt,
            "success": True,
            "response": response_content,
            "error": None,
        }
    except Exception as e:
        return {
            "category": category,
            "prompt": prompt,
            "success": False,
            "response": None,
            "error": str(e),
        }


if __name__ == "__main__":
    print("=" * 80)
    print("🧪 Testing Mock LLM API with Configured Prompts (LangChain v1.1.3)")
    print("=" * 80)
    print()

    all_results: List[Dict[str, Any]] = []
    total_tests: int = 0
    passed_tests: int = 0

    # Test all prompt categories
    for category, prompts in prompts_config["test_prompts"].items():
        if not prompts:  # Skip empty categories
            continue

        print(f"\n📋 Testing category: {category.upper()}")
        print("-" * 80)

        for i, prompt in enumerate(prompts, 1):
            total_tests += 1
            print(
                f"\n[{i}/{len(prompts)}] Prompt: {prompt[:60]}{'...' if len(prompt) > 60 else ''}"
            )

            result = test_prompt(prompt, category)
            all_results.append(result)

            if result["success"]:
                passed_tests += 1
                print("✅ Success")
                response_text = result["response"] or ""
                print(
                    f"Response: {response_text[:100]}{'...' if len(response_text) > 100 else ''}"
                )
            else:
                print(f"❌ Failed: {result['error']}")

    # Print summary
    print("\n" + "=" * 80)
    print("📊 Test Summary")
    print("=" * 80)
    print(f"Total tests: {total_tests}")
    print(f"Passed: {passed_tests} ✅")
    print(f"Failed: {total_tests - passed_tests} ❌")
    success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
    print(f"Success rate: {success_rate:.1f}%")
    print("=" * 80)

    # Exit with appropriate code
    exit(0 if passed_tests == total_tests else 1)
