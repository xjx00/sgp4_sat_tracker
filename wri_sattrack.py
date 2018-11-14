#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import jdcal
import serial
import GetSat
import GetLook



#if you want to use serial.
#ser = serial.Serial('/dev/ttyUSB0',9600)



while True:

	eciSat = GetSat.get_eciSat()

	tl = time.gmtime(time.time())

	date_now_julian = sum(jdcal.gcal2jd(tl.tm_year,tl.tm_mon,tl.tm_mday))+tl.tm_hour/24.0+tl.tm_min/24.0/60.0+tl.tm_sec/24.0/3600.0

	AZ,EL = GetLook.GetLook(date_now_julian,eciSat)

	print AZ,EL
	
	#if you want to use serial
	#ser.write("Whatever you need")

	#If you need to control the frequency of date out:
	#time.sleep()                 #Second
