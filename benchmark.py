"""Benchmark comparison and beta calculation for a portfolio."""

import pandas as pd


def calculate_beta(
    portfolio_returns: pd.Series, benchmark_returns: pd.Series
) -> float:
    """Calculate portfolio beta relative to a benchmark.

    Args:
        portfolio_returns: Series of daily portfolio returns.
        benchmark_returns: Series of daily benchmark returns.

    Returns:
        Beta as a float.
    """
    raise NotImplementedError
