#Explore 3-4 new shapes inside OpenCV

import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img.shape)

img[:] = 0,0,0   #Black Background

# Create a Line
cv2.line(img, (512,512), (200, 200), (0,0,255), 4) #redline

# Create a Triangle
cv2.line(img, (50,100), (50, 200), (0,150,150), 3)
cv2.line(img, (50,200), (100, 200), (0,150,150), 3)
cv2.line(img, (100,200), (50, 100), (0,150,150), 3)

#Create an Ellipse
cv2.ellipse(img, (350,50), (100,50), 0,0,180,255, -1)

cv2.imshow('Image', img)
cv2.waitKey(0)