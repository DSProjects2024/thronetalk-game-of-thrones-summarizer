import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from wordcloud import WordCloud
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from wordcloud import STOPWORDS
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
import re
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('omw-1.4')

class visualizationGenerator:
    def __init__(self, seasonFrom=1, episodeFrom=1  , seasonTo=1, episodeTo=1):
        self.episodeFrom = int(episodeFrom)
        self.episodeTo = int(episodeTo)
        self.seasonFrom = int(seasonFrom)
        self.seasonTo = int(seasonTo)
        self.df = pd.read_csv("data/ouput_dialogues.csv")
    
    def preProcessDataForCharacter(self, character):
        #s2 e3
        df = self.df
        episodeArr = []
        seasonArr = []
        characterMask = df[df['Character'].str.upper() == character.upper()]
        episodeArr = []
        seasonArr = []
        dialogueString = ''
        for i in range(self.seasonFrom,self.seasonTo+1):
            seasonMaskDF = characterMask[characterMask['Season'] == "season-0"+str(i)]
            for j in range(1, 11):
                # sesason 2 epi 4
                if(i  == self.seasonFrom and j>=self.episodeFrom):
                    episodeMaskDF = seasonMaskDF[seasonMaskDF['Episode'] == 'e'+str(j)]
                    #dialogueString = ''
                    for dialogue in episodeMaskDF.values:
                        dialogueString = dialogueString + dialogue[1]
                    #print("season: "+str(i)+" episode: "+str(j))
                elif(i  == self.seasonTo and j<=self.episodeTo):
                    episodeMaskDF = seasonMaskDF[seasonMaskDF['Episode'] == 'e'+str(j)]
                    #dialogueString = ''
                    for dialogue in episodeMaskDF.values:
                        dialogueString = dialogueString + dialogue[1]
                    #print("season: "+str(i)+" episode: "+str(j))
                elif(i<self.seasonTo and i>self.seasonFrom):
                    episodeMaskDF = seasonMaskDF[seasonMaskDF['Episode'] == 'e'+str(j)]
                    #dialogueString = ''
                    for dialogue in episodeMaskDF.values:
                        dialogueString = dialogueString + dialogue[1]
                    #print("season: "+str(i)+" episode: "+str(j))
        return(dialogueString)
   
    def preProcessDataForCharacterPerEpisode(self, character):
        df = self.df
        charEpisodeWiseArr = []
        characterMask = df[df['Character'].str.upper() == character.upper()]
        #print(characterMask.head(10))
        episodeArr = []
        seasonArr = []
        #s3 epi 6 to s5 epi 2
        for i in range(self.seasonFrom,self.seasonTo+1):
            seasonMaskDF = characterMask[characterMask['Season'] == "season-0"+str(i)]
            for j in range(1, 11):
                # sesason 2 epi 4
                if(i  == self.seasonFrom and j>=self.episodeFrom):
                    episodeMaskDF = seasonMaskDF[seasonMaskDF['Episode'] == 'e'+str(j)]
                    dialogueString = ''
                    for dialogue in episodeMaskDF.values:
                        dialogueString = dialogueString + dialogue[1]
                    charEpisodeWiseArr.append(dialogueString)
                    #print("season: "+str(i)+" episode: "+str(j))
                elif(i  == self.seasonTo and j<=self.episodeTo):
                    episodeMaskDF = seasonMaskDF[seasonMaskDF['Episode'] == 'e'+str(j)]
                    dialogueString = ''
                    for dialogue in episodeMaskDF.values:
                        dialogueString = dialogueString + dialogue[1]
                    charEpisodeWiseArr.append(dialogueString)
                    #print("season: "+str(i)+" episode: "+str(j))
                elif(i<self.seasonTo and i>self.seasonFrom):
                    episodeMaskDF = seasonMaskDF[seasonMaskDF['Episode'] == 'e'+str(j)]
                    dialogueString = ''
                    for dialogue in episodeMaskDF.values:
                        dialogueString = dialogueString + dialogue[1]
                    charEpisodeWiseArr.append(dialogueString)
                    #print("season: "+str(i)+" episode: "+str(j))
        return charEpisodeWiseArr

    
    
    def preProcessData(self):
        df = self.df
        episodeArr = []
        seasonArr = []
        for i in range(self.episodeFrom, self.episodeTo+1):
            episodeArr.append('e'+str(i))
        for i in range(self.seasonFrom,self.seasonTo+1):
            seasonArr.append("season-0"+str(i))

        seasonMaskDF = df[df['Season'].isin(seasonArr)]
        episodeMaskDF = seasonMaskDF[seasonMaskDF['Episode'].isin(episodeArr)]
        dialogueString = ''
        for dialogue in episodeMaskDF.values:
            dialogueString = dialogueString + dialogue[1]

        return(dialogueString)
    
    def multiWordCloud(self, charArr):
        print(charArr)
        plot_obj_arr = []
        for char in charArr:
            stopwords = set(STOPWORDS)
            wordCloudStr = self.preProcessDataForCharacter(char)
            print(wordCloudStr)
            words = wordCloudStr.lower().split()
            words = [re.sub("[.,!?:;-='...'@#_]", " ", s) for s in words]
            words = [re.sub(r'\d+', '', w) for w in words]
            words = [word.strip() for word in words if word not in stopwords]
            #words.remove('')
            tfidf = TfidfVectorizer().fit(words)
            lemmatiser = WordNetLemmatizer()
            lem_words = [lemmatiser.lemmatize(w, pos='v') for w in tfidf.get_feature_names()]
            words_counter = Counter(lem_words)
            wordcloud = WordCloud(stopwords=stopwords)
            wordcloud.generate_from_frequencies(words_counter)
            # plt.imshow(wordcloud, interpolation='bilinear')
            # plt.axis("off")
            # plt.show()
            # st.pyplot()
            plot_obj_arr.append(wordcloud)
        return plot_obj_arr
    
    def wordCloud(self):
        wordCloudStr = self.preProcessData()
        wordcloud = WordCloud().generate(wordCloudStr)
        # plt.imshow(wordcloud, interpolation='bilinear')
        # plt.axis("off")
        # plt.show()
        # st.pyplot()

    def preprocess_text_sentiment(self, text):
        #TODO - if a character does not speak in a given episode his sentiment should be None instead of 0.0
        tokens = word_tokenize(text)
        filtered_tokens = []
        for token in tokens:
            if token not in stopwords.words('english'):
                filtered_tokens.append(token)
        lemmatizer = WordNetLemmatizer()
        processed_text = ' '.join([lemmatizer.lemmatize(each_token) for each_token in filtered_tokens])
        return processed_text
    
    def get_sentiment(self, charArr):
        totArr = []
        episode_num = []
        season_num = []
        for char in charArr:
            sentimentArr = []
            sentimentArrperCharperEpisode = self.preProcessDataForCharacterPerEpisode(char)
            for episode in sentimentArrperCharperEpisode:
                processed_text = self.preprocess_text_sentiment(episode)
                analyzer = SentimentIntensityAnalyzer()
                scores = analyzer.polarity_scores(processed_text)
                #sentiment = 1 if scores['compound'] > 0 else 0
                sentimentArr.append(scores['compound'])
            totArr.append(sentimentArr)
        return totArr

    def generateSingleSentiment(self):
        sentiment = 0
        return sentiment
    
    def generateSentiment(self):
        listofSentiments = []
        
        return listofSentiments
    

    def sentimentAnalysisVisualization(self, charArr):
        sentimentArr = self.get_sentiment(charArr)
        #print("sdsadasd: "+str(sentimentArr))
        chart_data = pd.DataFrame(np.asarray(sentimentArr).transpose())
        #print(np.asarray(sentimentArr).transpose())
        #print(sentimentArr)
        #st.line_chart(chart_data)
        #plt.plot(chart_data)
        # #plt.axis("off")
        #plt.show()
        #st.pyplot()
        return chart_data
    
if __name__ == '__main__':
    vg = visualizationGenerator(1,1,1,3)
    vg.multiWordCloud([
  "narrator",
  "eddard",
  "catelyn"
])
    vg.sentimentAnalysisVisualization(['TYRION','WAYMAR'])
