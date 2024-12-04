from typing import List

from app.conversation_collection import conversations

import ollama


# async def embed_texts(texts: List[str]) -> None:
async def embed_texts(texts) -> None:
    for i, d in enumerate(texts):
        response = ollama.embeddings(model="llama3.2:1b",
                                     prompt=d)  # FIXME: this model is the same on the generate_response/endpoint?
        embedding = response["embedding"]
        conversations.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[d]
        )


async def generate_response(prompt: str, model: str) -> str:
    # Call ollama's chat function and stream the response # TODO: whats stream mean here?
    stream = ollama.chat(
        model=model,
        messages=[{'role': 'user', 'content': prompt}],
        stream=True
    )

    # Collect the streamed content
    response_text = "".join(chunk['message']['content'] for chunk in stream)

    return response_text


async def generate_embbeded_response(prompt: str, model: str) -> str:
    embed_result = ollama.embeddings(
        prompt=prompt,
        model=model
    )
    results = conversations.query(
        query_embeddings=[embed_result["embedding"]],
        n_results=1
    )
    response = results['documents'][0][0]

    return response
