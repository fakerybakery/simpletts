from simpletts.models import TTSModel, requires_package, requires_extra
from cached_path import cached_path

try:
    from f5_tts.api import F5TTS
except ImportError:
    requires_extra("f5")

from typing import Tuple, Optional
import numpy as np
import torch


class F5(TTSModel):
    def __init__(self, device: Optional[str] = "auto", **kwargs):
        super().__init__()
        if device == "auto":
            device = "cuda" if torch.cuda.is_available() else "cpu"

        self.f5tts = F5TTS(device=device)

    def synthesize(self, text: str, ref: str, **kwargs) -> Tuple[np.ndarray, int]:
        """
        Synthesize speech from text using F5-TTS.

        Args:
            text: Text to synthesize
            ref: Path to reference audio file
            **kwargs: Additional arguments passed to infer()

        Returns:
            Tuple containing:
                - Audio array as numpy array
                - Sample rate as integer
        """
        # Get reference text via transcription
        ref_text = self.f5tts.transcribe(ref)

        # Run inference
        wav, sr, _ = self.f5tts.infer(
            ref_file=ref, ref_text=ref_text, gen_text=text, **kwargs
        )

        return wav, sr
