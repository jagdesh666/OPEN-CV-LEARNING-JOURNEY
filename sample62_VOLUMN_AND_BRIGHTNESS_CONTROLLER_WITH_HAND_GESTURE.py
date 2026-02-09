import cv2
import mediapipe as mp
import math
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc


devices = AudioUtilities.GetSpeakers()
interface = (
        devices.Activate
            (
                IAudioEndpointVolume._iid_, CLSCTX_ALL, None
            )
)
volume = cast(interface, POINTER(IAudioEndpointVolume))
vol_min, vol_max = volume.GetVolumeRange()[:2]


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

def distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

def clamp(val, min_val, max_val):
    return max(min_val, min(val, max_val))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_lms, hand_info in zip(
            results.multi_hand_landmarks,
            results.multi_handedness
        ):
            label = hand_info.classification[0].label

            thumb = hand_lms.landmark[4]
            index = hand_lms.landmark[8]

            tx, ty = int(thumb.x * w), int(thumb.y * h)
            ix, iy = int(index.x * w), int(index.y * h)

            dist = distance((tx, ty), (ix, iy))
            dist = clamp(dist, 30, 200)

            if label == "Left":
                vol = (dist - 30) / (200 - 30)
                vol_db = vol * (vol_max - vol_min) + vol_min
                volume.SetMasterVolumeLevel(vol_db, None)

                cv2.putText(frame, f"VOLUMN: {int(vol*100)}%",
                            (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2)

            else:
                bright = int((dist - 30) / (200 - 30) * 100)
                bright = clamp(bright, 0, 100)
                sbc.set_brightness(bright)

                cv2.putText(frame, f"BRIGHTNESS: {bright}%",
                            (10, 80), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 255, 0), 2)


            cv2.circle(frame, (tx, ty), 8, (255, 0, 0), -1)
            cv2.circle(frame, (ix, iy), 8, (0, 255, 0), -1)
            cv2.line(frame, (tx, ty), (ix, iy), (255, 255, 255), 2)
            mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("BRIGHTNESS AND VOLUMN CONTROLLER", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()
