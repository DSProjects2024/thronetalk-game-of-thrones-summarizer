'''
Module that tests `scripts/model.py`. Makes use of `unittest` module.
Consists of smoke tests and edge tests.
'''
import unittest
from unittest.mock import patch
from utils import Model
from . import mock_constants

class TestModel(unittest.TestCase):
    '''Test suite for `scripts/model.py`'''
    def test_smoke_test(self):
        '''Smoke test for Model'''
        model = Model(1,1,1,3)
        self.assertIsInstance(model, Model)

    def test_edge_init(self):
        '''Edge tests for Model'''
        with self.assertRaises(TypeError):
            Model() # pylint: disable=no-value-for-parameter
            # disabling pylint to allow checking for empty class initialization
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

    def test_integration_create_summarizer_input(self):
        '''Integration test to check if create_summarizer_input function
        works with the remaining functions properly.'''
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

    @patch('utils.model.Model.azure_api_call')
    def test_integration_summarize(self, mock_summarize):
        '''Integration test to check if all functionality works as expected.'''
        mock_summarize.return_value = mock_constants.CHAT_COMPLETIONS_MOCK_RESPONSE
        
        model = Model(1,1,1,2)
        summary = model.summarize()
        self.assertIsInstance(summary, str)
        self.assertEqual(summary, mock_constants.CHAT_COMPLETIONS_MOCK_RESPONSE)

        # Assert that azure_api_call was called with the correct prompt
        message_text = model.create_summarizer_input()
        mock_summarize.assert_called_once_with(message_text)

if __name__ == "__main__":
    unittest.main()
