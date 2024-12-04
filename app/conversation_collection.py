from app.chroma import chroma_client

conversations = chroma_client.create_collection(name="conversations")

print('333333', conversations)