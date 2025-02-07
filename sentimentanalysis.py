import streamlit as st
import google.generativeai as gen_ai
from dotenv import load_dotenv
import os

def run():
    # Load environment variables
    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    # Configure Gemini-Pro
    gen_ai.configure(api_key=GOOGLE_API_KEY)
    model = gen_ai.GenerativeModel('gemini-pro')

    st.title("🧠💬 Sentiment Analysis for Food and Film Reviews")

    # Dropdown menu for selecting review type
    review_type = st.selectbox("Select Review Type", ["Food Review", "Film Review"])

    # Prompts for food and film sentiment detection
    food_prompt = '''
    You are an AI-powered Sentiment detector. Your task is to analyze the given sentiment text that contains food-related content. 
    You need to determine whether the sentiment is:

    1. "POSITIVE" if the text expresses satisfaction, enjoyment, or any good review about the food.
    2. "NEGATIVE" if the text expresses dissatisfaction, disappointment, or any bad review about the food.
    3. "NEUTRAL" if the text does not express clear positivity or negativity, and remains neutral or indifferent towards the food. 

    Return the result in JSON format: 
    {'review': 'POSITIVE' / 'NEGATIVE' / 'NEUTRAL'}
    '''
    
    film_prompt = '''
    You are an AI-powered Sentiment detector. Your task is to analyze the given sentiment text that contains film-related content.
    You need to determine whether the sentiment is:

    1. "POSITIVE" if the text expresses satisfaction, enjoyment, or any good review about the film.
    2. "NEGATIVE" if the text expresses dissatisfaction, disappointment, or any bad review about the film.
    3. "NEUTRAL" if the text does not express clear positivity or negativity, and remains neutral or indifferent towards the film. 

    Return the result in JSON format: 
    {'review': 'POSITIVE' / 'NEGATIVE' / 'NEUTRAL'}
    '''
    
    # Input field for sentiment text
    sentiment_text = st.text_area(f"Enter your {review_type.lower()} review...")

    if st.button("Detect Sentiment"):
        if sentiment_text.strip() == "":
            st.warning("Please enter some text.")
        else:
            # Select the appropriate prompt based on review type
            if review_type == "Food Review":
                full_prompt = f"Prompt {food_prompt} \n\n Sentiment content {sentiment_text} . Determine the sentiment as 'POSITIVE', 'NEGATIVE', or 'NEUTRAL'."
            else:
                full_prompt = f"Prompt {film_prompt} \n\n Sentiment content {sentiment_text} . Determine the sentiment as 'POSITIVE', 'NEGATIVE', or 'NEUTRAL'."
            
            # Get the sentiment response from the model
            response = model.generate_content(full_prompt)

            # Output the result
            st.write(response.text.strip())
