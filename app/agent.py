import os
from smolagents import CodeAgent, InferenceClientModel
from .tools.audio_tools import *
from .tools.lyrics_tools import *  # to be created

def create_music_agent():
    model = InferenceClientModel(
        model_id='Qwen/Qwen2.5-Coder-32B-Instruct', 
        token=os.getenv('HF_TOKEN')
    )
    return CodeAgent(
        tools=[analyze_audio, vocal_split, apply_autotune, matchering_suggest, generate_lyrics], # add more
        model=model,
        add_base_tools=True,
        verbosity_level=1
    )
