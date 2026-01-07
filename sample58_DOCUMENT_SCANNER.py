import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if frame is None:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)

    contours, _ = cv2.findContours(canny, 1, 2)
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
    


    cv2.imshow('blue', canny)


    cv2.imshow('original frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
