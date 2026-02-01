import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("OLLAMA_API")

def llama_model(prompt: str):
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url+"/api/generate", json=payload)
    return response