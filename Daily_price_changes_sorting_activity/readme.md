# Algorithmic Complexity Analysis: Gold Price Sorting

## Overview
This project validates the time complexity of sorting algorithms using real-world financial data. By benchmarking `numpy.sort` against daily gold price fluctuations, we empirically verify the theoretical $O(n \log n)$ complexity curve.

## Key Features
- **Real-World Data:** Uses daily Open-High-Low-Close (OHLC) gold price data to calculate volatility deltas.
- **Performance Benchmarking:** Utilizes `time.perf_counter` for high-precision measurement of sorting operations.
- **Complexity Fitting:** Fits empirical timing data against the theoretical $n \log n$ curve to validate algorithmic efficiency.

## Files
- `pricesortingactivity.py`: The main script for calculating deltas, running benchmarks, and plotting results.
- `gold_price.csv`: Raw historical gold price data.
- `daily_sorting_activity.png`: Output visualization comparing measured times vs. theoretical predictions.

## Usage
Run the analysis script to generate the complexity graph:

```bash
python pricesortingactivity.py