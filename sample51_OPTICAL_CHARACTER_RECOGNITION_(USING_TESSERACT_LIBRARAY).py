import cv2
import pytesseract

image = cv2.imread('image7.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray, lang='eng')

print(text)


cv2.waitKey(0)
cv2.destroyAllWindows()
