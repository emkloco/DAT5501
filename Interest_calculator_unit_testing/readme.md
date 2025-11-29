# Compound Interest Financial Modeler

![Language](https://img.shields.io/badge/Python-3.9%2B-blue)
![Status](https://img.shields.io/badge/Status-Tested-green)

## Project Overview
This module demonstrates the application of Python to financial forecasting. It implements a compound interest calculator that projects savings growth over time and algorithmically determines the "doubling time" of an investment.

The project emphasizes **Test-Driven Development (TDD)**, utilizing a robust unit test suite to verify mathematical accuracy against standard financial formulas (e.g., Rule of 72).

## Module Highlights

### 1. Financial Growth Projection
**Key Skills:** Mathematical Modeling, Iterative Logic.
- Implements the compound interest formula $A = P(1 + r)^t$ to project year-on-year growth.
- Outputs a formatted financial schedule to the console.

### 2. Algorithmic Forecasting
**Key Skills:** While-Loop Logic, Conditional Flow.
- Calculates the precise number of years required for the principal investment to double in value.
- Handles edge cases dynamically (e.g., high interest rates vs. low interest rates).

### 3. Automated Quality Assurance
**Key Skills:** Unit Testing, `unittest` Framework.
- Validates logic against known financial constants.
- Ensures the model scales correctly regardless of principal size ($1 vs $1,000,000).

## Usage

**1. Run the Calculator:**
```bash
python interest_calculator.py