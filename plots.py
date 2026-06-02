"""Generate and save portfolio charts to the outputs/ folder."""

import os

import matplotlib.pyplot as plt
import pandas as pd


def _ensure_dir(path: str) -> None:
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)


def _apply_base_style(ax: plt.Axes, title: str, xlabel: str, ylabel: str) -> None:
    ax.set_title(title, fontsize=14, fontweight="bold", pad=12)
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.tick_params(axis="both", labelsize=9)


def plot_cumulative_returns(
    portfolio_returns: pd.Series, output_path: str
) -> None:
    """Save a cumulative returns line chart to disk."""
    if portfolio_returns.empty:
        raise ValueError("portfolio_returns is empty.")

    _ensure_dir(output_path)

    cumulative = (1 + portfolio_returns).cumprod()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(cumulative.index, cumulative.values, linewidth=2, color="#2563EB")
    _apply_base_style(
        ax,
        title="Portfolio Cumulative Returns",
        xlabel="Date",
        ylabel="Growth of $1 Investment",
    )

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight", dpi=300)
    plt.close()


def plot_drawdown(drawdown: pd.Series, output_path: str) -> None:
    """Save a drawdown chart with filled area to disk."""
    if drawdown.empty:
        raise ValueError("drawdown is empty.")

    _ensure_dir(output_path)

    drawdown_pct = drawdown * 100

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(drawdown_pct.index, drawdown_pct.values, linewidth=1.5, color="#DC2626")
    ax.fill_between(drawdown_pct.index, drawdown_pct.values, 0, alpha=0.3, color="#DC2626")
    ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
    _apply_base_style(
        ax,
        title="Portfolio Drawdown",
        xlabel="Date",
        ylabel="Drawdown (%)",
    )

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight", dpi=300)
    plt.close()


def plot_return_distribution(
    portfolio_returns: pd.Series, output_path: str
) -> None:
    """Save a return distribution histogram with mean line to disk."""
    if portfolio_returns.empty:
        raise ValueError("portfolio_returns is empty.")

    _ensure_dir(output_path)

    mean_return = portfolio_returns.mean()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(
        portfolio_returns.values,
        bins=50,
        color="#2563EB",
        edgecolor="white",
        linewidth=0.4,
        alpha=0.85,
    )
    ax.axvline(0, color="black", linewidth=1.2, linestyle="--", label="Zero")
    ax.axvline(
        mean_return,
        color="#F59E0B",
        linewidth=1.8,
        linestyle="-",
        label=f"Mean ({mean_return:.4f})",
    )
    ax.legend(fontsize=10)
    _apply_base_style(
        ax,
        title="Distribution of Daily Portfolio Returns",
        xlabel="Daily Return",
        ylabel="Frequency",
    )

    plt.tight_layout()
    plt.savefig(output_path, bbox_inches="tight", dpi=300)
    plt.close()
