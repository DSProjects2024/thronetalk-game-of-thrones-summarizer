'''
Module that tests `scripts/visualization_generator.py`. Makes use of `unittest` module.
Consists of smoke tests, one-shot test and edge tests.
'''
import unittest
# from unittest.mock import patch
from utils import VisualizationGenerator
# from . import mock_functions

class TestVisualizationGenerator(unittest.TestCase):
    '''Test suite for `scripts/visualization_generator.py`'''

    # Edge tests
    def test_init_error(self):
        '''Edge tests for VisualizationGenerator'''
        with self.assertRaises(TypeError):
            VisualizationGenerator() # pylint: disable=no-value-for-parameter
        with self.assertRaises(ValueError):
            VisualizationGenerator("","","","")
        with self.assertRaises(ValueError):
            VisualizationGenerator(1,1,1,1)
        with self.assertRaises(ValueError):
            VisualizationGenerator(-1,1,1,1)
        with self.assertRaises(ValueError):
            VisualizationGenerator(-1,27,1,1)
        with self.assertRaises(ValueError):
            VisualizationGenerator(2,1,1,1)
        # mock.return_value = self.mock_imdb_data
        # imdb, script = data_manager.load_data()
        # recommender = Recommender(meta=imdb, scripts=script)
        # self.assertEqual(recommender.weights, [1, 1, 0.8, 0.5, 0.2, 0.2, 0.4])
        # self.assertIsNotNone(recommender.vector_list)
    # @patch('scripts.visualization_generator.pd.read_csv',
    #        side_effect=mock_functions.mocked_read_csv_ouput_dialogues)
    def test_wordcloud_error(self):
        '''Edge tests for wordcloud generation function'''
        v_g = VisualizationGenerator(1,1,1,2)
        with self.assertRaises(TypeError):
            v_g.multiWordCloud() # pylint: disable=no-value-for-parameter
        with self.assertRaises(ValueError):
            v_g.multiWordCloud([])
        with self.assertRaises(ValueError):
            v_g.multiWordCloud(['', ''])

    def test_sentiment_analysis_visualization_error(self):
        '''Edge tests for sentiment analysis viz generation function'''
        v_g = VisualizationGenerator(1,1,1,2)
        with self.assertRaises(TypeError):
            v_g.sentimentAnalysisVisualization() # pylint: disable=no-value-for-parameter
        with self.assertRaises(ValueError):
            v_g.sentimentAnalysisVisualization([])
        with self.assertRaises(ValueError):
            v_g.sentimentAnalysisVisualization(['', ''])

    # Smoke tests
    # @patch('scripts.visualization_generator.pd.read_csv',
    #        side_effect=mock_functions.mocked_read_csv_ouput_dialogues)
    # def test_smoke_test(self):
    #     top_3_characters = ["eddard","catelyn","robert"]
    #     vg = VisualizationGenerator(1,1,1,3)
    #     vg.multiWordCloud(top_3_characters)
    #     vg.sentimentAnalysisVisualization(top_3_characters)

if __name__ == "__main__":
    unittest.main()
