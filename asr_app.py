import streamlit as st
import os
import tempfile
import whisper

# Replace this with your automatic speech recognition function
def speech_recognition_function(audio_file_path):
    # Your ASR function goes here
    # It should take in the path of the audio file and return the transcribed text
    model = whisper.load_model("base")
    result = model.transcribe(audio_file_path)
    asr_text = result["text"]

    return asr_text

# # Function to rerun the app
# def rerun():
#     raise RerunException(RerunData(widget_state=None))

# Streamlit app title
st.title('Speech Recognition App')



# File uploader allows user to upload their own audio file
uploaded_file = st.file_uploader("Please upload an .mp3 audio file", type=["mp3"])

if uploaded_file is not None:
    # Get the file name and change the extension to .txt
    save_file_name = uploaded_file.name.rsplit('.', 1)[0] + '.txt'
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
        tmpfile.write(uploaded_file.getvalue())
        tmp_path = tmpfile.name  # We'll use this later

    # for processing banner
    placeholder = st.empty()

    # Button to trigger the transcription process
    if st.button(':blue[Transcribe]'):
        placeholder.text('Audio processing. Please wait ...')
        transcribed_text = speech_recognition_function(tmp_path)
        placeholder.text('Audio processing finished.')
        os.unlink(tmp_path)  # Deletes the temp file

        # Display the transcribed text
        st.text_area("Transcribed Text:", transcribed_text)

        # Button to download the transcribed text as a .txt file
        if st.download_button(label = ':blue[Download Transcribed Text]', 
                              data = transcribed_text, 
                              file_name = save_file_name,
                             mime = 'text/plain'):
           st.write('Thanks for downloading!')

    # # Button to reset the app to its initial state
    # if st.button('Clear Uploaded file and Rerun App'):
    #     uploaded_file = None
    #     placeholder.text('Uploaded file cleared.')
    #     st.experimental_rerun()