#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2015, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# RG_SMALL.py
# leds are turned on
#
# Author : nandyhsu
# Date   : 07/30/2015

import RPi.GPIO as GPIO
import time

LED_RED = 11
LED_GREEN = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_RED, GPIO.OUT)

try:
	while True:

		
		
		print("Red")
		GPIO.output(LED_RED, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(LED_RED, GPIO.LOW)
		
		print("Yellow")
		GPIO.output(LED_GREEN, GPIO.HIGH)
		GPIO.output(LED_RED, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(LED_GREEN, GPIO.LOW)
		GPIO.output(LED_RED, GPIO.LOW)
		
		print("Green")
		GPIO.output(LED_GREEN, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(LED_GREEN, GPIO.LOW)

except KeyboardInterrupt: 
	print "Exception: KeyboardInterrupt"
	
finally:
	GPIO.cleanup()
