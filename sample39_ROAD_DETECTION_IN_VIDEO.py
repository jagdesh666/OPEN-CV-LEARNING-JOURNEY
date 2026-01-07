import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy import dtype


#=====================================================
def REGION_OF_INTEREST(frame1, roi_vertices):
    mask = np.zeros_like(frame1)
    match_mask_color = 255
    vertices = np.array([roi_vertices], dtype=np.int32)
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(frame1, mask)
    return masked_image




def draw_lines(cropped_image, line_parameters):
    black_frame = np.zeros_like(cropped_image)

    for line in line_parameters:
        x1, y1, x2, y2 = line[0]
        cv2.line(black_frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    img_with_lines = cv2.addWeighted(cropped_image, 0.8, black_frame, 1, 0)
    return img_with_lines





#======================================================








video_capture = cv2.VideoCapture('test.mp4')

if not video_capture.isOpened():
    print("cannot open video.")
    exit()
else:
    print("video opened.")
    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("can not read frame.")
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gaussian_blur = cv2.GaussianBlur(gray_frame, (5, 5), 0)

        canny_edges = cv2.Canny(gaussian_blur, 50, 150)


        height = frame.shape[0]
        width = frame.shape[1]

        RegionOfInterest_vertices = [
            (0, height),
            (width/2, height/2),
            (width, height),
        ]

        cropped_frame = REGION_OF_INTEREST(canny_edges,RegionOfInterest_vertices)


        lines = cv2.HoughLinesP(cropped_frame, 1, np.pi/180, 100, minLineLength=50, maxLineGap=10)

        if lines is not None:
            frame_with_lines = draw_lines(frame, lines)
        else:
            frame_with_lines = frame



        cv2.imshow('video frame', frame_with_lines)

        # Press 'q' to exit early
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

video_capture.release()
cv2.destroyAllWindows()
