import numpy as np
import cv2
import os

def distance(a, b):
    return np.sqrt(((a-b)**2).sum())


def knn(train, test, k=5):
    dist = []

    for i in range(len(train)):
        x = train[i][:-1]  # features
        y = train[i][-1]   # label
        d = distance(test, x)
        dist.append((d, y))  # ✅ fixed: one argument, a tuple

    dist = sorted(dist, key=lambda x: x[0])  # sort by distance
    top_k = dist[:k]
    labels = [label for _, label in top_k]
    output = max(set(labels), key=labels.count)
    return output





face_data = []
labels = []
class_id = 0
class_id_to_name = {}

dataset_path = "./face_dataset/"


for fname in os.listdir(dataset_path):
    if fname.endswith(".npy"):
        name = fname[:-4]

        print("LOADING FILE: ",fname)

        data_item = np.load(os.path.join(dataset_path, fname))
        face_data.append(data_item)

        label_item = class_id * np.ones((data_item.shape[0]))
        labels.append(label_item)

        class_id_to_name[class_id] = name

        class_id = class_id + 1

X = np.concatenate(face_data, axis=0)
Y = np.concatenate(labels, axis=0).reshape(-1, 1)
training_set = np.concatenate((X, Y), axis=1)


print("TRAINING SET SHAPE: ", training_set.shape)
print("DATA SHAPE: ", X.shape)
print("LABELS SHAPE: ", Y.shape)
print("CLASS ID TO NAME MAPPING: ", class_id_to_name)





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
            continue  # skip if cropped face is empty

        face_section = cv2.resize(face_section, (100, 100))

        face_flatten = face_section.flatten()

        # Predict the name
        predicted_id = knn(training_set, face_flatten)
        predicted_name = class_id_to_name[int(predicted_id)]


        # Draw on frame
        cv2.putText(frame, predicted_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow("Face Recognition", frame)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
