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
    prompt: str
    model: Optional[str] = "gpt-3.5-turbo"
    # Add more fields as needed

def create_agent_from_template(template: AgentTemplate, directory: str, prompt: str) -> Agent:
    """
    Create an Agent instance from a template, directory, and prompt.
    The prompt is used to influence the agent's behavior (e.g., "Only answer like a pirate").
    """
    return Agent(
        name=template.name,
        role=template.role,
        goal=template.goal,
        model=template.model or "gpt-3.5-turbo",
        prompt=template.prompt
    )

class TemplateModule:
    """
    Utility for loading and rendering agent template files with variable replacement.
    """
    def __init__(self, template_dir: str):
        self.template_dir = template_dir

    def load_template(self, template_name: str, replacements: dict) -> str:
        """Load a template file and apply replacements."""
        import os
        template_path = os.path.join(self.template_dir, template_name)
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
        for key, value in replacements.items():
            content = content.replace(f"${key}$", value)
        return content

    def render_templates(self, replacements: dict) -> dict:
        """Render all .py templates in the directory with replacements. Returns dict of filename: content."""
        import os
        rendered = {}
        for fname in os.listdir(self.template_dir):
            if fname.endswith('.py'):
                rendered[fname] = self.load_template(fname, replacements)
        return rendered

if __name__ == "__main__":
    # Example usage
    template = AgentTemplate(
        name="ElectronicsSupply001",
        role="electronicsupply",
        goal="Answer stock and product availability questions for the electronics store.",
        prompt="Only answer like a pirate!",
        model="gpt-3.5-turbo"
    )
    directory = "./data/agents"
    # The prompt is a behavioral modifier, not a static question
    agent_instance = create_agent_from_template(template, directory, template.prompt)
    print(f"Created agent: {agent_instance.name}, role: {agent_instance.role}, goal: {agent_instance.goal}, prompt: {getattr(agent_instance, 'prompt', 'N/A')}, model: {agent_instance.model}")
