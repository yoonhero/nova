import RPi.GPIO as GPIO
import time


class DistanceSensor():
    def __init__(self):
        GPIO.cleanup()
        # GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)

        # set Distance Pins
        self.triggerPin = 18
        self.echoPin = 24

        # set GPIO direction (IN / OUT)
        GPIO.setup(self.triggerPin, GPIO.OUT)
        GPIO.setup(self.echoPin, GPIO.IN)

    def getDistance(self):
        # set Trigger to HIGH
        GPIO.output(self.triggerPin, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.triggerPin, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while GPIO.input(self.echoPin) == 0:
            StartTime = time.time()

        # save time of arrival
        while GPIO.input(self.echoPin) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        timeIntervel = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (timeIntervel * 34300) / 2

        return distance


if __name__ == '__main__':
    try:
        while True:
            sensor = DistanceSensor()
            dist = sensor.getDistance()
            print("Measured Distance = %.1f cm" % dist)
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
