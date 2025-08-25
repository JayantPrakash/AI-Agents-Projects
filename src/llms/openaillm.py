import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
class OpenAILLM:
    def __init__(self):
        load_dotenv()


    def get_llm(self):
        try:
            os.environ["OPENAI_API_KEY"]=self.open_api_key=os.getenv("OPENAI_API_KEY")
            llm=ChatOpenAI(api_key=self.open_api_key,model="gpt-5")
            return llm
        except Exception as e:
            raise ValueError("Error occurred with exception : {e}")