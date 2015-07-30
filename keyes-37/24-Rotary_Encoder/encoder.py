#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2015, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# encoder.py
# Reports which direction the encoder is turning
#
# Author : nandyhsu
# Date   : 07/30/2015

import RPi.GPIO as GPIO
import time 

PIN_1 = 11
PIN_2 = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_1, GPIO.IN)
GPIO.setup(PIN_2, GPIO.IN)

def getState(PIN):
	if GPIO.input(PIN) == GPIO.HIGH:
		return 1
	else:
		return 0
		
def turnState(A_old, A_current, B_old, B_current):
	if A_old == GPIO.LOW and A_current == GPIO.LOW and B_old == GPIO.LOW and B_current ==GPIO.HIGH:
		print("clockwise")
	elif A_old == GPIO.LOW and A_current == GPIO.HIGH and B_old == GPIO.HIGH and B_current ==GPIO.HIGH:
		print("clockwise")
	elif A_old == GPIO.HIGH and A_current == GPIO.HIGH and B_old == GPIO.HIGH and B_current ==GPIO.LOW:
		print("clockwise")
	else:
		print("counter-clockwise")
try:
	A_old = getState(PIN_1)
	B_old = getState(PIN_2)
	while True:
		A_current = getState(PIN_1)
		B_current = getState(PIN_2)
		if A_old != A_current or B_old != B_current:
		#	print("A:{} B:{}".format(A_current,B_current))
			turnState(A_old, A_current, B_old, B_current)
		A_old = A_current
		B_old = B_current
		time.sleep(1)
		
except KeyboardInterrupt: 
	print "Exception: KeyboardInterrupt"
	
finally:
	GPIO.cleanup()