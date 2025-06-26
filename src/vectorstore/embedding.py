"""
Embedding utilities: choose model, create Pinecone index, upload data.
"""
import os
from dotenv import load_dotenv
import openai
from pinecone import Pinecone

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")

# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

# 1. Choose embedding model
def get_embedding_model(model_name: str = "text-embedding-ada-002"):
    return model_name

# 2. Connect to an existing Pinecone index
def get_pinecone_index(index_name: str):
    if index_name not in pc.list_indexes().names():
        raise ValueError(f"Index '{index_name}' does not exist. Please create it in the Pinecone UI.")
    return pc.Index(index_name)

# 3. Upload data to vector store (upsert vectors)
def upload_to_vector_store(index_name: str, vectors):
    """
    vectors: list of (id, vector, metadata) tuples or dicts as required by Pinecone
    """
    index = get_pinecone_index(index_name)
    index.upsert(vectors)
    print(f"Upserted {len(vectors)} vectors to index '{index_name}'")
