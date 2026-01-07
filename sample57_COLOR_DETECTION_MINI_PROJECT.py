import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    if frame is None:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100,150,0])
    upper_blue = np.array([130,255,255])

    lower_red1 = np.array([0,150,50])
    upper_red1 = np.array([10,255,255])

    lower_red2 = np.array([170, 150, 50])
    upper_red2 = np.array([180, 255, 255])


    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)



    contours1, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours1:
        largest_contour = max(contours1, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(largest_contour)

        if radius > 10:
            center = (int(x), int(y))
            radius = int(radius)
            cv2.circle(frame, center, radius, (255, 0, 0), 2)
            cv2.putText(frame, "BLUE LIGHT", (center[0] - 40, center[1] - radius - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)



    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours_red:
        largest_contour = max(contours_red, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(largest_contour)
        if radius > 10:
            center = (int(x), int(y))
            radius = int(radius)
            cv2.circle(frame, center, radius, (255, 0, 0), 2)
            cv2.putText(frame, "RED LIGHT", (center[0] - 40, center[1] - radius - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2 )



    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask_blue)
    cv2.imshow('mask_red',mask_red)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
