"""Downside and tail-risk metrics for a portfolio."""

import numpy as np
import pandas as pd


def calculate_drawdown(portfolio_returns: pd.Series) -> pd.Series:
    """Calculate the drawdown series from portfolio returns."""
    if portfolio_returns.empty:
        raise ValueError("portfolio_returns is empty.")

    cumulative = (1 + portfolio_returns).cumprod()
    running_peak = cumulative.cummax()
    return (cumulative / running_peak) - 1


def maximum_drawdown(portfolio_returns: pd.Series) -> float:
    """Return the maximum (worst) drawdown over the full period."""
    if portfolio_returns.empty:
        raise ValueError("portfolio_returns is empty.")

    return float(calculate_drawdown(portfolio_returns).min())


def historical_var(
    portfolio_returns: pd.Series,
    confidence_level: float = 0.95,
) -> float:
    """Return historical Value at Risk as a positive loss figure."""
    if portfolio_returns.empty:
        raise ValueError("portfolio_returns is empty.")
    if not (0 < confidence_level < 1):
        raise ValueError("confidence_level must be between 0 and 1.")

    var_threshold = np.percentile(portfolio_returns, (1 - confidence_level) * 100)
    return abs(float(var_threshold))


def historical_cvar(
    portfolio_returns: pd.Series,
    confidence_level: float = 0.95,
) -> float:
    """Return historical CVaR (Expected Shortfall) as a positive loss figure."""
    if portfolio_returns.empty:
        raise ValueError("portfolio_returns is empty.")
    if not (0 < confidence_level < 1):
        raise ValueError("confidence_level must be between 0 and 1.")

    var_threshold = np.percentile(portfolio_returns, (1 - confidence_level) * 100)
    tail_losses = portfolio_returns[portfolio_returns <= var_threshold]

    if tail_losses.empty:
        raise ValueError("No tail losses found below the VaR threshold.")

    return abs(float(tail_losses.mean()))


def worst_days(portfolio_returns: pd.Series, n: int = 5) -> pd.Series:
    """Return the n worst daily returns, sorted from worst to least bad."""
    if portfolio_returns.empty:
        raise ValueError("portfolio_returns is empty.")
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")

    return portfolio_returns.nsmallest(n)
