# Models

## Supported Models

| Model | License | Description | Link |
|-------|---------|-------------|------|
| XTTS | CPML | High-quality multilingual TTS with voice cloning capabilities | [XTTS](https://github.com/coqui-ai/TTS/blob/dev/docs/source/models/xtts.md) |
| Kokoro | Apache-2.0 | Fast and lightweight English TTS with voice cloning | [Kokoro](https://huggingface.co/hexgrad/Kokoro-82M) |
| F5-TTS | CC BY-NC | Superb voice cloning and naturalness, but slower and less stable | [F5-TTS](https://github.com/SWivid/F5-TTS) |
| Parler TTS | Apache-2.0 | Describe a voice with a text prompt | [Parler TTS](https://github.com/huggingface/parler-tts) |

## XTTS

```python
from simpletts.models.xtts import XTTS
import soundfile as sf

# Initialize XTTS model
tts = XTTS(device="auto")

# Synthesize speech
text = "Hello world! This is a test of the XTTS text-to-speech system."
audio, sr = tts.synthesize(text, ref="sample.wav", language="en")

# Save output audio
sf.write("output.wav", audio, sr)
```

## Kokoro

!!! note

    Currently, only English is supported through SimpleTTS. The Kokoro model itself supports multiple languages.

```python
from simpletts.models.kokoro import Kokoro
import soundfile as sf

# Initialize Kokoro model
tts = Kokoro(device="auto")

# Synthesize speech
text = "Hello world! This is a test of the Kokoro text-to-speech system."
audio, sr = tts.synthesize(text, ref="af_heart")

# Save output audio
sf.write("output.wav", audio, sr)
```

## F5-TTS

```python
from simpletts.models.f5 import F5
import soundfile as sf

# Initialize F5 model
tts = F5(device="auto")

# Synthesize speech
text = "Hello world! This is a test of the F5 text-to-speech system."
audio, sr = tts.synthesize(text, ref="sample.wav")

# Save output audio
sf.write("output.wav", audio, sr)
```

## Parler TTS

!!! note

    If you are trying to install Parler TTS, you may run into dependency conflicts or other issues. Parler TTS is not officially supported by the SimpleTTS project, please do not report issues to the SimpleTTS project if you run into issues.

    Parler TTS is not officially available on PyPI, so we cannot add it as a required dependency due to PyPI security requirements. We have published several unofficial packages for Parler TTS and its dependencies to PyPI, however this is not guaranteed to work.

    If you run into issues, please try running `pip uninstall parler-tts` and then `pip install git+https://github.com/huggingface/parler-tts`.

```python
from simpletts.models.parler import Parler
import soundfile as sf

# Initialize Parler model
tts = Parler(device="auto")

# Synthesize speech
text = "Hello world! This is a test of the Parler text-to-speech system."
audio, sr = tts.synthesize(text, ref="A female speaker delivers a slightly expressive and animated speech with a moderate speed and pitch. The recording is of very high quality, with the speaker's voice sounding clear and very close up.")

# Save output audio
sf.write("output.wav", audio, sr)
```
