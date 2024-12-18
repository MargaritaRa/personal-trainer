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