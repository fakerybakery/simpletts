# SimpleTTS

Run and use TTS models with just a few lines of code. Quickly switch between models.

> [!NOTE]
> This is a work in progress. It's not ready for production use.

## Usage

```python
from simpletts.models.xtts import XTTS
import soundfile as sf

tts = XTTS(device="auto")
# Note: XTTS is licensed under the CPML license which restricts commercial use.

array, sr = tts.synthesize("Hello, world!", ref="sample.wav")

sf.write("output.wav", array, sr)
```

## Models

| Model | License |
|-------|---------|
| XTTS | CPML |
| Kokoro | Apache-2.0 |

## Progress

**Models**

- [x] XTTS
- [ ] StyleTTS 2
- [x] Kokoro (only supports English for now)
- [ ] F5-TTS

**Features**

- [x] Python API
- [ ] CLI
- [ ] API + Web UI

## License

This project is licensed under the BSD-3-Clause license. See the [LICENSE](LICENSE) file for more details.

While you may use this project for commercial purposes, some models supported by this project may require additional licensing or restrict commercial use.

Note that this project contains or references code from other projects, which are subject to their own licenses. See the `licenses` directory for more details.
