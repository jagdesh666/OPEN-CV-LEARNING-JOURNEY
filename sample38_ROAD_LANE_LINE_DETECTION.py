import cv2
import numpy as np
import matplotlib.pyplot as plt

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255
    vertices = np.array([vertices], dtype=np.int32)
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_the_lines(image, lines):
    blank_image = np.zeros_like(image)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), 5)
    img_with_lines = cv2.addWeighted(image, 0.8, blank_image, 1, 0)
    return img_with_lines

image = cv2.imread('road.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height = image.shape[0]
width = image.shape[1]

region_of_interest_vertices = [
    (0, height),
    (width/2, height/2),
    (width, height)
]

grey_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
canny_edges = cv2.Canny(grey_image, 50, 150)
cropped_image = region_of_interest(canny_edges, region_of_interest_vertices)

lines = cv2.HoughLinesP(cropped_image, 1, np.pi/180, 100, minLineLength=10, maxLineGap=10)

if lines is not None:
    image_with_lines = draw_the_lines(image, lines)
else:
    image_with_lines = image

plt.imshow(image_with_lines)
plt.show()
