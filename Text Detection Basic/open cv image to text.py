# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:59:34 2022

@author: Faizan
"""

import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread("img.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(pytesseract.image_to_string(img))
cv2.imshow('img', img)
cv2.waitKey(0)