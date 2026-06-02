"""Generate and save portfolio charts to the outputs/ folder."""

import pandas as pd


def plot_cumulative_returns(
    portfolio_returns: pd.Series, output_path: str
) -> None:
    """Save a cumulative returns chart to disk.

    Args:
        portfolio_returns: Series of daily portfolio returns.
        output_path: File path to save the chart (e.g. 'outputs/cumulative.png').
    """
    raise NotImplementedError


def plot_drawdown(drawdown: pd.Series, output_path: str) -> None:
    """Save a drawdown chart to disk.

    Args:
        drawdown: Series of drawdown values.
        output_path: File path to save the chart.
    """
    raise NotImplementedError


def plot_return_distribution(
    portfolio_returns: pd.Series, output_path: str
) -> None:
    """Save a return distribution histogram to disk.

    Args:
        portfolio_returns: Series of daily portfolio returns.
        output_path: File path to save the chart.
    """
    raise NotImplementedError
