from simpletts.models import TTSModel
import torch
import numpy as np
from cached_path import cached_path
from kokoro import KPipeline
from tqdm import tqdm

class Kokoro(TTSModel):
    def __init__(self, device="auto", **kwargs):
        super().__init__(device=device, **kwargs)
        if device == "auto":
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device

        self.model = KPipeline(lang_code='a', device=self.device)

    def synthesize(self, text: str, ref: str = "af_heart", verbose: bool = True, **kwargs) -> tuple[np.ndarray, int]:
        """
        Synthesize speech from text using Kokoro TTS.

        Args:
            text: Text to synthesize
            ref: Voice name or path to voice tensor
            verbose: Whether to show progress bar
            **kwargs: Additional arguments passed to pipeline generator

        Returns:
            Tuple of (audio_array, sample_rate)
        """
        generator = self.model(
            text,
            voice=ref,
            speed=kwargs.get('speed', 1),
            split_pattern=kwargs.get('split_pattern', r'\n+')
        )

        # Concatenate all audio segments
        audio_segments = []
        iterator = tqdm(generator, desc="Generating audio") if verbose else generator
        for _, _, audio in iterator:
            audio_segments.append(audio)
        
        audio = np.concatenate(audio_segments)
        return audio, 24000  # Kokoro uses 24kHz sample rate
