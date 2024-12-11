from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import pathlib
import textwrap
import google.generativeai as genai


envir = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=envir)

# function to load Gemini model and get reponse
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    
    response = chat.send_message(question,stream=True)
    return response

# streamlit app

st.set_page_config(page_title="Q&A_ChatBot")

st.header("Q&A ChatBot LLM Application")

# Initialize session state for chat history if not exist
if "chat_history" not in st.session_state:
    st.session_state["chat_history"]=[]

input = st.text_input("Write Prompt Here..... ", key="input")
submit = st.button("Submit")

if submit and input:
    response = get_gemini_response(input)
    st.session_state["chat_history"].append(("YOU",input))
    st.subheader("The Response is ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state["chat_history"].append(("Bot",chunk.text))
    st.subheader("The Chat History: ")

for role,text in st.session_state["chat_history"]:
    st.write(f"{role}:{text}")

