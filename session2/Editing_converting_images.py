import cv2
import numpy as np


img = cv2.imread ('Resources/lena.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   #convert to gray scale
img_blur = cv2.GaussianBlur(img, (7,7), 0)         #convert to blur
img_canny = cv2.Canny(img, 100, 100)               #convert to canny

print (img.shape)
print (img_gray.shape)
print (img_blur.shape)
print (img_canny.shape)

cv2.imshow ('Color', img)
cv2.imshow ('Gray', img_gray)
cv2.imshow ('Blur', img_blur)
cv2.imshow ('Canny', img_canny)

cv2.waitKey (0)










#convert to gray scale

# img = cv2.imread ('Resources/lena.png')
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print (img.shape)
# print (img_gray.shape)
# cv2.imshow ('Color', img)
# cv2.imshow ('Gray', img_gray)
# cv2.waitKey (0)


# #convert to blur

# img = cv2.imread ('Resources/lena.png')
# img_blur = cv2.GaussianBlur(img, (7,7), 0)
# print (img.shape)
# print (img_blur.shape)
# cv2.imshow ('Color', img)
# cv2.imshow ('Blur', img_blur)
# cv2.waitKey (0)


#convert to canny image

# img = cv2.imread ('Resources/lena.png')
# img_canny = cv2.Canny(img, 100, 100)
# print (img.shape)
# print (img_canny.shape)
# cv2.imshow ('Color', img)
# cv2.imshow ('Canny', img_canny)
# cv2.waitKey (0)


#convert to dilation

# kernel = np.ones ((5,5), np.uint8)
# print (kernel)
# img = cv2.imread ('Resources/lena.png')
# img_dilation = cv2.dilate (img, kernel, iterations=1)
# print (img.shape)
# print (img_dilation.shape)
# cv2.imshow ('Color', img)
# cv2.imshow ('Dilated', img_dilation)
# cv2.waitKey(0)


#convert to erode

# kernel = np.ones ((5,5), np.uint8)
# print (kernel)
# img = cv2.imread ('Resources/lena.png')
# img_erode = cv2.erode (img, kernel, iterations=2)
# print (img.shape)
# print (img_erode.shape)
# cv2.imshow ('Color', img)
# cv2.imshow ('Eroded', img_erode)
# cv2.waitKey(0)
