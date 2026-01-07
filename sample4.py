import cv2

cap = cv2.VideoCapture(0)

print('DEFAULT WIDTH: ',cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('DEFAULT HEIGHT: ',cap.get(cv2.CAP_PROP_FRAME_WIDTH))

cap.set(3, 1280)
cap.set(4, 720)

print('UPDATED WIDTH: ',cap.get(3))
print('UPDATED HEIGHT: ',cap.get(4))



while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()


