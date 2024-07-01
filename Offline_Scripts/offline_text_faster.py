from ctransformers import AutoModelForCausalLM

model_path = 'models/models--TheBloke--Llama-2-7B-GGUF/snapshots/b4e04e128f421c93a5f1e34ac4d7ca9b0af47b80'

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = AutoModelForCausalLM.from_pretrained(model_path, model_file="llama-2-7b.Q4_K_M.gguf", model_type="llama", gpu_layers=1)



prompt = "What is the capital city of nepal?"

# print(llm(f"Question: {prompt} Answer :"))
print(llm("Ai is going to "))
