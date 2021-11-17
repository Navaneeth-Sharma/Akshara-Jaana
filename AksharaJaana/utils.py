######################################################################################################################################
#                                                       Functions required 
######################################################################################################################################

import cv2
import numpy as np
from collections.abc import Iterable
import io

class utils:

    def __init__(self):
        pass

    def web(self,message):

        import webbrowser
        f = open('AksharaJaana/output/OCR_output.html','w')
        f.write(message)
        f.close()

        webbrowser.open_new_tab('AksharaJaana/output/OCR_output.html')

    def Resize(self, file_path,saving_path='AksharaJaana/output/out.jpg'):
        try:
            import cv2
         
            img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
            scale_percent = 10 # percent of original size
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)
            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            cv2.imshow("Resized image", resized)
            cv2.waitKey(1000)
            cv2.imwrite(saving_path,resized)

        except Exception as e:
            print(e)

    def write_as_html(self, text,saving_path = 'AksharaJaana/output/result.html'):
        file = open(saving_path,'a')
        file.write(text)
        file.close()
        return text


    def write_as_RTF(self, text,saving_path='AksharaJaana/output/result.rtf'):
        try:
            self.truncate_data(saving_path)
        except:
            pass    
        try:
            file = open(saving_path,'a')
            file.write(text)
            file.close()
        except:
            with io.open(saving_path, 'a', encoding='utf8') as f:
                f.write(text)
                f.close()
        return text

    def read_from_html(self):
        file = open('output/result.html','r')
        text = file.read()

    def truncate_data(self,file_path="output/result.rtf"):
        try:
            file = open("output/result.html","r+")
            file.truncate(0)
            file.close()
            file = open(file_path,"r+")
            file.truncate(0)
            file.close()
        except:
            pass

    def convt_to_string(self, file_path):
        import cv2 
        import pytesseract

        img = cv2.imread(file_path)

        # Adding custom options
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(img, lang='kan',config=custom_config)

        return text


    # get grayscale image
    def get_grayscale(self,image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # noise removal
    def remove_noise(self, image):
        return cv2.medianBlur(image,5)
     
    #thresholding
    def thresholding(self, image):
        return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    #dilation
    def dilate(self, image):
        kernel = np.ones((5,5),np.uint8)
        return cv2.dilate(image, kernel, iterations = 1)
        
    #erosion
    def erode(self, image):
        kernel = np.ones((5,5),np.uint8)
        return cv2.erode(image, kernel, iterations = 1)

    #opening - erosion followed by dilation
    def opening1(self, image):
        kernel = np.ones((5,5),np.uint8)
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    #canny edge detection
    def canny(self, image):
        return cv2.Canny(image, 10, 20)

    #skew correction
    def deskew(self, image):
        coords = np.column_stack(np.where(image > 0))
        angle = cv2.minAreaRect(coords)[-1]
        if angle < (-45):
            angle = -(90 + angle)
        else:
            angle = -angle
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return rotated

    #template matching
    def match_template(self, image, template):
        return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 


    def preprocessing(self, file_name):
        '''Before converting the image to the pytesseract the image is fed to this preprocessing'''
        # from utils import getIndexPositions,convt_to_list

        image = cv2.imread(file_name)
        gray = self.get_grayscale(image)
        # thresh = self.thresholding(gray)
        opening = self.opening1(gray)
        opening = cv2.adaptiveThreshold(opening, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY , 81,11 )
        actual_image = image.copy()

        opening = opening/255

        return actual_image,opening

    
    def flatten(self,A):
        rt = []
        for i in A:
            if isinstance(i,list): rt.extend(self.flatten(i))
            else: rt.append(i)
        return rt

    def ROW_CROP(self,actual_image,preprop_image):
        ''' For the dividing the image into the 2 or more parts'''

        image = preprop_image
        ROW_WISE = np.ones((1,image.shape[1]))

        positions = [i for i,j in enumerate(image) if np.all(j==ROW_WISE)]

        pos = []
        for i in range(len(positions)):
            try:
                if positions[i+1]-positions[i]>1600:
                    pos.append(positions[i])
                    pos.append(positions[i+1])
            except:
                pass
        pos.append(0)
        pos.sort()
        pos.append(image.shape[0])

        Pos = []
        for i in range(len(pos)):
            try:
                if pos[i+1]-pos[i]>1600:
                    Pos.append(pos[i])
                    Pos.append(pos[i+1])
            except:
                pass

        if Pos == []:
            Pos.append(pos[0])
            Pos.append(pos[len(pos)-1])
            pos = Pos
        else:
            pos = Pos
        

        if len(pos)>1:
            for i in range(len(pos)):

                # print(pos)
                if i==len(pos):
                    break
                else:
                    try:
                        img1 = actual_image[pos[i]:pos[i+1],:]
                        try:
                            import os
                            os.mkdir('output/OUT_ROW_CROP/')
                        except:
                            pass
                        cv2.imwrite('output/OUT_ROW_CROP/filenameR{0}.jpg'.format(i), img1)

                    except:
                        pass
        else:
            img = actual_image
            cv2.imwrite('output/OUT_ROW_CROP/filenameR0.jpg', img)

    def remove_duplicate(self,x):
      return list(dict.fromkeys(x))

    def COLUMN_CROP(self,actual_image,preprop_image, index):
        ''' For the Column crop'''
        
        image = preprop_image
        COLOMN_WISE = np.ones((image.shape[0],1))

        lis = np.ones(image.shape[0])

        positions = [i for i,j in enumerate(image.T) if np.all(j==lis)]

        pos = []
        for i in range(len(positions)):
            try:
                if positions[i+1]-positions[i]>8:
                    pos.append(positions[i])
                    pos.append(positions[i+1])
            except:
                pass
        pos.append(0)
        pos.sort()
        pos.append(image.shape[1])

        Pos = []
        for i in range(len(pos)):
            try:
                if pos[i+1]-pos[i]>8:
                    Pos.append(pos[i])
                    Pos.append(pos[i+1])
            except:
                pass

        if Pos == []:
            Pos.append(pos[0])
            Pos.append(pos[len(pos)-1])
            pos = Pos
        else:
            pos = Pos

        pos = self.remove_duplicate(pos)

        if len(pos)>1:
            for i in range(len(pos)):

                if i!=len(pos):
                    try:
                        if actual_image[:,pos[i]:pos[i+1]].shape[1] > 200:
                            img1 = actual_image[:,pos[i]:pos[i+1]]
                            try:
                                import os
                                os.mkdir('output/OUT/')                             
                            except:
                                pass
                            try:
                                import os
                                os.mkdir('output/OUT/'+str(index))

                            except:
                                pass

                            cv2.imwrite('output/OUT/'+str(index)+'/filename_{0}.jpg'.format(i), img1)  
                    except:
                        pass
                else:
                    pass
        else:
            img = actual_image
            cv2.imwrite('output/OUT/filename0.jpg', img)                

    def rearrange(self,array_of_filenames):
        import re

        def atoi(text):
            return int(text) if text.isdigit() else text

        def natural_keys(text):
            return [atoi(c) for c in re.split(r'(\d+)', text)]

        arr = [i for i in array_of_filenames]
        arr.sort(key=natural_keys)

        return arr


    def Ocr_image(self,filename):

        import glob, os, shutil

        try:

            [os.remove(f) for f in glob.glob('output/OUT_ROW_CROP'+'/'+'*')]
            [shutil.rmtree(f) for f in glob.glob('output/OUT'+'/'+'*')]

        except:
            pass

        actual_image,opening = self.preprocessing(filename)

        self.ROW_CROP(actual_image, opening)

        import os,shutil,glob

        files = glob.glob('output/OUT_ROW_CROP'+'/'+'*.jpg')

        for i,f in enumerate(files):
            actual_image,opening = self.preprocessing(f)
            self.COLUMN_CROP(actual_image, opening,index=i)

        files = glob.glob('output/OUT/'+'*')
        files = self.rearrange(files)
        files1 = [self.rearrange(glob.glob(f+'/'+'*.jpg')) for f in files]

        text1 = ''
        
        for f in files1:
            for f1 in f:
                try:
                    text1 += self.convt_to_string(str(f1))
                except:
                    text1 = self.convt_to_string(str(f1))
        try:
            return text1
        except:
            pass
