import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_entities(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{text}\n\nEntities:",
        temperature=0.3,
        max_tokens=60
    )
    return response.choices[0].text.strip()

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100
    )
    return response.choices[0].text.strip()