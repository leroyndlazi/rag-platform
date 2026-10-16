# RAG Platform

An internal knowledge-base system that allows users upload documents and ask questions about them. 
The system uses a Retrieval-Augmented Generation (RAG) approach to provide accurate and relevant answers based on the uploaded documents.

## Purpose

The system will:

1. Accept company documents
2. Extract their text
3. Split the text into smaller chunks
4. Create embeddings
5. Store the embeddings
6. Retrieve relevant information
7. Use an AI model to answer questions
8. Provide references to the original documents

## Tech Stack

Python
LangChain
OpenAI Embeddings
ChromaDB
Streamlit

## Project Structure

RAG-Platform/
├── app/
│   ├── ingest.py
│   ├── main.py
│   ├── search.py
│   └── vectorstore.py
├── data/
├── .gitignore
├── .env.example
└── README.md

##Setup

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install the project dependencies.
4. Configure the required environment variables.
5. Run the document ingestion and application scripts.

## Environment Variables

Create a local .env file containing your required API credentials. Never commit real API keys or secrets to GitHub.

## Status

Under development.


