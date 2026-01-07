import cv2
import numpy as np

img = cv2.imread('shapes.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0,0,0), 2)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx) == 3:
        cv2.putText(img, "TRINGLE", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

    elif len(approx) == 4:
        x,y,w,h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv2.putText(img, "SQUARE", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
        else:
            cv2.putText(img, "RECTANGLE", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

    elif len(approx) == 5:
        cv2.putText(img, "PENTAGON", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

    elif len(approx) == 10:
        cv2.putText(img, "STAR", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

    else:
        cv2.putText(img, "CIRCLE", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)


cv2.imshow('gray', gray)
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()