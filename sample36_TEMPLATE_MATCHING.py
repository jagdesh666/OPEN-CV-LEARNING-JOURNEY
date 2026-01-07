import numpy as np
import cv2

image = cv2.imread('messi.png')
image = cv2.resize(image, (600, 600))
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template = cv2.imread('messi_face.JPG', 0)

w, h = template.shape[::-1]

result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF)

threshold = 0.95
loc = np.where(result >= threshold)
print(loc)
for pt in zip(*loc[::-1]):
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    cv2.rectangle(image, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 2)

cv2.imshow('Result', image)
cv2.imshow('Template', template)
cv2.waitKey(0)
cv2.destroyAllWindows()
