#!/usr/bin/python  
import wiringpi as wpi

a=wpi.wiringPiI2CSetup(0x1e)
while True:
    wpi.wiringPiI2CWriteReg8(a,0x02,0b10000000)
   # t=10000
    #while t>0:
     #   t=t-1
    print wpi.wiringPiI2CReadReg8(a,0x04)



