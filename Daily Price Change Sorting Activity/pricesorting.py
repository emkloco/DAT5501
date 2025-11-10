import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# 1. Load CSV (replace 'gold_prices.csv' with your file)
df = pd.read_csv('gold_prices.csv')

# Assuming your CSV has a column named 'Price'
prices = df['Close/Last'].values

# 2. Calculate daily changes
delta_p = np.diff(prices)  # P[n+1] - P[n]

# 3. Measure sort times
n_values = range(7, len(delta_p)+1)  # from 7 to max
sort_times = []

for n in n_values:
    subset = delta_p[:n]
    start = time.perf_counter()
    sorted_subset = np.sort(subset)
    end = time.perf_counter()
    sort_times.append(end - start)

# 4. Plot T vs n
plt.figure(figsize=(10,6))
plt.plot(n_values, sort_times, label='Sort Time')
plt.xlabel('Number of daily changes (n)')
plt.ylabel('Time to sort (seconds)')
plt.title('Time to Sort Daily Price Changes')
plt.grid(True)
plt.legend()
plt.show()