# import streamlit as st
# import google.generativeai as gen_ai
# from dotenv import load_dotenv
# import os
# import whisper

# def run():
#     load_dotenv()
#     GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

#     gen_ai.configure(api_key = GOOGLE_API_KEY)
#     model = gen_ai.GenerativeModel('gemini-pro')

#     st.title("🗣️ Speech Recognition")

#     uploaded_audio_file = st.file_uploader("Upload audio",type=['mp3','wav','audio'])

#     if uploaded_audio_file:
#         st.write("Successfully uploaded..")

#     whisper_model = whisper.load_model("base")

#     audio_to_text_result = whisper_model.transcribe(uploaded_audio_file)

#     st.write("Extracted text is",audio_to_text_result["text"])
import streamlit as st
import whisper
import tempfile
import os

def run():
    st.title("🎙️ Speech Recognition - Convert Audio to Text")

    whisper_model = whisper.load_model("base")

    # Upload audio file
    uploaded_audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a"])

    if uploaded_audio_file is not None:
        # Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_audio.write(uploaded_audio_file.read())
            temp_audio_path = temp_audio.name  # Get the file path

        st.audio(uploaded_audio_file, format="audio/wav")  # Play audio

        # Transcribe the audio file
        result = whisper_model.transcribe(temp_audio_path)

        # Display transcription
        st.subheader("Transcription:")
        transcribed_text = result["text"]
        st.text_area("Transcribed Text", transcribed_text, height=200)

        # Create a downloadable text file
        txt_filename = "transcription.txt"
        with open(txt_filename, "w") as f:
            f.write(transcribed_text)

       # Provide download button
        with open(txt_filename, "rb") as f:
            st.download_button(
                label="📥 Download Transcription",
                data=f,
                file_name=txt_filename,
                mime="text/plain"
            )

        # Clean up temp files
        os.remove(temp_audio_path)
        os.remove(txt_filename)

