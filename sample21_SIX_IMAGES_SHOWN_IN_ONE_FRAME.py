import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image3.png', 0)
ret, th1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, th3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, th4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, th5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

titles = ['original image', 'binary', 'binary inverted', 'truncated', 'to_zero', 'to_zero inverted']
imgs = [img, th1, th2, th3, th4, th5]


for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.title(titles[i])
    plt.imshow(imgs[i], cmap='gray')
    plt.xticks([]), plt.yticks([])

plt.show()