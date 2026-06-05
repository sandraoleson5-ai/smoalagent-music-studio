import os
from smolagents import CodeAgent, InferenceClientModel
from .tools.audio_tools import *
from .tools.lyrics_tools import *

def create_music_agent():
    hf_token = os.getenv("HF_TOKEN")
    model = InferenceClientModel("Qwen/Qwen2.5-Coder-32B-Instruct", token=hf_token)
    return CodeAgent(
        tools=[analyze_audio, vocal_split, generate_lyrics, apply_autotune, generate_beat, hit_song_predictor],
        model=model,
        add_base_tools=True,
        verbosity_level=2
    )