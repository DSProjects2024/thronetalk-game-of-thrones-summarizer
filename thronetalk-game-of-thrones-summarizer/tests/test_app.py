'''
Module that tests `app.py`. Makes use of unittest and Streamlit AppTest module.
Consists of smoke tests, one-shot test and edge tests.
'''
import unittest
from unittest.mock import patch
from streamlit.testing.v1 import AppTest
from .mock_functions import mock_model_azure_api_call

class TestStreamlitApp(unittest.TestCase):
    """
    Test cases for the Streamlit app.
    """
    def setUp(self):
        """
        The unittest framework automatically runs this `setUp` function before
        each test. By refactoring the creation of the AppTest into a common
        function, we reduce the total amount of code in the file.
        """
        self.app_test = AppTest.from_file('app.py').run(timeout=30)

    # Utility function for other tests, not a test by itself.
    def mock_input(self):
        """
        Mocks user input by selecting values in the sidebar.
        """
        season_from = self.app_test.sidebar.selectbox[0]
        season_from.select("1")
        episode_from = self.app_test.sidebar.selectbox[1]
        episode_from.select("Season 1 - Episode 1")
        season_to = self.app_test.sidebar.selectbox[2]
        season_to.select("1")
        episode_to = self.app_test.sidebar.selectbox[3]
        #print(episode_to)
        episode_to.select("Season 1 - Episode 3")
        #app_test.sidebar.button("Submit").click()
        self.app_test.sidebar.button[0].click().run(timeout=30)

    def test_tile(self):
        """
        Test if the app title is correct.
        """
        self.assertEqual(self.app_test.title[0].value,  'Game of Thrones - Summarizer')

    @patch('utils.model.Model.azure_api_call', side_effect=mock_model_azure_api_call)
    def test_sidebar_selectboxes(self, _):
        """
        Test if the sidebar selectboxes contain expected values.
        """
        self.mock_input()
        self.assertIn(self.app_test.sidebar.selectbox[0].value,  ['1','2','3','4','5','6','7','8'])
        from_ep_full = self.app_test.sidebar.selectbox[1].value
        from_ep = from_ep_full.split()[4]
        self.assertIn(from_ep,  ['1','2','3','4','5','6','7','8', '9','10'])
        self.assertIn(self.app_test.sidebar.selectbox[2].value,  ['1','2','3','4','5','6','7','8'])
        to_ep_full = self.app_test.sidebar.selectbox[3].value
        to_ep = to_ep_full.split()[4]
        self.assertIn(to_ep,  ['1','2','3','4','5','6','7','8','9','10'])

    @patch('utils.model.Model.azure_api_call', side_effect=mock_model_azure_api_call)
    def test_headers(self, _):
        """
        Test if the subheaders are correctly displayed after generating summary.
        """
        self.mock_input()
        from_ep_full2 = self.app_test.sidebar.selectbox[1].value
        to_ep_full2 = self.app_test.sidebar.selectbox[3].value
        sub_header1= f"**Sentiment Scores Across {from_ep_full2} to {to_ep_full2}**"
        sub_header2= f"**Episode Summary from {from_ep_full2} to {to_ep_full2}**"
        episode_summary_subheader = self.app_test.subheader[5].value
        sentiment_analysis_subheader = self.app_test.subheader[0].value
        self.assertEqual(sentiment_analysis_subheader,sub_header1)
        self.assertEqual(episode_summary_subheader,sub_header2)

if __name__ == '__main__':
    unittest.main()
