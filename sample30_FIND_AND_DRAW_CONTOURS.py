import cv2


img = cv2.imread('opencv_logo.png', cv2.IMREAD_COLOR)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgGray, 127, 255, 0)
contuors, hirarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print('NUMBER OF CONTOURS: ',str(len(contuors)))

cv2.drawContours(img, contuors, -1, (255, 0, 255), 2)


cv2.imshow('original image', img)
cv2.imshow('grayscale image', imgGray)

cv2.waitKey(0)
cv2.destroyAllWindows()
