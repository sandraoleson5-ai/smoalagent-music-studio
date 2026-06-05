from smolagents import tool

@tool
def generate_lyrics(prompt: str, style: str = "hip-hop") -> str:
    """AI Lyrics Generator."""
    return f"🎵 Generated {style} lyrics for: {prompt}\n[Full lyrics here...]"