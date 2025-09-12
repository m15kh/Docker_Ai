from fastapi import FastAPI
from models import generate_text



app = FastAPI()


@app.post("/generate")

def generate_endpoint(prompt: str):
    return generate_text(prompt)