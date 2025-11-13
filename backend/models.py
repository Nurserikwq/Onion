from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import *
from langchain_community.chat_models import ChatOllama
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from docling.document_converter import DocumentConverter
from langchain_classic.schema import Document
from chromadb.config import Settings
import chromadb
from chromadb import PersistentClient

model = ChatOllama(model = "mistral")
pdf_files = r"C:\Users\Nurserik\Desktop\Onion\test_pdf"
embedding = FastEmbedEmbeddings()
converter = DocumentConverter()
client = chromadb.PersistentClient(path=r"C:\Users\Nurserik\Desktop\Onion\db")
collection = client.get_or_create_collection("Physics")

for i in os.listdir(pdf_files):
    if i.endswith(".pdf"):
        pdf_path = os.path.join(pdf_files, i)
        print(f"📄 Processing file: {i}")
        result = converter.convert(pdf_path)
        markdown_text = result.document.export_to_markdown()
        document = Document(page_content=markdown_text)

        # # RecursiveCharacterTextSplitter (Working)
        chunker = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=["\n\n", "\n", "."]
        )
        chunks = chunker.split_documents([document])
        print(f"✅ Created {len(chunks)} chunks from {i}")

        texts = [chunk.page_content for chunk in chunks]
        embeddings = embedding.embed_documents(texts)
        print(f"🧠 Generated embeddings for {len(texts)} chunks.\n")

        for idx, chunk in enumerate(chunks):
            print(f"\n--- 📘 Chunk {idx + 1} ---")
            print(chunk.page_content)

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

        collection.add(
            ids=[f"{i}_chunk_{j}" for j in range(len(texts))],
            documents=texts,
            embeddings=embeddings
        )


