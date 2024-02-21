import os
import openai
import streamlit as st
class model:
    def __init__(self, seasonFrom=1, episodeFrom=1  , seasonTo=1, episodeTo=1):
        self.episodeFrom = episodeFrom
        self.episodeTo = episodeTo
        self.seasonFrom = seasonFrom
        self.seasonTo = seasonTo
    
    def createSummarizerInput(self):
        if self.episodeFrom == self.episodeTo and self.seasonFrom == self.seasonTo:
            messageText = [{"role":"system","content":"Summarize Game of thrones season "+ str(self.seasonFrom) + " episode "+ str(self.episodeFrom) + " in 300 words."}]
            
        else:
            messageText = [{"role":"system","content":"Summarize Game of thrones from season "+ str(self.seasonFrom) + " episode "+ str(self.episodeFrom) + " to season " + str(self.seasonTo) + " episode " + str(self.episodeTo) + " in 300 words."}]
        return messageText 

    def azureAPICall(self, messageText):
        openai.api_type = "azure"
        openai.api_base = st.secrets["API_BASE"]
        #"https://soft-proj.openai.azure.com/"
        openai.api_version = "2023-07-01-preview"
        openai.api_key = st.secrets["API_KEY"]
        #need to secure apikey. Use tip#6 https://blog.streamlit.io/8-tips-for-securely-using-api-keys/
        completion = openai.ChatCompletion.create(
        engine="gpt35",
        messages = messageText,
        temperature=0.09,
        max_tokens=4096,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
        )
        completion = 'This is a test completion. API has been commented out '+ str(messageText)
        return completion
    
    def extractOutput(self, completion):
        return completion
    
    def summarize(self):
        summary = ''
        messageText = self.createSummarizerInput()
        rawData = self.azureAPICall(messageText)
        summary = self.extractOutput(rawData)
        return summary