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
      os.mkdir(line_dir+'pdfout/')
    except:
      pass
    files = glob.glob(line_dir+'pdfout/*')
    for f in files:
        os.remove(f)

    try:
      from pdf2image import convert_from_path
      pages = convert_from_path(filename, 500)
    except Exception as e:
      pass
    try:
      for page,i in zip(pages,range(len(pages))):
        page.save(line_dir+'pdfout/out{0}.jpg'.format(i), 'JPEG')
    except:
      pass


    line_dir = 'output/'

    try:
        os.mkdir(line_dir)
    except:
        pass

    files = glob.glob(line_dir+'*.png')
    print(files)

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
