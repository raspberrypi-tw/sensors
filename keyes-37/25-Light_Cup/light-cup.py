#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2015, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# light-cup.py
# turns on led when device is tilted
#
# Author : nandyhsu
# Date   : 07/30/2015

import RPi.GPIO as GPIO
import time

PIN_OUT = 11
PIN_IN = 13
delay = 1
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_OUT, GPIO.OUT)
GPIO.setup(PIN_IN, GPIO.IN)

try:
	while True:
		if GPIO.input(PIN_IN) == GPIO.LOW:
			print "Device is tilted"
			GPIO.output(PIN_OUT, GPIO.HIGH)
		else:
			GPIO.output(PIN_OUT, GPIO.LOW)
		time.sleep(delay)

except KeyboardInterrupt: 
	print "Exception: KeyboardInterrupt"
	
finally:
	GPIO.cleanup()
