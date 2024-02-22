import os
import streamlit as st
import pickle
import time
import langchain
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import OpenAI
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()  

st.title('News Research Tool 📈')
st.sidebar.title('News Article URLS')

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i + 1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLS")

main_placeholder = st.empty()
vector_store_openai = None

if process_url_clicked:
    #load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text('Data loading started...✅ ✅ ✅')
    data = loader.load()

    #split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size = 500
    )

    main_placeholder.text('Text splitter started...✅ ✅ ✅')
    docs = text_splitter.split_documents(data)

    #create embeddings and save them to FAISS index
    embeddings = OpenAIEmbeddings()
    vector_store_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    

llm = OpenAI(temperature=0.9, max_tokens=500)

query = main_placeholder.text_input("Question: ", '')

if query:
    if vector_store_openai:
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever = vector_store_openai.as_retriever())
        result = chain({'question':query}, return_only_outputs=True)

        # Display answers with sources
        st.header('Answer:')
        st.write(result['answer'])
       
        sources = result.get('sources','')
        if sources:
            st.subheader('Sources:')
            sources_list = sources.split('\n')
            for source in sources_list:
                st.write(source)
