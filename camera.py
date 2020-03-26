# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:39:26 2020

@author: Chaitanya
"""

import cv2

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
           
    screenSize = cv2.resize(img, (1000, 700))
    cv2.imshow('Camera',screenSize) 
   
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()