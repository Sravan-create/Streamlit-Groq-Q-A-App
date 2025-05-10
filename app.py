import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores.faiss import FAISS
import time

# Your Groq API key
groq_api_key = "YOUR API KEY"

# Initialize vector store once per session
if "vector" not in st.session_state:
    st.session_state.embeddings = OllamaEmbeddings(model="llama2")
    st.session_state.loader = WebBaseLoader("https://en.wikipedia.org/wiki/Chocolate")
    st.session_state.docs = st.session_state.loader.load()
    st.session_state.chunk_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    st.session_state.final_documents = st.session_state.chunk_splitter.split_documents(
        st.session_state.docs
    )
    st.session_state.vector = FAISS.from_documents(
        st.session_state.final_documents,
        st.session_state.embeddings
    )

st.title("Chat With Groq")

# Use a valid Groq model ID
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model="llama-3.1-8b-instant"
)

Prompt = ChatPromptTemplate.from_template(
    """Answer the questions based on the provided context only.
    Please provide the most accurate answers based on the context.
    <context>
    {context}
    <context>
    Question: {input}
    """
)

document_chain = create_stuff_documents_chain(llm, Prompt)
retriever = st.session_state.vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

prompt = st.text_input("Input your prompt here")

if prompt:
    response = retrieval_chain.invoke({"input": prompt})
    st.write(response["answer"])

    # Corrected key name from 'Context' to 'context'
    ctx = response.get("context", [])  # Lowercase 'context'

    if ctx:
        with st.expander("Show Context"):
            for doc in ctx:
                st.write(doc.page_content)
                st.write("---------------------------")
