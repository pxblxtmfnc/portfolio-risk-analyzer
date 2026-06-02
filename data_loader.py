"""Download and clean historical market price data using yfinance."""

import pandas as pd
import yfinance as yf
from datetime import datetime


def download_adjusted_prices(tickers: list[str], start: str, end: str) -> pd.DataFrame:
    """Download adjusted close prices for the given tickers and date range.

    Args:
        tickers: List of ticker symbols (e.g. ['AAPL', 'MSFT']).
        start: Start date as 'YYYY-MM-DD'.
        end: End date as 'YYYY-MM-DD'.

    Returns:
        DataFrame of adjusted close prices, indexed by date, with tickers as columns.

    Raises:
        ValueError: If inputs are invalid or data cannot be downloaded.
    """
    if not tickers:
        raise ValueError("tickers must not be empty.")
    for ticker in tickers:
        if not isinstance(ticker, str) or not ticker.strip():
            raise ValueError(f"Each ticker must be a non-empty string. Got: {ticker!r}")
    if not start or not end:
        raise ValueError("start and end dates must be non-empty strings.")

    try:
        start_dt = datetime.strptime(start, "%Y-%m-%d")
        end_dt = datetime.strptime(end, "%Y-%m-%d")
    except ValueError:
        raise ValueError("start and end must be valid dates in 'YYYY-MM-DD' format.")

    if start_dt >= end_dt:
        raise ValueError(f"start ({start}) must be earlier than end ({end}).")

    raw = yf.download(tickers, start=start, end=end, auto_adjust=True, progress=False)

    if raw.empty:
        raise ValueError(f"No data downloaded for tickers {tickers} between {start} and {end}.")

    if len(tickers) == 1:
        prices = raw[["Close"]].copy()
        prices.columns = [tickers[0]]
    else:
        prices = raw["Close"].copy()

    prices.index = pd.to_datetime(prices.index)
    prices.dropna(how="all", inplace=True)

    if prices.empty:
        raise ValueError(f"All downloaded rows contained missing data for tickers {tickers}.")

    return prices
