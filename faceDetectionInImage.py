import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

im = cv2.imread("face.jpeg", cv2.IMREAD_COLOR)
print("Shape", im.shape)
# im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
# cv2.imshow("Image",im)
# cv2.waitKey()


faces = face_cascade.detectMultiScale(im,1.3,5)
print("Face Coordinates (x,y,w,h)" , faces)

while True:

    for face in faces:
        x,y,w,h = face
        cv2.rectangle(im, (x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow("image",im)
   
    key = cv2.waitKey(3000)
    if key & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()



