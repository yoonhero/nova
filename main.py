from obstacle_detect.obstacle import ObstacleDetect
import io
import socket
import struct
from PIL import Image
import matplotlib.pyplot as pl
import cv2
import numpy as np
import time

server_socket = socket.socket()

ipAddress = "172.30.1.34"
portNum = 8000

server_socket.bind((ipAddress, portNum))
server_socket.listen(0)

# Object Detection Module
obstacle_detect = ObstacleDetect()


# Accept a single connection and make a file-like object out of it
connection = server_socket.accept()[0].makefile('rb')
try:
    img = None
    prevTime = 0
    while True:
        # Read the length of the image as a 32-bit unsigned int.
        image_len = struct.unpack(
            '<L', connection.read(struct.calcsize('<L')))[0]

        # if image is None break loop
        if not image_len:
            break

        # Construct a stream to hold the image data and read the image
        # data from the connection
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
        # Rewind the stream, open it as an image with PIL and do some
        # processing on it
        image_stream.seek(0)
        image = Image.open(image_stream)

        if img is None:
            img = pl.imshow(image)
        else:
            img.set_data(image)

        pl.pause(0.01)
        pl.draw()

        print('Image is %dx%d' % image.size)
        image.verify()
        print('Image is verified')

        curTime = time.time()

        # process the image
        convertedImg = image.convert("RGB")
        open_cv_image = np.array(convertedImg)
        # Convert RGB to BGR
        open_cv_image = open_cv_image[:, :, ::-1].copy()

        image_with_obstacle_detection, stop = obstacle_detect.recognize(
            open_cv_image)

        sec = curTime - prevTime
        prevTime = curTime
        fps = 1/(sec)
        fps_text = "FPS : %0.1f" % fps

        cv2.putText(image_with_obstacle_detection, fps_text, (0, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 5)
        cv2.imshow("Obstacle Detected Img", image_with_obstacle_detection)
        if stop:
            print("STOP!! Obstacle Detected")

finally:
    connection.close()
    server_socket.close()
