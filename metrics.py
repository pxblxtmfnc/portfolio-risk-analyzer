"""Standard return and performance metrics for a portfolio."""

import pandas as pd


def calculate_log_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """Calculate daily log returns from a price DataFrame.

    Args:
        prices: DataFrame of adjusted close prices indexed by date.

    Returns:
        DataFrame of daily log returns.
    """
    raise NotImplementedError


def calculate_portfolio_returns(
    returns: pd.DataFrame, weights: list[float]
) -> pd.Series:
    """Compute weighted portfolio returns from individual asset returns.

    Args:
        returns: DataFrame of daily log returns.
        weights: List of portfolio weights that must sum to 1.

    Returns:
        Series of daily portfolio returns.
    """
    raise NotImplementedError


def annualized_return(
    portfolio_returns: pd.Series, trading_days: int = 252
) -> float:
    """Calculate the annualized portfolio return.

    Args:
        portfolio_returns: Series of daily portfolio returns.
        trading_days: Number of trading days per year.

    Returns:
        Annualized return as a float.
    """
    raise NotImplementedError


def annualized_volatility(
    portfolio_returns: pd.Series, trading_days: int = 252
) -> float:
    """Calculate the annualized portfolio volatility (standard deviation).

    Args:
        portfolio_returns: Series of daily portfolio returns.
        trading_days: Number of trading days per year.

    Returns:
        Annualized volatility as a float.
    """
    raise NotImplementedError


def sharpe_ratio(
    portfolio_returns: pd.Series,
    risk_free_rate: float,
    trading_days: int = 252,
) -> float:
    """Calculate the annualized Sharpe Ratio.

    Args:
        portfolio_returns: Series of daily portfolio returns.
        risk_free_rate: Annual risk-free rate (e.g. 0.02 for 2%).
        trading_days: Number of trading days per year.

    Returns:
        Sharpe Ratio as a float.
    """
    raise NotImplementedError
