#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2015, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# reed_switch.py
# Reports when a magnetic field is detected
#
# Author : nandyhsu
# Date   : 07/30/2015

import RPi.GPIO as GPIO
import time 

delay = 1
PIN = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.IN)

try:
	while True:
		if GPIO.input(PIN) == GPIO.HIGH:
			print("Magnetic Field Detected")
		time.sleep(delay)

except KeyboardInterrupt: 
	print "Exception: KeyboardInterrupt"
	
finally:
	GPIO.cleanup()
