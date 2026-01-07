import cv2

image = cv2.imread('chess.jpg')
image = cv2.resize(image, (640, 700))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


dst = cv2.cornerHarris(gray, 5, 3, 0.04)
dst = cv2.dilate(dst, None)

image[dst > 0.05 * dst.max()] = [0, 255, 0]
cv2.imshow('dst', image)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
q
