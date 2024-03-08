import streamlit as st
import pandas as pd
import numpy as np
import base64
import os
import time
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scripts.model import model
from scripts.visualization_generator import VisualizationGenerator
from scripts.data_analysis import DataAnalysis

# Get the current directory of the script
current_directory = os.path.dirname(__file__)

# Define the path to the CSV file relative to the current directory
csv_file_path = os.path.join(current_directory, 'data', 'Season_Episode_MultiEpisode.csv')

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
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


def remove_zeros(lst):
    return [x for x in lst if x != '0']


#set_background('back.jpg')
st.title('Game of Thrones - Episode Summarizer')

df = pd.read_csv(csv_file_path)
seasons = df.columns.tolist()

st.sidebar.title('Pick From and To Season - Episode')

st.sidebar.header('From')
season_from = st.sidebar.selectbox("Season", seasons, key=0)
selected_season_episode_list1 = df[season_from]

selected_season_episode_list_from=remove_zeros(selected_season_episode_list1)
#*****
selected_episode_from = st.sidebar.selectbox(f"Episode from Season {season_from}", selected_season_episode_list_from, key = 1)

filtered_to_season = [s for s in seasons if s >= season_from]

st.sidebar.header('To')
season_to = st.sidebar.selectbox("Season", filtered_to_season)

selected_season_episode_list2 = df[season_to]

selected_season_episode_list_to=remove_zeros(selected_season_episode_list2)

#****
from_ep_no = selected_episode_from.split()[4]

filtered_to_episode = []
for ep in selected_season_episode_list_to:
    season_to = int(ep.split()[1])
    episode_to = int(ep.split()[4])

    if season_to > int(season_from):
        filtered_to_episode.append(ep)
    elif season_to == int(season_from):
        if episode_to >= int(from_ep_no):
            filtered_to_episode.append(ep)


selected_episode_to = st.sidebar.selectbox(f"Episode from  Season {season_to}", filtered_to_episode, key = 2)
#****
to_ep_no = selected_episode_to.split()[4]

submitted = st.sidebar.button("Submit")

out_text_temp = f"**Episode Summary from {selected_episode_from} to {selected_episode_to}**"
out_text_temp2 = f"**Sentiment Analysis and Word Clouds from {selected_episode_from} to {selected_episode_to}**"


if submitted:
    cleaned_data = pd.read_csv('data/ouput_dialogues.csv')
    data_analysis = DataAnalysis(cleaned_data)
    top_3_characters, top_3_characters_dialogues = data_analysis.get_top_n_characters(
        n_char=3,
        from_season=int(season_from),
        to_season=int(season_to),
        from_episode=int(from_ep_no),
        to_episode=int(to_ep_no)
    )
    characters = top_3_characters
    st.subheader(out_text_temp2)

    vg = VisualizationGenerator(
        int(season_from),
        int(from_ep_no),
        int(season_to),
        int(to_ep_no))
    line_chart = vg.sentimentAnalysisVisualization(characters)
    st.line_chart(line_chart)
    columns = st.columns(len(characters))
    wordcloud = vg.multiWordCloud(characters)

    # Display word cloud on Streamlit UI
    plots = []
    for w in wordcloud:
        plt.figure(figsize=(10, 5))
        plt.imshow(w, interpolation='bilinear')
        plt.axis('off')
        img = plt.gcf()
        plots.append(img)
    for i, col in enumerate(columns):
        with col:
            st.subheader(characters[i].capitalize())
            st.pyplot(plots[i])

    def spinner_loading_summary():
        got = model(season_from,from_ep_no, season_to, to_ep_no)
        time.sleep(1)
        return got.summarize()

    with st.spinner('Loading Summary...'):
        episode_summary = None
        while episode_summary is None:
            episode_summary = spinner_loading_summary()

    st.subheader(out_text_temp)
    st.success(episode_summary)