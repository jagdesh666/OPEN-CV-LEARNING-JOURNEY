import cv2

img = cv2.imread('image1.jpg', 0)
print(img)

cv2.imshow('image', img)

x = cv2.waitKey(0)

if x == 27:
    cv2.destroyAllWindows()
elif x == ord('s'):
    cv2.imwrite('image2_copy.jpg', img)
    cv2.destroyAllWindows()






