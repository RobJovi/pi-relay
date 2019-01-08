import RPi.GPIO as GPIO
import time

channel = 21

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)


def led_on(pin):
    print('hello')
    GPIO.output(pin, GPIO.HIGH)    # turn led on

def led_off(pin):
    GPIO.output(pin, GPIO.LOW)    # turn led off


led_on(channel)
led_off(channel)
    

