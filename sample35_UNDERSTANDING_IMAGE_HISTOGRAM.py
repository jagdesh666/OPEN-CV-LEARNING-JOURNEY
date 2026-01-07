import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('image1.jpg')

hist = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
