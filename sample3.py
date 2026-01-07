import numpy as np
import cv2


img = cv2.imread('image1.jpg', 1)

#============
# for black image
img1 = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
cv2.imshow('image', img1)
#============


img = cv2.line(img, (0,0), (255,255), (0,0,255), 10)

img = cv2.arrowedLine(img, (0,255), (255,255), (0,0,255), 10)

img = cv2.rectangle(img, (384,0), (510,128), (255,255), 10)

img = cv2.circle(img,(510,128), 63, (0,0,255), 10)


#to put the text on the image

img = cv2.putText(img, 'JAGDESH', (150,350), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 5, cv2.LINE_AA)


cv2.imshow('image1', img)

cv2.waitKey(0)
cv2.destroyAllWindows()