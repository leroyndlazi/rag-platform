from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

def create_vector_store(chunks):  #a function that will take chunks and create embeddings Using OpenAI 

    embeddings = OpenAIEmbeddings( #Creates and embedding model which converts text to numbers
        model = "text-embedding-3-small"
        )

    vector_store = Chroma.from_documents( #Takes chunks to embedding model and form vectors, and forms a vector database (ChromaDB)
        documents=chunks,
        embedding=embeddings,
        persist_directory="data/vectorstore/chroma" #persist_directory means the database is stored locally
        )

    return vector_store