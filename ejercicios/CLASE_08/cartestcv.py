# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 20:11:35 2021

@author: Juan Carlos
"""
import cv2
face_cascade=cv2.CascadeClassifier('cars.xml')
cap=cv2.VideoCapture('video2.avi')
while True:
    _,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow('TestFace',img)
    k=cv2.waitKey(50)
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()