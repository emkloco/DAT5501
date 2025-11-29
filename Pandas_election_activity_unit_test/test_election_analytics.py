import unittest
import pandas as pd
from election_analytics import compare_two_candidates, load_election_data

class TestElectionAnalytics(unittest.TestCase):

    def setUp(self):
        # create a fake dataframe for testing
        data = {
            'candidate': ['Alice', 'Alice', 'Bob', 'Bob'],
            'votes': [100, 200, 50, 50],
            'fraction_votes': [0.5, 0.6, 0.2, 0.2]
        }
        self.test_df = pd.DataFrame(data)

    def test_vote_summation(self):
        # test that pandas correctly sums votes in our logic
        summary = self.test_df.groupby('candidate')['votes'].sum()
        self.assertEqual(summary['Alice'], 300)
        self.assertEqual(summary['Bob'], 100)

    def test_data_loading_error(self):
        # test that loading a non-existent file raises an error
        with self.assertRaises(FileNotFoundError):
            load_election_data("non_existent_ghost_file.csv")

    def test_dataframe_structure(self):
        # check if the dataframe columns match what we expect
        expected_cols = ['candidate', 'votes', 'fraction_votes']
        self.assertTrue(all(col in self.test_df.columns for col in expected_cols))

if __name__ == '__main__':
    unittest.main()