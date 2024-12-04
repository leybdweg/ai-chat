from typing import List, Optional

from pydantic import BaseModel
from fastapi import APIRouter, Query

from app.conversation import generate_response, embed_texts, generate_embedded_response

api_router = APIRouter()


class PromptRequest(BaseModel):
    model: str | None = "llama3.2:1b"
    prompt: str


@api_router.post("/generate")
async def generate_text(request: PromptRequest):
    model = request.model
    prompt = request.prompt

    response = await generate_response(prompt, model)

    return {"generated_text": response}


@api_router.post("/generate_embed")
async def generate_embbeded_text(request: PromptRequest):
    model = request.model
    prompt = request.prompt

    response = await generate_embedded_response(prompt, model)

    return {"generated_embedded_text": response}


class EmbedRequest(BaseModel):
    texts: List[str]


@api_router.post("/embed")
async def embed(body: EmbedRequest):
    await embed_texts(body.texts)

    return "OK"


class OutputRequest(BaseModel):
    ids: Optional[List[str]] = Query(None, description="List of IDs"),
    where: Optional[str] = Query(None, description="Filter condition"),
    limit: Optional[int] = Query(None, description="Maximum number of results"),
    offset: Optional[int] = Query(None, description="Starting point for results")

    @classmethod
    def as_query(cls,
                 ids: List[str] = Query(None, description="List of IDs"),
                 where: Optional[str] = Query(None, description="Filter condition"),
                 limit: Optional[int] = Query(None, description="Maximum number of results"),
                 offset: Optional[int] = Query(None, description="Starting point for results")
                 ):
        print('as_query - idsss0', ids, ids[0])
        print('as_query - idsss1 type', type(ids), type(ids[0]))
        return cls(ids=ids, where=where, limit=limit, offset=offset)
