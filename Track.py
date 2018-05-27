#!/usr/bin/python
# -*- coding: utf-8 -*-

from HMC5883L import HMC5883L
from MMA8452Q import MMA8452Q
from numpy import deg2rad

import GetSat
import GetLook
import time
import jdcal
import math
import serial

#---setup----
ser=serial.Serial("/dev/ttyUSB0",230400,timeout=0.5)

azimuth = HMC5883L()
elevation 	= MMA8452Q()

azimuth.init()
elevation.init()

cmd='$100100'


#---set PID参数----

kp_x = 0.8
kp_y = 0.8
ki_x = 0.0
ki_y = 0.0
kd_x = 0.0
kd_y = 0.0








#---------------一次性--------------
eciSat = GetSat.get_eciSat()
tl = time.localtime(time.time())
date_now_julian = sum(jdcal.gcal2jd(tl.tm_year,tl.tm_mon,tl.tm_mday))+tl.tm_hour/24.0+tl.tm_min/24.0/60.0+tl.tm_sec/24.0/3600.0
AZ,EL = GetLook.GetLook(date_now_julian,eciSat)
AZ_now = azimuth.read()     #azimuth
EL_now = elevation.read()   #elevation
e_AZ_old = AZ - AZ_now
e_EL_old = EL - EL_now
e_AZ_old_2 = AZ - AZ_now
e_EL_old_2 = EL - EL_now



while True:

	eciSat = GetSat.get_eciSat()


	tl = time.localtime(time.time())

	date_now_julian = sum(jdcal.gcal2jd(tl.tm_year,tl.tm_mon,tl.tm_mday))+tl.tm_hour/24.0+tl.tm_min/24.0/60.0+tl.tm_sec/24.0/3600.0

	AZ,EL = GetLook.GetLook(date_now_julian,eciSat)
	#date_now为Julian形式

	AZ_now = azimuth.read()     #azimuth
	EL_now = elevation.read()   #elevation

	e_AZ = AZ - AZ_now
	e_EL = EL - EL_now

	s1=list(cmd)



#--------set omega_x-----------

	if(AZ_now < AZ):
		s1[1] = '1'

	else:
		s1[1] = '0'

	omega_x	=	omega_x + kp_x*(e_AZ - e_AZ_old) + ki_x * e_AZ + kd_x * (e_AZ - 2*e_AZ_old + e_AZ_old_2)


	if(omega_x>9.9):

		s1[2] = '9'
		s1[3] = '9'

	else:

		s1[2] = str(omega_x)[0]
		s1[3] = str(omega_x)[2]


#--------set omega_y-----------

	if(EL_now < EL):
		s1[4] = '1'

	else:
		s1[4] = '0'

	omega_y	=	omega_y + kp_y*(e_EL - e_EL_old) + ki_y * e_EL + kd_y * (e_EL - 2*e_EL_old + e_EL_old_2)


	if(omega_y>9.9):

		s1[5] = '9'
		s1[6] = '9'

	else:

		s1[5] = str(omega_y)[0]
		s1[6] = str(omega_y)[2]


#--------------set Command-------
	cmd=''.join(s1) 

	e_AZ_old_2 = AZ_old
	e_EL_old_2 = EL_old

	e_AZ_old = AZ_now
	e_EL_old = EL_now

	print 'AZ =',AZ，
	print 'AZ_now =',AZ_now，

	print 'EL =',EL，
	print 'EL_now =',EL_now，

	print cmd



	ser.write(cmd)
	time.sleep(0.1)




#ser=serial.Serial("/dev/ttyAMA0",115200,timeout=0.5) #使用树莓派的GPIO口连接串行口
#ser=serial.Serial("/dev/ttyUSB0",115200,timeout=0.5) #使用树莓派的GPIO口连接串行口

#print ser.name#打印设备名称
#print ser.port#打印设备名
#ser.open()
#打开端口
#s = ser.read(10)#从端口读10个字节
#ser.write("hello")#向端口些数据
#ser.close()#关闭端口
 #       data = ser.read(20) #是读20个字符

  #      data = ser.readline() #是读一行，以/n结束，要是没有/n就一直读，阻塞。

  #      data = ser.readlines()和ser.xreadlines()#都需要设置超时时间

 #       ser.baudrate = 9600 #设置波特率

 #       ser.isOpen() #看看这个串口是否已经被打开



#print( c + " 的ASCII 码为", ord(c))
#print( a , " 对应的字符为", chr(a))

