import openai
from dotenv import find_dotenv, load_dotenv

load_dotenv()

client = openai.OpenAI()
model = "gpt-3.5-turbo-16k"

# # ==  Create our Assistant (Uncomment this to create your assistant) ==
personal_trainer_assis = client.beta.assistants.create(
    name="Personal Trainer",
    instructions="""You are the best personal trainer and nutritionist who knows how to get clients to build lean muscles.\n
     You've trained high-caliber athletes and movie stars. """,
    model=model,
)
asistant_id = personal_trainer_assis.id
print(asistant_id)
# === Thread (uncomment this to create your Thread) ===
thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": "How do I get started working out to lose fat and build muscles?",
        }
    ]
)
thread_id = thread.id
print(thread_id)

# ==== Code made from using documents ===

from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()
model = "gpt-3.5-turbo-16k"

#  Create our Assistant #
personal_trainer_assis = client.chat.completions.create(
    model=model,
    messages=[
        {   
            "role": "system", 
            "content": [
                {
                    "type": "text",
                    "text": """
                        You are the best personal trainer and nutritionist who knows how to get clients to build lean muscles. You've trained high-caliber athletes and movie stars.
                    """
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "How do I get started working out to lose fat and build muscles?"
                }
            ]
        }
    ]
)
print(personal_trainer_assis.choices[0].message.content)

