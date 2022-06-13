import os
import glob
from os.path import exists
from warnings import warn

try:
	from utils import utils
except:
	from AksharaJaana.utils import utils

utils = utils()


def ocr_engine(filename):
  if exists(filename):
    try:
      os.mkdir("output/")
    except FileExistsError:
      pass
    line_dir = "output/"

    if ".pdf" in filename:
      try:
        f1 = open(filename)
        text = f1.read()
        if text is []:
          pass
        else:
          return text
      except Exception:
          print("Cant decode!! The file is being read through Image..")
        

      try:
        os.mkdir(line_dir + "pdfout/")
      except:
        pass
      files = glob.glob(line_dir + "pdfout/*")
      for f in files:
          os.remove(f)

      try:
        from pdf2image import pdfinfo_from_path, convert_from_path
        info = pdfinfo_from_path(filename, userpw=None, poppler_path=None)

        maxPages = info["Pages"]
        for page in range(1, maxPages + 1, 20): 
          pages = convert_from_path(filename, dpi=100, first_page=page, last_page=min(page + 20 - 1,maxPages))

          for page1, i in zip(pages,range(len(pages))):
            print("Reading Page No:", i+1)
            page1.save(line_dir + "pdfout/out{0}.jpg".format(page+i), "JPEG")
      except:
        pass


      line_dir = "output/"

      try:
          os.mkdir(line_dir)
      except:
          pass

      files = glob.glob(line_dir + "*.png")
            
      for f in files:
          try:
              os.unlink(f)
          except OSError as e:
              print("Error: %s : %s" % (f, e.strerror))

      utils.truncate_data()

      files = glob.glob(line_dir + "pdfout/*")

      list_of_line_img= os.listdir(line_dir + "pdfout/")

      arr = utils.rearrange(list_of_line_img)

      for f in arr:
        try:
          text += utils.Ocr_image("output/pdfout/" + f)

        except:
          text = utils.Ocr_image("output/pdfout/" + f)
      
      try:
        return text
      except:
        pass

    else:
      utils.truncate_data()
      text = utils.Ocr_image(filename)
      return text
  
  else:
    warn("\033[93m The file in the given path doesn't exists. Please give valid path!")
