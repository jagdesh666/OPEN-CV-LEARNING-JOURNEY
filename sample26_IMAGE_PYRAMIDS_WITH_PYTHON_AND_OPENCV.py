import cv2
import numpy as np

img = cv2.imread('image1.jpg')

lower_resolution1 = cv2.pyrDown(img)
lower_resolution2 = cv2.pyrDown(lower_resolution1)
higher_resolution1 = cv2.pyrUp(img)
higher_resolution2 = cv2.pyrUp(lower_resolution2)


cv2.imshow('image', img)
cv2.imshow('lower_resolution1', lower_resolution1)
cv2.imshow('lower_resolution2', lower_resolution2)
cv2.imshow('higher_resolution1', higher_resolution1)
cv2.imshow('higher_resolution2', higher_resolution2)


cv2.waitKey(0)
cv2.destroyAllWindows()
