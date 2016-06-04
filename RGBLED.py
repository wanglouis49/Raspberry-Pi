'''
Turning on an RBG LED with your Raspberry PI's GPIO Pins
Luyu Wang
2016-06-04
'''

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

for i in range(10):
	print "Red"
	GPIO.output(17,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(17,GPIO.LOW)


	print "Green"
	GPIO.output(22,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(22,GPIO.LOW)

	print "Blue"
	GPIO.output(6,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(6,GPIO.LOW)
