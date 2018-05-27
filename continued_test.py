from HMC5883L import HMC5883L
import time
azimuth = HMC5883L()
azimuth.init()
while(1):
	a=azimuth.read() 
	if(a>350):
		print('\a')
	print a
	time.sleep(0.2)


from MMA8452Q import MMA8452Q
import time
elevation 	= MMA8452Q()
elevation.init()
while(1):
	elevation.read() 
	time.sleep(0.2)


import serial
ser=serial.Serial("/dev/ttyUSB0",230400,timeout=0.5)
ser.write('$100030')