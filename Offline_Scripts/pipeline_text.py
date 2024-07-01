from transformers import pipeline

model_path = "models/models--distilbert-base-uncased-finetuned-sst-2-english/snapshots/714eb0fa89d2f80546fda750413ed43d93601a13"
model_path1 = "models/models--mistralai--Mistral-7B-Instruct-v0.3/snapshots/83e9aa141f2e28c82232fea5325f54edf17c43de"
classifier = pipeline("text-classification", model=model_path)


print(classifier(""))