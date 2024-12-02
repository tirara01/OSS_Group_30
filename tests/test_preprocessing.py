import unittest
from src.preprocessing.preprocess import preprocess_image
from src.preprocessing.ocr import extract_handwriting

class TestPreprocessing(unittest.TestCase):
    def test_preprocess_image(self):
        result = preprocess_image("data/input/sample_image.jpg")
        self.assertIsNotNone(result)

    def test_extract_handwriting(self):
        text = extract_handwriting("data/input/sample_image.jpg")
        self.assertTrue(len(text) > 0)

if __name__ == "__main__":
    unittest.main()
