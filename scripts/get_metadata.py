from imdb import Cinemagoer
import json

def get_show_metadata(show_id):
    if not show_id or len(show_id) == 0:
        raise ValueError('Provide a valid show_id!')
    ia = Cinemagoer()
    got = ia.get_movie(show_id)
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
    if len(output_file) < 5 or '.json' not in output_file:
        raise ValueError('Provide a valid output_file of .json type.')
    if not dict_data or len(dict_data.keys()) == 0:
        raise ValueError('Provide a valid dictionary data to write to the output file!')
    with open(output_file, 'w') as outfile:
        json.dump(dict_data, outfile, sort_keys=True, indent=2)

IMDB_GOT_ID = '0944947'
data = get_show_metadata(IMDB_GOT_ID)
write_show_metadata('../data/show_metadata.json', data)
# IMDB_EPISODE_IDS = {
#     1: ["1480055", "1668746", "1829962", "1829963", "1829964", "1837862", "1837863", "1837864", "1851398", "1851397"],
#     2: ["1971833", "2069318", "2070135", "2069319", "2074658", "2085238", "2085239", "2085240", "2084342", "2112510"],
#     3: ["2178782", "2178772", "2178802", "2178798", "2178788", "2178812", "2178814", "2178806", "2178784", "2178796"],
#     4: ["2816136", "2832378", "2972426", "2972428", "3060856", "3060910", "3060876", "3060782", "3060858", "3060860"],
#     5: ["3658012", "3846626", "3866836", "3866838", "3866840", "3866842", "3866846", "3866850", "3866826", "3866862"],
#     6: ["3658014", "4077554", "4131606", "4283016", "4283028", "4283054", "4283060", "4283074", "4283088", "4283094"],
#     7: ["5654088", "5655178", "5775840", "5775846", "5775854", "5775864", "5775874"],
#     8: ["5924366", "6027908", "6027912", "6027914", "6027916", "6027920"],
# }



