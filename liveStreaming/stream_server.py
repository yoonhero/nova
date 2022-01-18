from obstacle_detect import ObstacleDetect
import io
import socket
import struct
from PIL import Image
import matplotlib.pyplot as pl
import sys
sys.path.append(
    "/Users/yoonseonghyeon/Desktop/YSH/programming/python/OurAICar")

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

        ################################################################ WILL PROCESS IMAGE #################################################################

        stop = obstacle_detect.recognize(image)

        if img is None:
            img = pl.imshow(image)
        else:
            img.set_data(image)

        pl.pause(0.01)
        pl.draw()

        print('Image is %dx%d' % image.size)
        image.verify()
        print('Image is verified')
finally:
    connection.close()
    server_socket.close()
