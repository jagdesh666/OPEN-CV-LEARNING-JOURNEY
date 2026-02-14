import cv2
import mediapipe as mp
import numpy as np
import math

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    static_image_mode=False,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture("v2.mp4")

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0])
    angle = abs(radians*180.0/math.pi)
    if angle>180:
        angle=360-angle
    return angle

stages = {"squat": "up", "pushup": "up"}
counters = {"squat": 0, "pushup": 0}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = pose.process(rgb)

    if results.pose_landmarks:
        mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        lm = results.pose_landmarks.landmark

        hip = [lm[mp_pose.PoseLandmark.LEFT_HIP.value].x*w,
               lm[mp_pose.PoseLandmark.LEFT_HIP.value].y*h]

        knee = [lm[mp_pose.PoseLandmark.LEFT_KNEE.value].x*w,
                lm[mp_pose.PoseLandmark.LEFT_KNEE.value].y*h]

        ankle = [lm[mp_pose.PoseLandmark.LEFT_ANKLE.value].x*w,
                 lm[mp_pose.PoseLandmark.LEFT_ANKLE.value].y*h]

        knee_angle = calculate_angle(hip, knee, ankle)

        if knee_angle<90:
            stages["squat"]="down"
        if knee_angle>160 and stages["squat"]=="down":
            stages["squat"]="up"
            counters["squat"] += 1

        squat_feedback = ""
        if knee_angle<70:
            squat_feedback="go lower"
        elif knee_angle>160:
            squat_feedback = "stand straight"

        shoulder = [lm[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x*w,
                    lm[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y*h]

        elbow = [lm[mp_pose.PoseLandmark.LEFT_ELBOW.value].x*w,
                 lm[mp_pose.PoseLandmark.LEFT_ELBOW.value].y*h]

        wrist = [lm[mp_pose.PoseLandmark.LEFT_WRIST.value].x*w,
                 lm[mp_pose.PoseLandmark.LEFT_WRIST.value].y*h]

        elbow_angle = calculate_angle(shoulder, elbow, wrist)

        if elbow_angle<70:
            stages["pushup"]="down"
        if elbow_angle>160 and stages["pushup"]=="down":
            stages["pushup"]="up"
            counters["pushup"] += 1

        pushup_feedback = ""
        if elbow_angle<50:
            pushup_feedback="Go lower!"
        elif elbow_angle>160:
            pushup_feedback="Elbows straight!"


        cv2.putText(frame, f"squats: {counters['squat']}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

        cv2.putText(frame, squat_feedback, (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

        cv2.putText(frame, f"pushups: {counters['pushup']}", (10, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

        cv2.putText(frame, pushup_feedback, (10, 130),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    cv2.imshow("AI FITNESS TRAINER", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
