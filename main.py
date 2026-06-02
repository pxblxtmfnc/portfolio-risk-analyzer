"""CLI entry point for Portfolio Risk Analyzer."""

import argparse


def parse_args() -> argparse.Namespace:
    """Define and parse CLI arguments.

    Returns:
        Namespace object with all parsed arguments.
    """
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
    return parser.parse_args()


def main() -> None:
    """Run the Portfolio Risk Analyzer."""
    args = parse_args()

    print("Portfolio Risk Analyzer")
    print("-" * 40)
    print(f"Tickers:        {args.tickers}")
    print(f"Weights:        {args.weights}")
    print(f"Start:          {args.start}")
    print(f"End:            {args.end}")
    print(f"Risk-free rate: {args.risk_free_rate}")
    print(f"Benchmark:      {args.benchmark}")
    print("-" * 40)
    print("(Calculations not yet implemented.)")


if __name__ == "__main__":
    main()
