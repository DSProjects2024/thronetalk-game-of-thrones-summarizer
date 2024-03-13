"""
This module contains unit tests for various function defined in the `data_analyis` module.
"""

import unittest
from datetime import date
from unittest import mock
from utils import DataAnalysis

import pandas as pd

# Sample dialogue data
dialogue_data = {
    'Character': ['Arya', 'Jon Snow', 'Daenerys', 'Narrator', 'Tyrion', 'Arya', 'Jon Snow'],
    'Season_Number': [1, 1, 1, 1, 1, 1, 1],
    'Episode_Number': [1, 1, 2, 2, 2, 3, 3],
    'Text': [
        'I am Arya Stark.',  # Short dialogue
        'I am Jon Snow.',  # Short dialogue
        'I am Daenerys Targaryen. This is a long dialogue',  # Longer dialogue
        'Previously on...',  # Narrator
        'I drink and I know things.',  # Medium dialogue
        'Valar Morghulis.',  # Short dialogue
        'The North remembers.'  # Medium dialogue
    ]
}


class TestWeather(unittest.TestCase):
    """
      Test class for the util module data_analysis
    """
    def test_smoke_test(self):
        # Example test instantiation
        df = pd.DataFrame(dialogue_data)
        data_analysis = DataAnalysis(df)
        from_season = 1
        to_season = 2

        top_15_chars_screen_time, top_15_chars_occurence = data_analysis.get_top_n_characters(
        from_season=1, to_season=1, from_episode=5, to_episode=10)


def test_get_list_of_characters():
    expected_characters = sorted(['arya', 'jon snow', 'daenerys', 'narrator', 'tyrion'])  # Expected outcome
    actual_characters = sorted(data_analysis.get_list_of_characters(from_season=1, to_season=1))
    assert actual_characters == expected_characters, "Character list does not match expected output."
    print("Basic Character List Retrieval Test Passed!")

def test_get_top_n_characters():
    # Expected values need to be adjusted based on your manual calculations from the sample data
    expected_screen_time_chars = ['Daenerys', 'Tyrion', 'Jon Snow', 'Arya']  # Example based on dialogue length
    expected_occurence_chars = ['Arya', 'Jon Snow', 'Daenerys', 'Tyrion']  # Example based on frequency

    # Running the test for season 1 to 2, to include a range of episodes
    top_chars_screen_time, top_chars_occurence = data_analysis.get_top_n_characters(from_season=1, to_season=2, from_episode=1, to_episode=1)

    assert sorted(top_chars_screen_time) == sorted(expected_screen_time_chars), "Top characters by screen time do not match expected output."
    assert sorted(top_chars_occurence) == sorted(expected_occurence_chars), "Top characters by occurrence do not match expected output."
    print("One-Shot Comprehensive Analysis Test Passed!")
