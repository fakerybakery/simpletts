from simpletts.models import TTSModel
from simpletts.models.kokoro.kokoro import generate
from simpletts.models.kokoro.models import build_model
import torch
import numpy as np
from pathlib import Path
from munch import Munch
from cached_path import cached_path


class Kokoro(TTSModel):
    VOICE_NAMES = [
        "af",
        "af_bella",
        "af_sarah",
        "am_adam",
        "am_michael",
        "bf_emma",
        "bf_isabella",
        "bm_george",
        "bm_lewis",
        "af_nicole",
        "af_sky",
    ]

    def __init__(self, device="auto", **kwargs):
        super().__init__(device=device, **kwargs)
        if device == "auto":
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device

        self.model = build_model(
            str(cached_path("hf://hexgrad/Kokoro-82M/kokoro-v1_0.pth")), self.device
        )

    def synthesize(self, text: str, ref: str, **kwargs) -> tuple[np.ndarray, int]:
        """
        Synthesize speech from text using Kokoro TTS.

        Args:
            text: Text to synthesize
            **kwargs: Additional arguments passed to generate()

        Returns:
            Tuple of (audio_array, sample_rate)
        """
        if not ref in self.VOICE_NAMES:
            raise ValueError(
                f"Invalid voice name: {ref}. Must be one of {self.VOICE_NAMES}. This model does not support custom voices or voice cloning."
            )
        ref = torch.load(
            str(cached_path(f"hf://hexgrad/Kokoro-82M/voices/{ref}.pt")),
            weights_only=True,
        ).to(self.device)
        audio, _ = generate(self.model, text, ref, lang="a", **kwargs)
        return audio, 24000  # Kokoro uses 24kHz sample rate
