# NON docker start (with fastapi cli)
`pip install -r requirements.txt`  // only first time

`fastapi dev main.py`

# Dockerized FastAPI LLM Setup

This repository contains a FastAPI application packaged inside a Docker container for easy deployment and scalability. Follow the steps below to build and run the containerized FastAPI application.

## Prerequisites

Ensure you have the following installed on your system before proceeding:

- Docker (https://docs.docker.com/get-docker/)

## Steps to Build and Run the Dockerized FastAPI Application

Build the Docker Image
Run the following command to build the Docker image from the Dockerfile in your project directory. This will create a Docker image named `my-fastapi-app`:

`docker build -t ai-chat .`

Run the Docker Container
Once the image is built, you can run the container and map it to port `8000` on your local machine. Use the following command:

`docker run -p 8000:8000 ai-chat`

Explanation: - `-p 8000:8000`: Maps port 8000 on your local machine to port 8000 inside the Docker container, making the FastAPI app accessible at `http://localhost:8000`.

Access the Application
After running the container, the FastAPI app should be accessible at:

`http://localhost:8000`

You can interact with the API and view the automatically generated documentation provided by FastAPI at:

`http://localhost:8000/docs`
