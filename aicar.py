import matplotlib.pylab as plt
import cv2
import numpy as np
import math
from obstacle_detect import obstacle
from lane_detection import lane_detection
import time

# obstacle_detect = obstacle.ObstacleDetect()
lane_detect = lane_detection.Lane_Detection()

cap = cv2.VideoCapture(1)
# cap.set(cv2.CAP_PROP_FPS, 10)
prevTime = 0
while True:
    # 웹캠 프레임

    ret, frame = cap.read()

    h, w, c = frame.shape
    if ret:
        image_with_lines = lane_detect.detect(frame, advance_view=False)
        curTime = time.time()
        sec = curTime - prevTime
        prevTime = curTime
        fps = 1/(sec)
        fps_text = "FPS : %0.1f" % fps
        cv2.putText(image_with_lines, fps_text, (0, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 5)
        cv2.imshow('result', image_with_lines)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

    if cv2.waitKey(100) > 0:
        break

cap.release()
cv2.destroyAllWindows()
