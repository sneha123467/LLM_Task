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

    st.title("🌍🔤 Language Detection & Translation")

    # Dropdowns for selecting languages
    operation = st.selectbox("Select Operation", ["Language Detection", "Language Translation"])
    
    # Only show language selection for translation
    if operation == "Language Translation":
        source_lang = st.selectbox("Select Source Language", ["English", "French", "Spanish", "German", "Hindi","Telugu","Tamil"])
        target_lang = st.selectbox("Select Target Language", ["English", "French", "Spanish", "German", "Hindi","Telugu","Tamil"])

    input_text = st.text_area("Enter your text")

    if st.button(f"{operation}"):
        if input_text.strip() == "":
            st.warning("Please enter some text.")
        else:
            if operation == "Language Detection":
                prompt = f"""
                You are an AI Language Detector. Analyze the given text and determine the language name.
                Return the result in JSON format: {{"language": "English"}}
                """
            else:  # Language Translation
                prompt = f"""
                You are an AI Language Translator. Your task is to translate the given text from {source_lang} to {target_lang}.
                Return only the translated text.
                """

            # Generate response
            response = model.generate_content(prompt + f"\n\nInput Text: {input_text}")

            # Check response
            if response and response.candidates:
                translated_text = response.candidates[0].content.parts[0].text
                st.markdown(f"**Result:** {translated_text}")
            else:
                st.warning("No valid response was returned. Please try again.")

