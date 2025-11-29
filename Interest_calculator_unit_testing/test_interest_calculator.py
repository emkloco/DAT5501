import unittest
from interest_calculator import compound_interest_calculator

class TestInterestCalculator(unittest.TestCase):

    def test_standard_case(self):
        # test: 5% interest should take 15 years to double
        # logic: 1.05^14 = 1.97 (not quite double)
        # logic: 1.05^15 = 2.07 (doubled)
        result = compound_interest_calculator(1000, 5, 10)
        self.assertEqual(result, 15)

    def test_high_interest(self):
        # test: 100% interest should double in exactly 1 year
        # 100 * (1 + 1.00) = 200
        result = compound_interest_calculator(100, 100, 5)
        self.assertEqual(result, 1)

    def test_small_amount(self):
        # test: the math should work the same for $1 as for $1000
        # at 10% interest, it takes 8 years to double
        result = compound_interest_calculator(1, 10, 5)
        self.assertEqual(result, 8)

    def test_different_timelines(self):
        # test: the number of years printed (3rd argument) shouldn't affect the doubling calculation
        # even if we only print 2 years, the doubling loop should still find 15 years for 5%
        result_short_view = compound_interest_calculator(1000, 5, 2)
        result_long_view = compound_interest_calculator(1000, 5, 50)
        self.assertEqual(result_short_view, result_long_view)

if __name__ == '__main__':
    unittest.main()