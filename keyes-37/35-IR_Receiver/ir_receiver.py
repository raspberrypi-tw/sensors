#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2015, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# ir_receiver.py
# show the message when IR signal received
#
# Author : bella_c
# Date   : 12/15/2015

import RPi.GPIO as GPIO
import time

RECEIVER = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RECEIVER, GPIO.IN)

try:
	while True:
		
		if GPIO.input(RECEIVER) == GPIO.LOW:
			print "Detected"

except KeyboardInterrupt: 
	print "Exception: KeyboardInterrupt"
	
finally:
	GPIO.cleanup()