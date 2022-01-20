import socketserver
import cv2
import threading
import sys
import numpy as np

sensor_data = None


# Distance Data from Arduino Sensor
class SensorDataHandler(socketserver.BaseRequestHandler):
    data = ""

    def handle(self):
        global sensor_data
        while self.data:
            self.data = self.request.recv(1024)
            sensor_data = round(float(self.data), 1)

            print(sensor_data)

class VideoStreamHandler(socketserver.StreamRequestHandler):
    def handle(self):
        global sensor_data
        stream_bytes = b' '

        try:
            while True:
                stream_bytes += self.rfile.read(1024)
                first = stream_bytes.find(b'\xff\xd8')
                last = stream_bytes.find(b'\xff\xd9')
                if first != -1 and last != -1:
                    jpg = stream_bytes[first:last + 2]
                    stream_bytes = stream_bytes[last + 2:]
                    gray = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
                    image = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)

                    height, width = gray.shape
                    roi = gray[int(height/2):height, :]

                    cv2.imshow('image', image)
                    cv2.imshow('mlp_image', roi)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        print("car stopped")
                        break

        finally:
            cv2.destroyAllWindows()
            sys.exit()

class Server(object):
    def __init__(self, host, port1, port2):
        self.host = host
        self.port1 = port1
        self.port2 = port2

    def video_stream(self, host, port):
        s = socketserver.TCPServer((host, port), VideoStreamHandler)
        s.server_forever()

    def sensor_stream(self, host, port):
        s = socketserver.TCPServer((host, port), SensorDataHandler)
        s.server_forever()

    def start(self):
        sensor_thread = threading.Thread(
            target=self.sensor_stream, args=(self.host, self.port2))
        sensor_thread.deamon = True
        sensor_thread.start()

        self.video_stream(self.host, self.port1)
