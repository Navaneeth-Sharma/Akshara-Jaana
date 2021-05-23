# AksharaJaana

AksharaJaana is the package which uses tesseract ocr in backend to convert the kannada text to editable format.You can use
following sample code in ubuntu.The Special feature of this is it can separate columns in page


# The Requirements (Conda environment is prefered for the smooth use)

**python >= 3.6.9**  <br />
**opencv-python >= 4.2.0.32**  <br />
**numpy==1.18.4**  <br />
**pdf2image==1.13.1**   <br />
**pytesseract**   <br />
**tesseract**   <br />
**poppler**   <br />

# Details for installation (Complete installation including requirements) 
--------------------------------------------------------------Ubuntu------------------------------------------------------------

1. Installing tesseract-ocr in the sysytem
---> open terminal
---> type->   sudo apt-get update -y   -> press enter
---> type->   sudo apt-get install -y tesseract-ocr   -> press enter

2. Installing poppler in the system
---> open terminal
---> type->   sudo apt-get install -y poppler-utils  -> press enter

3. Installing python and pip (if pip is not installed)
---> open terminal 
---> type-> sudo apt install python==3.6.9

4. Installing packages for AksharaJaana
---> open terminal
---> type->   pip install opencv-python==4.2.0.32 --> press enter
---> type->   pip install numpy==1.18.4 --> press enter
---> type->   pip install pdf2image==1.13.1 --> press enter
---> type->   pip install AksharaJaana==0.1.2.9 --> press enter(1)
---> type->   pip install pytesseract --> press enter
or try running (1) and download requirements.txt from this and run pip install -r requirements.txt

------------------------------------------------------------- Windows-----------------------------------------------------------

1. Installing tesseract-ocr in the system 
---> go to the website --> https://github.com/UB-Mannheim/tesseract/wiki
---> click on --> tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe (64 bit) resp.
---> after downloading open that file --> hit enter --> you will give an option to choose the languages. --> choose kannada in both script and lang
---> next after installation of that files. check if this folder is present C:\Program Files\Tesseract-OCR\ 
---> if yes, then search for follow below procedure

	Add C:\Program Files\Tesseract-OCR\  to your system PATH by doing the following: 
	  1---> Click on the Windows start button, search for Edit the system environment variables, click on Environment Variables..., 
	  2---> under System variables, look for and double-click on PATH, click on New,
	  3---> then add C:\Program Files\Tesseract-OCR\, click OK.

---> if no, manually add the folder tesseract-ocr to the Program Files in the C drive which must be present at the download section (after extraction) and follow the same procedure

2. Installing poppler in the system
---> go to this page, http://blog.alivate.com.au/poppler-windows/
---> click on --> poppler-0.54_x86
---> after downloading open that file --> hit enter --> you will give an option to choose the languages. --> choose kannada in both script and lang
---> next after installation of that files. check if this folder is present C:\Program Files\Tesseract-OCR\ 
---> if yes, then search for follow below procedure
	Add C:\Program Files\poppler-0.68.0_x86\bin to your system PATH by doing the following:
	 1 ---> Click on the Windows start button, search for Edit the system environment variables, click on Environment Variables...,
	 2 ---> under System variables, look for and double-click on PATH, click on New,
	 3 ---> then add C:\Users\Program Files\poppler-0.68.0_x86\bin, click OK.
---> if no, manually add the folder poppler-0.68.0_x86 to the Program Files in the C drive which must be present at the download section (after extraction) and follow the same procedure

3. Installing python and pip in the system (If pip is not installed)
---> go to this page and download python (any version >= 3.6.9)
---> now click allow changes as soon as it pops up a window for allowing changes. 
---> now click next and accept and finally ok. here the pip is installed

4. Installing packages for AksharaJaana
---> open command prompt
---> type->   pip install opencv-python==4.2.0.32 --> press enter
---> type->   pip install numpy==1.18.4 --> press enter
---> type->   pip install pdf2image==1.13.1 --> press enter
---> type->   pip install AksharaJaana==0.1.2.9 --> press enter
---> type->   pip install pytesseract --> press enter

5.  Reboot the system before starting to use 



## Python Script
**Its in test.py in Github Repo** 
>import AksharaJaana.main as ak 

>text = ak.ocr_engine('/home/navaneeth/Desktop/NandD/OCR_kannada/CamScanner 06-28-2020 12.12.10.pdf')

>from AksharaJaana.utils import utils

>u = utils()

>u.write_as_RTF(text, saving_path='/home/navaneeth/Desktop/1.rtf')
