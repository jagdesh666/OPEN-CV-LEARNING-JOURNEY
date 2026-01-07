import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("tracking")

cv2.createTrackbar('LH', 'tracking', 0, 255, nothing)
cv2.createTrackbar('LS', 'tracking', 0, 255, nothing)
cv2.createTrackbar('LV', 'tracking', 0, 255, nothing)


cv2.createTrackbar('UH', 'tracking', 255, 255, nothing)
cv2.createTrackbar('US', 'tracking', 255, 255, nothing)
cv2.createTrackbar('UV', 'tracking', 255, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        print("not reading from camera: ")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    l_h = cv2.getTrackbarPos('LH', 'tracking')
    l_s = cv2.getTrackbarPos('LS', 'tracking')
    l_v = cv2.getTrackbarPos('LV', 'tracking')
    u_h = cv2.getTrackbarPos('UH', 'tracking')
    u_s = cv2.getTrackbarPos('US', 'tracking')
    u_v = cv2.getTrackbarPos('UV', 'tracking')

    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])


    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    result = cv2.bitwise_and(frame, frame, mask=mask)


    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)


    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
