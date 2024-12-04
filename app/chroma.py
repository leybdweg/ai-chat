import chromadb

print('11111')
# async def main():
chroma_client = chromadb.Client()
print('22222')

"""
collection.add(
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges"
    ],
    # metadatas=["aaa", "bbb"],
    ids=["id1", "id2"]
)
print('444444')
results = collection.query(
    query_texts=["This is a query document about hawaii"],  # Chroma will embed this for you
    n_results=2  # how many results to return
)
print('555555')
print(results)
# aaabc = 123
"""

