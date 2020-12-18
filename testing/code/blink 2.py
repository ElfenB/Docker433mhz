import RPi.GPIO as GPIO

def switchLEDon(led_pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.setwarnings(False)
    GPIO.output(led_pin, True)
    GPIO.cleanup()


def switchLEDoff(led_pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.setwarnings(False)
    GPIO.output(led_pin, False)
    GPIO.cleanup()
