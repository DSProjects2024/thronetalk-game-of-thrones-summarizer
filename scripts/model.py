import os
from openai import AzureOpenAI
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
        client = AzureOpenAI(
            azure_endpoint = st.secrets["AZURE_ENDPOINT"], 
            api_key = st.secrets["AZURE_OPENAI_KEY"],
            api_version="2024-02-15-preview"
)
        
        completion = client.chat.completions.create(
        model="ThroneTalk", # model = "deployment_name"
        messages = messageText,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
        )
        #completion = 'This is a test completion. API has been commented out '+ str(messageText)
        return completion.choices[0].message.content
    
    def summarize(self):
        summary = ''
        messageText = self.createSummarizerInput()
        summary = self.azureAPICall(messageText)
        #summary = self.extractOutput(rawData)
        return summary

if __name__ == '__main__':
    got = model(1,1,2,2)
    print(got.summarize()) 