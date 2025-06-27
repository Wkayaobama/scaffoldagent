"""
Agent template for demonstration.
"""
class Agent:
    def __init__(self, name: str, role: str, goal: str, prompt: str, model: str = "gpt-3.5-turbo"):
        self.name = name  # $NAME$
        self.role = role  # $ROLE$
        self.goal = goal  # $GOAL$
        self.prompt = prompt  # $PROMPT$
        self.model = model  # $MODEL$

    def info(self):
        return f"Agent(name={self.name}, role={self.role}, goal={self.goal}, prompt={self.prompt}, model={self.model})"
