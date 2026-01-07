import cv2
import numpy as np

# Start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

# Create a blank canvas ONCE (not inside the loop)
canvas = np.zeros((480, 640, 3), dtype=np.uint8)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    #frame = cv2.flip(frame, 1)  # Mirror effect

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define blue color range in HSV
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Get largest contour
        largest = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest)
        if area > 1000:
            # Get center of contour
            M = cv2.moments(largest)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                # Draw on canvas (persistent)
                cv2.circle(canvas, (cx, cy), 10, (255, 0, 0), -1)

    # Combine canvas and webcam frame
    combined = cv2.addWeighted(frame, 1, canvas, 1, 0)

    cv2.imshow("Virtual Painter", combined)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('c'):
        # Clear the canvas when 'c' is pressed
        canvas[:] = 0

cap.release()
cv2.destroyAllWindows()
