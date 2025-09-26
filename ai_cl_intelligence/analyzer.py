import openai, os, json
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_transcript(transcript):
    with open("vendor_resources.json") as f:
        vendor_db = json.load(f)

    prompt = f"""
You are an AI assistant analyzing a distributor–vendor call transcript.

Transcript:
{transcript}

Tasks:
1. List problems raised by distributor.
2. Match vendor solutions from this database: {vendor_db}
3. Generate 3 action items with task, owner, and deadline.
4. Tag each line with sentiment: Positive, Neutral, or Negative.

Respond in JSON with keys: problems, solutions, action_items, sentiment_tags.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return json.loads(response['choices'][0]['message']['content'])
