"""
This module provides tools for analyzing dialogue data from television shows or movies,
focusing on the extraction and analysis of character dialogue frequencies within
specified season and episode ranges. It supports operations such as listing
unique characters present in the data and identifying the most frequently
speaking characters within a given range of content.

The primary class, `DataAnalysis`, enables users to work directly with
dialogue data loaded into a pandas DataFrame. It offers methods to retrieve
unique characters and to determine the top characters based on dialogue count,
with the option to exclude the narrator from the analysis.

Classes:
    DataAnalysis: Analyzes dialogue data for television shows or movies.

Usage Example:
    >>> cleaned_data = pd.read_csv('data/output_dialogues.csv')
    >>> data_analysis = DataAnalysis(cleaned_data)
    >>> top_n_characters, top_n_characters_dialogues = data_analysis.get_top_n_characters(
    from_season=1, to_season=1, from_episode=1, to_episode=5)
    >>> print(top_n_characters)

Dependencies:
    pandas: Required for data manipulation and analysis.

Note:
    This module assumes that the input dialogue data is structured with specific
    columns for characters, seasons, and episodes. It is designed to be flexible
    with regard to the range of content being analyzed.
"""

import pandas as pd

class DataAnalysis:
    """
    A class for analyzing dialogue data for television shows or movies.
    It offers functionalities to identify and analyze characters based
    on their dialogue frequency and appearances across different seasons
    and episodes.

    Attributes:
        data (pd.DataFrame): DataFrame containing dialogue data with columns
                             for character names, seasons, and episodes.
    """
    def __init__(self, data):
        """
        Initializes the DataAnalysis instance with dialogue data.

        Parameters:
            data (pd.DataFrame): A pandas DataFrame containing dialogue data.
        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("""The input for analysis is incorrect,
                            please check the input it must be dataframe""")
        if data.shape == (0,0):
            raise TypeError("The input dataframe to analysis is empty")
        self.data = data

    def get_list_of_characters(self, from_season, to_season=None,
                               from_episode=None, to_episode=None):
        """
        Retrieves a list of unique characters appearing within a specified
        range of seasons and episodes.

        Parameters:
            from_season (int): The starting season number.
            to_season (int, optional): The ending season number. If not provided,
                                       analysis is limited to `from_season`.
            from_episode (int, optional): The starting episode number. If not
                                          provided, analysis spans all episodes
                                          in the specified seasons.
            to_episode (int, optional): The ending episode number. If not
                                        provided, analysis spans all episodes
                                        up to `to_episode` in `to_season`.

        Returns:
            list: A list of unique character names (lowercased) appearing in the
                  specified season and episode range.
        """
        if to_season:
            season_data = self.data.loc[(self.data['Season_Number'] >= from_season) &
                                        (self.data['Season_Number'] <= to_season)]
        else:
            season_data = self.data.loc[self.data['Season_Number'] == from_season]
        if to_episode:
            episode_data = season_data.loc[(season_data['Episode_Number'] >= from_episode) &
                                           (season_data['Episode_Number'] <= to_episode)]
        else:
            episode_data = season_data.loc[season_data['Episode_Number'] == from_episode]
        characters = episode_data['Character'].str.lower().unique().tolist()
        return characters

    def get_filtered_df(self, from_season,
                        to_season, from_episode,
                        to_episode):
        """
        Filters the dialogue data DataFrame based on season and episode ranges.

        This method filters the `data` DataFrame to include only the rows that fall within
        the specified ranges of seasons and episodes. It iterates through each season and episode,
        applying the specified filters to select the relevant data.

        Parameters:
            from_season (int): The starting season number for filtering.
            to_season (int): The ending season number for filtering.
            from_episode (int): The starting episode number for
            filtering within the starting season.
            to_episode (int): The ending episode number for
            filtering within the ending season.

        Returns:
            pd.DataFrame: A filtered DataFrame containing only the rows that match the specified
                        season and episode range criteria.
        """
        filtered_data = pd.DataFrame()
        start_season_data = self.data.loc[((self.data['Season_Number'] == from_season) &
                                        (self.data['Episode_Number'] >= from_episode))]

        end_season_data = self.data.loc[((self.data['Season_Number'] == to_season) &
                                        (self.data['Episode_Number'] <= to_episode))]

        mid_season_data = self.data.loc[((self.data['Season_Number'] > from_season) &
                                        (self.data['Season_Number'] < to_season))]
        filtered_data = pd.concat([start_season_data, mid_season_data, end_season_data], axis=0)

        return filtered_data

    @staticmethod
    def get_top_n_characters_by_screen_time(filtered_data):
        """
        Calculate and retrieve the names of the top 15 characters based on their
        screen time, measured by the total length of dialogue spoken by each character.

        Parameters:
            df (DataFrame): A DataFrame containing character dialogue data, with at least
                            'Character' and 'Text' columns.

        Returns:
            Series: A Pandas Series containing the names of the top 15 characters.
        """
        # Calculate dialogue length for each character
        filtered_data['Dialogue_Length'] = filtered_data['Text'].apply(lambda x: len(x.split()))

        # Group by character and sum their dialogue lengths
        screen_time = filtered_data.groupby('Character')['Dialogue_Length'].sum().reset_index()

        # Sort by screen time in descending order
        screen_time = screen_time.sort_values(by='Dialogue_Length',
                                              ascending=False)['Character'].to_list()[:15]

        return screen_time


    def get_top_n_characters(self, from_season,
                             to_season=None, from_episode=None,
                             to_episode=None):
        '''
        Retrieves the top characters based on their screen time and dialogue frequency
        within a specified range of seasons and episodes.

        Parameters:
            from_season (int): The starting season number.
            to_season (int, optional): The ending season number. If not provided,
                                    analysis is limited to `from_season`.
            from_episode (int, optional): The starting episode number. If not
                                        provided, analysis spans all episodes
                                        in the specified seasons.
            to_episode (int, optional): The ending episode number. If not
                                        provided, analysis spans all episodes
                                        up to `to_episode` in `to_season`.

        Returns:
            tuple: A tuple containing two tuples:
                - The first tuple contains the top characters based on screen time.
                - The second tuple contains the top characters based on dialogue frequency.
                Each tuple contains two lists:
                - The first list contains the names of the top characters.
                - The second list contains the corresponding screen time or dialogue counts.
        '''
        if to_season < from_season:
            raise ValueError("Incorrect season selection")
        if to_season == from_season:
            if to_episode < from_episode:
                raise ValueError("Incorrect episode selection")

        # Filter the data for the specified season and episode range
        filtered_data = self.get_filtered_df(from_season,
                             to_season, from_episode,
                             to_episode)
        # Exclude the narrator from the analysis
        filtered_data = filtered_data[filtered_data['Character'].str.lower() != 'narrator']

        top_n_characters_screen_time = self.get_top_n_characters_by_screen_time(filtered_data)

        return top_n_characters_screen_time
