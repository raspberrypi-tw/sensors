#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2015, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# RGB.py
# LEDS are turned on 
#
# Author : nandyhsu
# Date   : 07/30/2015

import RPi.GPIO as GPIO
import time

LED_BLUE = 11
LED_GREEN = 12
LED_RED = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_BLUE, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_RED, GPIO.OUT)

try:
	while True:
		print("Blue")
		GPIO.output(LED_BLUE, GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(LED_BLUE, GPIO.LOW)
		
		print("Green")
		GPIO.output(LED_GREEN, GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(LED_GREEN, GPIO.LOW)
		
		print("Red")
		GPIO.output(LED_RED, GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(LED_RED, GPIO.LOW)

except KeyboardInterrupt: 
	print "Exception: KeyboardInterrupt"
	
finally:
	GPIO.cleanup()
