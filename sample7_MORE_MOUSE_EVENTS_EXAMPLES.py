import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)



def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 5, (0, 0, 255), -1)
        points.append((x,y))

        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (0, 0, 255), 2)

        cv2.imshow('image',img)



points = []
img = cv2.imread('image1.jpg')
cv2.imshow('image',img)


cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()