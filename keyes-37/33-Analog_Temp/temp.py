#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2015, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# temp.py
# measures temperature proportion
#
# Author : nandyhsu
# Date   : 07/30/2015

import RPi.GPIO as GPIO
import time 
import spidev

spi =spidev.SpiDev()
spi.open(0,0)

def ReadChannel(channel):
	adc = spi.xfer2([1, (8+channel)<<4, 0])
	data = ((adc[1] & 3) << 8) + adc[2]
	return data
	
	
delay = 1
temp_channel = 0

try:
	while True:
		temp_level = ReadChannel(temp_channel)
		print("Inverse Temperature Proportion:{}".format(temp_level))
		time.sleep(delay)

except KeyboardInterrupt: 
	print "Exception: KeyboardInterrupt"
	
