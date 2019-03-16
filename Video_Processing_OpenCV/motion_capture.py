import cv2
import time
import pandas
from datetime import datetime


video = cv2.VideoCapture(0)
first_check, first_frame = video.read()
first_frame = cv2.cvtColor(first_frame, cv2.COLOR_RGB2GRAY)

times = []
last_status = 0

while True:
    status = 0
    check, frame = video.read()
    img_grey = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    img_grey = cv2.GaussianBlur(img_grey, (21, 21), 0)

    delta_frame = cv2.absdiff(first_frame, img_grey)
    thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta, None, iterations=2)

    (cnts,_) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 5000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0))
        status = 1
    if status != last_status:
        times.append(datetime.now())
    last_status = status
    cv2.imshow("test", frame)

    cv2.imshow("grau", img_grey)
    cv2.imshow("delta_frame", thresh_delta)
    key = cv2.waitKey(41)
    if key == ord('q'):
        times.append(datetime.now())
        break

times_df = pandas.DataFrame(columns=['Start', 'End'])
stepper = 2
for i in range(0, len(times), stepper):
    times_df = times_df.append({'Start':times[i], 'End':times[i+1]}, ignore_index=True)
print(times_df)
video.release()
cv2.destroyAllWindows
