#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2015, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# joystick.py
# show the x, y, z axis data
#
# Author : bella_c
# Date   : 12/15/2015

import spidev
import time
import os

spi = spidev.SpiDev()
spi.open(0,0)

def ReadChannel(channel):
    adc = spi.xfer2([1, (8+channel)<<4, 0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

swt_channel = 0
vrx_channel = 1
vry_channel = 2

delay = 0.5

while True:

    vrx_pos = ReadChannel(vrx_channel)
    vry_pos = ReadChannel(vry_channel)

    swt_val = ReadChannel(swt_channel)

    print("X : {}  Y : {}  Switch : {}".format(vrx_pos,vry_pos,swt_val))

    time.sleep(delay)
	