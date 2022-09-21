# Apply joining to lambo & robot images (Horizontal & Vertical)

import cv2
import numpy as np

img1 = cv2.imread('Resources/robot.png')
resized_img1 = cv2.resize(img1, (400, 250))

img2 = cv2.imread('Resources/lambo.png')
resized_img2 = cv2.resize(img2, (400, 250))

img_ver = np.vstack((resized_img1, resized_img2))
img_hor = np.hstack((resized_img1, resized_img2))

cv2.imshow("Vertical", img_ver)
cv2.imshow("Horizontal", img_hor)

cv2.waitKey(0)
