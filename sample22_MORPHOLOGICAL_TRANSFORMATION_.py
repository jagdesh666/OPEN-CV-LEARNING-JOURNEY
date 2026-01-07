import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
ret, mask = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((2, 2), np.uint8)
dilation = cv2.dilate(mask,kernel,iterations = 1)
erosion = cv2.erode(mask,kernel,iterations = 1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
top_hat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)

titles = ['image', 'mask', 'dilation', 'erosion', 'openingban', 'closing', 'gradient', 'top_hat']
images = [img, mask, dilation, erosion, opening, closing, gradient, top_hat]


for i in range(8):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
