# Date Duration Calculator & Vectorization

## Executive Summary
This project demonstrates the handling of time-series data using Python. It implements a calculator that determines the time elapsed between dates using `numpy.datetime64` for precision and efficiency.

The module includes both a user-interactive mode and a batch-processing mode that ingests a CSV file and calculates durations for large datasets automatically.

## Technical Methodology
*   **NumPy DateTime:** utilized `np.datetime64` instead of the standard Python `datetime` library to allow for faster, vectorized calculations on larger datasets.
*   **Input Validation:** implemented error handling to ensure invalid date formats do not crash the program.
*   **Unit Testing:** The test suite uses "dependency injection" (allowing a custom comparison date) to ensure tests are deterministic and do not break as real time moves forward.

## Files & Outputs

| File | Description |
| :--- | :--- |
| `duration_calculator.py` | Core logic script. Handles user input and CSV processing. |
| `random_dates.csv` | Sample dataset containing dates in `YYYY-MM-DD` format. |
| `test_duration_calculator.py` | Unit test suite. |

## How to Run

```bash
# Run the calculator (User Input + CSV Mode)
python duration_calculator.py

# Run the test suite
python test_duration_calculator.py