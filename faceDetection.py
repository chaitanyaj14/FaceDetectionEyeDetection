# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:31:00 2020

@author: Chaitanya
"""

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),1)
            
    screenSize = cv2.resize(img, (1000, 700))
    cv2.imshow('Face Detection',screenSize) 
   
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()