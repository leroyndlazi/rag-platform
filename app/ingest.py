from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from vectorstore import create_vector_store

pdf_path = r"C:\Users\leroy\Documents\Projects\rag-platform\data\documents\company_manual.pdf"

loader = PyPDFLoader(pdf_path) #Instantiates a PyPDFLoader object pointed at a given pdf

documents = loader.load() #Reads the file and returns a list of Doccument objects, one per page. Where each document haas page content and meta data
text_splitter = RecursiveCharacterTextSplitter( #text splitter configuration 
    chunk_size = 1000,
    chunk_overlap = 200
    )

chunks = text_splitter.split_documents(documents) #splits document into chunks of 1000 charaters

print(f"Number of pages:{len(documents)}")
print(f"Number of chunks: {len(chunks)}")

"""
for i, chunk in enumerate(chunks[:5]):
    print(f"\n--- Chunk {i+1}---")
    print(chunk.page_content)
    print("Metadata:",chunk.metadata)
"""
####
"""
for document in documents:
    print(document.page_content[:500])

"""

vector_store = create_vector_store(chunks) # Connect chunks to vector database

print("Vector database created successfully.")







