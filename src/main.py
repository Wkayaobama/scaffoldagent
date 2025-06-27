from swarm.repl import run_demo_loop
from src.orchestrator.triage import create_orchestrator

def main():
    triage_agent = create_orchestrator()
    context_variables = {
        "system_context": """
        System Status: Active
        Allowed Operations: All
        Previous Interactions: None
        """
    }
    run_demo_loop(triage_agent, context_variables=context_variables, debug=False)

if __name__ == "__main__":
    main()
