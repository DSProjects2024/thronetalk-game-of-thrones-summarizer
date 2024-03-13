"""
This module provides a class (`Model`) to summarize the plot of Game of Thrones (GoT) 
based on user-specified episode and season ranges.

The `Model` class utilizes the Azure OpenAI API to generate summaries through conversation prompts. 
It first constructs the prompt based on the provided season and episode information and then 
calls the Azure OpenAI API to obtain the summarized text.
"""
from openai import AzureOpenAI
import streamlit as st

class Model:
    """
    A class to create summary of GOT plot.
    """
    def __init__(self, season_from: int, episode_from: int,
                 season_to: int, episode_to: int) -> None:
        """
        Initializes the summarizer with episode and season information.

        Args:
            season_from: The starting season number (inclusive).
            episode_from: The starting episode number (inclusive) within the starting season.
            season_to: The ending season number (inclusive).
            episode_to: The ending episode number (inclusive) within the ending season.
        """
        # Python raises `TypeError` automatically if we don't provide the kwargs
        # (we'll need separate validation codes to check for both Model and VisualizationGenerator)
        # pylint: disable=duplicate-code
        params = [season_from, episode_from, season_to, episode_to]
        if any(not isinstance(param, int) for param in params):
            raise ValueError('''season_from, episode_from, season_to
                             and episode_to must be integers!''')
        if season_from < 1:
            raise ValueError("season_from can't be less than 1!")
        if not 1 <= episode_from <= 10 or not 1 <= episode_to <= 10:
            raise ValueError("episode_from and episode_to values should be within 1 to 10!")
        if season_to > 8:
            raise ValueError("season_from can't be greater than 8!")
        if (season_from * 10 + episode_from) > (season_to * 10 + episode_to):
            raise ValueError("From value can't be greater than To value!")
        self.episode_from = episode_from
        self.episode_to = episode_to
        self.season_from = season_from
        self.season_to = season_to
        self.client = None

    def create_summarizer_input(self):
        """
        Creates the prompt for summary based on episode input.

        Returns:
            A list containing a dictionary for the prompt.
        """
        if self.episode_from == self.episode_to and self.season_from == self.season_to:
            message_text = [{
                "role": "system",
                "content": f'''Summarize Game of thrones season {str(self.season_from)}
                  episode {str(self.episode_from)} in 300 words.'''
                }]
        else:
            message_text = [{
                "role": "system",
                "content": f'''Summarize Game of thrones from season {str(self.season_from)}
                    episode {str(self.episode_from)} to season {str(self.season_to)}
                    episode {str(self.episode_to)} in 300 words.'''
                }]
        return message_text

    def azure_api_call(self, message_text):
        """
        Calls the Azure OpenAI API with the prompt `message_text`.

        Args:
            message_text: A list of dictionaries containing the role ("system" or "user")
            and content of the messages.

        Returns:
            The completed response from the Azure OpenAI API as a string.
        """
        client = AzureOpenAI(
            azure_endpoint = st.secrets["AZURE_ENDPOINT"],
            api_key = st.secrets["AZURE_OPENAI_KEY"],
            api_version="2024-02-15-preview"
        )

        completion = client.chat.completions.create(
            model="ThroneTalk", # model = "deployment_name"
            messages=message_text,
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
        return completion.choices[0].message.content

    def summarize(self):
        """
        Summarizes content using the Azure OpenAI API. 
        Calls the `azure_api_call` function to get the summarized text from the Azure OpenAI API.

        Returns:
            The summarized text as a string.
        """
        summary = ''
        message_text = self.create_summarizer_input()
        summary = self.azure_api_call(message_text)
        return summary
