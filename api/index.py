from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from app.agent import create_music_agent

load_dotenv()

app = FastAPI(title="Smoalagent Music AI Studio")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Smoalagent Music AI Studio Ready 🎵", "status": "production"}

@app.post("/run")
async def run_agent(query: str = Form(...)):
    agent = create_music_agent()
    result = agent.run(query)
    return {"result": result}

# Audio upload endpoint example
@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...), task: str = Form(...)):
    contents = await file.read()
    temp_path = f"/tmp/{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(contents)
    # Call agent or tool with temp_path
    agent = create_music_agent()
    result = agent.run(f"Perform {task} on audio: {temp_path}")
    return {"result": result, "file": file.filename}
