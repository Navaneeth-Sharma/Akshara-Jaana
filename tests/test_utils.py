import unittest
import cv2
import numpy as np

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'AksharaJaana')))
from utils import ImageOperationUtils, FileOperationUtils, Core

class TestImageOperationUtils(unittest.TestCase):

    def setUp(self):
        self.utils = ImageOperationUtils()
        self.image = cv2.imread('imgs/test_image.jpeg')

    def test_get_grayscale(self):
        grayscale = self.utils.get_grayscale(self.image)
        self.assertEqual(len(grayscale.shape), 2)
        self.assertEqual(grayscale.shape[0], self.image.shape[0])
        self.assertEqual(grayscale.shape[1], self.image.shape[1])
        self.assertTrue(np.all(grayscale >= 0) and np.all(grayscale <= 255))

    def test_morph(self):
        kernel_size = 3
        morphed = self.utils.morph(self.image, kernel_size)
        self.assertEqual(len(morphed.shape), 3)
        self.assertEqual(morphed.shape[0], self.image.shape[0])
        self.assertEqual(morphed.shape[1], self.image.shape[1])
        self.assertTrue(np.all(morphed >= 0) and np.all(morphed <= 255))


class TestFileOperationUtils(unittest.TestCase):

    def setUp(self):
        self.file_utils = FileOperationUtils()
        self.test_data = "Test data"
        self.test_html_path = "test_file.html"
        self.test_rtf_path = "test_file.rtf"

    def tearDown(self):
        if os.path.exists(self.test_html_path):
            os.remove(self.test_html_path)
        if os.path.exists(self.test_rtf_path):
            os.remove(self.test_rtf_path)

    def test_save_in_html_and_open(self):
        self.file_utils.save_in_html_and_open(self.test_data, self.test_html_path)
        self.assertTrue(os.path.exists(self.test_html_path))

    def test_create_or_empty_a_file(self):
        self.file_utils.create_or_empty_a_file(self.test_rtf_path)
        self.assertTrue(os.path.exists(self.test_rtf_path))
        self.assertEqual(os.path.getsize(self.test_rtf_path), 0)

        with open(self.test_rtf_path, "w") as f:
            f.write("test")
        self.file_utils.create_or_empty_a_file(self.test_rtf_path)
        self.assertEqual(os.path.getsize(self.test_rtf_path), 0)

    def test_save_as_rtf(self):
        self.file_utils.save_as_rtf(self.test_data, self.test_rtf_path)
        self.assertTrue(os.path.exists(self.test_rtf_path))
        with open(self.test_rtf_path, "r", encoding="utf8") as f:
            saved_data = f.read()
        self.assertEqual(saved_data, self.test_data)

    def test_save_as_rtf_with_truncate_exception(self):
        with open(self.test_rtf_path, "w") as f:
            f.write("test")
        os.chmod(self.test_rtf_path, 0o444)  # make the file read-only
        self.assertRaises(Exception, self.file_utils.save_as_rtf, self.test_data, self.test_rtf_path)



class TestCore(unittest.TestCase):
    def setUp(self):
        self.core = Core()
        self.test_image = 'imgs/test_image.jpeg'


    def tearDown(self):
        self.core.clear_output_dirs()

    def test_image_to_string_pytesseract(self):
        text = self.core.image_to_string_pytesseract(self.test_image)
        self.assertNotEqual(text.strip(), '')

    def test_preprocessing(self):
        actual_image, preprocessed_image = self.core.preprocessing(self.test_image)

        self.assertTrue(isinstance(actual_image, np.ndarray))
        self.assertTrue(isinstance(preprocessed_image, np.ndarray))
        self.assertEqual(actual_image.shape, (1181, 1088, 3))
        self.assertEqual(preprocessed_image.shape, (1181, 1088))

    def test_crop_images_by_row(self):
        actual_image, preprocessed_image = self.core.preprocessing(self.test_image)
        self.core.crop_images_by_row(actual_image, preprocessed_image)
        self.assertTrue(os.path.exists(self.core.output_row_crop_dir))
        self.assertTrue(len(os.listdir(self.core.output_row_crop_dir)) > 0)

    def test_crop_images_by_column(self):
        actual_image, preprocessed_image = self.core.preprocessing(self.test_image)
        self.core.crop_images_by_row(actual_image, preprocessed_image)
        self.core.crop_images_by_column(actual_image, preprocessed_image, index=0)
        output_folder = os.path.join(self.core.output_dir, '0')
        self.assertTrue(os.path.exists(output_folder))
        self.assertTrue(len(os.listdir(output_folder)) > 0)

    def test_clear_output_dirs(self):
        os.makedirs(self.core.output_row_crop_dir, exist_ok=True)
        os.makedirs(self.core.output_dir, exist_ok=True)
        self.core.clear_output_dirs()
        self.assertFalse(os.path.exists(self.core.output_row_crop_dir))
        self.assertFalse(os.path.exists(self.core.output_dir))

    def test_get_text_from_image(self):
        text, columns, row = self.core.get_text_from_image(self.test_image)
        self.assertNotEqual(text, '')
        self.assertEqual(columns[0], 2)
        self.assertEqual(row, 1)


if __name__ == '__main__':
    unittest.main()
