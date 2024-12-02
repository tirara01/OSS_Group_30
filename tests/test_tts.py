import unittest
from src.tts.tts_engine import text_to_speech

class TestTTS(unittest.TestCase):
    def test_text_to_speech(self):
        audio_path = text_to_speech("Hello World", output_dir="data/output/")
        self.assertTrue(audio_path.endswith(".wav"))

if __name__ == "__main__":
    unittest.main()
