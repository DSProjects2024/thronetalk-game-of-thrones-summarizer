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
    

if __name__ == '__main__':
    cleaned_data = pd.read_csv('data/ouput_dialogues.csv')
    data_analysis = DataAnalysis(cleaned_data)
    s1_characters = data_analysis.get_list_of_characters(from_season=1, to_season=None, from_episode=1, to_episode=5, season_col='Season_Number', episode_col='Episode_Number')
    top_5_characters = s1_characters[:5]
    print(s1_characters)