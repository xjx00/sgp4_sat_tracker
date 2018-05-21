from HMC5883L import HMC5883L
import time
azimuth = HMC5883L()
azimuth.init()
while(1):
	azimuth.read() 
	time.sleep(0.2)


from MMA8452Q import MMA8452Q
import time
elevation 	= MMA8452Q()
elevation.init()
while(1):
	elevation.read() 
	time.sleep(0.2)
