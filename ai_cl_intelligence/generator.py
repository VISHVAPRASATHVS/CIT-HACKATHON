import openai, os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_transcript(distributor_name, challenges):
    prompt = f"""
Create a mock 10–14 line distributor–vendor call transcript.
Distributor: {distributor_name}
Challenges: {', '.join(challenges)}

Make it realistic, with a mix of positive and negative tone.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    lines = response['choices'][0]['message']['content'].split("\n")
    return [line.strip() for line in lines if line.strip()]
