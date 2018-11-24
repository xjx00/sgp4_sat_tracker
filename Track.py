#!/usr/bin/python
# -*- coding: utf-8 -*-

#Not Completed

from HMC5883L import HMC5883L
from MMA8452Q import MMA8452Q


import GetSat
import GetLook
import time
import jdcal
import math
import serial



#Change the System Time to Test.
#os.system('sudo date  --s="2018-05-27 19:59:00"')


#---setup----

#ser=serial.Serial("/dev/ttyUSB0",230400,timeout=0.5)

azimuth = HMC5883L()
elevation 	= MMA8452Q()

azimuth.init()
elevation.init()



#---set PID参数----

kp_x = 0.5
kp_y = 0.5
ki_x = 0.0
ki_y = 0.0
kd_x = 0.0
kd_y = 0.0



AZ_old = 0
EL_old = 0




#-----------Big Loop
while True:

	eciSat = GetSat.get_eciSat()


	tl = time.gmtime(time.time())

	date_now_julian = sum(jdcal.gcal2jd(tl.tm_year,tl.tm_mon,tl.tm_mday))+tl.tm_hour/24.0+tl.tm_min/24.0/60.0+tl.tm_sec/24.0/3600.0

	AZ,EL = GetLook.GetLook(date_now_julian,eciSat)
	#date_now为Julian形式

	AZ_now = azimuth.read()     #azimuth
	EL_now = elevation.read()   #elevation

#--------set omega_x & omega_y-----------

	omega_x = kp_x*abs(e_AZ)
	omega_y = kp_y*abs(e_EL)

#-----------------Move-------------------
	

	AZ_old = AZ
	EL_old = EL


	time.sleep(0.1)





