"""CLI entry point for Portfolio Risk Analyzer."""

import argparse
import os
import sys
from datetime import datetime

import pandas as pd

import benchmark as bench_module
import data_loader
import metrics
import plots
import risk


def parse_args() -> argparse.Namespace:
    """Define and parse CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Analyze the historical risk of an investment portfolio."
    )
    parser.add_argument(
        "--tickers",
        nargs="+",
        required=True,
        metavar="TICKER",
        help="Space-separated list of ticker symbols (e.g. AAPL MSFT NVDA).",
    )
    parser.add_argument(
        "--weights",
        nargs="+",
        type=float,
        required=True,
        metavar="WEIGHT",
        help="Portfolio weights matching each ticker, must sum to 1 (e.g. 0.3 0.3 0.4).",
    )
    parser.add_argument(
        "--start",
        required=True,
        metavar="YYYY-MM-DD",
        help="Start date for historical data.",
    )
    parser.add_argument(
        "--end",
        required=True,
        metavar="YYYY-MM-DD",
        help="End date for historical data.",
    )
    parser.add_argument(
        "--risk-free-rate",
        type=float,
        default=0.0,
        metavar="RATE",
        help="Annual risk-free rate as a decimal (e.g. 0.02 for 2%%). Default: 0.0.",
    )
    parser.add_argument(
        "--benchmark",
        default=None,
        metavar="TICKER",
        help="Optional benchmark ticker for comparison (e.g. SPY).",
    )
    parser.add_argument(
        "--output-dir",
        default="outputs",
        metavar="DIR",
        help="Directory to save output charts. Default: outputs.",
    )
    return parser.parse_args()


def validate_cli_inputs(args: argparse.Namespace) -> None:
    """Validate CLI arguments and raise ValueError with a clear message if invalid."""
    if len(args.tickers) != len(args.weights):
        raise ValueError(
            f"Number of tickers ({len(args.tickers)}) must match number of weights "
            f"({len(args.weights)})."
        )

    weights_sum = sum(args.weights)
    if abs(weights_sum - 1.0) > 1e-6:
        raise ValueError(f"Weights must sum to 1.0, but got {weights_sum:.6f}.")

    try:
        start_dt = datetime.strptime(args.start, "%Y-%m-%d")
        end_dt = datetime.strptime(args.end, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Dates must be in YYYY-MM-DD format.")

    if start_dt >= end_dt:
        raise ValueError(
            f"Start date ({args.start}) must be earlier than end date ({args.end})."
        )

    if args.risk_free_rate < 0:
        raise ValueError("Risk-free rate must be a non-negative value.")


def fmt_pct(value: float) -> str:
    """Format a decimal as a percentage string (e.g. 0.1523 → '15.23%')."""
    return f"{value * 100:.2f}%"


def print_summary(
    tickers: list[str],
    weights: list[float],
    start: str,
    end: str,
    ann_ret: float,
    ann_vol: float,
    s_ratio: float,
    max_dd: float,
    var_95: float,
    cvar_95: float,
    worst: pd.Series,
    benchmark_ticker: str | None = None,
    beta: float | None = None,
) -> None:
    """Print a formatted portfolio risk summary to the terminal."""
    print()
    print("Portfolio Risk Analyzer")
    print("=======================")
    print()
    print("Portfolio:")
    print(f"  Tickers : {', '.join(tickers)}")
    print(f"  Weights : {', '.join(f'{w * 100:.2f}%' for w in weights)}")
    print(f"  Period  : {start} to {end}")
    print()
    print("Performance Metrics:")
    print(f"  Annualized Return     : {fmt_pct(ann_ret)}")
    print(f"  Annualized Volatility : {fmt_pct(ann_vol)}")
    print(f"  Sharpe Ratio          : {s_ratio:.2f}")
    print()
    print("Risk Metrics:")
    print(f"  Maximum Drawdown    : {fmt_pct(max_dd)}")
    print(f"  Historical VaR  95% : {fmt_pct(var_95)}")
    print(f"  Historical CVaR 95% : {fmt_pct(cvar_95)}")
    print()

    if benchmark_ticker is not None and beta is not None:
        print("Benchmark:")
        print(f"  Benchmark         : {benchmark_ticker}")
        print(f"  Beta vs Benchmark : {beta:.2f}")
        print()

    print("Worst 5 Days:")
    for date, ret in worst.items():
        print(f"  {date.strftime('%Y-%m-%d')}  {fmt_pct(ret)}")
    print()


def main() -> None:
    """Run the Portfolio Risk Analyzer CLI."""
    args = parse_args()

    try:
        validate_cli_inputs(args)

        os.makedirs(args.output_dir, exist_ok=True)

        # Portfolio data
        print("Downloading portfolio data...")
        prices = data_loader.download_adjusted_prices(args.tickers, args.start, args.end)
        log_returns = metrics.calculate_log_returns(prices)
        port_returns = metrics.calculate_portfolio_returns(log_returns, args.weights)

        # Performance metrics
        ann_ret = metrics.annualized_return(port_returns)
        ann_vol = metrics.annualized_volatility(port_returns)
        s_ratio = metrics.sharpe_ratio(port_returns, args.risk_free_rate)

        # Risk metrics
        drawdown = risk.calculate_drawdown(port_returns)
        max_dd = risk.maximum_drawdown(port_returns)
        var_95 = risk.historical_var(port_returns)
        cvar_95 = risk.historical_cvar(port_returns)
        worst = risk.worst_days(port_returns)

        # Benchmark (optional)
        beta: float | None = None
        if args.benchmark:
            print("Downloading benchmark data...")
            bench_prices = data_loader.download_adjusted_prices(
                [args.benchmark], args.start, args.end
            )
            bench_log_returns = metrics.calculate_log_returns(bench_prices)
            bench_series = bench_log_returns.iloc[:, 0]
            beta = bench_module.calculate_beta(port_returns, bench_series)

        # Plots
        print("Saving charts...")
        plots.plot_cumulative_returns(
            port_returns,
            os.path.join(args.output_dir, "cumulative_returns.png"),
        )
        plots.plot_drawdown(
            drawdown,
            os.path.join(args.output_dir, "drawdown.png"),
        )
        plots.plot_return_distribution(
            port_returns,
            os.path.join(args.output_dir, "return_distribution.png"),
        )

        # Summary
        print_summary(
            tickers=args.tickers,
            weights=args.weights,
            start=args.start,
            end=args.end,
            ann_ret=ann_ret,
            ann_vol=ann_vol,
            s_ratio=s_ratio,
            max_dd=max_dd,
            var_95=var_95,
            cvar_95=cvar_95,
            worst=worst,
            benchmark_ticker=args.benchmark,
            beta=beta,
        )

        print(f"Charts saved to: {args.output_dir}/")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
