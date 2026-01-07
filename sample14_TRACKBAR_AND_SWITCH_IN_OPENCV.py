import numpy as np
import cv2

def nothing(x):
    print(x)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')


switch = '0 : OFF\n 1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)


cv2.createTrackbar('BLUE', 'image', 0, 255, nothing)
cv2.createTrackbar('GREEN', 'image', 0, 255, nothing)
cv2.createTrackbar('RED', 'image', 0, 255, nothing)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF

    if k == 27:
        break

    b = cv2.getTrackbarPos('BLUE', 'image')
    g = cv2.getTrackbarPos('GREEN', 'image')
    r = cv2.getTrackbarPos('RED', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = [0]
    else:
        img[:] = [b, g, r]



cv2.destroyAllWindows()
