import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)



def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,' ',y)
        strXY = str(x) + ',' + str(y)
        cv2.putText(img, strXY, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3 )
        cv2.imshow('image',img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        print(blue,green,red)
        strBGR = str(blue) + ',' + str(green) + ',' + str(red)
        cv2.putText(img, strBGR, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        cv2.imshow('image', img)




img = cv2.imread('image1.jpg')
cv2.imshow('image',img)


cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()