import numpy as np

def distance(v1, v2):
    return np.sqrt(((v1 - v2) ** 2).sum())

def knn(train, test, k=5):
    dist = []
    for i in range(len(train)):
        ix = train[i][:-1]
        iy = train[i][-1]
        d = distance(test, ix)
        dist.append((d, iy))


    dist = sorted(dist)[:k]
    labels = [label for _, label in dist]

    output = max(set(labels), key=labels.count)
    return output




import cv2
import numpy as np
import os

dataset_path = "./face_dataset/"
face_data = []
labels = []
class_id = 0
names = {} 

for fx in os.listdir(dataset_path):
    if fx.endswith('.npy'):
        name = fx[:-4]
        print(f"Loading data for: {name}")
        data_item = np.load(os.path.join(dataset_path, fx))
        face_data.append(data_item)

        target = class_id * np.ones((data_item.shape[0],))
        labels.append(target)
        names[class_id] = name
        class_id += 1

face_dataset = np.concatenate(face_data, axis=0)
face_labels = np.concatenate(labels, axis=0).reshape((-1, 1))

trainset = np.concatenate((face_dataset, face_labels), axis=1)

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.2, minNeighbors=5)

    for (x, y, w, h) in faces:
        offset = 10
        offset = 10
        x1 = max(x - offset, 0)
        y1 = max(y - offset, 0)
        x2 = min(x + w + offset, frame.shape[1])
        y2 = min(y + h + offset, frame.shape[0])

        face_section = frame[y1:y2, x1:x2]

        if face_section.size == 0:
            continue  

        face_section = cv2.resize(face_section, (100, 100))

        face_flatten = face_section.flatten()


        predicted_id = knn(trainset, face_flatten)
        predicted_name = names[int(predicted_id)]

        cv2.putText(frame, predicted_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow("Face Recognition", frame)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
