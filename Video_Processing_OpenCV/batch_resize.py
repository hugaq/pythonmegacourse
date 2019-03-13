import glob
import cv2
import os


for i in glob.glob('Video_Processing_OpenCV/sample-images/*'):
    tmp = cv2.imread(i, 0)
    tmp_resized = cv2.resize(tmp, (100, 100))
    name = os.path.join('Video_Processing_OpenCV/resized-images', os.path.split(i)[1])
    cv2.imwrite(name, tmp_resized)
