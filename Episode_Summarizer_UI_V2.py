import streamlit as st
import pandas as pd
import numpy as np
import base64

#st.image("back.jpg", use_column_width=True)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

    
def remove_zeros(lst):
    return [x for x in lst if x != '0']


set_background('back.jpg')
st.title('Game of Thrones - Episode Summarizer')

df = pd.read_csv('Season_Episode_MultiEpisode.csv')
seasons = df.columns.tolist()

st.sidebar.title('Pick From and To Season - Episode')

season_from = st.sidebar.selectbox("Select From Season", seasons)
selected_season_episode_list1 = df[season_from]

selected_season_episode_list_from=remove_zeros(selected_season_episode_list1)
selected_episode_from = st.sidebar.selectbox(f"Select episode from {season_from}", selected_season_episode_list_from, key = 1)


filtered_to_season = [s for s in seasons if s >= season_from]
season_to = st.sidebar.selectbox("Select To Season", filtered_to_season)
selected_season_episode_list2 = df[season_to]

selected_season_episode_list_to=remove_zeros(selected_season_episode_list2)

from_ep_no = selected_episode_from.split()[4]

filtered_to_episode = []
for ep in selected_season_episode_list_to:
    if(ep.split()[1] > season_from):
        filtered_to_episode.append(ep)
    elif(ep.split()[1] == season_from):
        if(ep.split()[4] >= from_ep_no):
            filtered_to_episode.append(ep)


selected_episode_to = st.sidebar.selectbox(f"Select episode from {season_to}", filtered_to_episode, key = 2)

submitted = st.sidebar.button("Submit")

#if submitted == TRUE:
    

#selection_label = f"Season {season_radio}, Episode {selected_episode}"
out_text_temp = f"Episode Summary from {selected_episode_from} to {selected_episode_to}"

#st.text_input("Chosen Season and Episode", value=selection_label)
st.text_area(out_text_temp, value='', height=200)