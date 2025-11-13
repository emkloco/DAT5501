import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time import perf_counter

# load cleaned CSV
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'gold_prices.csv')
df = pd.read_csv(csv_path)

# convert to numeric, get daily change
df['Close/Last'] = pd.to_numeric(df['Close/Last'], errors='coerce')
delta = df['Close/Last'].diff().dropna().to_numpy()

# test sorting time
max_n = min(365, len(delta))
ns = np.arange(7, max_n + 1)
times = []

for n in ns:
    arr = delta[:n].astype(float)
    np.sort(arr)  # warm-up
    repeats = 20
    t0 = perf_counter()
    for _ in range(repeats):
        _ = np.sort(arr)
    times.append((perf_counter() - t0) / repeats)

ns = np.array(ns)
times = np.array(times)

# fit to n·log2(n)
nlog = ns * np.log2(ns)
c = (times @ nlog) / (nlog @ nlog)
pred = c * nlog

# plot
plt.figure(figsize=(8,5))
plt.plot(ns, times, 'o-', label='Measured')
plt.plot(ns, pred, '--', label=f'n·log2(n), c={c:.3e}')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Sort time vs n (ΔP)')
plt.legend()
plt.grid(True)
plt.tight_layout()

out = os.path.join(script_dir, 'daily_sorting_activity.png')
plt.savefig(out)
print(f'Saved plot: {out}')
print(f'n: {ns[0]}..{ns[-1]}, c={c:.3e}')
print(f'Mean T/(n·log2 n): {np.mean(times/nlog):.3e}')