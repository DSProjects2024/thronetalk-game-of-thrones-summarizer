import numpy as np
import pandas as pd
import os


class DataCleaning:
    def __init__(self) -> None:
        self.data = pd.DataFrame()

    def read_csv(self, file_path):
        if os.path.exists(file_path):
            self.data = pd.read_csv(file_path)
        else:
            raise FileNotFoundError('Please check the input file path, it does not exists')
        
    def get_name_number(self, from_col_name='Episode', new_col_name='Episode_name', season_col='Season'):
        try:
            self.data[new_col_name] = self.data[from_col_name].str.split('-', expand=True)[1]
            self.data[from_col_name] = self.data[from_col_name].str.split('-', expand=True)[0]
        except:
            self.data[new_col_name] = None

        self.data['Episode_Number'] = self.data[from_col_name].apply(lambda x: int(x.split('-')[0].replace('e', '')))
        self.data['Season_Number'] = self.data[season_col].apply(lambda x: int(x.split('-')[1]))

    def get_dialogue_with_speaker(self, speaker_col='Speaker'):
        self.data[speaker_col].replace(pd.NA, "NARRATOR", inplace=True)
        self.data['dialogue_with_speaker'] = self.data[speaker_col]+":"+self.data['Text']
        self.data['dialogue_with_speaker'] = self.data['dialogue_with_speaker'].str.lstrip()
        return self.data
    
    def remove_additional_punct(self, dialogue_col='dialogue_with_speaker', speaker_col=None):
        # self.data[dialogue_col] = self.data[dialogue_col].str.replace('[','').str.replace(']','')
        self.data[dialogue_col] =  self.data[dialogue_col].apply(lambda x: x.replace('[','').replace(']','')) 
        if speaker_col:
            self.data[speaker_col] =  self.data[speaker_col].apply(lambda x: x.split(' ')[0]) 

    def write_dialogues_to_csv(self, output_file_name, cols_to_write=['dialogue_with_speaker']):
        self.data[cols_to_write].to_csv(output_file_name)

        
    def data_cleaning_main(self, file_path):
        self.read_csv(file_path=file_path)
        self.get_name_number()
        self.get_dialogue_with_speaker()
        self.remove_additional_punct(speaker_col='Speaker')
        self.write_dialogues_to_csv('data/ouput_dialogues.csv', cols_to_write=self.data.columns)


if __name__ == '__main__':
    data_cleaner = DataCleaning()
    data_cleaner.data_cleaning_main('data/game-of-thrones.csv')