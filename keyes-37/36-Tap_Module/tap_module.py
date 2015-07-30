#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2015, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# tap_module.py
# Reports when shock is detected
#
# Author : nandyhsu
# Date   : 07/30/2015

import RPi.GPIO as GPIO
import time

PIN = 12
BOUNCE_TIME = 200


GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.IN)

def callback_function(channel):
	print("Shock Detected")
	
try:
	GPIO.add_event_detect(PIN, GPIO.FALLING, callback = callback_function, bouncetime =BOUNCE_TIME)
	
	while True:
		time.sleep(10)
		
except KeyboardInterrupt: 
	print "Exception: KeyboardInterrupt"
	
finally:
	GPIO.cleanup()
