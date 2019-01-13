import cv2

captured = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")



while True:
    returned , frame = captured.read()
    if not returned:
        continue

    faces = face_cascade.detectMultiScale(frame,1.3,5)
    print(faces)
    for face in faces:
        x,y,w,h = face

        cv2.rectangle(frame,(x,y), (x+w,y+h),(0,0,255),2)

        # face_only = frame[y:y+h,x+w]
        # cv2.imshow("Face Capture" , face_only)
    cv2.imshow("Feed",frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
captured.release()
cv2.destroyAllWindows()
    
