from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
import os
from openai import OpenAI

# loads environment variables to access token
load_dotenv()
token = os.getenv("GITHUB_TOKEN")

# initialize embedding model and vector DB
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = Chroma(
    collection_name="pdf_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_db",
)

client = OpenAI(base_url="https://models.github.ai/inference", api_key=token)


def query(question):
    # retrieve chunks
    retrieved_docs = vector_store.similarity_search(question, k=3)
    docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)

    # define LLM instructions
    system_instructions = """You are a helpful assistant. Answer the question based only on the provided context."""

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"Guidelines: {system_instructions}",
            },
            {
                "role": "user",
                "content": f"Context: {docs_content}\n\nQuestion: {question}",
            },
        ],
        model="openai/gpt-4o-mini",
        temperature=0.2,
        max_tokens=1000,
        top_p=1,
    )

    return response.choices[0].message.content
