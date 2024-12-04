from app.chroma import chroma_client

# yes, this file is somewhat useless, but separation of concerns is important :)
conversations = chroma_client.create_collection(name="conversations")