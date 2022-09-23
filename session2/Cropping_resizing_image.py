# resizing an image

# import cv2
# img = cv2.imread ('Resources/lambo.png')
# print (img.shape)
# resized_img = cv2.resize (img, (360, 240))
# print (resized_img.shape)
# cv2.imshow ('Output', img)
# cv2.imshow ('Resized', resized_img)
# cv2.waitKey(0)


# cropping an image

import cv2
img = cv2.imread ('Resources/lambo.png')
cropped_img = img [0:200, 200:500]
cv2.imshow ('Output', img)
cv2.imshow ('Cropped', cropped_img)
cv2.waitKey (0)

