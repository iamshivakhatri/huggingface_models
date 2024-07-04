from transformers import pipeline
import torch
import streamlit as st
import os
from diffusers import DiffusionPipeline



@st.cache_resource()
def load_model_audio(model_path):
    model = pipeline("automatic-speech-recognition", model=model_path)
    return model

import os

def save_uploaded_audio(uploaded_file):
    try:
        # Create a directory to save the file
        os.makedirs("audioDir", exist_ok=True)
        
        # Create the full file path
        file_path = os.path.join("audioDir", uploaded_file.name)
        
        # Save the file to the directory
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        return file_path
    except Exception as e:
        return str(e)

    
def generate_text_from_audio(model, audio_file):
    try:
        file_path = save_uploaded_audio(audio_file)
        result = model(file_path)
        print(result)
        return result
    except Exception as e:
        return str(e)
# Image generation
@st.cache_resource()
def load_image_generation_model(model_path):
    model = DiffusionPipeline.from_pretrained(model_path)
    return model

# Generate image from text
def generate_image_from_text(model, text):
    image = model(text)
    return image

def main():
    # st.title("Audio to Text")
    # st.write("This is a simple audio to text conversion app using Hugging Face's pipeline API.")
    # model_path = "../models/models--openai--whisper-medium/snapshots/abdf7c39ab9d0397620ccaea8974cc764cd0953e"
    # model = load_model_audio(model_path)
    
    # uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "ogg"])
    
    # if uploaded_file:
    #     if st.button("Transcribe"):
    #         st.audio(uploaded_file, format="audio/wav")
    #         with st.spinner('Transcribing...'):
    #             result = generate_text_from_audio(model, uploaded_file)
    #             st.write(result)
    st.title("Text to Image")
    st.write("This is a simple text to image generation app using Hugging Face's pipeline API.")
    model_path = "../models/models--stabilityai--stable-diffusion-xl-base-1.0/snapshots/462165984030d82259a11f4367a4eed129e94a7b"
    model = load_image_generation_model(model_path)
    prompt = st.text_input("Enter a prompt", value="A cat sitting on a table")
    if st.button("Generate Image"):
        with st.spinner('Generating...'):
            image = generate_image_from_text(model, prompt)
            st.image(image, use_column_width=True)

       
if __name__ == "__main__":
    main()

