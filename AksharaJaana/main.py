import os
import glob
from os.path import exists
from warnings import warn

try:
    from utils import Core
except ImportError:
    from AksharaJaana.utils import Core


class OCREngine:
    def __init__(self):
        self.core = Core()

    def get_text_from_file(self, filename):
        if not exists(filename):
            warn(
                """\033[93m The file in the given path doesn't exist. 
                    Please provide a valid path!"""
            )
            return

        os.makedirs("output/", exist_ok=True)

        if ".pdf" in filename:
            text = self._read_pdf(filename)
        else:
            text, _, _ = self.core.get_text_from_image(filename)

        return text

    def _read_pdf(self, filename):
        os.makedirs("output/pdfout/", exist_ok=True)
        files = glob.glob("output/pdfout/*")
        for f in files:
            os.remove(f)

        try:
            from pdf2image import pdfinfo_from_path, convert_from_path

            info = pdfinfo_from_path(filename, userpw=None, poppler_path=None)
            maxPages = info["Pages"]

            for page in range(1, maxPages + 1, 20):
                pages = convert_from_path(
                    filename,
                    dpi=100,
                    first_page=page,
                    last_page=min(page + 20 - 1, maxPages),
                )

                for page1, i in zip(pages, range(len(pages))):
                    print("Reading Page No:", i + 1)
                    page1.save("output/pdfout/out{0}.jpg".format(page + i), "JPEG")
        except Exception as e:
            print(f"Exception {e} not able to read pdf properly")

        text = ""

        list_of_line_img = os.listdir("output/pdfout/")
        arr = self.core.rearrange(list_of_line_img)

        for f in arr:
            try:
                text_, _, _ = self.core.get_text_from_image("output/pdfout/" + f)
                text += text_
            except Exception:
                print(".")

        return text
