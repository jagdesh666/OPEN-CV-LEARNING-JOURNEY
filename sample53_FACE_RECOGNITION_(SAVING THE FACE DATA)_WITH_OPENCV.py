import cv2
import numpy as np
import os

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

skip = 0
face_data = []
dataset_path = "./face_dataset/"

file_name = input("ENTER THE FILE NAME: ").strip()

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.2, minNeighbors=5)

    for (x, y, w, h) in faces:
        offset = 10
        x1 = max(x - offset, 0)
        y1 = max(y - offset, 0)
        x2 = min(x + w + offset, frame.shape[1])
        y2 = min(y + h + offset, frame.shape[0])

        face_section = frame[y1:y2, x1:x2]

        if face_section.size != 0:
            face_section = cv2.resize(face_section, (100, 100))

        if skip % 10 == 0:
            face_data.append(face_section)
            print(f"SAVED FACE: {len(face_data)}")

        skip = skip + 1

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow("FACE", face_section)

    cv2.imshow("FRAME", frame)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

face_data = np.asarray(face_data)
face_data = face_data.reshape((face_data.shape[0], -1))

if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

np.save(os.path.join(dataset_path, file_name + '.npy'), face_data)
print(f"DATA SAVED AT: {os.path.join(dataset_path, file_name + '.npy')}")

cap.release()
cv2.destroyAllWindows()
