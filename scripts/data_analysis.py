# Importing modules
import pandas as pd

class DataAnalysis:
    def __init__(self, data):
        self.data = data

    def get_list_of_characters(self, from_season, to_season=None, from_episode=None, to_episode=None, season_col='Season_Number', episode_col='Episode_Number'):
        if to_season:
            season_data = self.data.loc[(self.data[season_col] >= from_season) & (self.data[season_col] <= to_season)] 
        else:
            season_data = self.data.loc[self.data[season_col] == from_season]
        if to_episode:
            episode_data = season_data.loc[(season_data[episode_col] >= from_episode) & (season_data[episode_col] <= to_episode)]
        else:
            episode_data = season_data.loc[season_data[episode_col] == from_episode]
        characters = episode_data['Speaker'].str.lower().unique().tolist()
        return characters
    
    def get_top_n_characters(self, n_char, from_season, to_season=None, from_episode=None, to_episode=None, season_col='Season_Number', episode_col='Episode_Number'):
        # Filter the data for the specified season and episode range

        season_data = self.data[(self.data[season_col] >= from_season) & (self.data[season_col] <= to_season)] 
        filtered_data = season_data[(season_data[episode_col] >= from_episode) & (season_data[episode_col] <= to_episode)]
       
        # Count the number of dialogues per character
        dialogue_count = filtered_data['Speaker'].str.lower().value_counts()

        # Get the top characters
        top_characters_names = dialogue_count.head(n_char).index.tolist() 
        top_characters_dialogues = dialogue_count.head(n_char).tolist()
        return top_characters_names, top_characters_dialogues

    

if __name__ == '__main__':
    cleaned_data = pd.read_csv('data/ouput_dialogues.csv')
    data_analysis = DataAnalysis(cleaned_data)
    top_5_characters, top_5_characters_dialogues = data_analysis.get_top_n_characters(n_char=10, from_season=1, to_season=1, from_episode=1, to_episode=5, season_col='Season_Number', episode_col='Episode_Number')
    # print(top_5_characters)