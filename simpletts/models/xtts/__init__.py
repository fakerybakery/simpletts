from simpletts.models import TTSModel, requires_package, requires_extra

try:
    from TTS.api import TTS
except ImportError:
    requires_extra("xtts")

from typing import Tuple, Optional
import numpy as np
import torch
import os


class XTTS(TTSModel):
    def __init__(
        self, device: Optional[str] = "auto", agree_cpml: bool = False, **kwargs
    ):
        super().__init__()
        if device == "auto":
            device = "cuda" if torch.cuda.is_available() else "cpu"
        if agree_cpml:  # Otherwise will ask for agreement to CPML license
            os.environ["COQUI_TOS_AGREED"] = "1"
        self.device = device
        self.model = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

    def synthesize(
        self, text: str, ref: str, language: str = "en", **kwargs
    ) -> Tuple[np.ndarray, int]:
        """
        Synthesize speech from text using XTTS.

        Args:
            text: Text to synthesize
            ref: Reference audio as tuple of (samples, sample_rate)
            **kwargs: Additional arguments passed to TTS.tts()

        Returns:
            Tuple containing:
                - Audio array as numpy array
                - Sample rate as integer
        """
        wav = self.model.tts(text=text, speaker_wav=ref, language=language, **kwargs)
        return wav, self.model.synthesizer.output_sample_rate
