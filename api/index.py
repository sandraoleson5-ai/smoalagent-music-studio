from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from app.agent import create_music_agent

load_dotenv()

app = FastAPI(title="Smoalagent Music Studio")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "🎵 Smoalagent Music Studio Live! AI Cover Studio, Autotune, Lyrics & More Ready."}

@app.post("/run")
async def run_agent(query: str):
    try:
        agent = create_music_agent()
        result = agent.run(query)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# TODO: Add /upload-audio endpoint for file processing