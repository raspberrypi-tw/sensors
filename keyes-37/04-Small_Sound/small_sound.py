#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2015, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# small_sound.py
# Report sounds levels above threshold 
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
sound_channel = 0
threshold = 40

try:
	while True:
		sound_level = ReadChannel(sound_channel)
		if sound_level > threshold:
			print("Sound Level Proportion:{}".format(sound_level))
		time.sleep(delay)

except KeyboardInterrupt: 
	print "Exception: KeyboardInterrupt"
	
