#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2015, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# heart.py
# Reports an inaccurate heart rate
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
	
def BPM(num_of_beats):
	rate = num_of_beats/5
	bpm = rate * 60
	return bpm
	
data_channel = 0
threshold = 100

try:
	while True:
		beat = 0
		start_time = time.time()
		prev_data = ReadChannel(data_channel)
		while time.time() - start_time < 5:
			current_data = ReadChannel(data_channel)
			
			if current_data - prev_data > threshold:
				beat = beat + 1
			prev_data = current_data
	
		bpm = BPM(beat)
		print("Beats Per Minute:{}".format(bpm))
		time.sleep(3)
		
except KeyboardInterrupt: 
	print "Exception: KeyboardInterrupt"
	
finally:
	GPIO.cleanup()
