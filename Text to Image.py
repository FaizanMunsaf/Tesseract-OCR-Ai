# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:58:37 2022

@author: Faizan
"""

from pytesseract import pytesseract  # tesseract Engine OCR Convertor
from PIL import Image # Pillow library to upload the image


# The path of installed tesseract
tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# The Image path
path_image = r"C:\Users\Faizan\Desktop\pg 2.jpg"


# Start the tesseract engine
pytesseract.tesseract_cmd = tesseract_path


# Open the image with PIL
img = Image.open(path_image)


# Extract the text from image
text1 = pytesseract.image_to_string(img)

# Print the Output
print("Image Text : \n\n", text1)

f = open("ppr 2.txt", "w")
f.write(text1)
f.close()

