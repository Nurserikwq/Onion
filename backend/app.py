from langchain_ollama import ChatOllama
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings

# Connect to your existing DB
from chromadb import PersistentClient
client = PersistentClient(path=r"C:\Users\Nurserik\Desktop\Onion\db")
collection = client.get_or_create_collection("Physics")

# Ask a question
query = "What is Newton's second law of motion?"

# Embed the query
embedding = FastEmbedEmbeddings()
query_embedding = embedding.embed_query(query)

# Retrieve the most relevant chunks
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3  # top 3 relevant chunks
)

# Show the retrieved text
for i, doc in enumerate(results["documents"][0]):
    print(f"\n🔍 Top {i+1} Result:")
    print(doc)

# Optional: send context to Mistral for QA
model = ChatOllama(model="mistral")
context = "\n\n".join(results["documents"][0])

prompt = f"""
You are a physics assistant. Using the context below, answer the question clearly.

Context:
{context}

Question: {query}
"""

answer = model.invoke(prompt)
print("\n🤖 Answer:\n", answer)
