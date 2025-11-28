# Global Inequality Forecasting & Polynomial Regression

## Overview
An analysis of global income inequality trends using polynomial regression. This project fits various polynomial models (degrees 1–15) to historical Gini index data (1820–1980) to evaluate their predictive power for post-1980 trends.

## Key Features
- **Model Selection:** Implements Reduced Chi-Squared ($\chi^2_\nu$) and Bayesian Information Criterion (BIC) to identify the optimal polynomial order.
- **Bias-Variance Tradeoff:** Visualizes the concepts of underfitting (Order 1) versus overfitting (Order 7+) on historical data.
- **Forecasting:** Tests the selected models against "unseen" reality data from 1980–1992.

## Files
- `forecastgraph.py`: Main script for data loading, model fitting, and plotting.
- `global-inequality.csv`: Historical dataset of global inequality metrics.
- `polynomial_comparison.png`: Visualization of Chi-Squared and BIC scores per model order.

## Usage
Run the script to generate the model comparison and forecast plots:

```bash
python forecastgraph.py