#!/usr/bin/python
# -*- coding: utf-8 -*-

#from MMA8452Q import MMA8452Q
#from HMC5883L import HMC5883L
from numpy import deg2rad

#import serial
import time
import GetLook
import math
import GetSat


#ser=serial.Serial("/dev/ttyUSB0",115200,timeout=0.5)
#ser.open()

#accel 	= MMA8452Q()
#compass = HMC5883L()

#accel.init()
#compass.init()



cmd='$100100'
#time.localtime(time.time())
#ime.time()
#date = satellite.jdsatepoch


while True:

	eciSat = GetSat.get_eciSat()

	date_now_julian = time.time()/3600+2440588.5


	AZ,EL = GetLook.GetLook(date_now_julian,eciSat)
	#date_now为Julian形式

	AZ_now = accel.read()     #azimuth
	EL_now = compass.read()   #elevation

	if(EL_now < EL):
		cmd[4] = 1
	else:
		cmd[4] = 0

	omega_y = EL 

	if()


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

