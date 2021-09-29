import RPi.GPIO as GPIO
import sys
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pin1 = 24
pin2 = 23

GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

try:
    while True:
        GPIO.output(pin1, False)
        GPIO.output(pin2, False)
        print("motor")
        time.sleep(2)
except:
    print("error")
