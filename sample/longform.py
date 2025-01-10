from simpletts.models.kokoro import Kokoro
import soundfile as sf

# Initialize Kokoro model
tts = Kokoro(device="auto")

# Synthesize speech
text = """
Text-to-speech technology has come a long way in recent years, with many powerful models now available to developers. However, the fragmented ecosystem of TTS libraries poses significant challenges. Each model typically comes with its own unique API, dependencies, and setup requirements, making it difficult for developers to experiment with different models or switch between them as needed.

This is where a unified TTS library becomes invaluable. By providing a consistent interface across multiple models, it dramatically simplifies the development process. Developers can focus on their applications rather than wrestling with different APIs and dependencies for each model they want to try.

A unified library also promotes better code maintainability and portability. When your application's TTS functionality is abstracted behind a common interface, switching models becomes as simple as changing a single line of code. This flexibility is especially important as the field of TTS continues to evolve rapidly, with new and improved models being released regularly.

Additionally, a unified library can handle common tasks like text preprocessing, audio post-processing, and long-form text synthesis consistently across all models. This reduces duplication of effort and helps ensure consistent behavior regardless of the underlying model being used.

For organizations, having a unified TTS library means reduced training time for developers, simplified maintenance, and the ability to easily benchmark different models against each other. It also makes it easier to swap out models based on specific needs - whether that's quality, speed, licensing requirements, or language support.

In conclusion, as TTS technology becomes increasingly important in modern applications, having a unified library isn't just convenient - it's becoming essential for efficient development and maintenance of TTS-enabled applications.
"""
audio, sr = tts.longform(text, ref="af")

# Save output audio
sf.write("output.wav", audio, sr)
