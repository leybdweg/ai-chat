# embed data to be used further on
curl -X POST --location "http://localhost:8000/embed" \
    -H "Content-Type: application/json" \
    -d '{
          "texts": [
            "Llamas are members of the camelid family meaning they'\''re pretty closely related to vicuñas and camels",
            "Llamas were first domesticated and used as pack animals 4,000 to 5,000 years ago in the Peruvian highlands",
            "Llamas can grow as much as 6 feet tall though the average llama between 5 feet 6 inches and 5 feet 9 inches tall",
            "Llamas weigh between 280 and 450 pounds and can carry 25 to 30 percent of their body weight",
            "Llamas are vegetarians and have very efficient digestive systems",
            "Llamas live to be about 20 years old, though some only live for 15 years and others live to be 30 years old"
          ]
        }'


# generate response based on embbeded data
curl -X POST --location "http://localhost:8000/infer" \
    -H "Content-Type: application/json" \
    -d '{
          "prompt": "What animals are llamas related to?",
          "model": "llama3.2:1b",
        }'

# generate response w/o embedding (just for fun)
curl -X POST --location "http://localhost:8000/infer" \
    -H "Content-Type: application/json" \
    -d '{
          "prompt": "What animals are llamas related to?",
          "model": "llama3.2:1b",
          "rag": false
        }'