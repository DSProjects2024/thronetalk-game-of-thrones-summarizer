# Component Specification

## Software Components

### Data Manager - Raagul

### Summarizer Utility Tools 
The Episode Summarizer Utility tool is a software component designed to generate concise summaries for Game of Thrones episodes or seasons based on user input. It will contain a summary generator class which will get input as episode number or season number from the Summarizer webpage. A sequence-to-sequence model with attention mechanism, transformer models, or pre-trained models like BERT and GPT can be employed to then use the episode dialogues, sentiments, key plot points and metadata from data manager to identify crucial moments that define the episode or season from GOT. 


Inputs: Cleaned episode and season metadata and script data from Data Manager \
Outputs: A concise summary of the requested episode or season, along with metadata and visualizations that enhance the user's understanding of the summarized content.

### User Interface - Baisakhi

### Component interaction - Abhinav



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
    d. Black-box testing of generated summary \
5. User Interface
    a. Decide on an initial design (prototype) \
    b. Implement using Streamlit
6. Write test cases
