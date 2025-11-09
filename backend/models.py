from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import *
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
import os
from langchain_community.document_loaders import PyPDFLoader




model = ChatOllama(model = "mistral")
pdf_files = r"C:\Users\Nurserik\Desktop\Onion\test_pdf"
embedding = FastEmbedEmbeddings()


for i in os.listdir(pdf_files):
    if i.endswith(".pdf"):
        pdf_path = os.path.join(pdf_files, i)
        print(f"📄 Processing file: {i}")
        loader = PyPDFLoader(pdf_path)
        document = loader.load()
        text = "\n".join([doc.page_content for doc in document])


        # Semantic Chunking (Testing)
        # prompt = f"""
        # You are a semantic text segmenter.
        # Read the following text and split it into clear chunks where each chunk represents a distinct topic or idea.
        # Return the output as numbered sections (Chunk 1, Chunk 2, ...).
        # Text:
        # {text}"""
        # result = model.invoke(prompt)
        # print(f"📘 Semantic chunks for {i}:\n")
        # print(result)








