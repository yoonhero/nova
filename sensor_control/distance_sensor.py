import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set Distance Pins
Distance_TRIGGER = 18
Distance_ECHO = 24

# set GPIO direction (IN / OUT)
GPIO.setup(Distance_TRIGGER, GPIO.OUT)
GPIO.setup(Distance_ECHO, GPIO.IN)


def distance():
    # set Trigger to HIGH
    GPIO.output(Distance_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(Distance_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(Distance_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(Distance_ECHO) == 1:
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
            dist = distance()
            print("Measured Distance = %.1f cm" % dist)
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
