from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()
model = "gpt-3.5-turbo-16k"

#  Create our Assistant #
personal_trainer_assis = client.chat.completions.create(
    model=model,
    messages=[
        {   "role": "system", 
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "How do I get started working out to lose fat and build muscles?"
        }
    ]
)
print(personal_trainer_assis.choices[0].message)
# asisitant_id = personal_trainer_assis.id
# print(asisitant_id)

# # Thread #
# thread = client.beta.threads.create(
    
# )
# thread_id = thread.id
# print(thread_id)