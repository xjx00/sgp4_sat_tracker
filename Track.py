#!/usr/bin/python
# -*- coding: utf-8 -*-


#sudo date  --s="2014-08-31 14:42:00"


from HMC5883L import HMC5883L
from MMA8452Q import MMA8452Q
from numpy import deg2rad

import os
import GetSat
import GetLook
import time
import jdcal
import math
import serial
import GetDirection



os.system('sudo date  --s="2018-05-27 19:59:00"')
#os.system('sudo date  --s="2018-05-28 20:24:20"')
#最大仰角23.1°
#19:59:00 开始

#---setup----
ser=serial.Serial("/dev/ttyUSB0",230400,timeout=0.5)

azimuth = HMC5883L()
elevation 	= MMA8452Q()

azimuth.init()
elevation.init()

cmd='$100100'

s1=list(cmd)

f=open('data.txt','w')


#---set PID参数----

kp_x = 0.5
kp_y = 0.5
ki_x = 0.0
ki_y = 0.0
kd_x = 0.0
kd_y = 0.0



AZ_old = 0
EL_old = 0




#---------------一次性--------------
omega_x = 0
omega_y = 0


#---------------Direction Choose-----






#-----------Big Loop
while True:

	eciSat = GetSat.get_eciSat()


	tl = time.localtime(time.time())

	date_now_julian = sum(jdcal.gcal2jd(tl.tm_year,tl.tm_mon,tl.tm_mday))+tl.tm_hour/24.0+tl.tm_min/24.0/60.0+tl.tm_sec/24.0/3600.0

	AZ,EL = GetLook.GetLook(date_now_julian,eciSat)
	#date_now为Julian形式
	AZ = AZ + 15.0

	if(AZ>360):
		AZ = AZ - 360.0

	AZ_now = azimuth.read()     #azimuth
	EL_now = elevation.read()   #elevation

	e_AZ = AZ - AZ_now
	e_EL = EL - EL_now

	s1[1] ,s1[4] = GetDirection.GetDirection( AZ_old , AZ , EL_old , EL)
#--------set omega_x-----------



	omega_x = kp_x*abs(e_AZ)


	if(omega_x>9.9):

		s1[2] = '9'
		s1[3] = '9'

	else:

		s1[2] = str(omega_x)[0]
		s1[3] = str(omega_x)[2]

	if( AZ > AZ_old and AZ_now > AZ):					#上升阶段,超调

		s1[5] = '0'
		s1[6] = '0'

	if( AZ < AZ_old and AZ_now < AZ):					#下降阶段,超调

		s1[5] = '0'
		s1[6] = '0'


#--------set omega_y-----------



	omega_y = kp_y * (abs(e_EL)+0.6)


	if(omega_y>9.9):

		s1[5] = '9'
		s1[6] = '9'

	else:

		s1[5] = str(omega_y)[0]
		s1[6] = str(omega_y)[2]

	if( EL > EL_old and EL_now > EL):					#上升阶段,超调

		s1[5] = '0'
		s1[6] = '0'

	if( EL < EL_old and EL_now < EL):					#下降阶段,超调

		s1[5] = '0'
		s1[6] = '0'

#--------------set Command-------
	cmd=''.join(s1) 



	print 'AZ =',AZ
	print 'AZ_now =',AZ_now

	print 'EL =',EL
	#print 'EL_now =',EL_now

	print cmd

	f.write(str(AZ)+','+str(AZ_now)+',')

	AZ_old = AZ
	EL_old = EL


	ser.write(cmd)
	time.sleep(0.1)





