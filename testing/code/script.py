import RPi.GPIO as GPIO
import time
import sys


def switchLED(led_pin, status):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(led_pin, GPIO.OUT)
    print(led_pin, status)
    GPIO.output(led_pin, status)
    GPIO.cleanup()


# testing GPIO ports
i = 0
while i < 10:
    switchLED(8, True)
    time.sleep(1)
    switchLED(8, False)
    time.sleep(1)

    i += 1


# Sets an infinite loop that waits for incoming messages
while True:
    try:
        time.sleep
    except KeyboardInterrupt:
        print('You pressed "Ctrl + C" - exiting')
        sys.exit()
