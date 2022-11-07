# reading an image

# import cv2
# img = cv2.imread ('Resources/lambo.png')
# print (img.shape)
# cv2.imshow ('Output', img)
# cv2.waitKey (0)


# reading a video

import cv2
cap = cv2.VideoCapture ('Resources/elon.mp4')
while True:
    success, img = cap.read()
    print (img.shape)
    cv2.imshow ('Output', img)
    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break

# reading the webcam

# import cv2
# cap = cv2.VideoCapture (0) #default webcam
# cap.set (3, 1280)
# cap.set (4, 720)
# while True:
#     success, img = cap.read()
#     print (img.shape)
#     cv2.imshow ('Output', img)
#     if cv2.waitKey(1) & 0xFF == ord ('q'):
#         break

