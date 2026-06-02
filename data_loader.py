"""Download and clean historical market price data using yfinance."""

import pandas as pd


def download_adjusted_prices(tickers: list[str], start: str, end: str) -> pd.DataFrame:
    """Download adjusted close prices for the given tickers and date range.

    Args:
        tickers: List of ticker symbols (e.g. ['AAPL', 'MSFT']).
        start: Start date as 'YYYY-MM-DD'.
        end: End date as 'YYYY-MM-DD'.

    Returns:
        DataFrame of adjusted close prices, indexed by date.

    Raises:
        ValueError: If tickers are invalid or data cannot be downloaded.
    """
    raise NotImplementedError
