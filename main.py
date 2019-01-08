import RPi.GPIO as GPIO
import time

channel = 21

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)


def led_on(pin):
    print('on')
    GPIO.output(pin, GPIO.LOW)    # turn led on

def led_off(pin):
    print('off')
    GPIO.output(pin, GPIO.HIGH)    # turn led off


led_on(channel)
time.sleep(5)
led_off(channel)
GPIO.cleanup()
