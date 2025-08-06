from agents import Agent

from _instructions import get_skill_instructions
from gemini_model import geminiModel


def skill_agent() -> Agent:
    """
    An agent that provides skill recommendations based on user input.
    """
    
    agent = Agent(
        name = "Skill Agent",
        instructions = get_skill_instructions,
        model = geminiModel
    )
    
    print("Skill Agent initialized.")
    return agent