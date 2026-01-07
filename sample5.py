import datetime
import cv2

cap = cv2.VideoCapture(0)

print('DEFAULT WIDTH: ',cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('DEFAULT HEIGHT: ',cap.get(cv2.CAP_PROP_FRAME_WIDTH))


while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        text = 'WIDTH: ' + str(cap.get(3)) + ' HEIGHT: ' + str(cap.get(4))
        frame = cv2.putText(frame,text, (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA )

        #get current date
        #============================================================================================================================
        current_date_time = str(datetime.datetime.now())
        frame = cv2.putText(frame, current_date_time, (20,80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA )
        # ============================================================================================================================

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()


