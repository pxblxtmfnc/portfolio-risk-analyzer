# Portfolio Risk Analyzer

A Python command-line tool for analyzing the historical risk and performance of an investment portfolio using real market data.

This project was built as a finance-focused Python learning project and as a clean portfolio piece for GitHub and LinkedIn. It combines market data extraction, portfolio return calculation, risk metrics, benchmark analysis, and automated chart generation.

![Cumulative Returns](assets/cumulative_returns.png)
![Drawdown](assets/drawdown.png)
![Return Distribution](assets/return_distribution.png)

---

## Overview

Portfolio Risk Analyzer allows users to build a custom portfolio from selected tickers, assign weights, and evaluate its historical performance over a chosen time period.

The tool calculates key return and risk metrics commonly used in investment analysis, including annualized return, volatility, Sharpe Ratio, maximum drawdown, Value at Risk, Conditional Value at Risk, and beta against a benchmark.

It is designed to be simple to run from the terminal while still producing meaningful financial insights and visual outputs.

---

## Key Features

* Downloads historical market data using `yfinance`
* Calculates daily log returns for individual assets
* Aggregates asset returns into a weighted portfolio
* Computes annualized return and annualized volatility
* Calculates Sharpe Ratio using a configurable risk-free rate
* Measures drawdowns and maximum drawdown
* Estimates historical Value at Risk, VaR
* Estimates Conditional Value at Risk, CVaR / Expected Shortfall
* Identifies the worst daily portfolio returns
* Compares portfolio performance against a benchmark
* Calculates portfolio beta relative to the selected benchmark
* Generates charts for cumulative returns, drawdown, and return distribution

---

## Example Use Case

An investor wants to analyze a portfolio made up of Apple, Microsoft, and Nvidia between 2020 and 2024, compare it against the S&P 500 ETF, and understand both its performance and downside risk.

This tool allows the user to run that analysis directly from the command line and generate both numerical metrics and visual charts.

---

## Installation

Clone the repository and create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the CLI with the desired tickers, portfolio weights, date range, risk-free rate, and benchmark:

```bash
python main.py \
  --tickers AAPL MSFT NVDA \
  --weights 0.3 0.3 0.4 \
  --start 2020-01-01 \
  --end 2024-01-01 \
  --risk-free-rate 0.02 \
  --benchmark SPY
```

Example parameters:

| Argument           | Description                                               |
| ------------------ | --------------------------------------------------------- |
| `--tickers`        | List of portfolio assets                                  |
| `--weights`        | Portfolio weights assigned to each asset                  |
| `--start`          | Start date for the historical analysis                    |
| `--end`            | End date for the historical analysis                      |
| `--risk-free-rate` | Annual risk-free rate used for Sharpe Ratio calculation   |
| `--benchmark`      | Benchmark ticker used for comparison and beta calculation |

---

## Outputs

The tool produces:

1. Portfolio performance metrics
2. Risk and downside metrics
3. Benchmark comparison metrics
4. Saved charts for visual analysis

Generated charts include:

* Cumulative portfolio returns
* Portfolio drawdown over time
* Distribution of daily portfolio returns

Charts are saved locally and can be used in reports, GitHub documentation, or portfolio presentations.

---

## Metrics Included

### Performance Metrics

* Daily portfolio returns
* Annualized return
* Annualized volatility
* Sharpe Ratio

### Risk Metrics

* Drawdown series
* Maximum drawdown
* Historical Value at Risk, VaR
* Conditional Value at Risk, CVaR / Expected Shortfall
* Worst daily returns

### Benchmark Metrics

* Benchmark cumulative returns
* Portfolio vs benchmark comparison
* Portfolio beta

---

## Project Structure

```text
.
├── CLAUDE.md              # Project instructions for Claude Code
├── data_loader.py         # Downloads and cleans historical market data
├── metrics.py             # Return and performance metrics
├── risk.py                # Downside risk and tail-risk metrics
├── benchmark.py           # Benchmark comparison and beta calculation
├── plots.py               # Chart generation
├── main.py                # CLI entry point
├── assets/                # Images used in the README
├── outputs/               # Generated charts
├── requirements.txt       # Python dependencies
└── README.md
```

---

## Tech Stack

* Python 3.10+
* pandas
* numpy
* matplotlib
* yfinance

---

## Why I Built This Project

I built this project to strengthen my ability to apply Python to real financial analysis.

The objective was not only to calculate portfolio metrics, but also to structure the project in a clean and understandable way, similar to how a small professional analytics tool would be organized.

This project helped me practice:

* Financial data analysis
* Portfolio risk measurement
* Python project structure
* CLI development
* Data visualization
* Writing clean documentation for technical projects

---

## Current Status

The project is fully functional as a command-line tool.

Completed components:

| Area                         | Status   |
| ---------------------------- | -------- |
| Market data loading          | Complete |
| Portfolio return calculation | Complete |
| Performance metrics          | Complete |
| Risk metrics                 | Complete |
| Benchmark analysis           | Complete |
| Chart generation             | Complete |
| CLI integration              | Complete |
| Documentation                | Complete |

---

## Disclaimer

This project is for educational and portfolio purposes only. It does not provide financial advice, investment recommendations, or trading signals.
