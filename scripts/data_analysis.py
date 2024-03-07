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
    >>> top_n_characters, top_n_characters_dialogues = data_analysis.get_top_n_characters(n_char=10,
    from_season=1, to_season=1, from_episode=1, to_episode=5)
    >>> print(top_n_characters)

Dependencies:
    pandas: Required for data manipulation and analysis.

Note:
    This module assumes that the input dialogue data is structured with specific
    columns for characters, seasons, and episodes. It is designed to be flexible
    with regard to the range of content being analyzed.
"""


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

    def get_top_n_characters(self, n_char, from_season,
                             to_season=None, from_episode=None,
                             to_episode=None):
        """
        Retrieves the names and dialogue counts of the top `n_char` characters based
        on their dialogue frequency within a specified range of seasons and episodes.
        Optionally excludes the narrator from the analysis.

        Parameters:
            n_char (int): The number of top characters to retrieve.
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
            tuple: A tuple containing two lists:
                   - The first list contains the names of the top `n_char` characters.
                   - The second list contains the dialogue counts of these characters.
        """

        # Filter the data for the specified season and episode range
        season_data = self.data[(self.data['Season_Number'] >= from_season) &
                                (self.data['Season_Number'] <= to_season)]
        filtered_data = season_data[(season_data['Episode_Number'] >= from_episode) &
                                    (season_data['Episode_Number'] <= to_episode)]

        # Exclude the narrator from the analysis
        filtered_data = filtered_data[filtered_data['Character'].str.upper() != 'NARRATOR']

        # Count the number of dialogues per character
        dialogue_count = filtered_data['Character'].str.upper().value_counts()

        # Get the top characters
        top_characters_names = dialogue_count.head(n_char).index.tolist()
        top_characters_dialogues = dialogue_count.head(n_char).tolist()

        return top_characters_names, top_characters_dialogues
