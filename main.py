from fastapi import FastAPI
from ollama_api import llama_model

app = FastAPI()

@app.post("/generate")
def generate(prompt):
    res = llama_model(prompt)
    return res.json()