from agents import Agent

from _instructions import get_job_instructions
from gemini_model import geminiModel


def job_agent() -> Agent:
    """
    "You are a JobAgent. Your role is to provide job options and career paths for a given goal.
    If someone says "hand off to job agent", take over. Be specific, ask clarifying questions if needed
    """
    
    agent = Agent(
        name = "Job Agent",
        instructions = get_job_instructions(),
        model = geminiModel
    )
    
    print("Job Agent initialized.")
    return agent