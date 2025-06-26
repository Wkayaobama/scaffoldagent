"""
Agent definition and configuration.
"""

class Agent:
    def __init__(self, name: str, role: str, goal: str, model: str = "gpt-3.5-turbo"):
        self.name = name
        self.role = role
        self.goal = goal
        self.model = model
    # Add configuration and methods as needed
