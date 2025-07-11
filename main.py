import openai
import os
from dotenv import load_dotenv
from agents.career_agent import careerAgent
from agents.skill_agent import skillAgent
from agents.job_agent import getJobListings

load_dotenv()
openai.api_key = os.getenv("OPEN_ROUTER_API_KEY")
openai.api_base = os.getenv("OPEN_ROUTER_BASE_URL", "https://openrouter.ai/api/v1")
AI_MODEL = os.getenv("OPEN_ROUTER_AI_MODEL")


if __name__ == "__main__":
    interest = input("Tell me your interests: ")
    suggestions = careerAgent(interest)
    print("\nSuggested Careers:\n")
    print(suggestions)

    selected_career = input("\nChoose one career to see a skill roadmap: ")
    roadmap = skillAgent(selected_career)
    print("\nSkill Roadmap:\n")
    print(roadmap)

    show_jobs = input("\nDo you want to see real-world job titles for this career? (yes/no): ").strip().lower()
    if show_jobs == ["yes", "y", "ye", "yeah", "yep", "sure", "ok", "hmm"]:
        job_info = getJobListings(selected_career)
        print("\nJob Roles:\n")
        print(job_info)
