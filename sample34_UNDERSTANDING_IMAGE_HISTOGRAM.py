import cv2
import matplotlib.pyplot as plt

image = cv2.imread('image1.jpg', 1)

b,g,r = cv2.split(image)

cv2.imshow('image', image)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)




plt.hist(image.ravel(), 256, range=[0, 256])
plt.hist(b.ravel(), 256, range=[0, 256])
plt.hist(g.ravel(), 256, range=[0, 256])
plt.hist(r.ravel(), 256, range=[0, 256])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
