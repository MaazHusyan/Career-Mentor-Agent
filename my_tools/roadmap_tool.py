from agents import Agent, function_tool, Runner


from _instructions import get_tool_instructions
from gemini_model import geminiModel

@function_tool
async def get_career_roadmap(career: str):
   """Generates a personalized career roadmap based on the provided career name."""
   
   agent = Agent(
        name = "Career Roadmap Builder Agent",
        instructions = get_tool_instructions,
        model = geminiModel
   )
   
   print("Career Roadmap Builder Agent initialized. (tool)")
   print(f"Generating roadmap for career: {career}")
   
   response = await Runner.run(
       agent = agent,
       input = career
   )
   
   result = response.final_output.strip()
   print(f"Generated roadmap: {result}")
   
   return result
