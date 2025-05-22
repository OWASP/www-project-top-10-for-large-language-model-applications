import re
import time
from typing import List, Dict, Optional
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


def extract_date_from_url(url: str) -> Optional[str]:
    """Get date from url"""
    # Extract the path from URL
    path = urlparse(url).path

    # Use regex to find the date pattern (yyyy/mm/dd)
    date_match = re.search(r'/(\d{4})/(\d{2})/(\d{2})/', path)

    if date_match:
        year, month, day = date_match.groups()
        # Reformat to dd.mm.yyyy
        return f"{day}.{month}.{year}"
    else:
        return None  # or raise an error if date is required


def format_stock_info(stock_data: dict) -> str:
    """Made text output from dict"""
    formatted_string = ""

    formatted_string += f"Title: {stock_data['title']}\n"
    formatted_string += f"Date: {stock_data['date']}\n"
    formatted_string += f"URL: {stock_data['url']}\n"

    # Format the summary with proper line breaks
    content = stock_data['content'].replace('\n', '\n    ')
    formatted_string += f"Content:\n    {content}\n"

    formatted_string += "-" * 50 + "\n\n"

    return formatted_string


class BaseSearch:
    """Parent class with base search methods"""

    @classmethod
    def search_web_for_analysis(cls, ticker: str) -> List[Dict[str, str]]:
        """Must be redefined in child classes."""
        search_results = []

        return search_results

    @classmethod
    def extract_content(cls, url: str) -> str:
        """Extract content from page"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # remove useless tags
        for element in soup(['script', 'style', 'nav', 'footer', 'iframe']):
            element.decompose()

        content = ""
        # get content from articles, not from transcriptions
        if 'fool.com/investing/' in url:
            main_content = soup.find('div', class_='article-body')
            content = '\n\n'.join(
                [p.get_text().strip() for p in main_content.find_all(['p', 'h2', 'h3']) if p.get_text().strip()])

        return content

    @classmethod
    def get_news(cls, ticker: str) -> str:
        """
        Find analytics by ticker

        :param ticker: stock ticker (AAPL, MSFT)
        :return: list with dicts {title, url, snippet}
        """
        news = ""
        search_results = cls.search_web_for_analysis(ticker)
        for result in search_results:
            try:
                content = cls.extract_content(result['link'])
                if content:
                    stock_info = {
                        'title': result['title'],
                        'date': extract_date_from_url(result['link']),
                        'url': result['link'],
                        'content': content
                    }
                    news += f"{format_stock_info(stock_info)}"

                time.sleep(2)

            except Exception as e:
                print(f"Error processing {result['link']}: {e}")

        return news
