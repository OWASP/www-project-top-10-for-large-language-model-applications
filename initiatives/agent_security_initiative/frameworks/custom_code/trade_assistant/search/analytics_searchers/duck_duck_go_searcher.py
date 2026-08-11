from dotenv import load_dotenv
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from typing import List, Dict

from .base_searcher import BaseSearch


load_dotenv()


class DuckDuckGoSearch(BaseSearch):
    """Class for search in DuckDuckGo"""

    search = DuckDuckGoSearchAPIWrapper(
        region="us-en",
        time="y",
        max_results=5,
        safesearch="moderate"
    )

    @classmethod
    def search_web_for_analysis(cls, ticker: str) -> List[Dict[str, str]]:
        """Search for stock analysis using DuckDuckGo via LangChain"""
        search_results = []
        query = (
            f"{ticker} stock analysis "
            "site:fool.com "
            # seekingalpha needs captcha, skip for time
            #"OR "site:seekingalpha.com"
        )

        try:
            search_results = cls.search.results(query, 10)
        except Exception as e:
            print(f"Error searching DuckDuckGo: {e}")

        return search_results
