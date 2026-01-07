import cv2
import numpy as np

# Load the video file
cap = cv2.VideoCapture('slow_traffic.mp4')

# Read the first frame from the video
ret, frame = cap.read()
if not ret or frame is None:
    print("Error loading video.")
    cap.release()
    exit()

# Get the frame dimensions
frame_height, frame_width = frame.shape[:2]

# Set initial tracking window (adjust as needed)
x, y, width, height = 300, 200, frame_width - 200, frame_height - 200
track_window = (x, y, width, height)

# Set up Region of Interest (ROI) for tracking
roi = frame[y:y+height, x:x+width]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# Create a mask to filter out low-saturation and low-value pixels
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))

# Calculate histogram of the ROI
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# Setup termination criteria: either 10 iterations or at least 1 point movement
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

# Start tracking loop
while cap.isOpened():
    ret, frame = cap.read()
    if not ret or frame is None:
        break

    # Convert current frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Calculate back projection using the histogram
    dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    # Apply CamShift to get the new location
    ret, track_window = cv2.CamShift(dst, track_window, term_crit)

    # Get rotated rectangle points & draw the tracking box
    pts = cv2.boxPoints(ret)
    pts = pts.astype(np.int32)  # ← fixed line
    final_image = cv2.polylines(frame, [pts], True, (255, 0, 0), 2)

    # Show the result
    cv2.imshow('Back Projection', dst)
    cv2.imshow('Tracking', final_image)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
