# Kokoro

from simpletts.models.kokoro import Kokoro
model = Kokoro(device="auto")

def simpletts(text: str, **kwargs):
    audio, sr = model.longform(text, ref="af_heart", **kwargs)
    
    class AudioData:
        def __init__(self, audio, sr):
            self.audio = audio
            self.sr = sr
            
        def save(self, path):
            import soundfile as sf
            sf.write(path, self.audio, self.sr)
            
    return AudioData(audio, sr)