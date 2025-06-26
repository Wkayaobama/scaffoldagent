# AI Chatbot Project

This project is a production-ready Python package for an AI chatbot using OpenAI and Pinecone, with support for Excel/CSV data sources.

## Setup

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Configure your environment variables in a `.env` file (see below).

## Project Structure
- `src/` - Main source code
- `data/` - Data files (CSV, Excel, etc.)
- `notebooks/` - Jupyter notebooks
- `tests/` - Unit tests

## Environment Variables
Create a `.env` file in the root directory with the following:
```
OPENAI_API_KEY=your_openai_key
PINECONE_API_KEY=your_pinecone_key
PINECONE_ENV=your_pinecone_env
```

# Electronics Supply Agent with Pinecone & OpenAI

This project demonstrates a Q&A agent for an electronics supply store, using OpenAI embeddings and Pinecone for vector search. It includes a Streamlit chat UI for interactive testing.

## Features
- Bulk upsert of Q&A data to Pinecone vector database
- OpenAI embedding integration (text-embedding-ada-002)
- Duplicate ID protection on upsert
- Conversational chat UI (Streamlit)
- Modular agent creation with Pydantic templates

## Setup Instructions

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd scaffoldagent
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the project root (or use Streamlit Cloud secrets) with:
```
OPENAI_API_KEY=your-openai-key
PINECONE_API_KEY=your-pinecone-key
PINECONE_ENVIRONMENT=your-pinecone-environment  # e.g. us-east-1-aws
```

### 4. Prepare Data
- The script `src/vectorstore/vectordb.py` contains a function to generate a mock Q&A CSV for electronics supply (`create_mock_qa_csv`).
- You can customize this or use your own data in the same format.

### 5. Pinecone Index Setup
- The script will programmatically create a Pinecone index (default: `electronicsupplyv2`, dimension: 1536 for OpenAI embeddings).
- If the index already exists, it will not be recreated.
- Data is upserted with duplicate ID protection (existing IDs are skipped).

### 6. Upsert Data to Pinecone
Run:
```sh
python src/vectorstore/vectordb.py
```
This will:
- Generate the mock Q&A CSV (or use your own)
- Create the Pinecone index if needed
- Upsert new records to Pinecone
- Test retrieval with a sample query

### 7. Run the Chat UI Locally
```sh
streamlit run src/chat_ui.py
```
- Interact with your agent in a browser at http://localhost:8501
- The UI uses the Pinecone index for contextual answers

### 8. Deploy to Streamlit Cloud
1. Push your code to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and create a new app.
3. Set the entry point to `src/chat_ui.py`.
4. Add your API keys and environment as secrets in the Streamlit Cloud UI.
5. Deploy and share your app!

## Customization
- To change the Q&A context, update the mock data in `create_mock_qa_csv` in `vectordb.py`.
- To use a different Pinecone index, update the index name in both `vectordb.py` and `chat_ui.py`.
- For more advanced agent logic or to create a new agent template, see `src/loader.py` and `src/agent.py`. The loader module provides the entry point for agent instantiation and template selection, allowing you to define new agent behaviors or swap out the Q&A context easily. Agent templates are defined using Pydantic models in `agent.py` for modularity and reusability.
- The embedding and upsert workflow is handled in `src/vectorstore/embedding.py`, which is responsible for generating OpenAI embeddings and preparing data for upsert to Pinecone. All Pinecone upserts should use the logic in this module to ensure consistency and correct dimension handling.

## Notes
- Ensure your Pinecone index dimension matches the embedding model (1536 for `text-embedding-ada-002`).
- Never commit your real API keys to version control.

---

For questions or support, open an issue or contact the maintainer.
