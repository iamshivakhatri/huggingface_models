from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the tokenizer
try:
    tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.3")
    print("Tokenizer loaded successfully")
except Exception as e:
    print(f"Error loading tokenizer: {e}")

# Load the model
try:
    model = AutoModelForCausalLM.from_pretrained("models/models--mistralai--Mistral-7B-Instruct-v0.3/snapshots/0417f4babd26db0b5ed07c1d0bc85658ab526ea3", torch_dtype=torch.float16).to(device)
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")

# Define the prompt
prompt = "What is the capital of Nepal?"

messages = [{"role": "user", "content": prompt}]

# Tokenize the input
try:
    encoded_input = tokenizer.apply_chat_template(messages, return_tensors="pt")
    input_ids = encoded_input.to(device)
    print("Input tokenized successfully")
except Exception as e:
    print(f"Error tokenizing input: {e}")

# Run the inference
try:
    output = model.generate(input_ids, max_new_tokens=100, do_sample=True, top_p=0.95, top_k=1000, temperature=1.0, pad_token_id=tokenizer.eos_token_id)
    print("Inference ran successfully")
    print(tokenizer.decode(output[0], skip_special_tokens=True))
except Exception as e:
    print(f"Error during inference: {e}")
