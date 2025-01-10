# SimpleTTS

A lightweight Python library for running TTS models with a unified API.

!!! warning

    This project is under active development and APIs may change. Not recommended for production use yet.

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

## Quick Start (Simple API)

The [Simple API](simple.md) provides the easiest way to get started with SimpleTTS. With just a few lines of code, you can generate natural-sounding speech. The Simple API **should not be used in environments that require customization or voice cloning** - it's designed for quick and easy use cases.

## Python API

```python
from simpletts.models.xtts import XTTS
import soundfile as sf

tts = XTTS(device="auto")
# Note: XTTS is licensed under the CPML license which restricts commercial use.

array, sr = tts.synthesize("Hello, world!", ref="sample.wav")

sf.write("output.wav", array, sr)
```

## Support & Feedback

If you encounter any issues or have questions, please open an [issue](https://github.com/fakerybakery/simpletts/issues).

## License

This project is licensed under the **BSD-3-Clause** license. See the [LICENSE](LICENSE) file for more details.

While SimpleTTS itself is open source and can be used commercially, please note that some supported models have different licensing terms:

- XTTS is licensed under CPML which restricts commercial use
- Kokoro is licensed under Apache-2.0 which allows commercial use
- Other models may have their own licensing requirements

Note that SimpleTTS **does not** use the GPL-licensed `phonemizer` library. Instead, it uses the BSD-licensed `openphonemizer` alternative. While this may slightly reduce pronunciation accuracy, it's license is compatible with the BSD-3-Clause license of SimpleTTS.

For complete licensing information for all included models and dependencies, please see the `licenses` directory.
