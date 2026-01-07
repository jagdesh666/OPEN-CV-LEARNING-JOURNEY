import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)



def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        my_color_image = np.zeros((512, 512, 3), np.uint8)
        my_color_image[:] = [blue, green, red]

        cv2.imshow('color',my_color_image)



img = cv2.imread('image1.jpg')
cv2.imshow('image',img)


cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()