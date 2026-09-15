import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_ai_check_message(message):
    if not message:
        return "No message provided."

    # text = "\n".join(
    #     f"- {a['title']} | {a['subject']} | due {a['due_date']} | status: {a['status']} | {a['days_left']} days left"
    #     for a in assignments
    # )
    text =message


    prompt = f"""
You are a smart message checker assistant.

Your goal is to Check if the message contains sensitive information.

PRIORITY RULES (VERY IMPORTANT):
1. check if the message contains details about an attack
2. something sensitive that links to the user(Curse words)
3. make sure it's not jokingly cursing
4. don't count curse words on himself or non realistic things.

RULES:
- If the message contains bad meaning-write: contains curse words 
- If the message is slightly contains bad words-write: warning
- Be practical and realistic

message:
{text}

OUTPUT FORMAT:

The message contains:
[curse_words,...]
message meaning:
joke/attack/curse/heavy_joke

End with:
- short tip for what to do,to block user or to warn
"""

    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "openai/gpt-oss-120b",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3
            }
        )

        data = response.json()
        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"AI Error: {str(e)}"