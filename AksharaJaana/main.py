import os,shutil,glob
try:
	from utils import utils
except:
	from AksharaJaana.utils import utils
utils = utils()
def ocr_engine(filename):
  try:
    os.mkdir('output/')
  except:
    pass
  line_dir = 'output/'
  if '.pdf' in filename:
    try:
      f1 = open(filename)
      text1 = f1.read()
      if text1 is []:
        pass
      else:
        return text
    except:
      pass
    try:
      os.mkdir(line_dir+'pdfout/')
    except:
      pass
    files = glob.glob(line_dir+'pdfout/*')
    for f in files:
        os.remove(f)

    try:
      from pdf2image import pdfinfo_from_path,convert_from_path
      info = pdfinfo_from_path(filename, userpw=None, poppler_path=None)

      maxPages = info["Pages"]
      for page in range(1, maxPages+1, 20): 
        pages = convert_from_path(filename, dpi=100, first_page=page, last_page = min(page+20-1,maxPages))

        for page1,i in zip(pages,range(len(pages))):
          print(i)
          page1.save(line_dir+'pdfout/out{0}.jpg'.format(page+i), 'JPEG')
    except:
      pass


    line_dir = 'output/'

    try:
        os.mkdir(line_dir)
    except:
        pass

    files = glob.glob(line_dir+'*.png')
           
    for f in files:
        try:
            os.unlink(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))

    utils.truncate_data()

    files = glob.glob(line_dir+'pdfout/*')

    list_of_line_img= os.listdir(line_dir+'pdfout/')

    arr = utils.rearrange(list_of_line_img)

    for f in arr:
      try:
        text+=utils.Ocr_image('output/pdfout/'+f)

      except:
        text = utils.Ocr_image('output/pdfout/'+f)
    
    try:
      return text
    except:
      pass

  else:
    utils.truncate_data()
    text = utils.Ocr_image(filename)
    return text
