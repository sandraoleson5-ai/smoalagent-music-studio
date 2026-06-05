import os
from smolagents import CodeAgent, InferenceClientModel
from .tools.audio_tools import *
from .tools.lyrics_tools import *
from .tools.social_tools import *

def create_music_agent():
    model = InferenceClientModel(
        model_id='Qwen/Qwen2.5-Coder-32B-Instruct', 
        token=os.getenv('HF_TOKEN')
    )
    return CodeAgent(
        tools=[analyze_audio, vocal_split, apply_autotune, matchering_suggest, generate_lyrics, generate_tiktok_clip, hit_song_predictor, daily_content_generator, social_automation],
        model=model,
        add_base_tools=True,
        verbosity_level=1
    )
