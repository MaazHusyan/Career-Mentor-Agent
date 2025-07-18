from dotenv import load_dotenv
import openai
import os

load_dotenv()
AI_MODEL = os.getenv("OPEN_ROUTER_AI_MODEL")
openai.api_base = os.getenv("OPEN_ROUTER_BASE_URL")
openai.api_key = os.getenv("OPENROUTER_API_KEY")

def careerAgent(user_interest):
    if not user_interest:
        return "Please provide your interests to get career suggestions."

    prompt = f"""
You are a career guidance expert. Based on the user's interest: "{user_interest}", suggest 2 to 3 career fields they might enjoy.
Only return the names of the fields with a one-line description for each.
"""

    response = openai.Completion.create(
        model=AI_MODEL,
        prompt=prompt,
        max_tokens=500,
        
    )

    return response['choices'][0]['text'].strip()
