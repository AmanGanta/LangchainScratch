from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

ld=PyPDFLoader(r"C:\Users\amang\Downloads\proj celeb search by krish naik\1706.03762v7.pdf")
dc=ld.load()

ts=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
docs=ts.split_documents(dc)
docs[:10]

if docs:
    db = Chroma.from_documents(docs, OpenAIEmbeddings(),persist_directory="./chroma_db")
else:
    print("No documents to process")


q="Discoveries of attention is all you need?"
r=db.similarity_search(q)


retriever = db.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 3, "score_threshold": 0.9},
)
relevant_docs = retriever.invoke(query)


print("\n--- Relevant Documents ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")
    if doc.metadata:
        print(f"Source: {doc.metadata.get('source', 'Unknown')}\n")