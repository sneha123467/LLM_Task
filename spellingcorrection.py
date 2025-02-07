import streamlit as st
import google.generativeai as gen_ai
from dotenv import load_dotenv
import os

def run():
    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    gen_ai.configure(api_key = GOOGLE_API_KEY)
    model = gen_ai.GenerativeModel('gemini-pro')

    st.title("✅ Spelling Correction")

    input_text = st.text_area("Enter your text ...")

    prompt = f'''
    Your are a smart AI Spelling Corrector . Your job is to use models like "TextBlob"or "GingerIt" or " LanguageTool"\
    to generate correct spelling and grammar in the input text.

    \n\n Input text\n
    {input_text}

    '''

    spelling_prompt = f"""
    You are a helpful AI assistant. Your task is to correct any grammatical errors or spelling mistakes 
    in the given text while ensuring the meaning remains the same. Avoid adding or removing information.
    Please return only the corrected text.

    \n\n Input text\n
    {input_text}

    """

    if st.button("Correction"):

        response = model.generate_content(prompt)

        st.markdown(response.text)