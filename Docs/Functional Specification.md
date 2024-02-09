# Functional Specification

### Background

Everyone loves a good TV show. Everyone loves binge-watching a good TV show. But life only gives us 24 hours every day to do that. That’s only 19 hours on some days if you are a UW MSDS student. Even less if you have an assignment or mid-term due the next day. As the days pass, you lose track of the plot of what you’ve watched. You try to google the summary till the episode/season you’ve watched, but end up getting spoilers for the next season and lose interest in the show. We’ve all been there.

Through this project, we try to provide a solution for this by generating recaps till the episode the user has watched or till the season the user has watched. By taking the subtitles data for each episode of Game of Thrones (all 8 seasons), we want to generate summaries according to the user’s inputs (generate summaries till a particular episode or generate season-level summaries). We hope to create a robust model that can generalize for other shows as well and help users catch up with their favorite TV shows.

### User profile

User 1: discontinued the show for a couple of weeks and now wants to get a recap of all the previous seasons.
Interaction method: Web application
Wants: Quick summarization pf season or episodes to quickly understand or catch up on episodes
Needs: Summary of previous watched episodes
Skills: Does not have any technical skills and values a simple interface

User 2: Screen writer/Content Creators
Wants: to research on the show to maybe create a similar show/ prequel or sequel using the episode summary generated.
Interaction method: Web application
Needs: More accurate summary
Skills: Does not have any technical skills and values a simple interface

User 3: AI/ML engineer
Wants:  AI/ML engineer who will update the model based on user feedback and other metrics.
Interaction method: Interaction with the codebase
Needs: Robust and bug-free model with high availability. Access to a dataset of GOT episode transcripts or summaries for training the model.
Skills: Highly technical and knows programming skills.


### Data sources

    1. Dialogues for each character - https://www.kaggle.com/datasets/gopinath15/gameofthrones
    2. Character allegiances and relationship data -https://www.kaggle.com/datasets/mylesoneill/game-of-thrones

### Use cases

Explicit Use case: 

    1. View season summary / summary till particular episode
        User: Selects either the season and episode option
        System: shows the options

        User: Opens the web application
        System: Two inputs one being season level summary and other for episode summary

        User: Clicks on generate summary
        System: Displays the summary to the user



Implicit Use Case: 

    1. Summarization ML model works every time
        User: Inputs either episode info or season info
        System: [if model returns a summary] Display the summary to the user
        [if model throws an error] Display "something went wrong" and give user the option to retry
