def tts(text: str, **kwargs):
    from simpletts.simple import simpletts
    return simpletts(text, **kwargs)