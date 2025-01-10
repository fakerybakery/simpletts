# Simple API

The Simple API provides an easy way to get started with SimpleTTS without worrying about model selection or configuration. It uses the Kokoro model by default.

## Usage

Import the `tts` function:

```python
from simpletts import tts
```

Generate and save audio:

```python
tts("Hello world!").save("output.wav")
```

That's all you need! The Simple API handles all the model initialization and configuration behind the scenes.

## Example

Here's a complete example showing natural text-to-speech generation:

```python
from simpletts import tts

tts("Enter your text. Supports longform synthesis.").save("output.wav")
```

The Simple API is great for basic use cases where you just want to convert text to speech without any special configuration. For more advanced usage like voice cloning or using different models, check out the [Models](models.md) documentation.