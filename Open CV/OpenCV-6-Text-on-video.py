# Save this file as OpenCV-6-Text-on-video.py

import cv2
#import numpy as np
print(cv2.__version__)

# Capture a video file
capture = cv2.VideoCapture('Resources/dog.mp4')

# Select font
font = cv2.FONT_HERSHEY_SIMPLEX

# Start capturing and show frames on window named 'Frame'
while True:
    success, img = capture.read()

    # below line is to resize video image frame, uncomment if you want to resize
    img = cv2.resize(img, (int(img.shape[1] / 1.5), int(img.shape[0] / 1.5)))

    # Put a red text on img
    cv2.putText(img, 'I am a cute dog!', (10, 400), font, 3, (0, 0, 255), 5)

    cv2.imshow('Frame', img)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()