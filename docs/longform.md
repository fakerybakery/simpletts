# Longform Narration

SimpleTTS supports longform narration as an **experimental feature**. Longform narration is powered by [`txtsplit`](https://github.com/fakerybakery/txtsplit). This means it may not always work as expected. Quality may vary.

## Example

Here is an example of how to use the `longform` method to with Kokoro:

```python
from simpletts.models.kokoro import Kokoro
import soundfile as sf

# Initialize Kokoro model
tts = Kokoro(device="auto")

# Synthesize speech
text = """
Enter your longform text here...
"""
audio, sr = tts.longform(text, ref="af_heart")

# Save output audio
sf.write("output.wav", audio, sr)
```