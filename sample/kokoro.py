from simpletts.models.kokoro import Kokoro
import soundfile as sf

# Initialize Kokoro model
tts = Kokoro(device="auto") 

# Synthesize speech
text = "Hello world! This is a test of the Kokoro text-to-speech system."
audio, sr = tts.synthesize(text, ref="af")

# Save output audio
sf.write("output.wav", audio, sr)
