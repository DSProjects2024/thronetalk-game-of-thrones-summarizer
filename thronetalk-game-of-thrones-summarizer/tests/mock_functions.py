'''
Mock functions for testing purposes.
'''
import pandas as pd
from . import mock_constants

# *args is required to catch arguments passed while using with
# unittest's @patch, disabling the pylint warning.
# pylint: disable=unused-argument
def mocked_read_csv_ouput_dialogues(*args):
    """
    Mock for pandas' read_csv function for output_dialogues.
    """
    mock_rows = [
        [0,"Hello brother.","","","","","",1,1,"","jon snow"],
        [1,"Valar Morghulis.","","","","","",1,1,"","arya stark"],
        [2,"Previously on...","","","","","",1,1,"","narrator"],
        [3,"The North remembers.","","","","","",1,1,"","arya stark"],
        [4,"hi brother","","","","","",1,1,"","jon snow"],
        [5,"Valar Morghulis.","","","","","",1,1,"","arya stark"],
        [6,"Previously on...","","","","","",1,1,"","narrator"],
        [7,"The North remembers.","","","","","",1,1,"","arya stark"],
    ]
    columns = [
        '', 'Text','Speaker','Episode','Season','Show','Episode_name',
        'Episode_Number','Season_Number','dialogue_with_speaker','Character'
    ]
    dataframe = pd.DataFrame(mock_rows, columns=columns)
    return dataframe

# *args is required to catch arguments passed while using with
# unittest's @patch, disabling the pylint warning.
# pylint: disable=unused-argument
def mock_model_azure_api_call(*args):
    '''Mocks the response of azure_api_call from model.py's Model class.'''
    return mock_constants.CHAT_COMPLETIONS_MOCK_RESPONSE
