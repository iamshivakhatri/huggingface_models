from flask import Flask, request, render_template, redirect, url_for
import os
from transformers import pipeline
import pdfplumber
import yt_dlp
from moviepy.editor import *
import requests

from youtube_transcript_api import YouTubeTranscriptApi


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '../../Flask_Apps/Summarization_App/uploads'

model_path = "../../models/models--facebook--bart-large-cnn/snapshots/37f520fa929c961707657b28798b30c003dd100b"

summarizer = pipeline("summarization", model=model_path)


def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        pages = [page.extract_text() for page in pdf.pages]
    return "".join(pages)


# def extract_transcript_from_youtube(url):
#     ydl_opts = {'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'wav', 'preferredquality': '192'}]}
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info_dict = ydl.extract_info(url, download=False)
#         video_id = info_dict.get("id", None)
#         video_title = info_dict.get('title', None)
#         video_duration = info_dict.get('duration', None)
#         transcript = ""
#         transcript_info = info_dict.get('subtitles', {}).get('en', [])
#         if transcript_info:
#             for trans in transcript_info:
#                 if 'url' in trans:
#                     transcript_url = trans['url']
#                     transcript_response = requests.get(transcript_url)
#                     transcript += transcript_response.text
#         print("This is transcript", transcript)
#     return transcript

def get_video_id(youtube_url):
    # Extract the video ID from the URL
    if "watch?v=" in youtube_url:
        return youtube_url.split("watch?v=")[-1]
    elif "youtu.be/" in youtube_url:
        return youtube_url.split("youtu.be/")[-1]
    else:
        raise ValueError("Invalid YouTube URL format")

def extract_transcript_from_youtube(url):
    try:
        transcript = ""
        video_id = get_video_id(url)
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        for entry in transcript_list:
            transcript = transcript + entry['text'] + " "
        print("Whole text: ", transcript)
    except Exception as e:
        print(f"An error occurred: {e}")
    return transcript

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print("This is request.form", request.form)
        print("thi is request.files", request.files)
        if "pdf" in request.form:
            print("This is pdf selected")
            file = request.files["pdf"]
            if file.filename != "":
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                print("This is file_path", file_path)
                file.save(file_path)
                text = extract_text_from_pdf(file_path)
                summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
                return render_template("index.html", summary=summary[0]['summary_text'])
        elif "youtube_url" in request.form:
            print("This is youtube_url", request.form["youtube_url"])
            youtube_url = request.form["youtube_url"]
            transcript = extract_transcript_from_youtube(youtube_url)
            summary = summarizer(transcript, max_length=130, min_length=30, do_sample=False)
            return render_template("index.html", summary=summary[0]['summary_text'])
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
