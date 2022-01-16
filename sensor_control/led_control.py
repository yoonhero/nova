import RPi.GPIO as GPIO
import time

ledPin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

while(True):
    GPIO.output(ledPin, False)
    time.sleep(2)
    GPIO.output(ledPin, True)
    time.sleep(2)
