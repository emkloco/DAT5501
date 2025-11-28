# Unit Testing: Data Normalization

## Overview
This module implements a **Min-Max Normalization** algorithm, a common technique in Data Science preprocessing to scale numerical data into a range of [0, 1]. 

The project demonstrates **Test-Driven Development (TDD)**, ensuring the function is robust against edge cases such as empty datasets, negative numbers, and type errors.

## Key Features
- **Algorithm:** Implements mathematical Min-Max scaling: $x' = \frac{x - \min(x)}{\max(x) - \min(x)}$
- **Robustness:** Includes error handling for non-numeric inputs and empty lists.
- **Zero-Division Protection:** Handles edge cases where the dataset has zero variance (all numbers are identical).

## Test Suite
The test suite (`test_data_processor.py`) validates:
1.  **Standard inputs:** Verifies correct math for mixed integers/floats.
2.  **Negative numbers:** Ensures range calculations work across zero.
3.  **Edge cases:** Validates behavior for empty lists and single-value lists.
4.  **Type Safety:** Ensures specific errors are raised for invalid inputs.

## Usage
Run the automated test suite from the terminal:

```bash
python test_data_processor.py