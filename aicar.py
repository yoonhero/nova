import matplotlib.pylab as plt
import cv2
import numpy as np
import math
from object_detection.main import ObjectDetection
from lane_detection.lane_detection import LaneDetection
import time

WIDTH = 640
HEIGHT = 320

object_detection = ObjectDetection(WIDTH, HEIGHT)
lane_detect = LaneDetection()

cap = cv2.VideoCapture("./dataset/lane_detection_1.mp4")
# cap.set(cv2.CAP_PROP_FPS, 10)
prevTime = 0
while True:
    # 웹캠 프레임

    ret, frame = cap.read()
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    h, w, c = frame.shape
    if ret:
        image_with_lines = lane_detect.detect(frame, advance_view=True)

        image_with_detection, stop, _ = object_detection.process(image_with_lines)
        
        curTime = time.time()
        sec = curTime - prevTime
        prevTime = curTime
        fps = 1/(sec)
        fps_text = "FPS : %0.1f" % fps
        cv2.putText(image_with_detection, fps_text, (0, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


        cv2.imshow('result', image_with_detection)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

    if cv2.waitKey(100) > 0:
        break

cap.release()
cv2.destroyAllWindows()
