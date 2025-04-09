import re
import time
from datetime import datetime
from urllib.parse import urljoin

import requests
from typing import List
from bs4 import BeautifulSoup

from .analytics_searchers.base_searcher import extract_date_from_url, format_stock_info


class TranscriptionsSearcher:
    """Class for searching conversations about companies with their officers"""

    @classmethod
    def extract_recent_links(cls, soup: BeautifulSoup) -> List[str]:
        """
        Extracts article links from page content, filtering for only recent years.

        Args:
            soup: BeautifulSoup object of the page

        Returns:
            List of article URLs from the specified recent years
        """
        base_url = "https://www.fool.com"
        min_year = datetime.now().year - 1
        links = []

        # Find all article containers
        articles = soup.find_all("div", class_="flex py-12px text-gray-1100")

        for article in articles:
            link = article.find("a", href=True)
            if not link:
                continue

            full_url = urljoin(base_url, link["href"])

            # Extract year from URL path
            try:
                # Parse URL path like "/earnings/call-transcripts/2025/02/13/company..."
                path_parts = link["href"].split('/')
                year_part = next(part for part in path_parts if part.isdigit() and len(part) == 4)
                year = int(year_part)
                if year >= min_year:
                    links.append(full_url)
            except (StopIteration, ValueError):
                continue  # Skip if no valid year found in URL

        return links

    @classmethod
    def get_transcriptions_links(cls) -> List[str]:
        """
        Gets all earnings call transcript links by simulating 'Load More' clicks
        """
        session = requests.Session()
        session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest"
        })

        # Get initial page
        main_url = "https://www.fool.com/earnings-call-transcripts/"
        response = session.get(main_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        all_links = cls.extract_recent_links(soup)

        # Find the load more button and its parameters
        load_more = soup.find("button", class_="load-more-button")
        api_url = load_more.get("data-url")

        page = 2
        has_actual_articles = True
        while has_actual_articles:
            params = {
                "page": page,
                "per_page": 20,
            }

            try:
                session.headers.update({
                    "X-Requested-With": "fetch"
                })
                api_url = urljoin("https://www.fool.com", api_url)
                response = session.get(api_url, params=params)
                response.raise_for_status()
                data = response.json()
                if not data.get("html"):
                    has_actual_articles = False
                    break

                new_soup = BeautifulSoup(data["html"], 'html.parser')

                # get only actual links - current year and last year
                extra_links = cls.extract_recent_links(new_soup)
                if not extra_links:
                    has_actual_articles = False
                    break
                all_links.extend(extra_links)

                # small delay to be polite
                time.sleep(1)

                page += 1

            except Exception as e:
                print(f"Error loading page {page}: {str(e)}")
                break

        return list(set(all_links))  # Remove duplicates

    @classmethod
    def extract_transcription(cls, target_ticker: str, url: str) -> str:
        """
        Extract transcript data from a Fool.com earnings call transcript page

        Args:
            target_ticker (str): ticker of analysed company
            url (str): URL of the transcript article

        Returns:
            transcription (str): text of call transcription
        """
        transcription = ""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract title
            title_tag = soup.find('h1')
            title = title_tag.get_text(strip=True) if title_tag else "Untitled Transcript"

            # Extract ticker from title (looking for uppercase text in parentheses)
            ticker = ""
            ticker_match = re.search(r'\(([A-Z]{1,5})\)', title)
            if ticker_match:
                ticker = ticker_match.group(1)

            if ticker == target_ticker:
                # Extract transcript text
                transcript_content = soup.find('div', class_='article-body')
                content = ""
                if transcript_content:
                    # Remove useless elements
                    for element in transcript_content(['script', 'style', 'iframe', 'nav', 'footer']):
                        element.decompose()

                    content = transcript_content.get_text('\n', strip=True)
                    content = re.sub(r'\n{3,}', '\n\n', content)

                if content:
                    stock_info = {
                        'title': title,
                        'date': extract_date_from_url(url),
                        'url': url,
                        'content': content
                    }
                    transcription = format_stock_info(stock_info)

        except Exception as e:
            print(f"Error processing {url}: {e}")

        return transcription

    @classmethod
    def get_transcriptions(cls, ticker: str) -> str:
        """
        Get information about company from calls transcriptions
        :param ticker: company ticker
        :return: text of transcriptions
        """
        links = cls.get_transcriptions_links()

        transcriptions = ""
        for link in links:
            transcription = cls.extract_transcription(ticker, link)
            if transcription:
                transcriptions += transcription
                # you can return only one transcription for minimise time
                # transcriptions = transcription
                # break

        return transcriptions
