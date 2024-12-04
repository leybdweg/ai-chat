from typing import List, Optional, Any

# from chromadb.api.types import ID, OneOrMany, Where
from pydantic import BaseModel
from fastapi import APIRouter, Query, Depends

from app.conversation import generate_response, embed_texts
from app.conversation_collection import conversations

api_router = APIRouter()


class PromptRequest(BaseModel):
    model: str | None = None
    prompt: str


@api_router.post("/generate")
async def generate_text(request: PromptRequest):
    model = request.model
    prompt = request.prompt

    # Generate the response using the helper function
    response = await generate_response(model, prompt)

    return {"generated_text": response}


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

        # print('as_query - idsss0', ids, ids[0])
        # print('as_query - idsss1 type', type(ids), type(ids[0]))
        # parsed_ids = [str(x) for x in ids] if ids else None
        # return cls(ids=parsed_ids, where=where, limit=limit, offset=offset)


@api_router.get("/output")
async def aaa(params: OutputRequest = Depends(OutputRequest.as_query)):
    print('idsss0', params.ids, params.ids[0])
    print('idsss1 type', type(params.ids), type(params.ids[0]))
    ooo = conversations.get(
        ids=params.ids,
        # where=params.where,
        # limit=params.limit,
        # offset=params.offset,
    )
    print("ooooooooo", ooo)
    return ooo
