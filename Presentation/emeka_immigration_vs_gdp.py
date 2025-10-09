import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os

# --- 1. data loading and preparation ---

# get the absolute path of the directory where this script is located.
script_dir = os.path.dirname(os.path.abspath(__file__))

# join the script's directory path with the CSV filename to create a full, reliable path.
csv_file_path = os.path.join(script_dir, 'immigration_gdp_data.csv')

try:
    # load the data directly from your local CSV file.
    df = pd.read_csv(csv_file_path)
except FileNotFoundError:
    print(f"Error: Could not find 'immigration_gdp_data.csv'.")
    print(f"Looked for it at this location: {csv_file_path}")
    print("Please make sure the CSV file is in the same folder as the Python script.")
    exit()

# set 'Year' as the index for easier plotting
df = df.set_index('Year')

# interpolate the Immigrant Population data to create a smooth line for visualization
df['Immigrant_Population'] = df['Immigrant_Population'].interpolate(method='linear')


# --- 2. plotting the graph ---

# set up the figure and the primary axis (for Immigration)
fig, ax1 = plt.subplots(figsize=(15, 9))

# plot Immigrant Population on the primary axis (ax1)
color1 = 'tab:blue'
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Immigrant Population (in millions)', color=color1, fontsize=14)
ax1.plot(df.index, df['Immigrant_Population'], color=color1, linewidth=3, label='Immigrant Population')
ax1.tick_params(axis='y', labelcolor=color1, labelsize=12)
ax1.tick_params(axis='x', labelsize=12)
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, pos: f'{x/1e6:.1f}M'))

# create the secondary axis for the actual GDP Per Capita value
ax2 = ax1.twinx()
color2 = 'tab:red'
ax2.set_ylabel('GDP Per Capita (Value)', color=color2, fontsize=14) # UPDATED LABEL
# PLOT THE ACTUAL 'GDP_per_Capita' COLUMN
ax2.plot(df.index, df['GDP_per_Capita'], color=color2, linestyle='--', marker='o', markersize=4, label='GDP Per Capita') # UPDATED PLOT
ax2.tick_params(axis='y', labelcolor=color2, labelsize=12)
# format the y-axis to show thousands (e.g., 40k)
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, pos: f'{x/1e3:.0f}k'))


# --- 3. adding sophistication (titles, legend, annotations) ---

# title
plt.title('UK Immigrant Population vs. GDP Per Capita (1990-2023)', fontsize=18, pad=20) # UPDATED TITLE

# unified legend for both axes
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=12)

# annotations for key events
# 2008 financial crisis
ax1.axvline(x=2008, color='k', linestyle='--', linewidth=1, alpha=0.7)
ax1.annotate('2008\nFinancial\nCrisis', xy=(2008, 48963), xycoords=ax2.get_yaxis_transform(), # Use ax2 coordinates for y
             xytext=(2006, 0.85), textcoords='axes fraction', # Position annotation relative to axis
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
             ha='center', fontsize=11, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=0.5))

# 2016 brexit referendum
ax1.axvline(x=2016, color='k', linestyle='--', linewidth=1, alpha=0.7)
ax1.annotate('2016\nBrexit\nReferendum', xy=(2016, 9.36e6), xytext=(2013, 10.5e6),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
             ha='center', fontsize=11, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=0.5))

# 2020 COVID-19 pandemic
ax1.axvline(x=2020, color='k', linestyle='--', linewidth=1, alpha=0.7)
ax1.annotate('2020\nCOVID-19\nPandemic', xy=(2020, 47144), xycoords=ax2.get_yaxis_transform(), # Use ax2 coordinates for y
             xytext=(2018.5, 0.5), textcoords='axes fraction', # Position annotation
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
             ha='right', fontsize=11, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=0.5))


# final touches
fig.tight_layout()
plt.grid(True, which='both', linestyle=':', linewidth=0.7)
plt.show()