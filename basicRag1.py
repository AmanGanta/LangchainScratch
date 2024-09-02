from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


ld=PyPDFLoader(r"C:\Users\amang\Downloads\proj celeb search by krish naik\1706.03762v7.pdf")
dc=ld.load()

ts=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
docs=ts.split_documents(dc)

