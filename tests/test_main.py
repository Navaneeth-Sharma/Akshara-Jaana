import unittest

import sys, os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "AksharaJaana"))
)
from main import OCREngine
from utils import ModelTypes

class TestOCREngine(unittest.TestCase):
    def setUp(self):
        self.tesseract_ocr = OCREngine(ModelTypes.Tesseract)
        self.easy_ocr = OCREngine(ModelTypes.Easyocr)
        self.paddle_ocr = OCREngine(ModelTypes.Paddleocr)

        self.test_image = "imgs/test_image.jpeg"

    def test_tesseract_get_text_from_file(self):
        text = self.tesseract_ocr.get_text_from_file(self.test_image)
        self.assertNotEqual(text, "")

    def test_easyocr_get_text_from_file(self):
        text = self.easy_ocr.get_text_from_file(self.test_image)
        self.assertNotEqual(text, "")

    def test_paddleocr_get_text_from_file(self):
        text = self.paddle_ocr.get_text_from_file(self.test_image)
        self.assertNotEqual(text, "")

if __name__ == "__main__":
    unittest.main()
