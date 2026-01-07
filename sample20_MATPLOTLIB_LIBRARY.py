import cv2
from matplotlib import pyplot as plt

img = cv2.imread('image1.jpg',-1)
cv2.imshow('original image', img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()