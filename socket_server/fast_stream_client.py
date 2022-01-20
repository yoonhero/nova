import io
import socket
import struct
import time
import picamera


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('172.30.1.34', 8000))
connection = client_socket.makefile("wb")

try:
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        camera.framerate = 15
        time.sleep(2)
        start = time.time()
        stream = io.BytesIO()

        for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            stream.seek(0)
            connection.write(stream.read())
            if time.time() - start > 600:
                stream.seek(0)
            stream.seek(0)
            stream.truncate()

    connection.write(struct.pack('<L', 0))
finally:
    connection.close()
    client_socket.close()
