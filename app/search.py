from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

#Connect to embeddings

embeddings = OpenAIEmbeddings(
    model = "text-embedding-3-small"
    )

#Connect to Chroma

vector_store = Chroma(
    persist_directory = "data/vectorstore/chroma",
    embedding_function=embeddings
    )


"""
results = vector_store.similarity_search(
    query,
    k=3 #k=3 means return three most similar chunks
    ) #note we actually have 2 chunks, so only those will be returned
"""

#Create retriever

retriever = vector_store.as_retriever(
    search_kwargs = {"k":3}

)

#Create chat model

llm = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature = 0
)

#Ask a question

def ask_question(query):
    results = retriever.invoke(query)

    context = "\n\n".join(
    document.page_content
    for document in results
    
    )

    prompt = f"""
    You are a helpful assitant answering questions about a company document.

    Use ONLY the information provided in the context below.

    If the answe cannot be found in the context, say:
    "I could not find the answer in the provided document."

    Context:
    {context}

    Question:
    {query}

    Answer

    """

    #Generate the answer

    response = llm.invoke(prompt)

    sources = []

    for document in results:
        source = document.metadata.get("source")

        if source and source not in sources:
            sources.append(source)

    return response.content, sources

#query = input("Ask a question?")

#Retrieve documents

#results = retriever.invoke(query)

#Combine the documents


#Create the prompt



#Display the answer

#print("\nAnswer:")
#print(response.content)

"""
for i, result in enumerate(results,start=1):

    print(f"\n--- Result {i} ---")

    print(result.page_content)

    print("\nMetadata:")
    print(result.metadata)
"""



