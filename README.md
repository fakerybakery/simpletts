# SimpleTTS

A lightweight Python library for text-to-speech synthesis that makes it easy to use and switch between different TTS models.

> [!NOTE]
> This project is under active development and APIs may change. Not recommended for production use yet.

## Features

- 🚀 Simple and intuitive API - get started in minutes
- 🔄 No model lock-in - switch models with just a few lines of code
- 🎯 Focus on ease of use - a single API for all models
- 📦 Minimal dependencies - one package for all models
- 🔌 Extensible architecture - easily add new models

## Installation

Install the latest release from PyPI:

```bash
pip install simpletts
```

Or get the latest version from source:

```bash
pip install git+https://github.com/fakerybakery/simpletts
```

## Quick Start

```python
from simpletts.models.xtts import XTTS
import soundfile as sf

tts = XTTS(device="auto")
# Note: XTTS is licensed under the CPML license which restricts commercial use.

array, sr = tts.synthesize("Hello, world!", ref="sample.wav")

sf.write("output.wav", array, sr)
```

## Supported Models

| Model | License | Description |
|-------|---------|-------------|
| XTTS | CPML | High-quality multilingual TTS with voice cloning capabilities |
| Kokoro | Apache-2.0 | Fast and lightweight English TTS with voice cloning |
| F5-TTS | CC BY-NC | Superb voice cloning and naturalness, but slower and less stable |

## Roadmap

**Models**

- [x] XTTS - Production-ready multilingual TTS
- [x] Kokoro - StyleTTS 2-based English TTS without voice cloning
- [x] F5-TTS - Superb voice cloning and naturalness, but slower and less stable
- [ ] StyleTTS 2 - Fast and efficient zero-shot voice cloning

**Features**

- [x] Simple Python API for easy integration
- [ ] Command-line interface for quick testing and batch processing
- [ ] REST API and web interface for remote access
- [ ] Model benchmarking tools
- [ ] Batch processing support
- [ ] Audio post-processing options
- [ ] Allow easier extensibility with a plugin system

## Support & Feedback

If you encounter any issues or have questions, please open an [issue](https://github.com/fakerybakery/simpletts/issues).

## License

This project is licensed under the **BSD-3-Clause** license. See the [LICENSE](LICENSE) file for more details.

While SimpleTTS itself is open source and can be used commercially, please note that some supported models have different licensing terms:

- XTTS is licensed under CPML which restricts commercial use
- Kokoro is licensed under Apache-2.0 which allows commercial use
- Other models may have their own licensing requirements

For complete licensing information for all included models and dependencies, please see the `licenses` directory.
