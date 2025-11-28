import unittest
from data_processor import normalize_data

class TestDataNormalization(unittest.TestCase):
    
    def test_standard_normalization(self):
        # test a standard list of integers
        input_data = [10, 20, 30]
        expected = [0.0, 0.5, 1.0]
        self.assertEqual(normalize_data(input_data), expected)

    def test_with_negative_numbers(self):
        # test that it handles negative numbers correctly
        input_data = [-10, 0, 10]
        # range is -10 to 10 (span of 20). 
        # -10 -> 0.0
        # 0   -> 0.5
        # 10  -> 1.0
        self.assertEqual(normalize_data(input_data), [0.0, 0.5, 1.0])

    def test_identical_values(self):
        # edge case: list with identical values should avoid ZeroDivisionError
        input_data = [5, 5, 5]
        # should return all 0.0s (or handle gracefully)
        self.assertEqual(normalize_data(input_data), [0.0, 0.0, 0.0])

    def test_empty_list_error(self):
        # edge case: empty list should raise ValueError
        with self.assertRaises(ValueError):
            normalize_data([])

    def test_invalid_input_type(self):
        # robustness: list containing strings should raise TypeError
        with self.assertRaises(TypeError):
            normalize_data([1, 2, "banana"])

if __name__ == '__main__':
    unittest.main() 