import socketserver
import cv2
import threading
import sys
import numpy as np
import time

# get distance data
sensor_data = None


# Distance Data from Arduino Sensor
class SensorDataHandler(socketserver.BaseRequestHandler):

    data = " "

    def handle(self):
        global sensor_data
        while self.data:
            try:
                self.data = self.request.recv(1024)
                sensor_data = round(float(self.data), 1)
                print("[SOCKET] SENSOR DATA RECEIVED")
                # client Address: self.client_address[0]))
            except:
                pass


class VideoStreamHandler(socketserver.StreamRequestHandler):
    def handle(self):
        global sensor_data
        stream_bytes = b' '

        try:
            print("[SOCKET] IMAGE RECEIVED")
            prevTime = 0
            while True:
                curTime = time.time()

                stream_bytes += self.rfile.read(1024)
                first = stream_bytes.find(b'\xff\xd8')
                last = stream_bytes.find(b'\xff\xd9')
                if first != -1 and last != -1:
                    jpg = stream_bytes[first:last + 2]
                    stream_bytes = stream_bytes[last + 2:]
                    gray = cv2.imdecode(np.frombuffer(
                        jpg, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
                    image = cv2.imdecode(np.frombuffer(
                        jpg, dtype=np.uint8), cv2.IMREAD_COLOR)

                    height, width = gray.shape
                    roi = gray[int(height/2):height, :]
                    
                    sec = curTime - prevTime
                    prevTime = curTime
                    fps = 1/(sec)
                    fps_text = "FPS : %0.1f" % fps

                    cv2.putText(image, fps_text, (0, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 5)

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
        s.serve_forever()

    def sensor_stream(self, host, port):
        s = socketserver.TCPServer((host, port), SensorDataHandler)
        s.serve_forever()

    def start(self):
        sensor_thread = threading.Thread(
            target=self.sensor_stream, args=(self.host, self.port2))
        sensor_thread.deamon = True
        sensor_thread.start()

        self.video_stream(self.host, self.port1)


if __name__ == "__main__":
    h, p1, p2 = "172.30.1.34", 8000, 8002

    ts = Server(h, p1, p2)
    ts.start()
