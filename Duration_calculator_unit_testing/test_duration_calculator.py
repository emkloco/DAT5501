import unittest
from duration_calculator import calculate_days_elapsed

class TestDurationCalculator(unittest.TestCase):

    def test_past_date(self):
        # testing a fixed range: 2023-01-01 to 2023-01-10 should be 9 days
        result = calculate_days_elapsed('2023-01-01', compare_date='2023-01-10')
        self.assertEqual(result, 9)

    def test_same_date(self):
        # if the dates are the same, result should be 0
        result = calculate_days_elapsed('2025-01-01', compare_date='2025-01-01')
        self.assertEqual(result, 0)

    def test_future_date(self):
        # if input is in the future relative to compare date, result should be negative
        result = calculate_days_elapsed('2025-01-10', compare_date='2025-01-01')
        self.assertEqual(result, -9)

    def test_invalid_format(self):
        # checking if the function handles garbage input gracefully
        result = calculate_days_elapsed('not-a-date')
        self.assertIn("error", str(result))

if __name__ == '__main__':
    unittest.main()