from dotenv import load_dotenv
import streamlit as st
import os
import pathlib
import textwrap
import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini  model and get response

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)

