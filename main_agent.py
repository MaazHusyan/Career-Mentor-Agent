import asyncio

from agents import Agent, Runner

from _instructions import get_main_agent_instruction
from my_agents import career_agent, job_agent, skill_agent
from gemini_model import geminiModel
from my_tools.roadmap_tool import get_career_roadmap



def main_agent():
    """
    You're a main orchestrator agent that manages the workflow of other agents.
    It can be used to coordinate tasks and ensure that the overall
    process runs smoothly. 
    """
    
    agent = Agent(
        name = "Main Orchestrator Agent",
        instructions = get_main_agent_instruction,
        handoffs= [career_agent, job_agent, skill_agent],
        tools= [get_career_roadmap],
        model = geminiModel
    )
    print("Main Orchestrator Agent initialized.")
    return agent

async def run_main_agent():
    agent = main_agent()
    
    print("WELLCOME TO THE CAREER MENTOR AGENT!")
    
    while True:
        query = input("😃: ").strip()
        
        if query.lower() in ["exit", "quit", "stop"]:
            print("Exiting the Career Mentor Agent. Goodbye!")
            break
        
        result = await Runner.run(
            agent,
            query,
            max_turns= 4
        )
        
        print(f"🤖: {result.final_output}\n")
        
if __name__ == "__main__":
    asyncio.run(run_main_agent())