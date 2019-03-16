import cv2


face_cascade = cv2.CascadeClassifier('Video_Processing_OpenCV/haarcascade_frontalface_default.xml')

img = cv2.imread('Video_Processing_OpenCV/news.jpg')
img_grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

faces = face_cascade.detectMultiScale(img_grey, scaleFactor=1.1, minNeighbors=5)
print(faces)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 10)

cv2.imshow("Gsicht", img)
cv2.waitKey(0)
