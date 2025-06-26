"""
Embedding utilities: choose model, create Pinecone index, upload data.
"""
import os
from dotenv import load_dotenv
import openai
import pinecone

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# 1. Choose embedding model
def get_embedding_model(model_name: str = "text-embedding-ada-002"):
    return model_name

# 2. Create Pinecone index (stub)
def create_pinecone_index(index_name: str, dimension: int = 1536):
    # pinecone.init(api_key=PINECONE_API_KEY, environment="us-east1-gcp")
    # pinecone.create_index(index_name, dimension=dimension)
    pass

# 3. Upload data to vector store (stub)
def upload_to_vector_store(index_name: str, vectors):
    # Implement upload logic
    pass


