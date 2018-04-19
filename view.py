#!/usr/bin/python
# -*- coding: utf-8 -*-

from MMA8452Q import MMA8452Q
from HMC5883L import HMC5883L
from numpy import deg2rad
import serial
import time
import GetLook
import math


from sgp4.earth_gravity import wgs72
from sgp4.ext import invjday, newtonnu, rv2coe
from sgp4.io import twoline2rv
from sgp4.propagation import sgp4


F                        =        1.0 / 298.26
XKMPER_WGS72             =        6378.135
EPOCH_JAN1_12H_2000      =        2451545.0
SEC_PER_DAY              =        86400.0
OMEGA_E                  =        1.00273790934


class Eci(object):
	position=[]
	velocity=[]



ser=serial.Serial("/dev/ttyUSB0",115200,timeout=0.5)
ser.open()

accel 	= MMA8452Q()
compass = HMC5883L()

accel.init()
compass.init()




line1 = ('1 00005U 58002B   00179.78495062  '
          '.00000023  00000-0  28098-4 0  4753')
line2 = ('2 00005  34.2682 348.7242 1859667 '
          '331.7664  19.3264 10.82419157413667')

satellite = twoline2rv(line1, line2, wgs72)

eciSat  = Eci()
Site    = Eci()
#eciSite = Eci()

Site.Position =[ deg2rad(30.463) , deg2rad(114.43) , 0.05 ]
#  Site.Position =[ deg2rad(Lat),deg2rad(Lon),kmAlt ]




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



time.localtime(time.time())
time.time()
date = satellite.jdsatepoch


while True:
	P,V = satellite.propagate(2000, 6, 28, 0, 50, 19.733567)
	eciSat.Position = list(P)
	eciSat.Velocity = list(V)

	GetLook.GetLook(date_now,eciSat,Site)
	#date_now为Julian形式

	AZ_now = accel.read()     #azimuth
	EL_now = compass.read()   #elevation


	time.sleep(0.1)