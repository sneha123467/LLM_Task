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

    st.title("📝  Summarization")

    long_text = st.text_area("Enter a long text to summarize....")
    
    prompt = '''
    Your are a smart AI Summarizer.You need to summarize a long text \
    that contains 7 to 8 paragraphs into brief summary with necessary \
    headings with proper formatting (Bold etc).
    The breif summary should have the important parts of the long text and should cover almost overall text with less numver of lines.
    '''
    if st.button("Summarize"):
        if long_text == "":
            st.warning("Please enter some text.")
        else:
            full_prompt = f"Prompt {prompt} \n\n User entered long text {long_text} \n\n"
            response = model.generate_content(full_prompt)
            st.markdown(f"### **Brief Summary:**")
            st.markdown(response.text)



