# AksharaJaana

<p align="center">
     <img src="https://user-images.githubusercontent.com/63489382/173416453-87824750-b79f-4213-b728-9e91405e541f.png" width=200px>
</p>

<p align="center">
   An OCR for Kannada.
</p>

<p align="center">
   <a href="https://www.npmjs.com/package/@swc/core">
     <a href="https://pypi.org/project/AksharaJaana/"><img src="https://img.shields.io/badge/pypi-package-blue?labelColor=black&style=flat&logo=python&link=https://pypi.org/project/AksharaJaana/" alt="pypi" /></a>
   </a>
</p>

AksharaJaana is a package which uses tesseract ocr in the backend to convert the read-only kannada text to editable format.
A Special feature of this is it can separate columns in the page and thus making it easier to read and edit.
Do consider using this  package if necessary and feel free to mail me for any clarifications.

- Email : navaneethsharma2310oct@gmail.com
- Twitter handle: https://twitter.com/navaneethakbh

Happy coding and installing.

To see the python package visit https://pypi.org/project/AksharaJaana/

## The Requirements

***Conda environment is preferred for the smooth use***

- AksharaJaana *(pip package)*, check out the latest version available
- Tesseract
- poppler

## Details for Installation

### Ubuntu

Open terminal and execute below commands.

1. **Installing tesseract-ocr in the system**

     ```bash
     sudo apt-get update -y 
     sudo apt-get install -y tesseract-ocr 
     ```

2. **Installing poppler in the system**

   ```bash
   sudo apt-get install -y poppler-utils 
   ```

3. **Installing python and pip (if pip is not installed)**

   ```bash
   sudo apt install python==3.6.9
   ```

4. **Installing packages for AksharaJaana**

   ```bash
   pip install --upgrade AksharaJaana
   ```

### Windows

1. Installing tesseract-ocr in the system
   - **Download tesseract**
     - go to the <a href="https://github.com/UB-Mannheim/tesseract/wiki">website</a>
     - click on `tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe (64 bit)`.
   - **Install tesseract for Kannada Language and Script**
     - open the downloaded file and click next and accept the agreement.
     - Next you will give an option to choose the languages.
     - **Choose kannada in both script and language**
   - **Add tesseract to Path**
     - Check if this folder `C:\Program Files\Tesseract-OCR\` is present. If yes, follow below procedure
     - Add `C:\Program Files\Tesseract-OCR\`  to your system PATH by doing the following
        1. Click on the `Windows start button`, search for `Edit the system environment variables`, click on Environment Variables
        2. Under System variables, look for and double-click on PATH, click on `New`.
        3. then add `C:\Program Files\Tesseract-OCR\`, click OK.
     - if folder is not present, manually add the folder tesseract-ocr to the Program Files in the C drive which must be present at the download section (after extraction) and follow the same procedure
     - See complete [docs](docs/tesseract_installation/README.md).

2. Installing poppler in the system

    - **Download Poppler**
      - go to <a href="http://blog.alivate.com.au/poppler-windows/">this</a> page
      - click on `poppler-0.54_x86`
    - **Unzip** the file and copy files to `C:\Users\Program Files\poppler-0.68.0_x86`
    - **Add poppler to path**
      - Add `C:\Program Files\poppler-0.68.0_x86\bin` to your system PATH by doing the following:
        1. Click on the Windows start button, search for Edit the system environment variables, click on Environment Variables
        2. under System variables, look for and double-click on PATH, click on New
        3. then add C:\Users\Program Files\poppler-0.68.0_x86\bin, click OK.

3. Installing python and pip in the system (If pip is not installed)
   - <a href="https://www.python.org/downloads/">Download python</a>

4. Installing packages for AksharaJaana
   - open command prompt

     ```bash
     pip install AksharaJaana
     ```

5. **Reboot** the system before starting to use

### Python Script

```python
import AksharaJaana.main as ak 
text = ak.ocr_engine("Your file Path") 
print(text) 
```
