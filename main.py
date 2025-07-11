import openai
import os
from dotenv import load_dotenv
from agents.career_agent import careerAgent

load_dotenv()
openai.api_key= os.getenv("OPEN_ROUTER_API_KEY")
openai.api_base = os.getenv("OPEN_ROUTER_BASE_URL", "https://openrouter.ai/api/v1")
AI_MODEL = os.getenv("OPEN_ROUTER_AI_MODEL")


if __name__ == "__main__":
    user_input = input("Tell me your interests: ")
    suggestions = careerAgent(user_input)
    print("\nSuggested Career Fields:\n")
    print(suggestions)
def main():
    pass