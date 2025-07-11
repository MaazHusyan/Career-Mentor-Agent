from dotenv import load_dotenv
import openai
import os

load_dotenv()
AI_MODEL = os.getenv("OPEN_ROUTER_AI_MODEL")


def careerAgent(user_interest):
    """
    This function takes a user's interest and returns career suggestions based on that interest.
    
    Args:
    user_interest (str): The user's interest to base career suggestions on.
    
    Returns:
    str: A string containing career suggestions.
    """
    if not user_interest:
        return "Please provide your interests to get career suggestions."
    
    else:
        system_prompt = """
            You are a career guidance expert. Based on the user's interests, suggest 2 to 3 career fields they might enjoy.
            Only return the names of the fields with a short description for each.
            """
            
        response = openai.ChatCompletion.create(
            model = AI_MODEL,
            message=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"My interests are: {user_interest}"}
            ]
        )
    return response['choices'][0]['message']['content']