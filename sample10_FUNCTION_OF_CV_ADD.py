import numpy as np
import cv2

img1 = cv2.imread('image1.jpg')
img2 = cv2.imread('image2.jpg')

img1 = cv2.resize(img1, (512, 512))
img2 = cv2.resize(img2, (512, 512))

result = cv2.add(img1, img2)

cv2.imshow('Result Image',result)
cv2.waitKey(0)
cv2.destroyAllWindows()
