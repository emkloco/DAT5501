# UK Economic Correlation Analysis: Immigration vs. GDP

## Executive Summary
This project investigates the relationship between demographic shifts and economic output in the UK (1990–2023). It addresses a common data storytelling challenge: **Visualizing variables with vastly different scales** (Population in Millions vs. GDP in Thousands).

## Analysis & Visualisation Strategy
*   **Dual-Axis Plotting:** Utilized `matplotlib` to overlay Immigrant Population and GDP Per Capita on a single timeline.
*   **Contextual Annotation:** Programmatically annotated key economic events (2008 Financial Crisis, COVID-19) to provide context.
*   **Statistical Correlation:** Calculated Pearson’s Correlation Coefficient ($r=0.86$) to quantify the strength of the relationship.

## Files & Outputs

| File | Description |
| :--- | :--- |
| `emeka_immigration_vs_gdp.py` | The main analysis script. **Running this saves the PNG plot.** |
| `immigration_gdp_data.csv` | Cleaned time-series data (Year, Population, GDP). |
| `Immigrant_vs_gdp.png` | **Output Artifact:** The final dual-axis visualization. |

## How to Run

1. **Install dependencies:**
   ```bash
   pip install pandas matplotlib scipy

2. **Run the script:**
Open your terminal in this folder and run:
    bash
   python emeka_immigration_vs_gdp.py



3. **View results:**

The script will print the Correlation Coefficient to the console.
A file named Immigrant_vs_gdp.png will be generated in this folder.

**Troubleshooting:**

File Not Found Error: Ensure you are running the command from inside the Presentation_data_visualisation folder so the script can see the CSV file.