"""Standard return and performance metrics for a portfolio."""

import numpy as np
import pandas as pd


def calculate_log_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """Calculate daily log returns from a price DataFrame."""
    if prices.empty:
        raise ValueError("prices DataFrame is empty.")
    if not all(pd.api.types.is_numeric_dtype(prices[col]) for col in prices.columns):
        raise ValueError("prices DataFrame must contain only numeric data.")
    returns = np.log(prices / prices.shift(1))
    return returns.dropna()


def calculate_portfolio_returns(
    returns: pd.DataFrame, weights: list[float]
) -> pd.Series:
    """Compute weighted portfolio returns from individual asset returns."""
    if returns.empty:
        raise ValueError("returns DataFrame is empty.")
    if not weights:
        raise ValueError("weights list is empty.")
    if len(weights) != returns.shape[1]:
        raise ValueError(
            f"Number of weights ({len(weights)}) must match number of assets ({returns.shape[1]})."
        )
    if abs(sum(weights) - 1.0) > 1e-6:
        raise ValueError(f"Weights must sum to 1.0, got {sum(weights):.6f}.")
    weights_array = np.array(weights)
    return returns.dot(weights_array)


def annualized_return(
    portfolio_returns: pd.Series, trading_days: int = 252
) -> float:
    """Calculate the annualized portfolio return."""
    if portfolio_returns.empty:
        raise ValueError("portfolio_returns Series is empty.")
    return float(portfolio_returns.mean() * trading_days)


def annualized_volatility(
    portfolio_returns: pd.Series, trading_days: int = 252
) -> float:
    """Calculate the annualized portfolio volatility (standard deviation)."""
    if portfolio_returns.empty:
        raise ValueError("portfolio_returns Series is empty.")
    return float(portfolio_returns.std() * np.sqrt(trading_days))


def sharpe_ratio(
    portfolio_returns: pd.Series,
    risk_free_rate: float,
    trading_days: int = 252,
) -> float:
    """Calculate the annualized Sharpe Ratio."""
    if portfolio_returns.empty:
        raise ValueError("portfolio_returns Series is empty.")
    ann_ret = annualized_return(portfolio_returns, trading_days)
    ann_vol = annualized_volatility(portfolio_returns, trading_days)
    if ann_vol == 0.0:
        raise ValueError("Annualized volatility is zero; Sharpe Ratio is undefined.")
    return (ann_ret - risk_free_rate) / ann_vol
