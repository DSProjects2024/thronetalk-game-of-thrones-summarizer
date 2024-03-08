'''
Module that tests `scripts/visualization_generator.py`. Makes use of `unittest` module.
Consists of smoke tests, one-shot test and edge tests.
'''
import unittest
from unittest.mock import patch
from utils import VisualizationGenerator
# from . import mock_functions

class TestVisualizationGenerator(unittest.TestCase):
    '''Test suite for `scripts/visualization_generator.py`'''

    # Edge tests
    def test_init_error(self):
        with self.assertRaises(TypeError):
            VisualizationGenerator()
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
        vg = VisualizationGenerator(1,1,1,2)
        with self.assertRaises(TypeError):
            vg.multiWordCloud()
        with self.assertRaises(ValueError):
            vg.multiWordCloud([])
        with self.assertRaises(ValueError):
            vg.multiWordCloud(['', ''])

    def test_sentimentAnalysisVisualization_error(self):
        vg = VisualizationGenerator(1,1,1,2)
        with self.assertRaises(TypeError):
            vg.sentimentAnalysisVisualization()
        with self.assertRaises(ValueError):
            vg.sentimentAnalysisVisualization([])
        with self.assertRaises(ValueError):
            vg.sentimentAnalysisVisualization(['', ''])

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