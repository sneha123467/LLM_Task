import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai
import os

def run():

    load_dotenv()
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

    gen_ai.configure(api_key = GOOGLE_API_KEY )
    model = gen_ai.GenerativeModel('gemini-pro')

    st.title("💡 Content Generation")

    topic_text = st.text_input("Enter your topic ...")

    specifications_text = st.text_area("Enter your specifications ...")

    prompt = f"""
    You are a smart AI Content generator. Your task is to generate the content based on the given topic and provided specifications.

    ### **Topic:**
    {topic_text} 

    ### **Specifications:**
    {specifications_text}

    """
    if st.button("Generate"):
        if topic_text == '' or specifications_text == '':
            st.warning("Please provide the topic name or specifications to create content ...")
        response = model.generate_content(prompt)
        st.markdown(response.text)