import numpy as np
import cv2
image = cv2.imread('smarties1.jpg')
output = image.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=20,param1=50, param2=30, minRadius=0, maxRadius=0)


detected_circles = np.uint16(np.around(circles))
for (x,y,r) in detected_circles[0, :]:
    cv2.circle(output, (x, y), r, (0, 255, 0), 2)
    cv2.circle(output, (x, y), 2, (0, 0, 0), 2)


cv2.imshow('output', output)
cv2.waitKey(0)
cv2.destroyAllWindows()