import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = os.getenv("OPEN_ROUTER_BASE_URL", "https://openrouter.ai/api/v1")
AI_MODEL = os.getenv("OPEN_ROUTER_AI_MODEL")

def getCareerRoadmap(career: str) -> list[str]:
    prompt = f"""
You are a career roadmap assistant. A student wants to become a '{career}'.
List 5 to 7 learning steps they should follow to master this career path.
Return only the list of steps, no extra explanation.
"""

    response = openai.Completion.create(
        model=AI_MODEL,
        prompt=prompt,
        max_tokens=400,
        temperature=0.7
    )

    text = response['choices'][0]['text'].strip()
    steps = text.split("\n")
    return [step.strip("-•1234567890. ") for step in steps if step.strip()]
