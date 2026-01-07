import cv2
import numpy as np

cap = cv2.VideoCapture('slow_traffic.mp4')

# take first frame of the video
ret, frame = cap.read()
if not ret or frame is None:
    print("Error loading video.")
    cap.release()
    exit()

# setup initial location of window dynamically
frame_height, frame_width = frame.shape[:2]
x, y, width, height = 300, 200, frame_width - 200, frame_height - 200
track_window = (x, y, width, height)

# set up the ROI for tracking
roi = frame[y:y+height, x:x+width]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# mask and histogram of the object
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# setup termination criteria
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret or frame is None:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    ret, track_window = cv2.meanShift(dst, track_window, term_crit)

    x, y, w, h = track_window
    final_image = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Back Projection', dst)
    cv2.imshow('Tracking', final_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
