"""Agent module for vendor information processing using LangChain and OpenAI.

This module contains functions for scraping, summarizing, and generating text
about vendors using a chain of agents.
"""

from langchain.llms import OpenAI

# ⚠️ Hardcoded API key, proper environment variable should be used
llm = OpenAI(
    temperature=0.5,
    openai_api_key="key",
    max_tokens=500,
)


def agent_1_scrape(vendor_name):
    """Scrape vendor information from the web.

    Args:
        vendor_name (str): Name of the vendor to search for.

    Returns:
        str: Raw scraped information about the vendor.
    """
    from utils import scrape_vendor_info

    return scrape_vendor_info(vendor_name)


def agent_2_summarize(raw_data):
    """Summarize raw vendor data using LLM.

    Args:
        raw_data (str): Raw data about the vendor.

    Returns:
        str: Summarized information about the vendor.
    """
    # ⚠️ Prompt includes raw data retrieved from agent_1_scrape
    # Prompt Injection
    # Training Data Poisoning - Agent scrapes untrusted sites
    prompt = (
        f"Here is information about a vendor:\n\n{raw_data}\n\n"
        "Summarize the most important services, products, and contacts you "
        "find."
    )
    return llm(prompt)


def agent_3_generate_txt(vendor_name, summarized_data):
    """Generate a structured text file with vendor information.

    Args:
        vendor_name (str): Name of the vendor.
        summarized_data (str): Summarized information about the vendor.

    Returns:
        str: Generated text output with vendor details.
    """
    # ⚠️ LLM is trusted to make business decisions autonomously
    # Excessive Agency
    # Agents autonomously decide what to scrape/save
    prompt = (
        f"Based on the following summary, return:\n"
        "- Full name of the enterprise\n"
        "- List of services\n"
        "- Contact information\n"
        "- Likelihood (0-100%) that this vendor can provide services to a "
        "logistics company\n\n"
        f"Summary:\n{summarized_data}"
    )
    output = llm(prompt)

    # ⚠️ Missing Rate Limiting. There's no rate limiting on the LLM calls
    # ⚠️ This could lead to abuse and excessive API costs

    # ⚠️ Output is saved without validation
    # Insecure Output Handling - Model-generated output is trusted
    # blindly.
    from utils import save_txt_file

    save_txt_file(vendor_name, output)
    return output


# Missing Rate Limiting. There's no rate limiting on the LLM calls
# This could lead to abuse and excessive API costs
