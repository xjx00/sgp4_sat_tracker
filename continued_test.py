#!/usr/bin/python
# -*- coding: utf-8 -*-

#Test Code
#Paste to Python Interpreter

from HMC5883L import HMC5883L
import time
azimuth = HMC5883L()
azimuth.init()
while(1):
	a=azimuth.read() 
	print a
	time.sleep(0.2)


from MMA8452Q import MMA8452Q
import time
elevation 	= MMA8452Q()
elevation.init()
while(1):
	elevation.read() 
	time.sleep(0.2)
