import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os
from scipy.stats import pearsonr

# --- 1. get the data ready ---

# this whole bit is just to find the csv file properly.
# it finds where this python script is running...
script_dir = os.path.dirname(os.path.abspath(__file__))
# ...and then looks for the csv in that same folder.
# this way you don't get that 'file not found' error.
csv_file_path = os.path.join(script_dir, 'immigration_gdp_data.csv')

# let's try to read the csv
try:
    df = pd.read_csv(csv_file_path)
except FileNotFoundError:
    print(f"error: can't find 'immigration_gdp_data.csv'.")
    print(f"i looked for it here: {csv_file_path}")
    print("just make sure the csv file is in the same folder as this script.")
    exit()

# make 'Year' the index, just makes life easier for plotting
df = df.set_index('Year')

# the immigration data only has points every few years,
# so let's just draw straight lines between them (interpolate) to make the graph look smooth.
df['Immigrant_Population'] = df['Immigrant_Population'].interpolate(method='linear')


# --- 2. now for the actual graph ---

# set up the plot window and the first y-axis (the left one)
fig, ax1 = plt.subplots(figsize=(15, 9))

# this one's for the immigration numbers, on the left
color1 = 'tab:blue'
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Immigrant Population (in millions)', color=color1, fontsize=14)
ax1.plot(df.index, df['Immigrant_Population'], color=color1, linewidth=3, label='Immigrant Population')
ax1.tick_params(axis='y', labelcolor=color1, labelsize=12)
ax1.tick_params(axis='x', labelsize=12)
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, pos: f'{x/1e6:.1f}M')) # formats the label to show "M" for millions

# now let's make the second y-axis (the right one) for gdp
ax2 = ax1.twinx()
color2 = 'tab:red'
ax2.set_ylabel('GDP Per Capita (Value)', color=color2, fontsize=14)
ax2.plot(df.index, df['GDP_per_Capita'], color=color2, linestyle='--', marker='o', markersize=4, label='GDP Per Capita')
ax2.tick_params(axis='y', labelcolor=color2, labelsize=12)
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, pos: f'{x/1e3:.0f}k')) # formats the label to show "k" for thousands


# --- 3. make it look good (titles, labels, and the story points) ---

# the main title
plt.title('UK Immigrant Population vs. GDP Per Capita (1990-2023)', fontsize=18, pad=20)

# the trick to getting one legend for two different axes is to grab the labels from both
# and then put them together in one box.
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=12)

# --- here are the annotations for the key events ---

# 2008 financial crisis
ax1.axvline(x=2008, color='k', linestyle='--', linewidth=1, alpha=0.7)
ax1.annotate('2008\nFinancial\nCrisis',
             xy=(2008, df.loc[2008, 'GDP_per_Capita']), # point the arrow at the 2008 gdp data point
             xycoords=ax2.get_yaxis_transform(), # y-value needs to be based on the right axis (ax2)
             xytext=(0.5, 0.85), # this just positions the text box so it looks neat
             textcoords='axes fraction',
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
             ha='center', fontsize=11, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=0.5))


# 2020 covid-19 pandemic
ax1.axvline(x=2020, color='k', linestyle='--', linewidth=1, alpha=0.7)
ax1.annotate('2020\nCOVID-19\nPandemic',
             xy=(2020, df.loc[2020, 'GDP_per_Capita']), # arrow points to the big 2020 gdp dip
             xycoords=ax2.get_yaxis_transform(),
             xytext=(0.85, 0.57),
             textcoords='axes fraction',
             arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
             ha='center', fontsize=11, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=0.5))


# --- 4. calculate stats and add the box ---

from scipy.stats import pearsonr

# drop any rows with missing values
df_for_corr = df.dropna(subset=['Immigrant_Population', 'GDP_per_Capita'])

# correlation and significance
correlation, p_value = pearsonr(df_for_corr['Immigrant_Population'], df_for_corr['GDP_per_Capita'])
std_immigrants = df['Immigrant_Population'].std()
std_gdp = df['GDP_per_Capita'].std()

# display formatting
p_value_display = f"p < 0.001" if p_value < 0.001 else f"p = {p_value:.3f}"
r2 = correlation**2

# create stats text box
stats_text = (
    f"Key Statistics\n"
    f"Correlation Coefficient: {correlation:.2f}\n"
    f"R²: {r2:.2f}"
)

ax1.text(0.95, 0.25, stats_text, transform=ax1.transAxes, fontsize=12,
         verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='black'))


# last few touches to make it clean
fig.tight_layout()
plt.grid(True, which='both', linestyle=':', linewidth=0.7)
plt.show()