from transformers import pipeline

model_path = "models/models--facebook--bart-large-cnn/snapshots/37f520fa929c961707657b28798b30c003dd100b"
summarizer = pipeline("summarization", model=model_path)


ARTICLE = """ New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York.

"""
print(summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False))
