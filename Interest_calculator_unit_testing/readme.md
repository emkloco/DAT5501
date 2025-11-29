# Compound Interest Financial Modeler

## Overview
This project implements a financial forecasting tool to project savings growth over time. It calculates year-on-year compound interest and algorithmically determines the time required for a principal investment to double in value. It is built using Test-Driven Development (TDD) principles.

## Key Features
- **Financial Modeling:** Implements the compound interest formula to project annual growth.
- **Doubling Logic:** Uses iterative logic to calculate the precise "doubling time" of an investment.
- **Robust Testing:** Includes a comprehensive unit test suite to verify mathematical accuracy against standard financial rules.

## Files
- `interest_calculator.py`: The main script that performs the calculations and prints the financial schedule.
- `test_interest_calculator.py`: The unit test suite using `unittest` to validate the logic.

## Usage
Run the main calculator:

```bash
python interest_calculator.py


Run the automated tests:

code
Bash
python test_interest_calculator.py