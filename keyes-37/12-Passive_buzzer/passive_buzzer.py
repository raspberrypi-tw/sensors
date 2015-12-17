#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2015, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# passive_buzzer.py
# buzzer turns on
#
# Author : bella_c
# Date   : 12/08/2015

import RPi.GPIO as GPIO
import time

PIN = 12


GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

try:
	while True:
		print("BUZZER ON")
		GPIO.output(PIN, GPIO.HIGH)
		time.sleep(3)
		
		print("BUZZER OFF")
		GPIO.output(PIN, GPIO.LOW)
		time.sleep(1)
		
except KeyboardInterrupt: 
	print "Exception: KeyboardInterrupt"
	
finally:
	GPIO.cleanup()