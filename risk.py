"""Downside and tail-risk metrics for a portfolio."""

import pandas as pd


def calculate_drawdown(portfolio_returns: pd.Series) -> pd.Series:
    """Calculate the drawdown series from portfolio returns.

    Args:
        portfolio_returns: Series of daily portfolio returns.

    Returns:
        Series of drawdown values (negative floats).
    """
    raise NotImplementedError


def maximum_drawdown(portfolio_returns: pd.Series) -> float:
    """Calculate the maximum drawdown over the full period.

    Args:
        portfolio_returns: Series of daily portfolio returns.

    Returns:
        Maximum drawdown as a negative float.
    """
    raise NotImplementedError


def historical_var(
    portfolio_returns: pd.Series, confidence_level: float = 0.95
) -> float:
    """Calculate historical Value at Risk (VaR).

    Args:
        portfolio_returns: Series of daily portfolio returns.
        confidence_level: Confidence level (e.g. 0.95 for 95%).

    Returns:
        VaR as a negative float representing the loss threshold.
    """
    raise NotImplementedError


def historical_cvar(
    portfolio_returns: pd.Series, confidence_level: float = 0.95
) -> float:
    """Calculate historical Conditional VaR (CVaR / Expected Shortfall).

    Args:
        portfolio_returns: Series of daily portfolio returns.
        confidence_level: Confidence level (e.g. 0.95 for 95%).

    Returns:
        CVaR as a negative float representing the expected tail loss.
    """
    raise NotImplementedError


def worst_days(portfolio_returns: pd.Series, n: int = 5) -> pd.Series:
    """Return the n worst daily returns.

    Args:
        portfolio_returns: Series of daily portfolio returns.
        n: Number of worst days to return.

    Returns:
        Series of the n lowest daily returns, sorted ascending.
    """
    raise NotImplementedError
