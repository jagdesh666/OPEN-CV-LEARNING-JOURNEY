import cv2

face_casecade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('group_photo.jpeg')
image = cv2.resize(image, (640,700))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_casecade.detectMultiScale(gray, 1.3, 5)


for (x,y,w,h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 6)






cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()