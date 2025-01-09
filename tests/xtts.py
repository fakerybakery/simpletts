import unittest
import numpy as np
import soundfile as sf
from simpletts.models.xtts import XTTS

class TestXTTS(unittest.TestCase):
    def setUp(self):
        self.tts = XTTS(device="cpu")
        
    def test_init(self):
        self.assertIsInstance(self.tts, XTTS)
        
    def test_synthesize(self):
        text = "Hello, world!"
        audio, sr = self.tts.synthesize(text, ref="sample.wav")
        
        # Check return types
        self.assertIsInstance(audio, np.ndarray)
        self.assertIsInstance(sr, int)
        
        # Check audio properties
        self.assertEqual(len(audio.shape), 1)  # Should be mono audio
        self.assertTrue(len(audio) > 0)  # Should have some audio data
        
if __name__ == '__main__':
    unittest.main()
