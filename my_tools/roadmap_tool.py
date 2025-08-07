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
   
   try:
    response = await Runner.run(
        starting_agent=agent,
        input=career
    )
    result = response.final_output.strip()
   except Exception as e:
    result = f"Error generating roadmap: {str(e)}"

    return result
