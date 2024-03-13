"""
VisualizationGenerator class for Game of Thrones dialogue analysis

This class generates visualizations based on dialogue data from Game of Thrones.

Key features:
- Generates WordCloud visualizations for multiple characters.
- Performs sentiment analysis on character dialogues across multiple episodes.
- Creates DataFrames for sentiment visualization.

Methods:
- __init__(self, season_from: int, episode_from: int, season_to: int, episode_to: int)
    - Initializes the class with specified season and episode ranges for analysis.
- pre_process_data_for_character(self, character: str) -> str
    - Preprocesses dialogue data for a character, returning a concatenated string.
- pre_process_data_for_character_per_episode(self, character: str) -> list[str]
    - Preprocesses dialogue data for a character, returning a list of dialogue strings per episode.
- multi_word_cloud(self, char_arr: list[str]) -> list
    - Generates a list of WordCloud objects for multiple characters.
- preprocess_text_sentiment(self, text: str) -> str
    - Preprocesses text for sentiment analysis (removing stop words, lemmatization).
- get_sentiment(self, char_arr: list[str]) -> list[list[float]]
    - Calculates sentiment scores for characters across episodes using NLTK's VADER.
- sentiment_analysis_visualization(self, char_arr: list[str]) -> pd.DataFrame
    - Generates a DataFrame with sentiment scores for visualization.
"""
import re
from collections import Counter
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud, STOPWORDS
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('omw-1.4')

def read_dataframe(file_name):
    '''Function to read dataframe for different environments. Used for tests
    and app.py'''
    file_data = None
    try:
        file_data = pd.read_csv(f'data/{file_name}')
    except FileNotFoundError:
        file_data = pd.read_csv(f'./thronetalk-game-of-thrones-summarizer/data/{file_name}')
    return file_data

data = read_dataframe('ouput_dialogues.csv')

class VisualizationGenerator:
    """
    This class generates visualizations for characters' dialogue in Game of Thrones.

    Args:
        season_from (int): Starting season (inclusive)
        episode_from (int): Starting episode (inclusive) within season_from
        season_to (int): Ending season (inclusive)
        episode_to (int): Ending episode (inclusive) within season_to
    """

    def __init__(self, season_from: int, episode_from: int,
                 season_to: int, episode_to: int) -> None:
        params = [season_from, episode_from, season_to, episode_to]
        # Python raises `TypeError` automatically if we don't provide the kwargs
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
            raise ValueError("From value can't be greater than or equal to To value!")

        self.episode_from = int(episode_from)
        self.episode_to = int(episode_to)
        self.season_from = int(season_from)
        self.season_to = int(season_to)

    def pre_process_data_for_character(self, character: str) -> str:
        """
        Preprocesses dialogue data for a specific character across specified seasons and episodes.

        Args:
            character (str): Name of the character

        Returns:
            str: Concatenated dialogue string for the character
        """
        # data = self.data
        character_mask = data[data['Character'].str.upper() == character.upper()]
        dialogue_string = ''
        for i in range(self.season_from, self.season_to + 1):
            season_mask_df = character_mask[character_mask['Season'] == "season-0" + str(i)]
            for j in range(1, 11):
                if ((i == self.season_from and j >= self.episode_from) or
                    (i == self.season_to and j <= self.episode_to) or
                    (self.season_from < i < self.season_to)):
                    episode_mask_df = season_mask_df[season_mask_df['Episode'] == 'e' + str(j)]
                    for dialogue in episode_mask_df.values:
                        dialogue_string += dialogue[1]
        return dialogue_string

    def pre_process_data_for_character_per_episode(self, character: str) -> list[str]:
        """
        Preprocesses dialogue data for a specific character across specified seasons and episodes,
        returning a list of dialogue strings per episode.

        Args:
            character (str): Name of the character

        Returns:
            list[str]: List of dialogue strings for the character, one per episode
        """
        # data = self.data
        char_episode_wise_arr = []
        character_mask = data[data['Character'].str.upper() == character.upper()]
        for i in range(self.season_from, self.season_to + 1):
            season_mask_df = character_mask[character_mask['Season'] == "season-0" + str(i)]
            if self.season_from == self.season_to:
                for j in range(self.episode_from,self.episode_to+1):
                    episode_mask_df = season_mask_df[season_mask_df['Episode'] == 'e' + str(j)]
                    dialogue_string = ''
                    for dialogue in episode_mask_df.values:
                        dialogue_string += dialogue[1]
                    char_episode_wise_arr.append(dialogue_string)
                break
            for j in range(1, 11):
                if ((i == self.season_from and j >= self.episode_from) or
                    (i == self.season_to and j <= self.episode_to) or
                    (self.season_from < i < self.season_to)):
                    episode_mask_df = season_mask_df[season_mask_df['Episode'] == 'e' + str(j)]
                    dialogue_string = ''
                    for dialogue in episode_mask_df.values:
                        dialogue_string += dialogue[1]
                    char_episode_wise_arr.append(dialogue_string)
        return char_episode_wise_arr

    def multi_word_cloud(self, char_arr: list[str]) -> list:
        """
        Generates a list of WordCloud objects for multiple characters.

        Args:
            char_arr (list[str]): List of character names

        Returns:
            list: List of generated WordCloud objects
        """

        if not isinstance(char_arr, list):
            raise TypeError("char_arr should be a list!")
        if not char_arr:  # Check for empty list
            raise ValueError("Provide at least 1 character name.")
        if not all(isinstance(name, str) for name in char_arr):
            raise ValueError("All names in char_arr should be strings!")
        if not all(name for name in char_arr):  # Check for empty names
            raise ValueError("Names cannot be empty!")

        plot_obj_arr = []
        for char in char_arr:
            stopwords_from_wordcloud = set(STOPWORDS)
            wordcloud_raw_string = self.pre_process_data_for_character(char)
            words = wordcloud_raw_string.lower().split()
            words = [re.sub(r"[.,!?:;-='...'@#_]", " ", s) for s in words]
            words = [re.sub(r"\d+", "", w) for w in words]
            words = [word.strip() for word in words if word not in stopwords_from_wordcloud]
            tfidf = TfidfVectorizer().fit(words)
            lemmatizer = WordNetLemmatizer()
            lem_words = [lemmatizer.lemmatize(w, pos="v") for w in tfidf.get_feature_names_out()]
            words_counter = Counter(lem_words)
            wordcloud = WordCloud(stopwords=stopwords_from_wordcloud)
            wordcloud.generate_from_frequencies(words_counter)
            plot_obj_arr.append(wordcloud)
        return plot_obj_arr

    def preprocess_text_sentiment(self, text: str) -> str:
        """
        Preprocesses text for sentiment analysis.

        Args:
            text (str): The text to preprocess

        Returns:
            str: The preprocessed text
        """
        tokens = word_tokenize(text)
        filtered_tokens = []
        for token in tokens:
            if token not in stopwords.words('english'):
                filtered_tokens.append(token)
        lemmatizer = WordNetLemmatizer()
        processed_text = ' '.join([lemmatizer.lemmatize(each) for each in filtered_tokens])
        return processed_text

    def get_sentiment(self, char_arr: list[str]) -> list[list[float]]:
        """
        Calculates sentiment scores for a list of characters across episodes.

        Args:
            char_arr (list[str]): List of character names

        Returns:
            list[list[float]]: List of sentiment scores per character, per episode
        """
        sentiment_scores_per_character = []
        for char in char_arr:
            episode_sentiment_scores = self.pre_process_data_for_character_per_episode(char)
            sentiment_scores = []
            for episode in episode_sentiment_scores:
                processed_text = self.preprocess_text_sentiment(episode)
                analyzer = SentimentIntensityAnalyzer()
                scores = analyzer.polarity_scores(processed_text)
                sentiment_scores.append(scores['compound'])
            sentiment_scores_per_character.append(sentiment_scores)

        return sentiment_scores_per_character

    def sentiment_analysis_visualization(self, char_arr: list[str]) -> pd.DataFrame:
        """
        Generates sentiment scores for characters and creates a DataFrame for visualization.

        Args:
            char_arr (list[str]): List of character names

        Returns:
            pd.DataFrame: DataFrame with sentiment scores for visualization
        """
        if not isinstance(char_arr, list):
            raise TypeError("char_arr should be a list!")
        if len(char_arr) < 1:
            raise ValueError("Provide at least 1 character names.")
        if any(not isinstance(name, str) for name in char_arr):
            raise ValueError("Names in char_arr should be string!")
        if any(len(name) < 1 for name in char_arr):
            raise ValueError("Names cannot be empty!")
        sentiment_arr = []
        episode_wise_desc = []
        for i in range(self.season_from, self.season_to + 1):
            if self.season_from == self.season_to:
                for j in range(self.episode_from,self.episode_to+1):
                    episode_wise_desc.append("S"+str(i)+":E"+str(j))
                break
            for j in range(1, 11):
                if i == self.season_from and j >= self.episode_from:
                    episode_wise_desc.append("S"+str(i)+":E"+str(j))
                elif i == self.season_to and j <= self.episode_to:
                    episode_wise_desc.append("S"+str(i)+":E"+str(j))
                elif self.season_from < i < self.season_to:
                    episode_wise_desc.append("S"+str(i)+":E"+str(j))
        sentiment_arr.append(episode_wise_desc)
        sentiment_arr = sentiment_arr + self.get_sentiment(char_arr)
        chart_data = pd.DataFrame(np.asarray(sentiment_arr).transpose(),
                                  columns=['season-episode']+char_arr)
        return chart_data
