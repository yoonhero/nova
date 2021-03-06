import time
try:
    import RPi.GPIO as gpio
    test_environment = False
except (ImportError, RuntimeError):
    test_environment = True


class Motor:
    def __init__(self, test_environment):
        if test_environment:
            self.test_environment = True
            return

        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        self.StepPins = [12, 16, 20, 21]

        for pin in self.StepPins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

        self.StepCounter = 0

        self.StepCount = 4

        self.Seq = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
        self.backSeq = list(reversed(self.Seq))

    def goForward(self):
        if self.test_environment:
            return
        try:
            while True:
                for pin in range(0, 4):

                    xpin = self.StepPins[pin]
                    if self.Seq[self.StepCounter][pin] != 0:
                        GPIO.output(xpin, True)
                    else:
                        GPIO.output(xpin, False)

                self.StepCounter += 1

                if self.StepCounter == self.StepCount:
                    self.StepCounter = 0
                if self.StepCounter < 0:
                    self.StepCounter = self.StepCount
                time.sleep(0.01)

        except:
            print("Error on Control Motor!!")

    def goBackward(self):
        if self.test_environment:
            return
        try:
            while True:
                for pin in range(0, 4):
                    xpin = self.StepPins[pin]
                    if self.backSeq[self.StepCounter][pin] != 0:
                        GPIO.output(xpin, True)
                    else:
                        GPIO.output(xpin, False)

                self.StepCounter += 1

                if self.StepCounter == self.StepCount:
                    self.StepCounter = 0
                if self.StepCounter < 0:
                    self.StepCounter = self.StepCount
                time.sleep(0.01)

        except:
            print("Error on Control Motor!!")

    def stop(self):
        if self.test_environment:
            return
        try:
            for pin in range(0, 4):
                xpin = self.StepPins[pin]
                GPIO.output(xpin, False)

        except:
            print("Error on Stop Motor")


if __name__ == "__main__":
    motor = Motor(test_environment=test_environment)
    while True:
        mode = input(": ")
        if mode == "f":
            motor.goForward()
        elif mode == "b":
            motor.goBackward()
        else:
            motor.stop()

    GPIO.cleanup()
