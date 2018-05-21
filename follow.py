#!/usr/bin/python
# -*- coding: utf-8 -*-

#from HMC5883L import HMC5883L
from MMA8452Q import MMA8452Q
from numpy import deg2rad

import serial
import time
import GetLook
import math
import GetSat
import jdcal

ser=serial.Serial("/dev/ttyUSB0",230400,timeout=0.5)


#azimuth = HMC5883L()
elevation 	= MMA8452Q()


#azimuth.init()
elevation.init()



cmd='$100100'
#time.localtime(time.time())
#ime.time()
#date = satellite.jdsatepoch


#TEST MODE
date_julian_5_22_20_37 = 2458261.025694	;
after = sum(jdcal.gcal2jd(tl.tm_year,tl.tm_mon,tl.tm_mday))+tl.tm_hour/24.0+tl.tm_min/24.0/60.0+tl.tm_sec/24.0/3600.0 - date_julian_5_22_20_37


#PID参数设置
kp=1

while True:

	eciSat = GetSat.get_eciSat()


	tl = time.localtime(time.time())


	#True Mode 
	#date_now_julian = sum(jdcal.gcal2jd(tl.tm_year,tl.tm_mon,tl.tm_mday))+tl.tm_hour/24.0+tl.tm_min/24.0/60.0+tl.tm_sec/24.0/3600.0

	#Test Mode
	date_now_julian = sum(jdcal.gcal2jd(tl.tm_year,tl.tm_mon,tl.tm_mday))+tl.tm_hour/24.0+tl.tm_min/24.0/60.0+tl.tm_sec/24.0/3600.0
	date_now_julian = date_now_julian - after

	AZ,EL = GetLook.GetLook(date_now_julian,eciSat)
	#date_now为Julian形式

	#AZ_now = azimuth.read()     #azimuth
	EL_now = elevation.read()   #elevation

	if(EL_now < EL):
		s1=list(cmd)
		s1[4] = '1'

		omega_y = kp*(EL-EL_now)
		s1[5] = str(int(omega_y))
		s1[6] = str(int(omega_y*10%10))

		cmd=''.join(s1) 
	else:
		s1=list(cmd)
		s1[4] = '0'

		omega_y = kp*(EL-EL_now)
		s1[5] = str(int(omega_y))
		s1[6] = str(int(omega_y*10%10))

		cmd=''.join(s1) 


	print 'Goal =',EL
	print 'Now =',EL_now
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


#ser.write(chr(40))


#print( c + " 的ASCII 码为", ord(c))
#print( a , " 对应的字符为", chr(a))

