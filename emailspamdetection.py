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

    st.title("📧 Email-Spam Detection")


    prompt = '''
    You are an AI-powered email spam detector. Your task is to analyze the given email content and classify it as either "Spam" or "Not Spam" (Ham). 

    Follow the below guidelines carefully

    1.If the email contains promotional offers, phishing attempts, scams, or excessive use of spam trigger words (e.g., "free", "win", "urgent", "claim now"), classify it as **Spam**.
    2.If the email is a regular, professional, or personal message without spam characteristics, classify it as **Not Spam**.
    3.Return the result in JSON format:
    {"email_type": "Spam"} '''


    email_text = st.text_area("Enter the email content:", "")

    if st.button("Detect Spam"):
        if email_text.strip() == "":
            st.warning("Please enter some text.")
        else:
            full_prompt = f'Prompt {prompt} \n\n Email content {email_text} .Classify the email as either "Spam" or "Not Spam (Ham)"'
            response = model.generate_content(full_prompt)

            response = response.text.strip()
            st.write(response)

