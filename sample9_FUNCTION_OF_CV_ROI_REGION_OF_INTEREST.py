import numpy as np
import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('clicked')
        print(x, y)
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        cv2.putText(img, str(x) + ', ' + str(y), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('image', img)


img = cv2.imread('image1.jpg')
print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge([b,g,r])

cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)


img2 = cv2.imread('image1.jpg')
face = img2[18:276, 232:276]
img2[52:52 + face.shape[0], 62:62 + face.shape[1]] = face
cv2.imshow('image1',img2)




cv2.waitKey(0)
cv2.destroyAllWindows()