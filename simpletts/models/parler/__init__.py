from simpletts.models import TTSModel, requires_package, requires_extra
from typing import Tuple, Optional
import numpy as np
import torch

try:
    from parler_tts import ParlerTTSForConditionalGeneration
    from transformers import AutoTokenizer
except ImportError:
    requires_extra("parler")


class Parler(TTSModel):
    def __init__(self, device: Optional[str] = "auto", **kwargs):
        super().__init__()
        if device == "auto":
            device = "cuda" if torch.cuda.is_available() else "cpu"

        self.device = device
        self.model = ParlerTTSForConditionalGeneration.from_pretrained(
            "parler-tts/parler-tts-mini-v1"
        ).to(device)
        self.tokenizer = AutoTokenizer.from_pretrained("parler-tts/parler-tts-mini-v1")

    def synthesize(self, text: str, ref: str, **kwargs) -> Tuple[np.ndarray, int]:
        """
        Synthesize speech from text using Parler TTS.

        Args:
            text: Text to synthesize
            ref: Voice description text
            **kwargs: Additional arguments passed to generate()

        Returns:
            Tuple containing:
                - Audio array as numpy array
                - Sample rate as integer
        """
        input_ids = self.tokenizer(ref, return_tensors="pt").input_ids.to(self.device)
        prompt_input_ids = self.tokenizer(text, return_tensors="pt").input_ids.to(
            self.device
        )

        generation = self.model.generate(
            input_ids=input_ids, prompt_input_ids=prompt_input_ids, **kwargs
        )
        audio = generation.cpu().numpy().squeeze()

        return audio, self.model.config.sampling_rate
