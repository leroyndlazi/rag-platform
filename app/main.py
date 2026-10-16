import streamlit as st
from search import ask_question

st.set_page_config(
    page_title = "RAG Knowledge Base"
    #page_icon = "D"
    
    )

st.title("RAG Knowledge Base")

st.write(
    "Ask a question about the documents in the knowledge base."
    )

query = st.text_input(
    "Ask a question"
    )

if st.button("Ask"):

    if query:

        with st.spinner("Searching the knowledge base..."):

            answer, sources = ask_question(query)

        st.subheader("Answer")

        st.write(answer)

        st.subheader ("Sources")

        for source in sources:
            st.write(f"-{source}")

    else:

        st.warning("Please enter a question.")



















