Gold Price Sorting Activity
Verifying the time complexity of sorting algorithms using real-world market data.

I grabbed daily gold price changes (deltas), ran benchmarks on numpy.sort with increasing dataset sizes, and fitted the empirical timing results against the theoretical curve to see how well they align.

Content:

pricesortingactivity.py: The script. It calculates the price differentials, times the sorting operation using perf_counter, and plots the measured time vs. the expected complexity.

gold_price.csv: The raw OHLC price data.

daily_sorting_activity.png: The resulting plot showing the fit between the actual sort times and the model.


To run:

You'll need pandas, numpy, and matplotlib.

Run the script:
python pricesortingactivity.py

It generates the plot in the same folder.