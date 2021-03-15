import cv2
#import numpy as np
print(cv2.__version__)
from random import randint

capture = cv2.VideoCapture(0)

capture.set(3,640) # 3 is the width of the frame
capture.set(4,480) # 4 is the height of the frame

x = 0
y = 0
dx = 2
dy = 2
# Start capturing and show frames on window named 'Frame'
while True:
    success, img = capture.read()
    cv2.rectangle(img, (x, y), (x + 50, y + 50), (randint(0,255), randint(0,255), randint(0,255)), 3)
    x = x + dx
    y = y + dy
    if x >= 590 or x <= 0:
        dx = dx * (-1)
    if y >= 430 or y <= 0:
        dy = dy  * (-1)

    cv2.imshow('Frame', img)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()