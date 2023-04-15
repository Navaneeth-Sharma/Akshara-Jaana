import unittest

import sys, os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "AksharaJaana"))
)
from main import OCREngine


class TestOCREngine(unittest.TestCase):
    def setUp(self):
        self.ocr_engine = OCREngine()
        self.test_image = "imgs/test_image.jpeg"

    def test_get_text_from_file(self):
        text = self.ocr_engine.get_text_from_file(self.test_image)
        self.assertNotEqual(text, "")


if __name__ == "__main__":
    unittest.main()
