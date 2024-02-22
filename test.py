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

urls = [
'https://www.moneycontrol.com/news/business/air-india-tata-advanced-systems-to-invest-rs-2300-crore-in-karnataka-12302971.html',
'https://www.moneycontrol.com/news/business/air-india-to-upgrade-boeing-777-787-fleet-with-thales-inflight-entertainment-system-12307191.html',
'https://www.moneycontrol.com/news/business/dgca-fines-air-india-rs-1-10-crore-for-for-deploying-aircraft-with-less-emergency-use-oxygen-reserve-12116001.html'
]


#load data
loader = UnstructuredURLLoader(urls=urls)
data = loader.load()

#text splitter
text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size = 1000
    )
docs = text_splitter.split_documents(data)

embeddings = OpenAIEmbeddings()
vector_store_openai = FAISS.from_documents(docs, embeddings)


llm = OpenAI(temperature=0.9, max_tokens=500)
chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever = vector_store_openai.as_retriever())
query = 'How much is Air India & TASL planning to invest in Karnataka?'
result = chain({'question':query}, return_only_outputs=True)
print(result)
print('-------------')
query = 'Why did DGCA impose penalty on Air India?'
result = chain({'question':query}, return_only_outputs=True)
print(result)