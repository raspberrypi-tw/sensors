#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2015, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# ir_emission.py
# send the IR signal
#
# Author : bella_c
# Date   : 12/15/2015

import RPi.GPIO as GPIO
import time

SEND = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SEND, GPIO.OUT)

try:
	while True:
		print("Send the IR signal")
		GPIO.output(SEND, GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(SEND, GPIO.LOW)
		

except KeyboardInterrupt: 
	print "Exception: KeyboardInterrupt"
	
finally:
	GPIO.cleanup()