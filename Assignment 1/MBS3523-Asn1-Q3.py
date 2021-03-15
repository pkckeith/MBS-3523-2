import cv2
import numpy as np
print(cv2.__version__)
from random import randint

car_classifier = cv2.CascadeClassifier('Resources/haarcascade_car.xml')
body_classifier = cv2.CascadeClassifier('Resources/haarcascade_fullbody.xml')
capture = cv2.VideoCapture('Resources/cars.mp4')

# Start capturing and show frames on window named 'Frame'
while True:
    success, img = capture.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_classifier.detectMultiScale(imgGray, 1.4, 2)
    bodies = body_classifier.detectMultiScale(imgGray, 1.2, 3)

    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (randint(0,255), randint(0,255), randint(0,255)), 2)

    cv2.imshow('Cars', img)

    for (x, y, w, h) in bodies:
        cv2.rectangle(img, (x, y), (x + w, y + h), (randint(0,255), randint(0,255), randint(0,255)), 2)
    cv2.imshow('Pedestrian', img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()