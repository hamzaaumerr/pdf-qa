import os
import streamlit as st
from tempfile import NamedTemporaryFile
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_cohere import CohereEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain_cohere import ChatCohere
from langchain.prompts import PromptTemplate

# Initialize session state variables
if 'api_key' not in st.session_state:
    st.session_state.api_key = ""
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'vector_db' not in st.session_state:
    st.session_state.vector_db = None

st.title("Chat with PDF")

# Sidebar for user input
st.sidebar.title("Configuration")
st.sidebar.subheader("Cohere API Key")
st.session_state.api_key = st.sidebar.text_input("Enter your Cohere API Key", type="password")

# File upload
uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type="pdf")

# Check if API key is entered
if st.session_state.api_key:
    # Load and process the PDF
    if uploaded_file:
        bytes_data = uploaded_file.read()
        with NamedTemporaryFile(delete=False) as tmp:
            tmp.write(bytes_data)
            # tmp.flush()
            pages = PyPDFLoader(tmp.name).load()
        os.remove(tmp.name)

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500,
            chunk_overlap=150,
        )
        splits = text_splitter.split_documents(pages)

        # Initialize embeddings and vector store
        embeddings_model = CohereEmbeddings(cohere_api_key=st.session_state.api_key, model="embed-english-light-v3.0")
        persist_directory = "chroma"
        st.session_state.vector_db = Chroma.from_documents(
            documents=splits,
            embedding=embeddings_model,
            persist_directory=persist_directory,
        )

        st.sidebar.success("PDF loaded and processed successfully!")

        # Display chat history
        for chat in st.session_state.chat_history:
            st.write(f"**You:** {chat['question']}")
            st.write(f"**Bot:** {chat['answer']}")

        # Create a prompt template
        template = """Use the following pieces of context to answer the question at the end. 
        If you don't know the answer, just say that you don't know, don't try to make up an answer. 
        Use ten sentences maximum. Keep the answer as concise as possible.must add "thank you" in the end of response. 
        {context}
        Question: {question}
        Helpful Answer:"""
        QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

        # Initialize the LLM
        llm = ChatCohere(cohere_api_key=st.session_state.api_key, model="command-r")

        # Initialize the QA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm,
            retriever=st.session_state.vector_db.as_retriever(),
            return_source_documents=True,
            chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
        )

        with st.form(key="chat_form", clear_on_submit=True):
            # Query input
            query = st.text_input("Ask a question about the document")
            submit_button = st.form_submit_button("Ask")
            if submit_button:
                if query:
                    result = qa_chain.invoke({"query": query})
                    answer = result["result"]

                    # Save the chat history
                    st.session_state.chat_history.append({"question": query, "answer": answer})
                    st.rerun()
else:
    st.sidebar.warning("Please enter your Cohere API key to continue.")