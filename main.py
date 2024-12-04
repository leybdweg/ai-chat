import ollama
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import chromadb
app = FastAPI()

# Model for the API input
class PromptRequest(BaseModel):
    model: str = "llama3.2:1b"
    prompt: str

# Helper function to interact with ollama
async def generate_response(model: str, prompt: str) -> str:
    try:
        # Call ollama's chat function and stream the response
        stream = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}],
            stream=True
        )

        response_text = ""
        # Collect the streamed content
        for chunk in stream:
            response_text += chunk['message']['content']

        return response_text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating response: {e}")

@app.post("/generate")
async def generate_text(request: PromptRequest):
    model = request.model
    prompt = request.prompt

    # Generate the response using the helper function
    response = await generate_response(model, prompt)

    return {"generated_text": response}

@app.get("/chroma")
async def chroma():
    chroma_client = chromadb.Client()

    # Generate the response using the helper function
    response = await generate_response(model, prompt)

    return {"generated_text": response}