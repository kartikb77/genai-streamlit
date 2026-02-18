# Streamlit + langchain
#import required libraries

import os
import streamlit as st

#imports python's built in os module to interact with the operating system, allowing the code to access environment variables and perform file operations.

from langchain_community.llms import Ollama

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser


#step 1 : create prompt template
#this defines how ai should behave and how it receives user input
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant , please answer clearly to the questions asked by the user"),
        ("user", "Question : {question}"),
    ]
)

#step 2 : stream app ui
st.title("Chatbot with Streamlit and Langchain")

#text input box for user to ask question
input_txt = st.text_input("Ask a question?")

#step 3 : load ollama model
#load local gemma model using ollama
model = Ollama(model="gemma2:2b")

#convert output model to string
output_parser = StrOutputParser()

#create langchain pipeline (prompt --> model --> output_parser)
chain = prompt | model | output_parser

#step 4: 
if input_txt:
    with st.spinner("Generating response..."):
        response = chain.invoke({"question": input_txt})
    st.write("Response:", response)