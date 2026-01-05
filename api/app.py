# api/app.py
from fastapi import FastAPI
from pydantic import BaseModel
from flows.summarize_flow import summarize_flow

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/summarize/text")
def summarize_text(input: TextInput):
    result = summarize_flow({"text": input.text})
    return result
