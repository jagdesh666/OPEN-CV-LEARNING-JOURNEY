import cv2

image = cv2.imread('image6.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)

for i in corners:
    x, y = i.ravel()
    cv2.circle(image, (int(x), int(y)), 5, (0, 0, 255), -1)

cv2.imshow('image', image)
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
