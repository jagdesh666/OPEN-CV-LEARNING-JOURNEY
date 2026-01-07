import numpy as np
import cv2

def nothing(x):
    print(x)


img = cv2.imread('image1.jpg')
cv2.namedWindow('image')
cv2.createTrackbar('CURRENT_POSITION', 'image', 10, 400, nothing)


switch = 'color/gray'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)


while(1):
    img_copy = img.copy()

    position = cv2.getTrackbarPos('CURRENT_POSITION', 'image')
    cv2.putText(img_copy, str(position), (50, 250), cv2.FONT_HERSHEY_SIMPLEX,
                3, (0, 0, 255), 3)

    switch_position = cv2.getTrackbarPos(switch, 'image')

    print('BEFORE COLOR IMAGE: \n')

    if switch_position == 1:
        img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
        img_copy = cv2.cvtColor(img_copy, cv2.COLOR_GRAY2BGR)
        print('BEFORE GRAY SCALE IMAGE: \n')



    cv2.imshow('image', img_copy)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break





cv2.waitKey(0)
cv2.destroyWindow('image')



