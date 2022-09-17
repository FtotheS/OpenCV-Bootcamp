# ASSIGNMENT 17/9/2022
# Coded by: Farman

# Part 1: Read a video & convert the image frames to grayscale & show the output realtime 

import cv2
import numpy as np

cap = cv2.VideoCapture('Resources/elon.mp4')

while True:
    success, img = cap.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Output', img_gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Part 2: Read a video & crop the frame of the video sequence & show it real time

import cv2
import numpy as np

cap = cv2.VideoCapture('Resources/elon.mp4')

while True:
    success, frame = cap.read()
    vid = frame[0:200, 0:400]
    cv2.imshow('Output', vid)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
