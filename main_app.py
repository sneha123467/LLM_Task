import streamlit as st
from streamlit_option_menu import option_menu
import invoice_qna
import json_app
import multipleinvoice_qna
import emailspamdetection
import summarization
import sentimentanalysis
import language
import spellingcorrection
import textclassification
import contentgeneration


st.set_page_config(page_title="Sreamlit App", page_icon="💼", layout="wide")

with st.sidebar:
    selected = option_menu(
        menu_title = "Main menu",
        options = ["📜 JSON Parsing","💬  Invoice QnA", "💬 Multiple Invoice QnA", "📧 Email Spam Detection","📝  Summarization","🧠💬 Sentiment Analysis","🌍🔤  Language Detection & Translation","✅ Spelling Correction","🏷️ Text Classification","💡 Content Generation"],
        icons = ['Home','Home',"Buger",'Home',"Buger",'Home',"Buger",'Home',"Buger",'Home',"Buger"]
    )

if selected == "📜 JSON Parsing":
    json_app.run()
elif selected == "💬  Invoice QnA":
    invoice_qna.run() 

elif selected == "💬 Multiple Invoice QnA":
    multipleinvoice_qna.run() 

elif selected == "📧 Email Spam Detection":
    emailspamdetection.run()

elif selected == "📝  Summarization":
    summarization.run()

elif selected == "🧠💬 Sentiment Analysis":
    sentimentanalysis.run()

elif selected == "🌍🔤  Language Detection & Translation":
    language.run()

elif selected == "✅ Spelling Correction":
    spellingcorrection.run()

elif selected == "🏷️ Text Classification":
    textclassification.run()

elif selected == "💡 Content Generation":
    contentgeneration.run()











