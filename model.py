from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
import streamlit as st
import os

os.environ["GOOGLE_API_KEY"] = st.secrets["api_keys"]["GOOGLE_API_KEY"]


llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", temperature = 0.5)

#prompt
prompt = PromptTemplate(input_variables=['history', 'input'], template='You are a helpful chatbot. \n\nCurrent conversation:\n{history}\nHuman: {input}\nAI:')

memory = ConversationBufferWindowMemory(k=10)
chain = ConversationChain(llm=llm, memory = memory, prompt = prompt)

def generate_response(user_input):
    result = chain.invoke(user_input)
    return result['response']