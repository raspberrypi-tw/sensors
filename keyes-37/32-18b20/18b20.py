#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2015, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# 18b20.py
# measures temperature in degrees C
#
# Author : nandyhsu
# Date   : 07/30/2015

# source: http://www.reuk.co.uk/DS18B20-Temperature-Sensor-with-Raspberry-Pi.htm

import time

try:
	while True:
		tempfile = open("/sys/bus/w1/devices/28-041460cb6cff/w1_slave")
		text = tempfile.read()
		tempfile.close()
		data = text.split("\n")[1].split(" ")[9]
		temp = float(data[2:])
		temp = temp/1000
		print ("Temperature: {} degrees C".format(temp))
		
		time.sleep(1)
		
except KeyboardInterrupt: 
	print "Exception: KeyboardInterrupt"
	