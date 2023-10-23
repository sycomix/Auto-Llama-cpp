import requests
import io
import os.path
from PIL import Image
from config import Config
import uuid
from base64 import b64decode

cfg = Config()

working_directory = "auto_gpt_workspace"

def generate_image(prompt):
    if cfg.image_provider != 'sd':
        return "No Image Provider Set"
    API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
    headers = {"Authorization": f"Bearer {cfg.huggingface_api_token}"}

    response = requests.post(API_URL, headers=headers, json={
        "inputs": prompt,
    })

    image = Image.open(io.BytesIO(response.content))
    print(f"Image Generated for prompt:{prompt}")

    image.save(os.path.join(working_directory, filename))

    return f"Saved to disk:{filename}"
