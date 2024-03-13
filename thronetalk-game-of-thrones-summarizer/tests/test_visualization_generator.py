'''
Module that tests `scripts/visualization_generator.py`. Makes use of `unittest` module.
Consists of smoke tests, edge and one-shot tests.
'''
import unittest
from unittest.mock import patch
from wordcloud import WordCloud
import pandas as pd
from utils import VisualizationGenerator
from . import mock_functions
from .mock_constants import (TEST_CHARACTER,
                             WAYMAR_ROYCE_DIALOG_STRING,
                             WAYMAR_ROYCE_SENTIMENT_STRING)

class TestVisualizationGenerator(unittest.TestCase):
    '''Test suite for `scripts/visualization_generator.py`'''

    def test_smoke(self):
        v_g = VisualizationGenerator(1,1,1,1)
        self.assertIsInstance(v_g, VisualizationGenerator)

    def test_edge_init(self):
        '''Edge tests for VisualizationGenerator'''
        with self.assertRaises(TypeError):
            VisualizationGenerator() # pylint: disable=no-value-for-parameter
            # disabling pylint to allow checking for empty class initialization
        with self.assertRaises(ValueError):
            VisualizationGenerator("","","","")
        with self.assertRaises(ValueError):
            VisualizationGenerator(-1,1,1,1)
        with self.assertRaises(ValueError):
            VisualizationGenerator(1,27,1,1)
        with self.assertRaises(ValueError):
            VisualizationGenerator(2,1,1,1)
        with self.assertRaises(ValueError):
            VisualizationGenerator(1,1,9,1)

    def test_edge_sentiment_analysis_visualization(self):
        '''Edge tests for sentiment analysis viz generation function'''
        v_g = VisualizationGenerator(1,1,1,2)
        with self.assertRaises(TypeError):
            v_g.sentiment_analysis_visualization() # pylint: disable=no-value-for-parameter
            # disabling pylint to allow checking for empty class initialization
        with self.assertRaises(TypeError):
            v_g.sentiment_analysis_visualization("")
        with self.assertRaises(ValueError):
            v_g.sentiment_analysis_visualization([])
        with self.assertRaises(ValueError):
            v_g.sentiment_analysis_visualization([1,2,3])
        with self.assertRaises(ValueError):
            v_g.sentiment_analysis_visualization(['', ''])

    def test_edge_wordcloud(self):
        '''Edge tests for wordcloud generation function'''
        v_g = VisualizationGenerator(1,1,1,2)
        with self.assertRaises(TypeError):
            v_g.multi_word_cloud() # pylint: disable=no-value-for-parameter
            # disabling pylint to allow checking for empty class initialization
        with self.assertRaises(TypeError):
            v_g.multi_word_cloud("")
        with self.assertRaises(ValueError):
            v_g.multi_word_cloud([])
        with self.assertRaises(ValueError):
            v_g.multi_word_cloud([1,2,3])
        with self.assertRaises(ValueError):
            v_g.multi_word_cloud(['', ''])

    def test_one_shot_pre_process_data_for_character(self):
        '''Test for pre_process_data_for_character function'''
        v_g = VisualizationGenerator(1,1,1,1)
        dialog_string = v_g.pre_process_data_for_character(TEST_CHARACTER)
        self.assertCountEqual(
            dialog_string.split(),
            WAYMAR_ROYCE_DIALOG_STRING.split()
        )

    def test_one_shot_pre_process_data_for_character_per_episode(self):
        '''Test for pre_process_data_for_character_per_episode function'''
        v_g = VisualizationGenerator(1,1,1,1)
        dialog = v_g.pre_process_data_for_character_per_episode(TEST_CHARACTER)[0].strip()
        expected_output = " ".join(WAYMAR_ROYCE_DIALOG_STRING.split())
        self.assertEqual(dialog, expected_output)

    def test_one_shot_preprocess_text_sentiment(self):
        '''Test for preprocess_text_sentiment function'''
        v_g = VisualizationGenerator(1,1,1,1)
        text = v_g.pre_process_data_for_character(TEST_CHARACTER)
        sentiment_text = v_g.preprocess_text_sentiment(text)
        self.assertCountEqual(
            sentiment_text.split(),
            WAYMAR_ROYCE_SENTIMENT_STRING.split()
        )

    @patch('utils.visualization_generator.pd.read_csv',
           side_effect=mock_functions.mocked_read_csv_ouput_dialogues)
    def test_integration(self, _):
        '''Integration test for VisualizationGenerator to check
        all functionality works as expected.'''
        top_3_characters = ["arya stark", "jon snow", "catelyn stark"]
        v_g = VisualizationGenerator(1,1,1,3)
        plot_obj_arr = v_g.multi_word_cloud(top_3_characters)
        line_chart = v_g.sentiment_analysis_visualization(top_3_characters)
        for plot_obj in plot_obj_arr:
            self.assertIsInstance(plot_obj, WordCloud)
        self.assertIsInstance(line_chart, pd.DataFrame)

        # Assert expected columns
        expected_columns = ['season-episode'] + top_3_characters
        self.assertEqual(list(line_chart.columns), expected_columns)
        

if __name__ == "__main__":
    unittest.main()
