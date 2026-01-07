import numpy as np
import cv2

img1 = np.zeros((512, 512, 3), np.uint8)
cv2.rectangle(img1, (100, 100), (200, 200), (255, 255, 255), -1)

img2 = cv2.imread('image1.jpg')
img2 = cv2.resize(img2, (512, 512))


bit_and = cv2.bitwise_and(img1, img2)
bit_or = cv2.bitwise_or(img1, img2)
bit_xor = cv2.bitwise_xor(img1, img2)
bit_not1 = cv2.bitwise_not(img1)
bit_not2 = cv2.bitwise_not(img2)




cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('bit_and', bit_and)
cv2.imshow('bit_or', bit_or)
cv2.imshow('bit_xor', bit_xor)
cv2.imshow('bit_not1', bit_not1)
cv2.imshow('bit_not2', bit_not2)



cv2.waitKey(0)
cv2.destroyAllWindows()
