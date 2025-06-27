"""
Agent definition and configuration.
"""

class Agent:
    def __init__(self, name: str, role: str, goal: str, model: str = "gpt-3.5-turbo", prompt: str = ""):
        self.name = name
        self.role = role
        self.goal = goal
        self.model = model
        self.prompt = prompt  # Behavioral modifier for LLM responses

    def info(self):
        return f"Agent(name={self.name}, role={self.role}, goal={self.goal}, prompt={self.prompt}, model={self.model})"

    def format_query(self, user_query: str) -> str:
        """
        Prepend the behavioral prompt to the user query for LLM calls.
        """
        if self.prompt:
            return f"{self.prompt}\n{user_query}"
        return user_query
