from typing import List

from app.conversation_collection import conversations

import ollama

# async def embed_texts(texts: List[str]) -> None:
async def embed_texts(texts) -> None:
    for i, d in enumerate(texts):
        # response = ollama.embeddings(model="mxbai-embed-large",
        #                              prompt=d)  # FIXME: this model is the same on the generate_response/endpoint?
        # embedding = response["embedding"]
        conversations.add(
            ids=[str(i)],
            # embeddings=[embedding],
            documents=[d]
        )

# async def generate_response(prompt, model) -> str:
#     return "aa"
# async def generate_response(prompt: str, model: str = "llama3.2:1b") -> str
async def generate_response(prompt: str, model: str = "mxbai-embed-large") -> str:
    # Call ollama's chat function and stream the response # TODO: whats stream mean here?
    stream = ollama.chat(
        model=model,
        messages=[{'role': 'user', 'content': prompt}],
        stream=True
    )

    # Collect the streamed content
    response_text = "".join(chunk['message']['content'] for chunk in stream)

    return response_text
