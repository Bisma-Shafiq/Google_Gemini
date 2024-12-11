import os
import pathlib
import streamlit as st
import textwrap
from dotenv import load_dotenv
load_dotenv()

from PIL import Image
import google.generativeai as genai

envir = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=envir)

def get_gemini_response(input,image,prompt):
        
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([input,image[0],prompt])
        return response.text

def input_image_setup(upload):
     if upload is not None:
          byte_data = upload.getvalue()
          image_part = [
               {
               "mime_type": upload.type,
               "data": byte_data
               }
          ]
          return image_part
     else:
          raise FileNotFoundError("no file found")

# Streamlit app 

st.set_page_config(page_title="Invoice-Extractor")

st.header("LLM Invoice Extractor/Translator")

input = st.text_input("Input Prompt: ",key="input")

upload = st.file_uploader("Choose an image of invoice ...", type=["jpg", "jpeg", "png"])
image=""   

if upload is not None:
    image = Image.open(upload)
    st.image(image, caption="Image Uploaded.", use_column_width=True)

button = st.button("Tell me about invoice")

input_prompt = """
               you are an expert in understanding invoice.
               Recieve an input invoice and give answer according to this image"""

if button:
    image_data = input_image_setup(upload)
    response = get_gemini_response(input_prompt ,image_data,input)
    st.subheader("Response is: ")
    st.write(response)




    