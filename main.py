import openai
from dotenv import find_dotenv, load_dotenv

# from openai import OpenAI
# client = OpenAI()
load_dotenv()

# openai.api_key = os.enviton.ger("OPENAI_API_KEY")

client = openai.OpenAI()
model = "gpt-3.5-turbo-16k"

#  Create our Assistant
personal_trainer_assis = client.beta.assistants.create(
    name="Personal Trainer",
    instructions= """You are the best personal trainer and nutritionalist who knows how to get clients to build lean muscles. \n You've trained high-caliber athletes and movie starts.""",
    model=model
)
# print(personal_trainer_assis.id)