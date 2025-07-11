import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = os.getenv("OPEN_ROUTER_BASE_URL", "https://openrouter.ai/api/v1")
AI_MODEL = os.getenv("OPEN_ROUTER_AI_MODEL")


def getJobListings(career: str) -> str:
    prompt = f"""
Suggest 3 realistic job titles and companies for a '{career}'.
Include role name, company, and location.
Format each in a new line like this:
- [Job Title] at [Company] ([Location])
"""

    response = openai.Completion.create(
        model=AI_MODEL,
        prompt=prompt,
        max_tokens=300,
        temperature=0.7
    )

    return response['choices'][0]['text'].strip()
