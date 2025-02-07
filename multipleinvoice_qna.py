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

    # Function to extract text from PDFs
    def pdf_to_text(file_name):
        doc = fitz.open(file_name)
        text = '\n'.join(page.get_text() for page in doc)
        return text

    pdf_dir = "./invoice_templates"
    pdf_texts = ""

    # Load and extract text from all PDFs
    for pdf_file in os.listdir(pdf_dir):
        if pdf_file.endswith('.pdf'):
            file_path = os.path.join(pdf_dir, pdf_file)
            pdf_texts += pdf_to_text(file_path) + "\n\n"

    # Initialize session state for this chatbot
    if "multi_invoice_chat_history" not in st.session_state:
        st.session_state.multi_invoice_chat_history = []

    st.title("💬 Multiple Invoice Chatbot")

    # Display chat history
    for qa in st.session_state.multi_invoice_chat_history:
        st.chat_message("user").markdown(qa["question"])
        st.chat_message("assistant").markdown(qa["answer"])

    # User input
    user_prompt = st.chat_input('Ask about all invoices...')
    if user_prompt:
        st.chat_message("user").markdown(user_prompt)

        # Build conversation history
        multi_history_text = "\n".join([f"User: {qa['question']}\nAI: {qa['answer']}" for qa in st.session_state.multi_invoice_chat_history])

        prompt1 = f'''
        You are an AI assistant that only answers questions **based on the provided multiple invoices**.
        Here is the content from all invoices:\n\n
        {pdf_texts}

        ### **Conversation History**
        {multi_history_text}

        User Query: {user_prompt}
        '''

        prompt2=f'''
        Your are a smart AI assistant .You should answer all the user queries based on only invoice data.
        Follow below guidelines carefully
        1.If the user asks a follow-up question, use the **conversation history and previous responses ** while answering.
        2.If the previous responses refer to a specific file priortize details from the file in the next answer.
        3.If it is the overall query use the entire content and give answer from all the content based on the user condition.
        \n\nInvoice content.\n
        {pdf_texts}
        \n\nHistory.\n
        {multi_history_text}
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
        st.session_state.multi_invoice_chat_history.append({"question": user_prompt, "answer": assistant_response})

        # Display response
        st.chat_message("assistant").markdown(assistant_response)
