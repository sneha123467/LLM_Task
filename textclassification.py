import streamlit as st
import google.generativeai as gen_ai
from dotenv import load_dotenv
import os

def run():
    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    gen_ai.configure(api_key = GOOGLE_API_KEY)
    model = gen_ai.GenerativeModel('gemini-pro')

    st.title("🏷️ Text Classification")

    input_text = st.text_area("Enter your text here ....")

    prompt = f"""
    Your are samrt AI Text Classifier . Your task is to classify the text predefined labels(Technology, Finance, Medical, Agriculture) 
    You need to return in the table format . the table contains two rows and columns\
    with column names as "Text" and "Label" and it is the first row/
    in the second row under "Text" column provide user entered input text and\
    under "Label" column return the classification name or label name.

    \n\n Input text\n
    {input_text}

    """

    prompt1 = f"""
    You are a highly intelligent AI text classifier. Your task is to analyze the given input text and classify it into the most relevant category.  

    You are not restricted to predefined labels but should determine the most appropriate classification dynamically based on the text content.  

    ### **Guidelines:**  
    1. Understand the meaning and context of the input text.  
    2. Assign a suitable category, such as Technology, Finance, Health, Sports, Education, Politics, Entertainment, Business, Agriculture, Travel, Science, and more.  
    3. If the text does not fit a known category, classify it as "General" or "Other." 
    
    ### **Output Format:**
    1. Analyze the input text and determine the most relevant category.
    2. Return the result in a **table format** with the following structure:
    - **Columns:** "Text" and "Label"
    - **First row:** Column names
    - **Second row:** User-entered input under "Text" and the classified label under "Label".

    ### **Input Text:**
    {input_text}
    """


    if st.button("Classify"):
        if input_text.strip() == "":
            st.wraning("Please enter some text to classify")
        else:
            response = model.generate_content(prompt1)

            st.write(response.text)