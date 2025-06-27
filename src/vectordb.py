"""
Vector database utilities: load, inspect, clean, and upload CSV dataset to Pinecone.
"""
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 1. Load CSV dataset
def load_dataset(csv_path: str) -> pd.DataFrame:
    return pd.read_csv(csv_path)

# 2. Print a few rows for inspection
def print_sample_rows(df: pd.DataFrame, n: int = 5):
    print(df.head(n))

# 3. Optional: Clean the file (stub)
def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    # Implement cleaning logic as needed
    return df

# 4. Vectorize and upload to Pinecone
def vectorize_and_upload(df: pd.DataFrame, index_name: str):
    """
    Embed the 'question' field using OpenAI, format for Pinecone, and upsert to the specified index.
    """
    import openai
    from pinecone import Pinecone
    from dotenv import load_dotenv
    import os
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
    openai.api_key = OPENAI_API_KEY
    pc = Pinecone(api_key=PINECONE_API_KEY)
    # Debug: print available indexes
    available_indexes = pc.list_indexes().names()
    print(f"Available Pinecone indexes: {available_indexes}")
    if index_name not in available_indexes:
        raise ValueError(f"Index '{index_name}' does not exist. (Available: {available_indexes})")
    index = pc.Index(index_name)
    # Prepare vectors
    vectors = []
    for _, row in df.iterrows():
        # Get embedding for the question (OpenAI v1.x)
        response = openai.embeddings.create(
            input=row['question'],
            model="text-embedding-ada-002"
        )
        embedding = response.data[0].embedding
        # Prepare metadata
        metadata = {
            "question": row['question'],
            "answer": row['answer'],
            "category": row.get('category', ''),
            "source": row.get('source', '')
        }
        vectors.append((str(row['id']), embedding, metadata))
    # Upsert to Pinecone
    index.upsert(vectors)
    print(f"Upserted {len(vectors)} vectors to index '{index_name}'")

def create_pinecone_index(index_name: str, dimension: int = 1536, metric: str = "cosine"): 
    """
    Programmatically create a Pinecone index for OpenAI text-embedding-ada-002 (1536 dims).
    """
    from pinecone import Pinecone, ServerlessSpec
    import os
    from dotenv import load_dotenv
    load_dotenv()
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
    # Parse region from environment string (e.g., 'us-east-1-aws')
    region = PINECONE_ENVIRONMENT.replace('-aws', '') if PINECONE_ENVIRONMENT else 'us-east-1'
    pc = Pinecone(api_key=PINECONE_API_KEY)
    available_indexes = pc.list_indexes().names()
    if index_name in available_indexes:
        print(f"Index '{index_name}' already exists.")
        return
    pc.create_index(
        name=index_name,
        dimension=dimension,
        metric=metric,
        spec=ServerlessSpec(cloud="aws", region=region)
    )
    print(f"Created Pinecone index '{index_name}' with dimension {dimension} and metric '{metric}' in region '{region}'")

def query_agent(question: str, index_name: str, top_k: int = 1, agent=None):
    """
    Embed the user question, query Pinecone for top_k matches, and print the results.
    If an agent with a behavioral prompt is provided, prepend the prompt to the user query.
    """
    import openai
    from pinecone import Pinecone
    import os
    from dotenv import load_dotenv
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    openai.api_key = OPENAI_API_KEY
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(index_name)
    # Use agent's behavioral prompt if provided
    if agent and hasattr(agent, "format_query"):
        question = agent.format_query(question)
    # Embed the query
    response = openai.embeddings.create(
        input=question,
        model="text-embedding-ada-002"
    )
    query_embedding = response.data[0].embedding
    # Query Pinecone
    results = index.query(vector=query_embedding, top_k=top_k, include_metadata=True)
    for match in results['matches']:
        print(f"Score: {match['score']:.3f}")
        print(f"Q: {match['metadata']['question']}")
        print(f"A: {match['metadata']['answer']}")
        print("---")

def create_mock_qa_csv(csv_path: str):
    """
    Generate mock Q&A data for an electronics supply agent with proper metadata fields for Pinecone.
    """
    data = [
        {"id": "1", "question": "What is the warranty period for the UltraHD TV?", "answer": "The UltraHD TV comes with a 2-year warranty.", "category": "warranty", "source": "UltraHD_TV_manual.pdf"},
        {"id": "2", "question": "Which laptops are available with 16GB RAM?", "answer": "Models X200, Y500, and ZBook all come with 16GB RAM.", "category": "laptops", "source": "laptop_inventory_2025.xlsx"},
        {"id": "3", "question": "Do you offer bulk discounts on HDMI cables?", "answer": "Yes, bulk discounts are available for orders over 50 units.", "category": "cables", "source": "pricing_policy_2025.pdf"},
        {"id": "4", "question": "What is the return policy for smartphones?", "answer": "Smartphones can be returned within 30 days of purchase with a receipt.", "category": "returns", "source": "return_policy_2025.pdf"},
        {"id": "5", "question": "Are there any eco-friendly appliances in stock?", "answer": "Yes, we have a range of eco-friendly refrigerators and washing machines.", "category": "appliances", "source": "eco_products_2025.pdf"}
    ]
    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False)
    print(f"Mock Q&A CSV created at {csv_path}")

if __name__ == "__main__":
    csv_path = "./data/electronicsupply_qa_mock.csv"
    create_mock_qa_csv(csv_path)
    df = load_dataset(csv_path)
    print_sample_rows(df)
    # Create Pinecone index for OpenAI embeddings if not exists
    create_pinecone_index("electronicsupplyv2", dimension=1536, metric="cosine")
    # Upsert to Pinecone index
    vectorize_and_upload(df, "electronicsupplyv2")
    # Test agent retrieval
    print("\n--- Agent Retrieval Test ---")
    query_agent("What is the warranty period for the UltraHD TV?", "electronicsupplyv2")
