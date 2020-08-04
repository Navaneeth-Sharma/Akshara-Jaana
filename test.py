import AksharaJaana.main as ak 
text = ak.ocr_engine('/home/navaneeth/Desktop/NandD/OCR_kannada/CamScanner 06-28-2020 12.12.10.pdf')

from AksharaJaana.utils import utils
u = utils()
u.write_as_RTF(text, saving_path='/home/navaneeth/Desktop/1.rtf')
