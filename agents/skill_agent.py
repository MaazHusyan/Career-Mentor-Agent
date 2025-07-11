from tools.roadmap_tools import getCareerRoadmap

def skillAgent(career_field: str) -> str:
    steps = getCareerRoadmap(career_field)
    if "No roadmap" in steps[0]:
        return f"Sorry, I don't have a roadmap for: {career_field}"

    roadmap_text = f"Here's a skill roadmap for becoming a {career_field}:\n"
    for i, step in enumerate(steps, 1):
        roadmap_text += f"{i}. {step}\n"
    
    return roadmap_text