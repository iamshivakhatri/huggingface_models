import ollama
import time
import json
import os
import numpy as np
from numpy.linalg import norm

def parse_file(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        paragraphs = []
        buffer = []
        for line in file.readlines():
            line = line.strip()
            if line:
                buffer.append(line)
            elif len(buffer) >0:
                paragraphs.append((" ").join(buffer)) 
                buffer = []

        # Append the last paragraph if buffer is not empty
        if buffer:
            paragraphs.append((" ").join(buffer))
        return paragraphs
    
def get_embeddings(filename, model_name, chunks):

    if (embeddings:= load_embeddings(filename)) is not False:
        return embeddings
    embeddings = [
        ollama.embeddings(model=model_name, prompt=chunk)["embedding"]
        for chunk in chunks
    ]

    # Save embeddings to file
    save_embeddings(filename, embeddings)
    return embeddings

def save_embeddings(filename, embeddings):
    if not os.path.exists("Rag_Apps/Groundup/embeddings"):
        os.makedirs("Rag_Apps/Groundup/embeddings/")

    with open(f"Rag_Apps/Groundup/embeddings/{filename}.json", 'w', encoding='utf-8') as file:
        json.dump(embeddings, file)

def load_embeddings(filename):
    if not os.path.exists(f"Rag_Apps/Groundup/embeddings/{filename}.json"):
        return False
    
    with open(f"Rag_Apps/Groundup/embeddings/{filename}.json", 'r', encoding='utf-8') as file:
        return json.load(file)

def find_most_similar(needle, haystack):
    needle_norm = norm(needle)
    similarity_scores = [
        np.dot(needle, item)/(needle_norm * norm(item)) for item in  haystack
    ]
    return sorted(zip(similarity_scores, range(len(haystack))), reverse=True)
 
def main():
    filename = "./output_text_file.txt"
    paragraphs = parse_file(filename)
    start = time.perf_counter()
    embeddings = get_embeddings(filename, "mistral", paragraphs)
    end = time.perf_counter()

    prompt = "How to tell a nice story?"
    print(embeddings)
    prompt_embedding = ollama.embeddings(model="mistral", prompt=prompt)["embedding"]

    # Find the most similar paragraph to the prompt
    most_similar_chunks = find_most_similar(prompt_embedding, embeddings)[:5]
    for item in most_similar_chunks:
        print(item[0], paragraphs[item[1]])

    print(f"Time taken: {end-start}")



if __name__  == "__main__":
    main()