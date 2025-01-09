from simpletts.models.xtts import XTTS
import soundfile as sf

# Initialize XTTS model
tts = XTTS(device="auto") 

# Synthesize speech
text = "Hello world! This is a test of the XTTS text-to-speech system."
audio, sr = tts.synthesize(text, ref="sample.wav", language="en")

# Save output audio
sf.write("output.wav", audio, sr)
