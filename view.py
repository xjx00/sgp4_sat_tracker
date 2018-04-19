# hmc5883l as compass

from MMA8452Q import MMA8452Q
from HMC5883L import HMC5883L
import time

accel 	= MMA8452Q()
compass = HMC5883L()

accel.init()
compass.init()

while True:
	
	AZ_now = accel.read()     #azimuth
	EL_now = compass.read()   #elevation
	time.sleep(0.1)