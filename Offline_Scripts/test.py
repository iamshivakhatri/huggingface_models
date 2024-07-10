from ctransformers import GPT2

# Load the model
model = GPT2()

# Generate text
prompt = "Once upon a time"
generated_text = model.generate(prompt, max_length=50)

print(generated_text)
