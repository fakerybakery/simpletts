from simpletts.models.parler import Parler
import soundfile as sf

# Initialize Parler model
tts = Parler(device="auto")

# Synthesize speech
text = "Hello world! This is a test of the Parler text-to-speech system."
audio, sr = tts.synthesize(text, ref="A female speaker delivers a slightly expressive and animated speech with a moderate speed and pitch. The recording is of very high quality, with the speaker's voice sounding clear and very close up.")

# Save output audio
sf.write("output.wav", audio, sr)
