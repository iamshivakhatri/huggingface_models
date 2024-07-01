from diffusers import DiffusionPipeline

model_path = 'models/models--stabilityai--stable-diffusion-xl-base-1.0/snapshots/462165984030d82259a11f4367a4eed129e94a7b'

base = DiffusionPipeline.from_pretrained(model_path)

prompt = "A painting of a beautiful gir near a calm lake."

image = base(prompt,  num_inference_steps=20, guidance_scale=4).images[0]
image.show()