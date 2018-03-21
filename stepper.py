#!/usr/bin/python
#coding=utf-8

#enX,Y=8

#DirX=5
#StepX=2

#DirY=6
#StepY=3


import wiringpi as wpi
import math


wpi.wiringPiSetup()
wpi.pinMode(0,1)#en
wpi.pinMode(1,1)#dirX
wpi.pinMode(2,1)#dirY
wpi.pinMode(3,1)#stepX
wpi.pinMode(4,1)#stepY


wpi.digitalWrite(0,0)#en
wpi.digitalWrite(1,1)#dirX
wpi.digitalWrite(2,1)#dirY

#AE=AZ or EL
#角度制



while True:

	for num in range(1,3200):

		    wpi.digitalWrite(3,0)
		    wpi.delayMicroseconds(200)
		    wpi.digitalWrite(3,1)
		    wpi.delayMicroseconds(200)




	print wpi.millis()


