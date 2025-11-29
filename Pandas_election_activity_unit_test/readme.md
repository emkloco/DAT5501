# US 2016 Primary Election Analysis

## Executive Summary
This project utilizes the **Pandas** library to perform exploratory data analysis (EDA) on the 2016 US Primary Election dataset. The goal is to visualize voting distributions and programmatically compare candidate performance across varying demographics.

## Technical Methodology
*   **Data Ingestion:** Parses non-standard CSV files (semicolon-delimited) using Pandas.
*   **Distribution Analysis:** Generates histograms to visualize the `fraction_votes` spread, helping identify if a candidate's support is polarized or consistent.
*   **Aggregated Metrics:** Utilizes `groupby` operations to calculate total vote counts for direct candidate comparison.

## Files & Outputs

| File | Description |
| :--- | :--- |
| `election_analytics.py` | Main script for data processing and visualization. |
| `US-2016-primary.csv` | Raw dataset containing county-level election returns. |
| `Donald_Trump_histogram.png` | **Artifact:** Visualization of Trump's vote share distribution. |
| `Hillary_Clinton_histogram.png` | **Artifact:** Visualization of Clinton's vote share distribution. |
| `test_election_analytics.py` | Unit test suite ensuring data aggregation logic is accurate. |

## How to Run

1. **Install dependencies:**
   ```bash
   pip install pandas matplotlib

2. **Run the analysis:**
   ```bash
   python election_analytics.py

3. **Run the tests:**
   ```bash
   python test_election_analytics.py