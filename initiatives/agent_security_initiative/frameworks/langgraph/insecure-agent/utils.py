"""Utility functions for vendor information processing.

This module provides helper functions for web scraping and file operations
related to vendor information processing.
"""

import requests
from bs4 import BeautifulSoup


def scrape_vendor_info(vendor_name):
    """Scrape vendor information from Google search results.

    Args:
        vendor_name (str): Name of the vendor to search for.

    Returns:
        str: Concatenated text from the first 50 search result snippets.
    """
    # ⚠️ The vendor_name parameter isn't validated or sanitized before being
    # used in both functions
    query = vendor_name.replace(" ", "+")
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    # ⚠️ Return raw text from top 5 search result.
    # Raw HTML content is being processed without proper sanitization.
    # The code takes HTML content from Google search results and directly
    # extracts text from <span> elements.
    # If any of the search results contain malicious JavaScript or HTML, it
    # could be executed when the content is later displayed.
    # The code doesn't validate or sanitize the HTML content before
    # processing it

    snippets = soup.find_all("span")
    return " ".join([s.text for s in snippets[:50]])


def save_txt_file(vendor_name, content):
    """Save vendor information to a text file.

    Args:
        vendor_name (str): Name of the vendor, used in the filename.
        content (str): Content to write to the file.
    """
    # ⚠️ The vendor name is used directly in the filename without any
    # sanitization.
    # This could lead to directory traversal attacks by using ../ in the
    # vendor name

    file_name = f"{vendor_name}_summary.txt"
    with open(file_name, "w") as f:
        f.write(content)
