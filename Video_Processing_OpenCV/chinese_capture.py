import cv2
import time

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('Video_Processing_OpenCV/haarcascade_frontalface_default.xml')


while True:
    check, frame = video.read()
    img_grey = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(img_grey, scaleFactor=1.1, minNeighbors=5)
    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0))
    cv2.imshow("test", frame)
    key = cv2.waitKey(41)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows
