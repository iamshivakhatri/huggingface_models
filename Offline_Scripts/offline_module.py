from transformers import pipeline
import torch
import streamlit as st


def load_model_audio(model_path):
    model = pipeline("automatic-speech-recognition", model=model_path)
    return model

def save_uploaded_audio(uploaded_file):
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return uploaded_file.name
