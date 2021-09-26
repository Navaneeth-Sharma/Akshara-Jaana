# AksharaJaana

AksharaJaana is the package which uses tesseract ocr in backend to convert the kannada text to editable format.The Special feature of this is it can separate columns in page


## The Requirements 
#### *Conda environment is prefered for the smooth use*
- AksharaJaana (pip package), check out the latest version available
- Tesseract 
- poppler

## Details for Installation 
#### *Complete installation including requirements*
### Ubuntu
1. **Installing tesseract-ocr in the system**
- open terminal
- sudo apt-get update -y 
- sudo apt-get install -y tesseract-ocr 

2. **Installing poppler in the system**
- sudo apt-get install -y poppler-utils 

3. **Installing python and pip (if pip is not installed)** 
- sudo apt install python==3.6.9

4. **Installing packages for AksharaJaana**
- pip install AksharaJaana

### Windows
1. Installing tesseract-ocr in the system 
- go to the <a href="https://github.com/UB-Mannheim/tesseract/wiki">website</a> -->  click on --> tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe (64 bit) resp.
- After downloading open that file --> hit enter --> you will give an option to choose the languages. --> choose kannada in both script and language
- next check if this folder **C:\Program Files\Tesseract-OCR\** is present 
- If yes, follow below procedure
- Add C:\Program Files\Tesseract-OCR\  to your system PATH by doing the following: 
> &nbsp;&nbsp;1. Click on the Windows start button, search for Edit the system environment variables, click on Environment Variables <br />
> &nbsp;&nbsp;2. under System variables, look for and double-click on PATH, click on New <br />
> &nbsp;&nbsp;3. then add C:\Program Files\Tesseract-OCR\, click OK <br />

- if no, manually add the folder tesseract-ocr to the Program Files in the C drive which must be present at the download section (after extraction) and follow the same procedure

2. Installing poppler in the system
- go to <a href=" http://blog.alivate.com.au/poppler-windows/">this</a> page
- click on --> poppler-0.54_x86
- after downloading open that file --> hit enter --> you will give an option to choose the languages. --> choose kannada in both script and lang
- next after installation of that files. check if this folder is present C:\Program Files\Tesseract-OCR\ 
- if yes, then search for follow below procedure
- Add C:\Program Files\poppler-0.68.0_x86\bin to your system PATH by doing the following:
> &nbsp;&nbsp;	 1. Click on the Windows start button, search for Edit the system environment variables, click on Environment Variables <br />
> &nbsp;&nbsp;	 2. under System variables, look for and double-click on PATH, click on New <br />
> &nbsp;&nbsp;	 3. then add C:\Users\Program Files\poppler-0.68.0_x86\bin, click OK <br />
- if no, manually add the folder poppler-0.68.0_x86 to the Program Files in the C drive which must be present at the download section (after extraction) and follow the same procedure

3. Installing python and pip in the system (If pip is not installed)
- <a href="https://www.python.org/downloads/">Click</a> here and download python

4. Installing packages for AksharaJaana
- open command prompt
- pip install AksharaJaana

5.  Reboot the system before starting to use 



### Python Script
**Its in test.py in Github Repo** 

>import AksharaJaana.main as ak <br>
>text = ak.ocr_engine("Your file Path") <br>
>print(text) <br>

