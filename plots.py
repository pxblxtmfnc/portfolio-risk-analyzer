"""Generate and save portfolio charts to the outputs/ folder."""

import os

import matplotlib.pyplot as plt
import pandas as pd


def _ensure_dir(path: str) -> None:
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)


def plot_cumulative_returns(
    portfolio_returns: pd.Series, output_path: str
) -> None:
    """Save a cumulative returns chart to disk."""
    if portfolio_returns.empty:
        raise ValueError("portfolio_returns is empty.")

    _ensure_dir(output_path)

    cumulative = (1 + portfolio_returns).cumprod()

    fig, ax = plt.subplots()
    ax.plot(cumulative.index, cumulative.values)
    ax.set_title("Cumulative Portfolio Returns")
    ax.set_xlabel("Date")
    ax.set_ylabel("Growth of $1")
    ax.grid(True)

    plt.savefig(output_path, bbox_inches="tight")
    plt.close()


def plot_drawdown(drawdown: pd.Series, output_path: str) -> None:
    """Save a drawdown chart to disk."""
    if drawdown.empty:
        raise ValueError("drawdown is empty.")

    _ensure_dir(output_path)

    fig, ax = plt.subplots()
    ax.plot(drawdown.index, drawdown.values)
    ax.set_title("Portfolio Drawdown")
    ax.set_xlabel("Date")
    ax.set_ylabel("Drawdown")
    ax.grid(True)

    plt.savefig(output_path, bbox_inches="tight")
    plt.close()


def plot_return_distribution(
    portfolio_returns: pd.Series, output_path: str
) -> None:
    """Save a return distribution histogram to disk."""
    if portfolio_returns.empty:
        raise ValueError("portfolio_returns is empty.")

    _ensure_dir(output_path)

    fig, ax = plt.subplots()
    ax.hist(portfolio_returns.values, bins=50, edgecolor="black")
    ax.set_title("Portfolio Return Distribution")
    ax.set_xlabel("Daily Return")
    ax.set_ylabel("Frequency")
    ax.grid(True)

    plt.savefig(output_path, bbox_inches="tight")
    plt.close()
