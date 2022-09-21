import cv2
import numpy as np

### Apply face detection to elon video
# haarcascade = "Resources/haarcascade_frontalface_default.xml"
# cap = cv2.VideoCapture('Resources/elon.mp4')
# cap.set(3, 640) #set width
# cap.set(4, 480) #set height
# while True:
#     success, img = cap.read()
#     facecascade = cv2.CascadeClassifier(haarcascade)
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = facecascade.detectMultiScale(img_gray, 1.1, 4)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 1)
#     cv2.imshow("elon face", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

### Apply face detection to lena image
haarcascade = "Resources/haarcascade_frontalface_default.xml"
img = cv2.imread('Resources/lena.png')
while True:
    facecascade = cv2.CascadeClassifier(haarcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(img_gray, 1.1, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 1)
    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
