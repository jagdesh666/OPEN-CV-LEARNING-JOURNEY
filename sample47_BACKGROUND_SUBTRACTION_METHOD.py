import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi.mp4')
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
while True:
    ret, frame = cap.read()
    if frame is None:
        break

    frame = cv2.resize(frame, (640, 480))

    fgmask = fgbg.apply(frame)


    cv2.imshow('fgmask', fgmask)
    cv2.imshow('frame', frame)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
