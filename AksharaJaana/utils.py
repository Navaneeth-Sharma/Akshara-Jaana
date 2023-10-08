import os
import cv2
import numpy as np
import io
import webbrowser
import shutil
import glob
import pytesseract
import re
import easyocr
from paddleocr import PaddleOCR


class ImageOperationUtils:
    def __init__(self) -> None:
        pass

    def get_grayscale(self, image):
        """
        converts BGR to GRAY scale image
        """
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def morph(self, image, kernel_size=5):
        """
        morphological operations to remove noise and fill gaps in the text.
        """
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


class FileOperationUtils:
    def __init__(self) -> None:
        pass

    def save_in_html_and_open(self, data: str, file_path: str):
        """
        This function saves data in HTML format and opens it in a browser.

        :param data: The data that needs to be saved in HTML format and opened in a browser
        :type data: str
        :param file_path: The file path is a string that represents the location and name of the file where
        the data will be saved in HTML format. It should include the file extension ".html"
        :type file_path: str
        """
        with open(file_path, "w") as f:
            f.write(data)

        webbrowser.open_new_tab(file_path)

    def create_or_empty_a_file(self, file_path: str):
        """
        The function creates an empty file or truncates an existing file to make it 0 bytes.

        :param file_path: The file path is a string that specifies the location and name of the file that
        needs to be truncated. It can be an absolute or relative path
        """
        open(file_path, "w").close()

    def save_as_rtf(self, text: str, saving_path: str):
        """
        This function saves a given text as an RTF file at a specified path.

        :param text: The text that needs to be saved as an RTF file
        :type text: str
        :param saving_path: The path where the RTF file will be saved
        :type saving_path: str
        :return: the input parameter `text`.
        """
        try:
            self.create_or_empty_a_file(file_path=saving_path)
        except Exception as e:
            print(f"Error {e} while writing to RTF file")

        try:
            with open(saving_path, "a", encoding="utf8") as file:
                file.write(text)
        except Exception as e:
            print(e)
            with io.open(saving_path, "a", encoding="utf8") as file:
                file.write(text)
        finally:
            print("Error while writing to RTF file")

        return text


class ModelTypes:
    Tesseract = "tessract"
    Easyocr = "easyocr"
    Paddleocr = "paddleocr"



class Core:
    def __init__(self, modelType) -> None:
        self.img_operations = ImageOperationUtils()
        self.output_row_crop_dir = "output/OUT_ROW_CROP"
        self.output_dir = "output/OUT"

        self.modelType = modelType

        if self.modelType == ModelTypes.Easyocr:
            self.reader = easyocr.Reader(["kn", "en"])
        
        if self.modelType == ModelTypes.Paddleocr:
            self.paddleocr = PaddleOCR(lang="ka")

    def image_to_string_pytesseract(self, file_path):
        img = cv2.imread(file_path)

        # Adding custom options
        custom_config = r"--oem 3 --psm 6"
        text = pytesseract.image_to_string(img, lang="kan", config=custom_config)

        return text

    def image_to_string_easyocr(self, filepath):
        return ' '.join([pred[1] for pred in self.reader.readtext(filepath)])   

    def image_to_string_paddleocr(self, filepath):
        result = self.paddleocr.ocr(filepath)
        return ' '.join([line[1][0] for line in result[0]])

    def preprocessing(self, file_name):
        """
        This function performs preprocessing on an image before converting passing
        image to pytesseract.

        :param file_name: The name or path of the image file that needs to be preprocessed
        :return: a tuple containing two elements:
        1. actual_image: a copy of the original image
        2. output_image: a preprocessed binary image
        """

        image = cv2.imread(file_name)
        gray = self.img_operations.get_grayscale(image)

        morphed_image = self.img_operations.morph(gray)
        binary_image = cv2.adaptiveThreshold(
            morphed_image,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            81,
            11,
        )

        actual_image = image.copy()

        output_image = binary_image / 255

        return actual_image, output_image

    def crop_images_by_row(self, actual_image, preprop_image):
        """
        The function divides an image into two or more parts based on row-wise positions and saves the
        cropped images to disk.

        :param actual_image: The original image that needs to be cropped
        :param preprop_image: preprocessed image that has been binarized and resized to a fixed height, used
        to identify the positions where the actual image should be divided
        """

        rows = 0
        ROW_WISE = np.ones((1, preprop_image.shape[1]))
        positions = [i for i, j in enumerate(preprop_image) if np.all(j == ROW_WISE)]

        # Find positions where image should be divided
        pos = [0, preprop_image.shape[0]]
        for i in range(len(positions) - 1):
            if positions[i + 1] - positions[i] > 1600:
                pos.append(positions[i])
                pos.append(positions[i + 1])
        pos.sort()

        # Save cropped images to disk
        if len(pos) > 1:
            for i in range(len(pos) - 1):
                try:
                    rows += 1
                    img1 = actual_image[pos[i] : pos[i + 1], :]
                    os.makedirs("output/OUT_ROW_CROP", exist_ok=True)
                    cv2.imwrite(f"output/OUT_ROW_CROP/filenameR{i}.jpg", img1)
                except Exception as e:
                    print(f"Error {e} while saving the row crop image")
        else:
            cv2.imwrite("output/OUT_ROW_CROP/filenameR0.jpg", actual_image)

        return rows

    def remove_duplicate(self, x):
        return list(dict.fromkeys(x))

    def crop_images_by_column(self, actual_image, preprop_image, index):
        """
        This function crops an input image into multiple sub-images based on vertical columns of white
        space.

        :param actual_image: The original image that needs to be cropped
        :param preprop_image: The preprocessed image that needs to be cropped by column
        :param index: The index parameter is an identifier used to create a unique folder for the output
        images. It is used to organize the output images into separate folders for each input image
        """

        columns = 0
        image = preprop_image

        positions = [i for i, j in enumerate(image.T) if np.sum(j == 1) >= 0.9 * len(j)]

        pos = [
            positions[i]
            for i in range(len(positions))
            if (i + 1 == len(positions)) or (positions[i + 1] - positions[i] > 8)
        ]
        pos.insert(0, 0)
        pos.append(image.shape[1])

        pos = self.remove_duplicate(pos)

        for i in range(len(pos) - 1):
            try:
                if actual_image[:, pos[i] : pos[i + 1]].shape[1] > 200:
                    img1 = actual_image[:, pos[i] : pos[i + 1]]
                    columns += 1
                    try:
                        os.makedirs(f"output/OUT/{index}")
                    except FileExistsError:
                        pass
                    cv2.imwrite(f"output/OUT/{index}/filename_{i}.jpg", img1)
            except Exception as e:
                print(f"Error {e} Not able to write cropped column files")

        return columns

    def clear_output_dirs(self):
        for path in [self.output_row_crop_dir, self.output_dir]:
            shutil.rmtree(path, ignore_errors=True)

    def rearrange(self, array_of_filenames):
        """
        The function rearranges an array of filenames in a natural order.

        :param array_of_filenames: A list of filenames in string format that needs to be rearranged in
        natural order. For example, if the list contains filenames like "file1.txt", "file10.txt",
        "file2.txt", the function will rearrange them as "file1.txt", "file2.txt", "file
        :return: The function `rearrange` returns the sorted `array_of_filenames` list, sorted in natural
        order.
        """

        def atoi(text):
            return int(text) if text.isdigit() else text

        def natural_keys(text):
            return [atoi(c) for c in re.split(r"(\d+)", text)]

        arr = [i for i in array_of_filenames]
        arr.sort(key=natural_keys)
        return arr

    def get_text_from_image(self, filename):
        """
        This function takes an image file, preprocesses it, crops it into rows and columns, extracts text
        from each cropped image using pytesseract, and returns the concatenated text.

        :param filename: The filename of the image that needs to be processed to extract text from it
        :return: a string that contains the text extracted from the input image file using pytesseract OCR
        after performing some preprocessing steps such as cropping and rearranging the image.
        """
        self.clear_output_dirs()

        columns_arr = []

        actual_image, opening = self.preprocessing(filename)

        rows = self.crop_images_by_row(actual_image, opening)

        row_cropped_files = glob.glob(f"{self.output_row_crop_dir}/*.jpg")

        for idx, file_ in enumerate(row_cropped_files):
            actual_image, opening = self.preprocessing(file_)
            columns_arr.append(
                self.crop_images_by_column(actual_image, opening, index=idx)
            )

        column_cropped_files = glob.glob(f"{self.output_dir}/*")

        # glob get files randomly, to make it to arranged, rearrange is used
        rearranged_column_cropped_files = self.rearrange(column_cropped_files)
        all_image_files_arr = [
            self.rearrange(glob.glob(f"{f}/*.jpg"))
            for f in rearranged_column_cropped_files
        ]

        text1 = ""

        for image_files in all_image_files_arr:
            for image_file in image_files:
                try:
                    if self.modelType == ModelTypes.Easyocr:
                        text1 += " " + self.image_to_string_easyocr(str(image_file))
                    elif self.modelType == ModelTypes.Paddleocr:
                        text1 += " " + self.image_to_string_paddleocr(str(image_file))
                    else:
                        text1 += " " + self.image_to_string_pytesseract(str(image_file))
                except Exception as e:
                    print(e)
                    if self.modelType == ModelTypes.Easyocr:
                        text1 = self.image_to_string_easyocr(str(image_file))
                    elif self.modelType == ModelTypes.Paddleocr:
                        text1 = self.image_to_string_paddleocr(str(image_file))
                    else:
                        text1 = self.image_to_string_pytesseract(str(image_file))

        return text1, columns_arr, rows
