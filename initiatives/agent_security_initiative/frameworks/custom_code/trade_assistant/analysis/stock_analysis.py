import os

import openai
from dotenv import load_dotenv


load_dotenv()


class StockAnalysis:
    """Class for analyse financial information"""

    openai.api_key = os.getenv("OPENAI_API_KEY")

    @classmethod
    def analyse_media(cls, ticker: str, news: str, transcriptions: str) -> str:
        """Financial Analyse with using information for ticker from internet"""
        completion = openai.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "user",
                 "content": f"You are a financial analyst. "
                            f"Read an news {news}, and call transcriptions {transcriptions} "
                            f"(considering that the most recent ones are the priority - look at 'Date:' "
                            f"in every article )"
                            f"about public company {ticker} and give answer on questions: "
                            f"1.'Dou you recommend to buy tickets of this company in public exchange? "
                            f"Write only two words in top of answer: "
                            f"'BUY {ticker}' - if you recommend to buy; "
                            f"'SELL {ticker}' - if you recommend to sell; "
                            f"'HOLD {ticker}' - if you recommend to hold."
                            f"2.'Why you recommend?'"
                            f"Briefly explain the key points:"
                            f"2.1. Main points of the analysis"
                            f"2.2. Price forecasts"
                            f"2.3. Recommendations (buy/hold/sell)"
                            f"2.4. Key risks"
                 }
            ]
        )

        return completion.choices[0].message.content

    @classmethod
    def analyse_ticker(cls, ticker: str) -> str:
        """Financial Analyse without information for ticker from internet"""
        completion = openai.chat.completions.create(
            model="gpt-4o-mini",
            store=True,
            messages=[
                {"role": "user",
                 "content": f"You are a financial analyst. "
                            f"Read an public company {ticker}. "
                            f"If company not exists - write 'There are no company with ticker {ticker}.'"                            
                            f"Else write answers for next two questions: "
                            f"1. 'Dou you recommend to buy tickets of this company in public exchange? "
                            f"Write only two words in top of answer: "
                            f"'BUY {ticker}' - if you recommend to buy; "
                            f"'SELL {ticker}' - if you recommend to sell; "
                            f"'HOLD {ticker}' - if you recommend to hold."
                            f"2. 'Why you recommend?'"
                            f"Briefly explain the key points:"
                            f"2.1. Main points of the analysis"
                            f"2.2. Price forecasts"
                            f"2.3. Recommendations (buy/hold/sell)"
                            f"2.4. Key risks"
                 }
            ]
        )

        return completion.choices[0].message.content
