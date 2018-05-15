#!/usr/bin/python
# -*- coding: utf-8 -*-

from MMA8452Q import MMA8452Q
from numpy import deg2rad

import serial
import time
import GetLook
import math
import GetSat

ser=serial.Serial("/dev/ttyUSB0",115200,timeout=0.5)


accel 	= MMA8452Q()
accel.init()


cmd='$000111'

while True:



	AZ = 200;

	AZ_now = accel.read()     #azimuth


	if(AZ_now < AZ):

		s1=list(cmd)
		s1[4] = '1'
		cmd=''.join(s1) 
		print

	else:

		s1=list(cmd)
		s1[4] = '0'
		cmd=''.join(s1) 



	ser.write(cmd)
	time.sleep(1)