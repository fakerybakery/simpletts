from simpletts.models.f5 import F5
import soundfile as sf

# Initialize F5 model
tts = F5(device="auto")

# Synthesize speech
text = "Hello world! This is a test of the F5 text-to-speech system."
audio, sr = tts.synthesize(text, ref="sample.wav")

# Save output audio
sf.write("output.wav", audio, sr)
