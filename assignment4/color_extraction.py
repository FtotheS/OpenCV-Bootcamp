# Apply color extraction on an image

import cv2
import numpy as np

path = "Resources/robot.png"

def empty():
    pass

cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar", 400, 150)
cv2.createTrackbar("Hue Min", "TrackBar", 2, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBar", 27, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBar", 137, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBar", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBar", 96, 255, empty)
cv2.createTrackbar("Val Max", "TrackBar", 255, 255, empty)

while True:
    img = cv2.imread(path)
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#TrackBar Objects
hue_min = cv2.getTrackbarPos("Hue Min", "TrackBar")
hue_max = cv2.getTrackbarPos("Hue Max", "TrackBar")
sat_min = cv2.getTrackbarPos("Sat Min", "TrackBar")
sat_max = cv2.getTrackbarPos("Sat Max", "TrackBar")
val_min = cv2.getTrackbarPos("Val Min", "TrackBar")
val_max = cv2.getTrackbarPos("Val Max", "TrackBar")

print(hue_min, hue_max, sat_min, sat_max, val_min, val_max)

lower = np.array([hue_min, sat_min, val_min])
upper = np.array([hue_max, sat_max, val_max])
mask = cv2.inRange(img_HSV, lower, upper)

img_result = cv2.bitwise_and(img, img, mask = mask)

cv2.imshow("Original image", img)
cv2.imshow("HSV image", img_HSV)
cv2.imshow("Masked image", mask)
cv2.imshow("Resulting image", img_result)

if cv2.waitKey(1) & 0xFF == ord('q'):
        break
