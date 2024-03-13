"""
This module contains unit tests for various function defined in the `data_analyis` module.
"""

import unittest
import pandas as pd
from utils import DataAnalysis


# Sample dialogue data



class TestDataAnalysis(unittest.TestCase):
    """
      Test class for the util module data_analysis
    """
    def setUp(self):
        dialogue_data = {
                        'Character': ['Arya', 'Jon Snow', 'Daenerys', 'Narrator', 'Tyrion', 'Arya', 'Jon Snow'],
                        'Season_Number': [1, 1, 1, 1, 1, 2, 2],
                        'Episode_Number': [1, 1, 2, 2, 2, 1, 2],
                        'Text': [
                            'I am Arya Stark.',  # Short dialogue
                            'I am Jon Snow.',  # Short dialogue
                            'I am Daenerys Targaryen. This is a long dialogue. Mother of dragons',  # Longer dialogue
                            'Previously on...',  # Narrator
                            'I drink and I know things.',  # Medium dialogue
                            'Valar Morghulis.',  # Short dialogue
                            'The North remembers.'  # Medium dialogue
                        ]
                    }
        self.dialogue_data = pd.DataFrame(dialogue_data)

    def test_initialization(self):
        with self.assertRaises(TypeError):
            DataAnalysis('not a dataframe')

        with self.assertRaises(TypeError):
            DataAnalysis(pd.DataFrame())

        with self.assertRaises(TypeError):
            DataAnalysis()

    def test_smoke_test(self):
        '''Smoke test for DataAnalysis'''
        data_analysis = DataAnalysis(self.dialogue_data)
        self.assertIsInstance(data_analysis, DataAnalysis)

    def test_get_list_of_characters(self):
        data_analysis = DataAnalysis(self.dialogue_data)
        from_season = 1
        to_season = 2
        from_episode = 1
        to_episode = 2
        expected_chars = ['Daenerys', 'Jon Snow', 'Arya', 'Tyrion']
        chars_st, _ = data_analysis.get_top_n_characters(from_season=from_season, to_season=to_season,
                                           from_episode=from_episode, to_episode=to_episode)
        self.assertListEqual(chars_st, expected_chars)

    # def test_season_check(self):
