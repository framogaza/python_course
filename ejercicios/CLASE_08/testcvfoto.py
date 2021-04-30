# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 17:56:05 2021

@author: Juan Carlos
"""
import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
img = cv2.imread('foto.jpg')
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 6)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 1)
# Display the output
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()