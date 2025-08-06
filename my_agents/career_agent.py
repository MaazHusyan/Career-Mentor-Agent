from agents import Agent

from _instructions import get_career_instructions
from gemini_model import geminiModel


def career_agent()-> Agent:
    """
    An agent that suggests careers based on user input.
    """
    
    agent = Agent(
        name = "Career  Agent",
        instructions=get_career_instructions,
        model=geminiModel
    )
    
    print("Career Agent initialized.")
    return agent