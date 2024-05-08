# loading all the envornment verriables
from dotenv import load_dotenv
from google.generativeai.types.discuss_types import ResponseDict
from grpc.framework.interfaces.face.face import ResponseReceiver
load_dotenv()

import streamlit as st 
import os
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load gemini pro model and get responses 
model = genai.GenerativeModel("gemini-pro")
def get_response(question):
    response=model.generate_content(question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked
if submit:
    response=get_response(input)
    st.subheader("The answer is")
    st.write(response)