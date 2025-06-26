"""
Functions for agent interaction with the outside environment, utilizing memory manager and path.
"""
from .memory_utils import MemoryManager

def perform_action_with_memory(memory_path: str, action: str):
    memory = MemoryManager(memory_path)
    # Implement logic to perform action using memory
    pass
