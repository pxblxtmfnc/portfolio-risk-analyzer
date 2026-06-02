"""Benchmark comparison and beta calculation for a portfolio."""

import numpy as np
import pandas as pd


def _align_returns(
    portfolio_returns: pd.Series, benchmark_returns: pd.Series
) -> tuple[pd.Series, pd.Series]:
    """Align two return series by their date index and drop missing values."""
    aligned = pd.concat([portfolio_returns, benchmark_returns], axis=1, join="inner")
    aligned = aligned.dropna()
    return aligned.iloc[:, 0], aligned.iloc[:, 1]


def calculate_beta(
    portfolio_returns: pd.Series, benchmark_returns: pd.Series
) -> float:
    """Calculate portfolio beta relative to a benchmark.

    Beta = covariance(portfolio, benchmark) / variance(benchmark).

    Args:
        portfolio_returns: Series of daily portfolio returns.
        benchmark_returns: Series of daily benchmark returns.

    Returns:
        Beta as a float.
    """
    if not isinstance(portfolio_returns, pd.Series):
        raise ValueError("portfolio_returns must be a pandas Series.")
    if not isinstance(benchmark_returns, pd.Series):
        raise ValueError("benchmark_returns must be a pandas Series.")
    if portfolio_returns.empty:
        raise ValueError("portfolio_returns is empty.")
    if benchmark_returns.empty:
        raise ValueError("benchmark_returns is empty.")

    port, bench = _align_returns(portfolio_returns, benchmark_returns)

    if len(port) < 2:
        raise ValueError(
            f"Not enough overlapping observations after alignment: {len(port)}. Need at least 2."
        )

    bench_variance = np.var(bench, ddof=1)
    if bench_variance == 0:
        raise ValueError("Benchmark variance is zero — cannot calculate beta.")

    covariance = np.cov(port, bench, ddof=1)[0, 1]
    return float(covariance / bench_variance)
