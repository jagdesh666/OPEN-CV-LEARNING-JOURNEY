import cv2
import numpy as np

image = cv2.imread('image4.png')
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(imageGray, 50, 150)
cv2.imshow('edges', edges)

lines = cv2.HoughLines(edges, 1, np.pi/180, 100)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho

    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('HOUGH LINE IMAGE', image)
cv2.imshow('imageGray', imageGray )
cv2.waitKey(0)
cv2.destroyAllWindows()