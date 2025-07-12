import openai
import os
from dotenv import load_dotenv
from agents.career_agent import careerAgent
from agents.skill_agent import skillAgent
from agents.job_agent import getJobListings

load_dotenv()
AI_MODEL = os.getenv("OPEN_ROUTER_AI_MODEL")

def run_pipeline(user_interest):
    # Step 1: Always run CareerAgent
    print("\n👉 Handoff to CareerAgent...\n")
    context = careerAgent(user_interest)
    print(context)

    # Step 2: Ask for SkillAgent
    selected_field = input("\n📌 Choose one career field from above: ").strip()
    print("\n👉 Handoff to SkillAgent...\n")
    roadmap = skillAgent(selected_field)
    print(roadmap)

    # Step 3: Ask for JobAgent
    run_jobs = input("\n❓ Do you want to see real-world job roles? (yes/no): ").strip().lower()
    if run_jobs == "yes":
        print("\n👉 Handoff to JobAgent...\n")
        context = getJobListings(user_interest)
        print(context)
    else:
        print("✅ Skipped JobAgent.")

if __name__ == "__main__":
    interest = input("🎯 Tell me your interests: ")
    run_pipeline(interest)
