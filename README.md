[GitHub](https://github.com/fakerybakery/simpletts) | [Docs](https://fakerybakery.github.io/simpletts/) | [PyPI](https://pypi.org/project/simpletts/)

# SimpleTTS

A lightweight Python library for running TTS models with a unified API.

> [!NOTE]
> This project is under active development and APIs may change. Not recommended for production use yet.

## Features

- 🚀 Simple and intuitive API - get started in minutes
- 🔄 No model lock-in - switch models with just a few lines of code
- 🎯 Focus on ease of use - a single API for all models
- 📦 Minimal dependencies - one package for all models
- 🔌 Extensible architecture - easily add new models
- 💎 Feature-rich - includes longform narration, voice cloning support, and more

## Models

- XTTS
- Kokoro
- F5-TTS
- [& more](https://fakerybakery.github.io/simpletts/models/)

## Installation

Install the latest release from PyPI:

```bash
pip install simpletts
```

## Quick Start

```python
import soundfile as sf
from simpletts.models.xtts import XTTS

tts = XTTS(device="auto")
# Easily swap out for F5-TTS:
# from simpletts.models.f5 import F5TTS
# tts = F5TTS(device="auto")

array, sr = tts.synthesize("Hello, world!", ref="sample.wav")

sf.write("output.wav", array, sr)
```

Please see the [docs](https://fakerybakery.github.io/simpletts/) for more information, such as available models, code examples, and more.

## Support & Feedback

If you encounter any issues or have questions, please open an [issue](https://github.com/fakerybakery/simpletts/issues).

## License

This project is licensed under the **BSD-3-Clause** license, which means it can be used commercially. See the [LICENSE](LICENSE) file for more details.

While SimpleTTS itself is open source and can be used commercially, please note that some supported models have different licensing terms:

- XTTS is licensed under CPML which restricts commercial use
- Kokoro is licensed under Apache-2.0 which allows commercial use
- Other models may have their own licensing requirements

Note that SimpleTTS **does not** use the GPL-licensed `phonemizer` library. Instead, it uses the BSD-licensed `openphonemizer` alternative. While this may slightly reduce pronunciation accuracy, it's license is compatible with the BSD-3-Clause license of SimpleTTS.

For complete licensing information for all included models and dependencies, please see the `licenses` directory.
