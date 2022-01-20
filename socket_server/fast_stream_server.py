import socketserver
import cv2
import threading
import sys
import numpy as np


class Server(object):
    def __init__(self, host, port1, port2):
        self.host = host
        self.port1 = port1
        self.port2 = port2

    def sensor_stream(self, host, port):
        s = socketserver.TCPServer((host, port), SensorDataHandler)

    def start(self):
        sensor_thread = threading.Thread(
            target=self.sensor_stream, args=(self.host, self.port2))
