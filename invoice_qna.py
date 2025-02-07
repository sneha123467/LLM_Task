import streamlit as st
import fitz
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

    # Function to extract text from a PDF file
    def pdf_to_text(file_name):
        doc = fitz.open(file_name)
        text = '\n'.join(page.get_text() for page in doc)
        return text

    # Load the invoice PDF 
    pdf_file_name = "invoice_templates/invoice_.pdf"  
    content = pdf_to_text(pdf_file_name)

    # Initialize session state for this chatbot
    if "invoice_chat_history" not in st.session_state:
        st.session_state.invoice_chat_history = []

    st.title("💬 Invoice Chatbot ")

    # Display chat history
    for qa in st.session_state.invoice_chat_history:
        st.chat_message("user").markdown(qa["question"])
        st.chat_message("assistant").markdown(qa["answer"])

    # User input
    user_prompt = st.chat_input('Ask about the invoice...')
    if user_prompt:
        st.chat_message("user").markdown(user_prompt)

        # Build conversation history
        history_text = "\n".join([f"User: {qa['question']}\nAI: {qa['answer']}" for qa in st.session_state.invoice_chat_history])

        prompt1 = f'''
        You are an AI assistant that only answers questions **based on the provided invoice**.
        Here is the invoice content:\n\n
        {content}

        ### **Conversation History**
        {history_text}

        User Query: {user_prompt}
        '''

        prompt2=f'''
        You are a smart AI assistant you should answer all user queries bansed only on provided invoice content.
        1.If the user greets you, respond with a friendly greeting. However, only greet the user **once per conversation**, not for every individual query.
        2.Your responses should be **exclusively based on the provided invoice data**. Do not infer, speculate, or include any external information.
        3.If the user asks a follow-up question, use the **conversation history and previous responses ** while answering.
        
        \n\nInvoice content.\n
        {content}
        \n\nHistory.\n
        {history_text}
        \n\n user query.\n
        {user_prompt}
        
        '''

        # Get response from Gemini
        try:
            gemini_response = model.generate_content(prompt2)
            assistant_response = gemini_response.text.strip() or "Sorry, I couldn't generate a response."
        except ValueError:
            assistant_response = "There was an issue processing your request. Please try again later."

        # Store in chat history
        st.session_state.invoice_chat_history.append({"question": user_prompt, "answer": assistant_response})

        # Display response
        st.chat_message("assistant").markdown(assistant_response)
