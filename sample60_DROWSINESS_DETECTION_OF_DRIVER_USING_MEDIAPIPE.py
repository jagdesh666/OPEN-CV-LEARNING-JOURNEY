import cv2
import mediapipe as mp
import math
import pygame
import os

pygame.mixer.init()

script_dir = os.path.dirname(os.path.abspath(__file__))
alarm_file_wav = os.path.join(script_dir, "alarm.wav")
alarm_file_mp3 = os.path.join(script_dir, "alarm.mp3")

if os.path.exists(alarm_file_wav):
    alarm_path = alarm_file_wav
elif os.path.exists(alarm_file_mp3):
    alarm_path = alarm_file_mp3
else:
    raise FileNotFoundError("FILE NOT FOUND")

pygame.mixer.music.load(alarm_path)

def euclidean_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True
)
mp_draw = mp.solutions.drawing_utils

LEFT_EYE_IDX = [33, 160, 158, 133, 153, 144]
RIGHT_EYE_IDX = [362, 385, 387, 263, 373, 380]

cap = cv2.VideoCapture(0)

alarm_on = False
EAR_THRESHOLD = 0.20

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:

            left_eye_points = []
            for idx in LEFT_EYE_IDX:
                point = face_landmarks.landmark[idx]
                h, w, _ = frame.shape
                x, y = int(point.x * w), int(point.y * h)
                left_eye_points.append((x, y))
                cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)

            right_eye_points = []
            for idx in RIGHT_EYE_IDX:
                point = face_landmarks.landmark[idx]
                h, w, _ = frame.shape
                x, y = int(point.x * w), int(point.y * h)
                right_eye_points.append((x, y))
                cv2.circle(frame, (x, y), 3, (0, 0, 255), -1)

            p1, p2, p3, p4, p5, p6 = left_eye_points
            vertical1 = euclidean_distance(p2, p6)
            vertical2 = euclidean_distance(p3, p5)
            horizontal = euclidean_distance(p1, p4)
            EAR_left = (vertical1 + vertical2) / (2.0 * horizontal)

            p1, p2, p3, p4, p5, p6 = right_eye_points
            vertical1 = euclidean_distance(p2, p6)
            vertical2 = euclidean_distance(p3, p5)
            horizontal = euclidean_distance(p1, p4)
            EAR_right = (vertical1 + vertical2) / (2.0 * horizontal)

            EAR = (EAR_left + EAR_right) / 2.0
            cv2.putText(frame, f"EAR: {EAR:.2f}", (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            if EAR < EAR_THRESHOLD:
                cv2.putText(frame, "ALERT! DROWSINESS DETECTED", (30, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                if not alarm_on:
                    pygame.mixer.music.play(-1)
                    alarm_on = True
            else:
                if alarm_on:
                    pygame.mixer.music.stop()
                    alarm_on = False

    cv2.imshow("MEDIAPIPE FACEMESH", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
