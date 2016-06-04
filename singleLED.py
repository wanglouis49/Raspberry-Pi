'''
Turning on an LED with your Raspberry PI's GPIO Pins
https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins
'''

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

print "LED on"
GPIO.output(17,GPIO.HIGH)
time.sleep(1)
print "LED off"
GPIO.output(17,GPIO.LOW)
