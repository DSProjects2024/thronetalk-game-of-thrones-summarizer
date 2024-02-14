# Component Specification

## Software Components

### Data Manager
1. Episode subtitles (cleaned dialogue for each character, per episode, per season, chunked as input vectors)

Input: Information accessed from Data Constants (mentioned below) \
Output: Preprocessed episode text. Cleaned and tokenized text from each episode's subtitles, stored in a dictionary where keys are episode IDs and values are lists of tokens.

2. Episode and season metadata (title, rating, images and links, description, cast, director, etc.)

Input: CSV file accessed via a local path in Data Constants (below) \
Output: A dictionary containing the episode's metadata (information as key-value pairs).

#### Data Constants
This file contains links to the publicly stored cloud data needed to load episode metadata and episode scripts.

Inputs: None
Outputs: Path to datasets for the scripts to use


### Summarizer Utility Tools 
The Episode Summarizer Utility tool is a software component designed to generate concise summaries for Game of Thrones episodes or seasons based on user input. It will contain a summary generator class which will get input as episode number or season number from the Summarizer webpage. A sequence-to-sequence model with attention mechanism, transformer models, or pre-trained models like BERT and GPT can be employed to then use the episode dialogues, sentiments, key plot points and metadata from data manager to identify crucial moments that define the episode or season from GOT. 

Inputs: Cleaned episode and season metadata and script data from Data Manager \
Outputs: A concise summary of the requested episode or season, along with metadata and visualizations that enhance the user's understanding of the summarized content.

### Episode Summarizer Webpage
The Episode Summarizer Webpage serves as the user interface for our episode summarization system, providing concise and spoiler-free summaries of Game of Thrones episodes. It leverages machine learning models and episode metadata to generate summaries tailored to user preferences. It uses utilizes Python code to integrate Streamlit functions, such as dropdown menus for selecting seasons and episodes or a multiselect box for choosing multiple episodes, and markdown for displaying IMDb descriptions on clicking. Upon getting the input from the user it will run the Episode Summarizer Utility Tool and display the desired episode summary on Streamlit UI. 

Inputs: 
1. Episode Summarizer Utility Tool  
2. User-selected episode (Dropdown) 

Outputs: 
1. Streamlit UI displaying episode summaries based on user input. 


Functionality: 

Dropdown Menu: Users can select the desired season and episode from a dropdown menu, ensuring they receive a summary up to their chosen episode without encountering spoilers. 

Episode Summary: Upon selecting the desired episode, the Streamlit UI dynamically generates a summary of that episode, offering a brief overview of its key events and plot developments. 

Spoiler Prevention: The system ensures that only information up to the selected episode is included in the summary, preventing spoilers for subsequent episodes. 

Streamlit Integration: Utilizing Streamlit functions, the webpage provides an interactive and user-friendly experience, enhancing accessibility and ease of use. 

Additional Features (Good to Have – if time permits): The webpage may include additional elements such as character highlights, notable quotes, or theme analysis to enrich the user's understanding of the episode. 

---

### Component interaction diagram

![alt text](images/comp_spec_uml.png "Title")

---

### Preliminary Plan

1. Scrape data \
    a. Episode/season metadata \
    b. Ratings info for each episode/season \
    c. Episode/season summary \
    d. Episode/season images data (good to have)
2. Clean the subtitles data
3. Data preparation
    a. Text preprocessing \
    b. Chunking text
4. Implement the summarization
    a. Finalize model for summarization \
    b. Train model for text generation \
    c. Fine tune the model on Game of Thrones data \
    d. Black-box testing of generated summary 
5. User Interface
    a. Decide on an initial design (prototype) \
    b. Implement using Streamlit
6. Write test cases
