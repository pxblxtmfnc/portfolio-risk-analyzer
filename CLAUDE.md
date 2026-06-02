# CLAUDE.md

## Project Overview

This project is a Python CLI tool called **Portfolio Risk Analyzer**.

The goal is to analyze the historical risk of an investment portfolio using real market data. The user provides tickers, portfolio weights, start and end dates, risk-free rate, and an optional benchmark. The program calculates portfolio risk metrics and saves visual outputs.

This project is built for learning purposes and should remain clean, modular, and suitable for a GitHub / LinkedIn portfolio.

## Main Learning Goals

* Practice Python applied to finance.
* Learn how to structure a financial analytics project.
* Improve Claude Code workflow.
* Work in small validated phases.
* Avoid asking the AI to build the entire project at once.
* Keep the code readable, testable, and presentable.

## Tech Stack

Use:

* Python 3.10+
* pandas
* numpy
* matplotlib
* yfinance
* argparse

Do not introduce additional dependencies unless explicitly requested.

## Project Structure

Expected structure:

```text
.
├── CLAUDE.md
├── data_loader.py
├── metrics.py
├── risk.py
├── benchmark.py
├── plots.py
├── main.py
├── outputs/
├── requirements.txt
├── README.md
└── .gitignore
```

## Module Responsibilities

### data_loader.py

Responsible only for downloading and cleaning market price data.

Expected responsibilities:

* Download adjusted close prices with yfinance.
* Return clean pandas DataFrames.
* Validate missing data.
* Raise clear ValueError messages when data cannot be downloaded or inputs are invalid.

Do not calculate portfolio metrics here.

### metrics.py

Responsible for standard return and performance metrics.

Expected responsibilities:

* Calculate log returns.
* Calculate portfolio returns.
* Calculate annualized return.
* Calculate annualized volatility.
* Calculate Sharpe Ratio.

Do not download data here.

### risk.py

Responsible for downside and tail-risk metrics.

Expected responsibilities:

* Calculate drawdown series.
* Calculate maximum drawdown.
* Calculate historical Value at Risk.
* Calculate historical CVaR / Expected Shortfall.
* Identify worst daily returns.

Do not create plots here.

### benchmark.py

Responsible for benchmark-related analysis.

Expected responsibilities:

* Calculate benchmark returns.
* Calculate benchmark metrics.
* Calculate portfolio beta versus the benchmark.

Do not download portfolio data here unless explicitly requested by the current task.

### plots.py

Responsible only for generating and saving charts.

Expected responsibilities:

* Save plots into the `outputs/` folder.
* Use `plt.savefig(...)`.
* Use `plt.close()` after saving each chart.
* Never open interactive Matplotlib windows.
* Do not calculate financial metrics here.

### main.py

Responsible for the CLI and overall workflow.

Expected responsibilities:

* Parse arguments using argparse.
* Validate CLI inputs.
* Call the other modules in the correct order.
* Print a clean summary of the results.
* Save charts to `outputs/`.

Do not place complex calculation logic directly in main.py.

## Coding Standards

Use:

* Type hints.
* Short docstrings.
* Clear function names.
* Small functions.
* Explicit input validation.
* Clear ValueError messages.
* Clean imports.

Avoid:

* Overengineering.
* Unnecessary classes.
* Hidden global state.
* Mixing responsibilities between files.
* Printing from utility modules unless explicitly needed.
* Opening Matplotlib windows.
* Implementing multiple phases at once.

## Development Workflow

Work in small phases.

Before writing code for a new phase:

1. Briefly explain what will be changed.
2. Modify only the files required for that phase.
3. Keep the implementation minimal but correct.
4. After each phase, provide validation commands.
5. Do not move to the next phase until the current phase is validated.

## Phase Plan

### Phase 1: Project skeleton

Create the file structure and placeholders only.

No complex financial logic yet.

### Phase 2: Data loading

Implement `data_loader.py`.

### Phase 3: Portfolio metrics

Implement `metrics.py`.

### Phase 4: Risk metrics

Implement `risk.py`.

### Phase 5: Benchmark analysis

Implement `benchmark.py`.

### Phase 6: Plotting

Implement `plots.py`.

### Phase 7: CLI integration

Implement `main.py`.

### Phase 8: README polish

Improve README for GitHub and LinkedIn presentation.

## CLI Target Example

Final intended usage:

```bash
python main.py --tickers AAPL MSFT NVDA --weights 0.3 0.3 0.4 --start 2020-01-01 --end 2024-01-01 --risk-free-rate 0.02 --benchmark SPY
```

## Output Requirements

The final program should:

* Print portfolio metrics in the terminal.
* Print benchmark comparison if a benchmark is provided.
* Save charts to `outputs/`.
* Never open plot windows.
* Fail gracefully with clear error messages.

## Important Constraints

Do not implement the full project in one step.

When asked to work on a phase, only work on that phase.

If a change requires modifying more files than expected, explain why before doing it.

Prefer simple, readable code over clever code.

This is a learning project, not a production-grade financial system.
