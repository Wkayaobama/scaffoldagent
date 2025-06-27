import sys
import os
from pathlib import Path
from swarm import Agent
from typing import Dict, Optional
import importlib.util
import re
import pandas as pd
from src.lookup import lookup_by_key
from src.functions import reset_memory, escalate_to_human

# Add the parent directory to the Python path
sys.path.append(str(Path(__file__).parent.parent))

class AgentOrchestrator:
    def __init__(self):
        self.triage_agent = None
        self.db = self._load_db()

    def _load_db(self):
        # Load the real CSV Q&A database
        csv_path = Path(__file__).parent.parent.parent / "data" / "electronicsupply_qa_mock.csv"
        return pd.read_csv(csv_path)

    def answer_query(self, user_input: str):
        # Search for a relevant question in the CSV
        matches = self.db[self.db['question'].str.contains(user_input, case=False, na=False)]
        if not matches.empty:
            # Return the first matching answer
            return matches.iloc[0]['answer']
        # Fallback: try to match keywords in the answer column
        matches = self.db[self.db['answer'].str.contains(user_input, case=False, na=False)]
        if not matches.empty:
            return matches.iloc[0]['answer']
        return "Sorry, I couldn't find an answer to your question in the database."

    def create_triage_agent(self):
        def handle_user(user_input: str = ""):
            return self.answer_query(user_input)
        return Agent(
            name="Centralized Lookup Agent",
            instructions="Answer user questions using the electronicsupply_qa_mock.csv database. Use handle_user(user_input) to respond.",
            functions=[handle_user, reset_memory, escalate_to_human]
        )

def create_orchestrator():
    orchestrator = AgentOrchestrator()
    return orchestrator.create_triage_agent()
