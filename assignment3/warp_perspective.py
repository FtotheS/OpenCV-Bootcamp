#Apply warp perspective to the docs images inside Resources

import cv2
import numpy as np

width , height = 500, 700

img = cv2.imread("Resources/docs.jpg")

pts1 = np.float32([[720,24],[1110,17],[746,560],[1220,547]])
pts2 = np.float32([[0,0], [width,0], [0,height], [width,height]])

metrix = cv2.getPerspectiveTransform(pts1,pts2)
img_out = cv2.warpPerspective(img, metrix, (width,height))

cv2.imshow('docs', img)
cv2.imshow('docs_warp', img_out)

cv2.waitKey(0)
