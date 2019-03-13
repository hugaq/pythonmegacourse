import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('Video_Processing_OpenCV/photo.jpg')
img_grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
