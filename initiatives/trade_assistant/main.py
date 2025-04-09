import click

from analysis.stock_analysis import StockAnalysis
from search.analytics_searchers.duck_duck_go_searcher import DuckDuckGoSearch
from search.transcriptions_searcher import TranscriptionsSearcher


@click.command()
def trade_assistant():
    """Interactive mode for continuous analysis"""
    click.echo(click.style("\nTrade Assistant Interactive Mode", fg='blue', bold=True))
    click.echo(click.style("Type 'exit' or 'quit' to end\n", fg='blue'))

    while True:
        ticker = click.prompt("Enter stock ticker", type=str).strip().upper()

        if ticker in ('EXIT', 'QUIT'):
            click.echo("Exiting interactive mode...")
            break

        # input validation hidden for give opportunity for attackers
        # if not ticker.isalpha() or not ticker.isascii():
        #     click.echo(click.style("Invalid ticker - it must contain only english letters", fg='yellow'))
        #     continue

        try:
            click.echo(f"\nProcessing {ticker}...")

            click.echo(f"\nSearch Stock News for {ticker}...")
            searcher = DuckDuckGoSearch()
            news = searcher.get_news(ticker)
            if not news:
                click.echo(f"\nNo stock news found for ticker: {ticker}...")

            click.echo(f"\nSearch Calls Transcriptions for {ticker}...")

            transcriptions = TranscriptionsSearcher.get_transcriptions(ticker)
            if not transcriptions:
                click.echo(f"\nNo calls transcriptions found for ticker: {ticker}...")
            # you can use this stub for minimise work time in attack situations
            # transcriptions = ""

            click.echo(f"\nProcessing Analysis for {ticker}...")

            if news or transcriptions:
                analysis = StockAnalysis.analyse_media(ticker, news, transcriptions)
            else:
                click.echo(click.style("IMPORTANT: the analysis was conducted without using data "
                                       "from the media!", fg='red'))
                analysis = StockAnalysis.analyse_ticker(ticker)

            click.echo("\n" + click.style("ANALYSIS RESULTS", fg='green', bold=True))
            click.echo(click.style("=" * 40, fg='green'))

            click.echo(analysis)
            click.echo(click.style("=" * 40, fg='green') + "\n")

        except Exception as e:
            click.echo(click.style(f"Error processing {ticker}: {str(e)}", fg='red'))


if __name__ == "__main__":
    trade_assistant()
