import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi.mp4')
fgbg = cv2.createBackgroundSubtractorKNN()

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    if frame is None:
        break

    fgmask = fgbg.apply(frame)


    cv2.imshow('image', frame)
    cv2.imshow('image', fgmask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()