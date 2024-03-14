"""
Game of Thrones - Episode Summarizer App

This Streamlit application provides a user interface
for summarizing episodes of Game of Thrones.
It includes sentiment analysis, word clouds, episode summaries,
and images from the selected range of episodes.

Usage:
1. Select the desired range of episodes using the provided dropdown menus
        for season and episode numbers.
2. Click on the "Generate Summary" button to generate the episode summary for the
        selected range of episodes and sentiment
        analysis and word clouds for top 3 characters.
3. Scroll down to view the generated content, including the episode summary,
        sentiment analysis, word clouds, and images.

"""
import os
import time
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
from utils.model import Model
from utils.visualization_generator import VisualizationGenerator, read_dataframe
from utils.data_analysis import DataAnalysis

st.set_page_config(layout="wide")
current_directory = os.path.dirname(__file__)
csv_file_path = os.path.join(current_directory, 'data', 'Season_Episode_MultiEpisode.csv')
def remove_zeros(lst):
    """"
    Remove zeros from a list.
    Args:
        lst (list): A list containing elements.
    Returns:
        list: A new list with zeros removed.
    Example:
        remove_zeros([0, 1, 2, 0, 3, 0])
        output = [1, 2, 3]
    """
    return [x for x in lst if x != '0']
st.title('Game of Thrones - Summarizer')
df = pd.read_csv(csv_file_path)
seasons = df.columns.tolist()
st.sidebar.title('Select Season : Episode range')
st.sidebar.header('From')
season_from = st.sidebar.selectbox("Season", seasons, key=0)
selected_season_episode_list1 = df[season_from]
selected_season_episode_list_from=remove_zeros(selected_season_episode_list1)
selected_episode_from = st.sidebar.selectbox(f"Episode from Season {season_from}",
                                             selected_season_episode_list_from, key = 1)
filtered_to_season = [s for s in seasons if s >= season_from]
st.sidebar.header('To')
season_to = st.sidebar.selectbox("Season", filtered_to_season)
selected_season_episode_list2 = df[season_to]
selected_season_episode_list_to=remove_zeros(selected_season_episode_list2)
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
selected_episode_to = st.sidebar.selectbox(f"Episode from  Season {season_to}",
                                           filtered_to_episode, key = 2)
to_ep_no = selected_episode_to.split()[4]
submitted = st.sidebar.button("Generate Summary")
H1 = "Sentiment Scores Across"
out_text_temp = f"**Episode Summary from {selected_episode_from} to {selected_episode_to}**"
out_text_temp2 = f"**{H1} {selected_episode_from} to {selected_episode_to}**"
season_from = int(season_from)
from_ep_no = int(from_ep_no)
season_to = int(season_to)
to_ep_no = int(to_ep_no)
if submitted:
    cleaned_data = read_dataframe('ouput_dialogues.csv')
    data_analysis = DataAnalysis(cleaned_data)
    top_3_characters = data_analysis.get_top_n_characters(
        from_season=int(season_from),
        to_season=int(season_to),
        from_episode=int(from_ep_no),
        to_episode=int(to_ep_no)
    )
    characters_tuple = top_3_characters[:3]
    #st.write(characters_tuple)
    characters = list(characters_tuple)
    st.subheader(out_text_temp2)
    st.markdown('''This line chart visualizes the ***sentiment scores*** across seasons and episodes
                for the top 3 most active characters within the range selected by the user,
                based ***on-screen time***. Sentiment scores reflect the emotional tone of dialogue
                and actions, with positive scores indicating positive sentiment and negative scores
                indicating negative sentiment. This visualization allows users to track the
                emotional journey of key characters throughout the series, identifying trends,
                patterns, and significant moments in their development.''')
    vg = VisualizationGenerator(
        int(season_from),
        int(from_ep_no),
        int(season_to),
        int(to_ep_no)
    )
    line_chart = vg.sentiment_analysis_visualization(characters)
    chart = alt.Chart(line_chart).transform_fold(
                    characters, as_=["character name", "value"]
                    ).mark_line(
                        point={
                        "filled": False,
                        "fill": "white"
                        }
                            ).encode(
                    x=alt.X('season-episode:O',title = 'Season:Episode', sort=None),
                    y=alt.Y('value:Q', title = 'Sentiment score'),
                    color='character name:N'

                )
    st.altair_chart(chart,use_container_width=True)
    H2 = "Word Cloud of top 3 characters from "
    out_text_2 = f"**{H2} {selected_episode_from} to {selected_episode_to}**"
    st.subheader(out_text_2)
    st.markdown('''These word clouds display the most frequently used words
                 associated with the top 3 characters selected from the sentiment
                analysis above. Each word cloud visually represents the prominence
                of words in the dialogue or actions of these characters throughout
                the selected seasons and episodes. Larger words indicate higher
                frequency of use, offering users a glimpse into the key themes,
                topics, and attributes associated with each character.''')
    columns = st.columns(len(characters))
    wordcloud = vg.multi_word_cloud(characters)
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
    st.write("\n")
    episodes_metadata_for_img_df = read_dataframe('episodes_metadata.csv')
    st.subheader(out_text_temp)
    #Summarizer
    def spinner_loading_summary():
        """
        Generate episode summary using a model with spinner loading.
        Args: None
        Returns:
        string: The episode summary.
        Example Usage:
        spinner_loading_summary()
        'Text with Episode summary for Season x, Episode y to Season m, Episode n'
        """
        got = Model(season_from,from_ep_no, season_to, to_ep_no)
        time.sleep(1)
        return got.summarize()
    with st.spinner('Loading Summary...'):
        EPISODE_SUMMARY = None
        while EPISODE_SUMMARY is None:
            EPISODE_SUMMARY = spinner_loading_summary()
    # st.subheader(out_text_temp)
    # st.success(EPISODE_SUMMARY)
    #*************************************************************
    image_url_list = []
    def generate_combinations(seasonfrom, from_epno, seasonto, to_epno):
        """
        Generate combinations of season and episode numbers.
        Args:
            seasonfrom (int): Starting season number.
            from_epno (int): Starting episode number.
            seasonto (int): Ending season number.
            to_epno (int): Ending episode number.
        Returns:
            pandas.DataFrame: DataFrame containing combinations of season and episode numbers.
        Example Usage:
            generate_combinations(1, 1, 1, 3)
                Season  Episode
            0       1        1
            1       1        2
            2       1        3
        """
        num_episodes = [10, 10, 10, 10, 10, 10, 7, 6]
        combinations = []
        for season in range(seasonfrom, seasonto + 1):
            start_ep = from_epno if season == seasonfrom else 1
            end_ep = to_epno if season == seasonto else num_episodes[season - 1]
            for episode in range(start_ep, end_ep + 1):
                combinations.append((season, episode))
        df2 = pd.DataFrame(combinations, columns=['Season', 'Episode'])
        return df2
    def select_and_print_combinations(df2,no_of_images):
        """
        Randomly select and print combinations of season and episode
        corresponding images on streamlit UI using URLs from dataset
        Args:
            df2 (pandas.DataFrame): DataFrame containing combinations of season and episode numbers.
            no_of_images (int): Number of images to select.
        Returns:
            None
        Example Usage:
            select_and_print_combinations(df2, 3) - This will print 3 images
            on the Streamlit UI
        """
        #selection_list = []
        selected_combinations = df2.sample(no_of_images)
        for _, row in selected_combinations.iterrows():
            #st.write(row['Episode'])
            #st.write(f"Selected Season: {row['Season']}, Episode: {row['Episode']}")
            filtered_df = episodes_metadata_for_img_df[episodes_metadata_for_img_df['season']
                                                       == row['Season']]
            selected_image_url = filtered_df.loc[filtered_df['episode']
                                                 == row['Episode'], 'full-size cover url'].iloc[0]
            #selection_df = pd.DataFrame(selection_list)
            image_url_list.append(selected_image_url)
            #st.write(j)
    combinations_df = generate_combinations(season_from, from_ep_no, season_to, to_ep_no)
    selected_range_length = len(combinations_df.index)
    NO_OF_DISPLAY_IMAGES = 5
    NO_OF_DISPLAY_IMAGES = min(NO_OF_DISPLAY_IMAGES, selected_range_length)
    NO_OF_DISPLAY_IMAGES = int(NO_OF_DISPLAY_IMAGES)
    select_and_print_combinations(combinations_df,NO_OF_DISPLAY_IMAGES)
   #************************************************************
    para_list = []
    text = EPISODE_SUMMARY
    text_to_words = text.split()
    text_length = len(text_to_words)
    part_length=abs(text_length // NO_OF_DISPLAY_IMAGES)
    parts = [text_to_words[i:i+part_length] for i in range(0, text_length, part_length)]
    for i, part in enumerate(parts):
        PARAGRAPH = " ".join(part)
        para_list.append(PARAGRAPH)
        #st.write(para_list)
        #st.write(PARAGRAPH)
    #*************************************************************
    col1, col2 = st.columns(2)
    #for i in range(len(image_url_list)):
    for i, (image_url, para) in enumerate(zip(image_url_list, para_list)):
        if i % 2 == 0:
            with col1:
                st.image(image_url_list[i])
            with col2:
                st.write(para_list[i])
        else:
            with col1:
                st.write(para_list[i])
            with col2:
                st.image(image_url_list[i])
