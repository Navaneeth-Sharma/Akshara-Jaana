import AksharaJaana.main as ak
from AksharaJaana.utils import utils


def test_write_as_RTF():
    text = ak.ocr_engine('/home/navaneeth/Desktop/NandD/OCR_kannada/CamScanner 06-28-2020 12.12.10.pdf')
    u = utils()
    u.write_as_RTF(text, saving_path='/home/navaneeth/Desktop/1.rtf')
