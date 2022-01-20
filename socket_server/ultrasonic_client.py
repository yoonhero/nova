from socket import *
import time
import RPi.GPIO as GPIO

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('172.30.1.34', 8002))


class DistanceSensor():
    def __init__(self):
        # GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)

        # set Distance Pins
        self.triggerPin = 18
        self.echoPin = 24

        # set GPIO direction (IN / OUT)
        GPIO.setup(self.triggerPin, GPIO.OUT)
        GPIO.setup(self.echoPin, GPIO.IN)
        GPIO.output(self.triggerPin, False)

    def getDistance(self):
        GPIO.output(self.triggerPin, True)
        time.sleep(0.00001)
        GPIO.output(self.triggerPin, False)
        start = time.time()

        while GPIO.input(self.echoPin) == 0:
            start = time.time()

        while GPIO.input(self.echoPin) == 1:
            stop = time.time()

        # time difference between start and arrival
        timeIntervel = stop - start
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (timeIntervel * 34300) / 2

        return distance


try:
    while True:
        sensor = DistanceSensor()
        dist = sensor.getDistance()
        print("Measured Distance = %.1f cm" % dist)
        client_socket.send(str(dist).encode('utf-8'))
        time.sleep(1)
# Reset by pressing CTRL + C
except KeyboardInterrupt:
    client_socket.close()
    GPIO.cleanup()
