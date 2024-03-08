'''
Module that tests `scripts/visualization_generator.py`. Makes use of `unittest` module.
Consists of smoke tests, one-shot test and edge tests.
'''
import unittest
from unittest.mock import patch
from scripts import VisualizationGenerator
from . import mock_functions

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
    def test_smoke_test(self):
        top_3_characters = ["eddard","catelyn","robert"]
        vg = VisualizationGenerator(1,1,1,3)
        vg.multiWordCloud(top_3_characters)
        vg.sentimentAnalysisVisualization(top_3_characters)
    
    # def test_get_show_metadata_smoke(self):
    #     '''Smoke test to make sure the function runs properly.'''
    #     get_show_metadata("0944947")

    # def test_write_show_metadata_smoke(self):
    #     '''Smoke test to make sure the function runs properly.'''
    #     write_show_metadata(self.mock_path, self.mock_data)
    
    # def test__format_episode_metadata_smoke(self):
    #     '''Smoke test to make sure the function runs properly.'''
    #     _format_episode_metadata(self.mock_data)
    
    # def test_get_episode_metadata_smoke(self):
    #     '''Smoke test to make sure the function runs properly.'''
    #     get_episode_metadata()

    # def test_write_episode_metadata_smoke(self):
    #     '''Smoke test to make sure the function runs properly.'''
    #     write_episode_metadata(self.mock_path, self.mock_data)

    # Edge Tests
    # def test_edge_invalid_get_show_metadata(self):
    #     '''Edge test for get_show_metadata function.'''
    #     with self.assertRaises(TypeError):
    #         get_show_metadata()
    #     with self.assertRaises(TypeError):
    #         get_show_metadata(1234567)
    #     with self.assertRaises(ValueError):
    #         get_show_metadata("123")

    # def test_edge_invalid_write_show_metadata(self):
    #     '''Edge test for write_show_metadata function.'''
    #     # Check values of first parameter
    #     with self.assertRaises(ValueError):
    #         write_show_metadata()
    #     with self.assertRaises(TypeError):
    #         write_show_metadata(1234567, self.mock_data)
    #     with self.assertRaises(ValueError):
    #         write_show_metadata("", self.mock_data)
    #     with self.assertRaises(ValueError):
    #         write_show_metadata(".json", self.mock_data)
    #     # Check values of second parameter
    #     with self.assertRaises(ValueError):
    #         write_show_metadata(self.mock_path)
    #     with self.assertRaises(ValueError):
    #         write_show_metadata(self.mock_path, {})

    # def test_edge_invalid__format_episode_metadata(self):
    #     '''Edge test for _format_episode_metadata function.'''
    #     # with self.assertRaises(ValueError):
    #     #     _format_episode_metadata()
    #     with self.assertRaises(ValueError):
    #         _format_episode_metadata({})
    
    # def test_edge_invalid_write_episode_metadata(self):
    #     '''Edge test for write_episode_metadata function.'''
    #     # Check values of first parameter
    #     with self.assertRaises(ValueError):
    #         write_episode_metadata()
    #     with self.assertRaises(TypeError):
    #         write_episode_metadata(1234567, self.mock_data)
    #     with self.assertRaises(ValueError):
    #         write_episode_metadata("", self.mock_data)
    #     with self.assertRaises(ValueError):
    #         write_episode_metadata(".csv", self.mock_data)
    #     # Check values of second parameter
    #     with self.assertRaises(ValueError):
    #         write_episode_metadata(self.mock_path)
    #     with self.assertRaises(ValueError):
    #         write_episode_metadata(self.mock_path, {})

if __name__ == "__main__":
    unittest.main()