'''
Module that tests `scripts/model.py`. Makes use of `unittest` module.
Consists of smoke tests and edge tests.
'''
import unittest
# from unittest.mock import patch
from utils import Model

class TestModel(unittest.TestCase):
    '''Test suite for `scripts/model.py`'''
    # Smoke tests
    # @patch('scripts.visualization_generator.pd.read_csv',
    #        side_effect=mock_functions.mocked_read_csv_ouput_dialogues)
    def test_smoke_test(self):
        '''Smoke test for Model'''
        Model(1,1,1,3)

    # Edge tests
    def test_init_error(self):
        '''Edge tests for Model'''
        with self.assertRaises(TypeError):
            Model() # pylint: disable=no-value-for-parameter
        with self.assertRaises(ValueError):
            Model("","","","")
        with self.assertRaises(ValueError):
            Model(-1,1,1,1)
        with self.assertRaises(ValueError):
            Model(1,1,10,1)
        with self.assertRaises(ValueError):
            Model(1,27,1,1)
        with self.assertRaises(ValueError):
            Model(2,1,1,1)

    # One-shot test
    def test_create_summarizer_input_error(self):
        '''One-shot test for create_summarizer_input function'''
        # We remove all whitespaces and compare because assertEqual fails
        # for multiline f-strings
        def get_message_content(season_from, episode_from, season_to, episode_to):
            model = Model(season_from, episode_from, season_to, episode_to)
            prompt = model.create_summarizer_input()
            return prompt[0]['content'].replace(" ", "")

        season_from, episode_from, season_to, episode_to = 1,1,1,1
        computed_message = get_message_content(season_from, episode_from, season_to, episode_to)
        expected_message = f'''Summarize Game of thrones season {str(season_from)}
            episode {str(episode_from)} in 300 words.'''.replace(" ", "")
        self.assertEqual(expected_message, computed_message)

        season_from, episode_from, season_to, episode_to = 1,1,1,2
        computed_message = get_message_content(season_from, episode_from, season_to, episode_to)
        expected_message = f'''Summarize Game of thrones from season {str(season_from)}
            episode {str(episode_from)} to season {str(season_to)}
            episode {str(episode_to)} in 300 words.'''.replace(" ", "")
        self.assertEqual(expected_message, computed_message)

if __name__ == "__main__":
    unittest.main()
