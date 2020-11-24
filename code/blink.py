import RPi.GPIO as GPIO
import time

led_pin = 8

# Configure the PIN # 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setwarnings(False)

def switchLEDon():
    GPIO.output(led_pin, True)


def swithLEDoff():
    GPIO.output(led_pin, False)


# Release Resources
GPIO.cleanup()
