"""
Loader for creating agents with a Pydantic model, directory path, and prompt.
"""
from pydantic import BaseModel
from typing import Optional
from agent import Agent

class AgentTemplate(BaseModel):
    name: str
    role: str
    goal: str
    model: Optional[str] = "gpt-3.5-turbo"
    # Add more fields as needed

def create_agent_from_template(template: AgentTemplate, directory: str, prompt: str) -> Agent:
    """
    Create an Agent instance from a template, directory, and prompt.
    """
    # You can use directory and prompt for further customization if needed
    return Agent(
        name=template.name,
        role=template.role,
        goal=template.goal,
        model=template.model or "gpt-3.5-turbo"
    )

if __name__ == "__main__":
    # Example usage
    template = AgentTemplate(
        name="ElectronicsSupply001",
        role="electronicsupply",
        goal="Answer stock and product availability questions for the electronics store.",
        model="gpt-3.5-turbo"
    )
    directory = "./data/agents"
    prompt = "What is the warranty period for the UltraHD TV?"
    agent_instance = create_agent_from_template(template, directory, prompt)
    print(f"Created agent: {agent_instance.name}, role: {agent_instance.role}, goal: {agent_instance.goal}, model: {agent_instance.model}")
