'''
Contains the implementation of the logic to get the metadata
for the show and all episodes. Uses dependencies ImdbPY and Pandas.
'''
import json
from imdb import Cinemagoer
import pandas as pd

IMDB_GOT_ID = '0944947'
IMDB_EPISODE_IDS = {
    1: ["1480055", "1668746", "1829962", "1829963", "1829964", "1837862", "1837863",
        "1837864", "1851398", "1851397"],
    2: ["1971833", "2069318", "2070135", "2069319", "2074658", "2085238", "2085239",
        "2085240", "2084342", "2112510"],
    3: ["2178782", "2178772", "2178802", "2178798", "2178788", "2178812", "2178814",
        "2178806", "2178784", "2178796"],
    4: ["2816136", "2832378", "2972426", "2972428", "3060856", "3060910", "3060876",
        "3060782", "3060858", "3060860"],
    5: ["3658012", "3846626", "3866836", "3866838", "3866840", "3866842", "3866846",
        "3866850", "3866826", "3866862"],
    6: ["3658014", "4077554", "4131606", "4283016", "4283028", "4283054", "4283060",
        "4283074", "4283088", "4283094"],
    7: ["5654088", "5655178", "5775840", "5775846", "5775854", "5775864", "5775874"],
    8: ["5924366", "6027908", "6027912", "6027914", "6027916", "6027920"],
}

def get_show_metadata(show_id):
    '''
    Gets all the relevant the metadata for the show. Requires a 7 digit string id of
    the show (only numeric values), which must be the IMDB id for the show. Returns a
    dictionary with the relevant metadata like title, genres, ratings etc.
    '''
    if not show_id:
        raise TypeError("Provide show_id parameter!")
    if not isinstance(show_id, str):
        raise TypeError("show_id must be of type str.")
    if len(show_id) != 7:
        raise ValueError('Provide a valid show_id of length 7!')
    scraper = Cinemagoer()
    got = scraper.get_movie(show_id)
    relevant_keys = [
        'title',
        'number of seasons',
        'genres',
        'rating',
        'plot',
        'synopsis',
        'plot outline',
        'runtimes',
        'votes',
        'full-size cover url'
    ]
    show_data= {}
    for key in relevant_keys:
        show_data[key] = got[key]
    show_data['release year'] = int(got['year'])
    show_data['end year'] = int(got['series years'].split('-')[-1])
    show_data['writers'] = [writer['name'] for writer in got['writer']]
    show_data['cast'] = [writer['name'] for writer in got['cast']]
    return show_data

def write_show_metadata(output_file, dict_data):
    '''
    Writes the show metadata into output file. Takes two inputs - 
    1. output_file - must be of string type, should be of type `.json`
    2. dict_data - the output from `get_show_metadata` function
    '''
    if not output_file:
        raise ValueError("Provide output_file parameter!")
    if not isinstance(output_file, str):
        raise TypeError("output_file must be of type str.")
    if len(output_file) < 5 or '.json' not in output_file:
        raise ValueError('Provide a valid output_file of .json type.')
    if not dict_data:
        raise ValueError("Provide dict_data parameter!")
    if len(dict_data.keys()) == 0:
        raise ValueError('Provide a valid dictionary data to write to the output file!')
    with open(output_file, 'r+', encoding="utf-8") as outfile:
        json.dump(dict_data, outfile, sort_keys=True, indent=2)

def _format_episode_metadata(episode_metadata):
    '''
    Takes IMDBPy episode metadata as input and returns a dictionary of formatted values
    of the relevant fields for data analysis. To be accessed only by `get_episode_metadata`
    function.
    '''
    if not episode_metadata:
        raise ValueError("Provide episode_metadata parameter!")
    if len(episode_metadata.keys()) == 0:
        raise ValueError('Provide episode_metadata with valid keys!')
    relevant_keys = [
        'title',
        'synopsis',
        'plot outline',
        'season',
        'episode',
        # 'genres',
        'rating',
        'runtimes',
        'votes',
        'full-size cover url'
    ]
    list_keys = [
        'cast',
        'director',
        'producer',
        'writer',
        # 'composer'
    ]
    show_data= {}
    for key in relevant_keys:
        show_data[key] = episode_metadata[key]
    show_data['plot'] = " ".join(episode_metadata['plot'])
    show_data['previous episode imdb id'] = episode_metadata['previous episode']
    show_data['next episode imdb id'] = episode_metadata.get('next episode', '')
    show_data['release year'] = int(episode_metadata['year'])
    for key in list_keys:
        writers = [writer.get('name', '') for writer in episode_metadata[key]]
        show_data[f'{key}s'] = [w for w in writers if w]
    return show_data

def get_episode_metadata():
    '''
    Gets the relevant the metadata for all the episodes from every season of the show.
    Currently configured to run only on Game of Thrones show.
    '''
    scraper = Cinemagoer()
    episodes = []
    for _, episodes_list in IMDB_EPISODE_IDS.items():
        for episode in episodes_list:
            episode_metadata = scraper.get_movie(episode)
            formatted_metadata = _format_episode_metadata(episode_metadata)
            episodes.append(formatted_metadata)
    return episodes

def write_episode_metadata(output_file, episodes_data):
    '''
    Writes the episodes metadata into output file. Takes two inputs - 
    1. output_file - must be of string type, should be of type `.csv`
    2. episodes_data - the output from `get_episode_metadata` function
    '''
    if not output_file:
        raise ValueError("Provide output_file parameter!")
    if not isinstance(output_file, str):
        raise TypeError("output_file must be of type str.")
    if len(output_file) < 4 or '.csv' not in output_file:
        raise ValueError('Provide a valid output_file of .csv type.')
    if not episodes_data:
        raise ValueError("Provide episodes_data parameter!")
    if len(episodes_data.keys()) == 0:
        raise ValueError('Provide a valid dictionary data to write to the output file!')

    dataframe = pd.DataFrame(episodes_data)
    dataframe.head()
    dataframe.to_csv(output_file, index=False)

if __name__ == "__main__":
    data = get_show_metadata(IMDB_GOT_ID)
    write_show_metadata('thronetalk-game-of-thrones-summarizer/data/show_metadata.json', data)
    episodes_metadata = get_episode_metadata()
    write_episode_metadata('thronetalk-game-of-thrones-summarizer/data/episodes_metadata.csv', episodes_metadata)
