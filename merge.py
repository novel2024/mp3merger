import streamlit as st
from pydub import AudioSegment
from io import BytesIO

def combine_mp3_files(file1, file2):
    sound1 = AudioSegment.from_file(file1)
    sound2 = AudioSegment.from_file(file2)
    combined = sound1 + sound2
    return combined

st.title('MP3 Combiner')

uploaded_file1 = st.file_uploader("Choose the first MP3 file", type="mp3")
uploaded_file2 = st.file_uploader("Choose the second MP3 file", type="mp3")

if uploaded_file1 is not None and uploaded_file2 is not None:
    combined_mp3 = combine_mp3_files(uploaded_file1, uploaded_file2)
    
    # Convert the combined audio to bytes
    bytes_io = BytesIO()
    combined_mp3.export(bytes_io, format="mp3")
    
    st.audio(bytes_io, format='audio/mp3')
    
    # Let users download the combined MP3
    st.download_button(
        label="Download combined MP3",
        data=bytes_io.getvalue(),
        file_name="combined.mp3",
        mime="audio/mp3"
    )