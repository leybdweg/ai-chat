# What's the idea here?

- I'm always into learning new stuff. The new hype is clearly AI + python (fastApi, RAG & ollama)
- Conclusion: here's a small project using my web developer abilities from nodeJS trying to find my way with the new technologies
- packages and technologies are on requirements.txt


# How to run
- if you've got docker & docker-compose, you're good to go
  - `docker compose up --no-deps --watch`

# Expected flows:
  - embed data + generate embedded prompt
  - generate prompt w/o embed (obviously, takes much longer)


# How to access the Application
After running the container, the FastAPI app should be accessible at:

`http://localhost:8000`

You can interact with the API and view the automatically generated documentation provided by FastAPI at:

`http://localhost:8000/docs`

# What's missing?

- e2e tests are a must
- probably some renaming and some files moving around


### Special thanks for
- YF for giving the idea
- ND for instructing me on AI stuff
- https://github.com/Da9el00/Docker_FastAPI_Ollama for providing the head start
