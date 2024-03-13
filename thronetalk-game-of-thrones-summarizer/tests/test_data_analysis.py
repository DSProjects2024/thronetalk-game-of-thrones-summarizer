"""
This module contains unit tests for various function defined in the `data_analyis` module.
"""

import unittest
import pandas as pd
from utils import DataAnalysis

class TestDataAnalysis(unittest.TestCase):
    """
    A test class for the DataAnalysis class within the data_analysis module. This class
    contains unit tests that verify the functionality and robustness of the DataAnalysis
    class, ensuring it behaves as expected under various conditions.
    """
    def setUp(self):
        """
        Set up method to initialize test data before each test method is run. This method
        prepares a DataFrame `self.dialogue_data` with sample dialogue information from a
        fictional dataset that mimics television or movie scripts.
        """
        dialogue_data = {
                        'Character': ['Arya', 'Jon Snow', 'Daenerys', 'Narrator',
                                      'Tyrion', 'Arya', 'Jon Snow'],
                        'Season_Number': [1, 1, 1, 1, 1, 2, 2],
                        'Episode_Number': [1, 1, 2, 2, 2, 1, 2],
                        'Text': [
                            'I am Arya Stark.',  # Short dialogue
                            'I am Jon Snow.',  # Short dialogue
                            'I am Daenerys Targaryen. Mother of dragons',  # Longer dialogue
                            'Previously on...',  # Narrator
                            'I drink and I know things.',  # Medium dialogue
                            'Valar Morghulis.',  # Short dialogue
                            'The North remembers.'  # Medium dialogue
                        ]
                    }
        self.dialogue_data = pd.DataFrame(dialogue_data)

    def test_initialization(self):
        """
        Tests the initialization process of the DataAnalysis class. It checks if the
        class correctly raises TypeError when initialized with incorrect input types or
        missing arguments. This ensures that DataAnalysis instances can only be created
        with valid DataFrame inputs.
        """
        with self.assertRaises(TypeError):
            DataAnalysis('not a dataframe')

        with self.assertRaises(TypeError):
            DataAnalysis(pd.DataFrame())

        # with self.assertRaises(TypeError):
        #     DataAnalysis()

    def test_smoke_test(self):
        """
        Performs a basic "smoke test" on the DataAnalysis class by attempting to create
        an instance with valid input data. This test verifies that the class can be
        instantiated without errors and behaves as expected in a normal scenario.
        """
        data_analysis = DataAnalysis(self.dialogue_data)
        self.assertIsInstance(data_analysis, DataAnalysis)

    def test_get_top_n_characters(self):
        """
        Tests the `get_top_n_characters` method of the DataAnalysis class. It verifies
        that the method returns the correct list of top characters based on the provided
        season and episode range. This test ensures the method's accuracy in identifying
        top characters from dialogue data.
        """
        data_analysis = DataAnalysis(self.dialogue_data)
        from_season = 1
        to_season = 2
        from_episode = 1
        to_episode = 2
        expected_chars = ['Daenerys', 'Jon Snow', 'Arya', 'Tyrion']
        chars_st = data_analysis.get_top_n_characters(from_season=from_season, to_season=to_season,
                                           from_episode=from_episode, to_episode=to_episode)
        self.assertListEqual(chars_st, expected_chars)

    def test_season_check(self):
        """
        Tests the season range validation within the `get_top_n_characters` method of the
        DataAnalysis class. It ensures that the method raises a ValueError when the
        starting season is after the ending season, validating the logical consistency of
        season range parameters.
        """
        data_analysis = DataAnalysis(self.dialogue_data)
        from_season = 2
        to_season = 1
        from_episode = 1
        to_episode = 2
        with self.assertRaises(ValueError):
            data_analysis.get_top_n_characters(from_season=from_season, to_season=to_season,
                                           from_episode=from_episode, to_episode=to_episode)

    def test_episode_check(self):
        """
        Tests the episode range validation within the `get_top_n_characters` method of the
        DataAnalysis class. It ensures that the method raises a ValueError when the
        starting episode is after the ending episode, validating the logical consistency of
        episode range parameters.
        """
        data_analysis = DataAnalysis(self.dialogue_data)
        from_season = 1
        to_season = 1
        from_episode = 2
        to_episode = 1
        with self.assertRaises(ValueError):
            data_analysis.get_top_n_characters(from_season=from_season, to_season=to_season,
                                           from_episode=from_episode, to_episode=to_episode)

    def test_get_list_of_chars(self):
        """
        Tests the `get_list_of_characters` method of the DataAnalysis class. This test
        verifies that the method correctly retrieves a list of unique characters within
        the specified range of seasons and episodes. It checks for the method's ability
        to handle season and episode ranges and ensure the uniqueness and correct casing
        of character names.
        """
        data_analysis = DataAnalysis(self.dialogue_data)
        characters = data_analysis.get_list_of_characters(1, 1, 1, 2)
        self.assertCountEqual(characters, ['arya', 'jon snow', 'daenerys', 'narrator', 'tyrion'])

if __name__ == "__main__":
    unittest.main()
