#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2015, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# photo_interrupt.py
# Reports when an object is detected
#
# Author : nandyhsu
# Date   : 07/30/2015

import RPi.GPIO as GPIO
import time

PIN = 12
delay = 0.5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.IN)

try:
	while True:
		if GPIO.input(PIN) == GPIO.HIGH:
			print("Object Detected")
		time.sleep(delay)
		
except KeyboardInterrupt: 
	print "Exception: KeyboardInterrupt"
	
finally:
	GPIO.cleanup()