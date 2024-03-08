import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS
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

class VisualizationGenerator:
    def __init__(self, seasonFrom, episodeFrom, seasonTo, episodeTo):
        params = [seasonFrom, episodeFrom, seasonTo, episodeTo]
        # Python raises `TypeError` automatically if we don't provide the kwargs
        if any([not isinstance(param, int) for param in params]):
            raise ValueError("seasonFrom, episodeFrom, seasonTo and episodeTo must be integers!")
        if seasonFrom < 1:
            raise ValueError("seasonFrom can't be less than 1!")
        if 1 < episodeFrom < 10 or 1 < episodeFrom < 10:
            raise ValueError("episodeFrom and episodeTo values should be within 1 to 10!")
        if seasonTo > 8:
            raise ValueError("seasonFrom can't be greater than 8!")
        if (seasonFrom*10 + episodeFrom) >= (seasonTo*10 + episodeTo):
            raise ValueError("From value can't be greater than or equal to To value!")

        self.episodeFrom = int(episodeFrom)
        self.episodeTo = int(episodeTo)
        self.seasonFrom = int(seasonFrom)
        self.seasonTo = int(seasonTo)
        self.df = pd.read_csv("data/ouput_dialogues.csv")
    
    def preProcessDataForCharacter(self, character):
        #s2 e3
        print("chars: ")
        df = self.df
        characterMask = df[df['Character'].str.upper() == character.upper()]
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
        print("sdsfsd: ",str(dialogueString))
        return(dialogueString)
   
    def preProcessDataForCharacterPerEpisode(self, character):
        df = self.df
        charEpisodeWiseArr = []
        characterMask = df[df['Character'].str.upper() == character.upper()]
        #print(characterMask.head(10))
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
        if not isinstance(charArr, list):
            raise TypeError("charArr should be a list!")
        if len(charArr) < 1:
            raise ValueError("Provide at least 1 character names.")
        if any([not isinstance(name, str) for name in charArr]):
            raise ValueError("Names in charArr should be string!")
        if any([len(name) < 1 for name in charArr]):
            raise ValueError("Names cannot be empty!")
        
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
            print(words)
            tfidf = TfidfVectorizer().fit(words)
            lemmatiser = WordNetLemmatizer()
            lem_words = [lemmatiser.lemmatize(w, pos='v') for w in tfidf.get_feature_names_out()]
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
        if not isinstance(charArr, list):
            raise TypeError("charArr should be a list!")
        if len(charArr) < 1:
            raise ValueError("Provide at least 1 character names.")
        if any([not isinstance(name, str) for name in charArr]):
            raise ValueError("Names in charArr should be string!")
        if any([len(name) < 1 for name in charArr]):
            raise ValueError("Names cannot be empty!")
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
    vg = VisualizationGenerator(1,1,1,3)
    vg.multiWordCloud([
  "narrator",
  "eddard",
  "catelyn"
])
    vg.sentimentAnalysisVisualization(['TYRION','WAYMAR'])