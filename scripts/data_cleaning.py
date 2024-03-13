"""
A module for cleaning and processing dialogue data from CSV files. This module
includes functionalities to read CSV files containing dialogue and reference data,
manipulate and clean the dialogue data, match dialogue speakers to characters from
the reference data, and write the processed data back to a CSV file.

Classes:
    DataCleaning: A class that encapsulates methods for data cleaning and processing.

Example usage:
    data_cleaner = DataCleaning()
    data_cleaner.data_cleaning_main('data/game-of-thrones.csv', 'data/characters_v4.csv')
"""

import os
import warnings
import pandas as pd
import numpy as np

# Ignore all warnings
warnings.filterwarnings("ignore")



class DataCleaning:
    """
    A class used to perform data cleaning operations on dialogue and character reference data.

    Attributes:
        data (pd.DataFrame): A DataFrame to store dialogue data.
        ref_data (pd.DataFrame): A DataFrame to store reference data about characters.

    Methods:
        read_csv(file_path_dialogue_data, file_path_ref_data):
            Reads dialogue and reference data from CSV files.

        get_name_number(from_col_name, new_col_name, season_col):
            Extracts and separates episode number and name, and assigns season numbers.

        get_dialogue_with_speaker(speaker_col):
            Prepares dialogue text with speaker names prefixed.

        remove_additional_punct(dialogue_col, speaker_col, ref_col):
            Cleans punctuation and formats speaker names and reference characters.

        write_dialogues_to_csv(df, output_file_name, cols_to_write):
            Writes specified columns of a DataFrame to a CSV file.

        partial_match_join_speaker(row, key_column, ref_column):
            Matches speakers in dialogue data with characters in reference data
            based on partial string matching.

        data_cleaning_main(file_path_dialogue_csv, file_path_char_csv):
            Orchestrates the data cleaning process using specified CSV files
            for dialogue and characters.
    """
    def __init__(self) -> None:
        """
        Initializes the DataCleaning class with empty DataFrames for storing
        dialogue and reference data.
        """
        self.data = pd.DataFrame()
        self.ref_data = pd.DataFrame()

    def read_csv(self, file_path_dialogue_data, file_path_ref_data):
        """
        Reads dialogue and reference data from the specified CSV files into DataFrames.

        Parameters:
            file_path_dialogue_data (str): The file path for the dialogue data CSV.
            file_path_ref_data (str): The file path for the reference data CSV.

        Raises:
            FileNotFoundError: If either of the specified file paths does not exist.
        """
        if os.path.exists(file_path_dialogue_data):
            self.data = pd.read_csv(file_path_dialogue_data)
        else:
            raise FileNotFoundError(f"""Please check the input file path for dialogue data,
                                    {file_path_dialogue_data} does not exists""")

        if os.path.exists(file_path_ref_data):
            self.ref_data = pd.read_csv(file_path_ref_data)
        else:
            raise FileNotFoundError(f"""Please check the input file path for reference data,
                                    {file_path_ref_data} does not exists""")

    def get_name_number(self, from_col_name='Episode', new_col_name='Episode_name',
                        season_col='Season'):
        """
        Extracts and separates episode numbers and names from a specified column,
        and assigns season numbers.

        Parameters:
            from_col_name (str): The name of the column containing episode
            identifiers to split. Defaults to 'Episode'.
            new_col_name (str): The name for the new column to store episode names.
            Defaults to 'Episode_name'.
            season_col (str): The name of the column containing season identifiers.
            Defaults to 'Season'.
        """
        # try:
        self.data[new_col_name] = self.data[from_col_name].str.split('-', expand=True)[1]
        self.data[from_col_name] = self.data[from_col_name].str.split('-', expand=True)[0]
    # except Exception:
        self.data[new_col_name] = None

        self.data['Episode_Number'] = self.data[from_col_name].apply(lambda x:
                                                                     int(x.split('-')[0]
                                                                         .replace('e', '')))
        self.data['Season_Number'] = self.data[season_col].apply(lambda x: int(x.split('-')[1]))

    def get_dialogue_with_speaker(self, speaker_col='Speaker'):
        """
        Prepends speaker names to dialogue text and cleans up formatting.

        Parameters:
            speaker_col (str): The name of the column containing speaker identifiers.

        Returns:
            pd.DataFrame: The updated DataFrame with dialogue texts prefixed by speaker names.
        """
        self.data[speaker_col].replace(pd.NA, "NARRATOR", inplace=True)
        self.data['dialogue_with_speaker'] = self.data[speaker_col]+":"+self.data['Text']
        self.data['dialogue_with_speaker'] = self.data['dialogue_with_speaker'].str.lstrip()
        return self.data

    def remove_additional_punct(self, dialogue_col='dialogue_with_speaker',
                                speaker_col=None, ref_col='Character'):
        """
        Cleans up punctuation and formats speaker names and reference characters for consistency.

        Parameters:
            dialogue_col (str): The name of the column containing dialogue texts.
            Defaults to 'dialogue_with_speaker'.
            speaker_col (str, optional): The name of the column containing speaker identifiers.
            If specified, only the first name is kept.
            ref_col (str): The name of the column in the reference
            DataFrame containing character names.
            Defaults to 'Character'.
        """
        self.data[dialogue_col] =  self.data[dialogue_col].apply(lambda x:
                                                                 x.replace('[','').replace(']',''))
        if speaker_col:
            self.data[speaker_col] =  self.data[speaker_col].apply(lambda x: x.split(' ')[0])

        self.data[speaker_col] = self.data[speaker_col].str.lower()
        self.ref_data[ref_col] = self.ref_data[ref_col].str.lower()
        self.ref_data[ref_col] = self.ref_data[ref_col].str.replace('willa','will')
        self.ref_data[ref_col] = self.ref_data[ref_col].str.replace("'", '').str.replace("#", '')
        self.data[speaker_col] = self.data[speaker_col].str.replace('[','').str.replace(']','')
        self.data[speaker_col] = self.data[speaker_col].str.replace('(',' ').str.replace(')',' ')
        self.data[speaker_col] = self.data[speaker_col].str.replace('(v.o.)', '', regex=True)

    @staticmethod
    def write_dialogues_to_csv(df_to_write, output_file_name, cols_to_write):
        """
        Writes specified columns of a DataFrame to a CSV file.

        Parameters:
            df (pd.DataFrame): The DataFrame to write to CSV.
            output_file_name (str): The name of the output CSV file.
            cols_to_write (list of str): The list of column names to include in the output CSV.
            Defaults to ['dialogue_with_speaker'].
        """
        df_to_write[cols_to_write].to_csv(output_file_name)

    def partial_match_join_speaker(self, row, key_column='Speaker', ref_column='Character'):
        """
        Attempts to match dialogue speakers to characters in the reference
        data based on partial string matching. This method is designed
        to be applied row-wise to a DataFrame. For each row in the dialogue data,
        it searches for partial matches in the 'Character' column of the
        reference data. If a match is found,the first matching row from the
        reference data is returned. If no match is found, an empty pandas Series
        is returned.

        Parameters:
            row (pd.Series): A row from the dialogue data DataFrame.
                            This function is intended to be used with
                            the DataFrame.apply() method,
                            which passes each row to this function as a Series.
            key_column (str): The name of the column in the dialogue
                            DataFrame that contains the speaker names.
                            Defaults to 'Speaker'.
            ref_column (str): The name of the column in the reference
                            DataFrame that contains character names
                            to match against. Defaults to 'Character'.

        Returns:
            pd.Series: The first row from the reference DataFrame that
            matches the speaker name based on partialstring matching.
            If no match is found, an empty Series is returned.

        Raises:
            ValueError: If `key_column` does not exist in the row or
            `ref_column` does not exist in the reference
            DataFrame, indicating a misconfiguration or data issue.
        """

        key_value = row.get(key_column)
         # Ensure the key exists and is not NaN
        if pd.isna(key_value) or not isinstance(key_value, str):
            return pd.Series()
        match = self.ref_data[self.ref_data[ref_column].str.contains(key_value, na=False)]
        if not match.empty:
            return match[ref_column].iloc[0]

        return pd.Series({col: (row[key_column] if col == ref_column else np.nan)
                          for col in self.ref_data.columns})

    def data_cleaning_main(self, file_path_dialogue_csv, file_path_char_csv):
        """
        Executes the main data cleaning pipeline for dialogue and character data. It reads the
        dialogue and character data from CSV files, formats episode and season info, appends
        speaker names to dialogues, cleans up punctuation, and standardizes speaker names.

        Parameters:
            file_path_dialogue_csv (str): Path to the dialogue data CSV file.
            file_path_char_csv (str): Path to the character reference data CSV file.

        Example usage:
            data_cleaner = DataCleaning()
            data_cleaner.data_cleaning_main('path/to/dialogue.csv', 'path/to/characters.csv')

        Note:
            Assumes correctly formatted and existing input CSV files.
        """
        self.read_csv(file_path_dialogue_data=file_path_dialogue_csv,
                      file_path_ref_data=file_path_char_csv)
        self.get_name_number()
        self.get_dialogue_with_speaker()
        self.remove_additional_punct(speaker_col='Speaker')

        # Applying the function row-wise
        matches = self.data.apply(self.partial_match_join_speaker, axis=1,
                                  args=('Speaker', 'Character'))
        # Combining the original dataframe with the matches
        result = pd.concat([self.data, matches], axis=1)
        result['Character'].fillna('narrator', inplace=True)
        result['Character'] = result['Character'].str.replace("'", '').str.replace("#", '')
        cols_to_write = self.data.columns.tolist() + ['Character']
        self.write_dialogues_to_csv(result, 'thronetalk-game-of-thrones-summarizer/data/ouput_dialogues.csv', cols_to_write=cols_to_write)





if __name__ == '__main__':
    data_cleaner = DataCleaning()
    data_cleaner.data_cleaning_main('thronetalk-game-of-thrones-summarizer/data/game-of-thrones.csv', 'thronetalk-game-of-thrones-summarizer/data/characters_v4.csv')
