# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 12:53:56 2022

@author: Faizan
"""

import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread("img.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

##### Detecting Characters 

h_img,w_img,_ = img.shape

boxes = pytesseract.image_to_boxes(img)

for b in boxes.splitlines():
    print(b)
    b = b.split(" ")
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, h_img - h), (w, h_img - h),(50, 50, 25), 2)
    cv2.putText(img, b[0], (x, h_img - y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (50,50,255), 2)
    
cv2.imshow('img',img)
cv2.waitKey(0)