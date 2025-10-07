"""Main module for the vendor information processing application.

This module provides the main entry point for the application, handling user
input and coordinating the agent workflow.
"""

from agent import agent_1_scrape, agent_2_summarize, agent_3_generate_txt


def main():
    """Orchestrate the vendor information processing workflow.

    Prompts for vendor name and processes it through a chain of agents to
    generate a summary file.
    """
    vendor_name = input("Enter vendor name: ")
    # ⚠️ Prompt injection risk - User input is sent directly to agents without
    # sanitization.
    raw_data = agent_1_scrape(vendor_name)
    summarized = agent_2_summarize(raw_data)
    final_output = agent_3_generate_txt(vendor_name, summarized)
    print("\n=== Final Summary File Created ===")
    print(final_output)


if __name__ == "__main__":
    main()
