from fastapi import FastAPI
from models import SeedBrief, TranscriptRequest, TranscriptResponse, InsightsResponse
from generator import generate_transcript
from analyzer import analyze_transcript
from customer_data import router as customer_router

app = FastAPI()
app.include_router(customer_router)

@app.post("/generate_transcript", response_model=TranscriptResponse)
async def generate(seed: SeedBrief):
    lines = generate_transcript(seed.distributor_name, seed.challenges)
    return {"transcript": lines}

@app.post("/analyze_transcript", response_model=InsightsResponse)
async def analyze(request: TranscriptRequest):
    return analyze_transcript("\n".join(request.transcript))
