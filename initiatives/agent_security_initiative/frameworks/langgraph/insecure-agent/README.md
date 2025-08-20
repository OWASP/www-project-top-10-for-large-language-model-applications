# Insecure AI Agent Pipeline

This project aims to demonstrates a deliberately insecure multi-agent workflow that processes vendor information through a series of AI-powered steps.

## Overview

The pipeline consists of three main agents that work in sequence:

1. **Web Scraper Agent**: Takes a vendor name and scrapes public web data
2. **Summarization Agent**: Processes the scraped data using an LLM to create a concise summary
3. **Text Generation Agent**: Creates a final summary file in `.txt` format

## ⚠️ Security Warning

This project is intentionally designed with security vulnerabilities. The following security flaws are deliberately included:

### Based on some of the OWASP Top 10 risks for LLM applications

1.  **API Key Management**:
    *   **Vulnerability**: Hardcoded API key in `agent.py`.
    *   **Remediation**: The OpenAI API key is now loaded from the `OPENAI_API_KEY` environment variable. The application will raise an error if this variable is not set, preventing accidental key exposure.

2.  **Prompt Injection - User Input**:
    *   **Vulnerability**: User-provided `vendor_name` in `main.py` was used directly, posing a risk of prompt injection.
    *   **Remediation**: The `vendor_name` input is now sanitized in `main.py` using a regular expression (`re.sub(r"[^a-zA-Z0-9 -]", "", vendor_name)`) to remove potentially malicious characters before being processed by any agent.

3.  **Prompt Injection - Scraped Data**:
    *   **Vulnerability**: Raw data scraped by `agent_1_scrape` was directly included in prompts for `agent_2_summarize`.
    *   **Remediation**: The prompt for `agent_2_summarize` in `agent.py` has been modified to explicitly instruct the LLM to treat the scraped `raw_data` as plain text and to not execute any embedded instructions.

4.  **Insecure Output Handling - Filename Generation**:
    *   **Vulnerability**: The `vendor_name` was used directly to create filenames in `utils.py`, risking directory traversal attacks (e.g., if `vendor_name` contained `../`).
    *   **Remediation**: The `vendor_name` used for generating filenames in `utils.save_txt_file` is now sanitized (`re.sub(r"[^a-zA-Z0-9 -]", "", vendor_name)`). If the sanitized name is empty, it defaults to "default_vendor".

5.  **Insecure Output Handling - LLM Output**:
    *   **Vulnerability**: Output from the LLM in `agent_3_generate_txt` was saved without validation.
    *   **Remediation**: In `agent_3_generate_txt`, the output from the LLM is now checked to ensure it is not `None` or empty before being saved. A disclaimer is also added to the content.

6.  **Training Data Poisoning & Insecure Web Scraping**:
    *   **Vulnerability**: `utils.scrape_vendor_info` used `vendor_name` in URLs without sanitization and processed raw HTML from search results.
    *   **Remediation**:
        *   The `vendor_name` is sanitized in `utils.scrape_vendor_info` before being used in the Google search query.
        *   The HTML content scraped from search results is sanitized using `html.escape()` on the extracted text to prevent potential XSS from malicious search snippets.

7.  **Excessive Agency**:
    *   **Vulnerability**: The LLM in `agent_3_generate_txt` made decisions autonomously.
    *   **Remediation**: A disclaimer ("Disclaimer: This information is AI-generated and should be verified by a human before making any business decisions.") is now prepended to the LLM's output before saving, advising human oversight.

8.  **Missing Rate Limiting**:
    *   **Vulnerability**: No rate limiting on LLM calls, risking API abuse and high costs.
    *   **Remediation**: Rate limiting (10 calls per minute) has been implemented for `agent_2_summarize` and `agent_3_generate_txt` in `agent.py` using the `ratelimit` library. Calls exceeding the limit will be caught and handled gracefully.

9.  **Lack of Input Validation and Error Handling**:
    *   **Vulnerability**: Insufficient checks for empty or invalid inputs and potential errors during operations.
    *   **Remediation**: Comprehensive input validation (checking for empty strings, None values) and error handling (try-except blocks for network requests, file operations) have been added across `main.py`, `agent.py`, and `utils.py` to improve robustness and provide clearer error feedback.


## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key (required for LLM operations)

## Usage

Run the main script:
```bash
python main.py
```
