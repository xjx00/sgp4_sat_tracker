#!/usr/bin/python

import wiringpi as wpi
import math
import time


a=wpi.wiringPiI2CSetup(0x1e)

	#set range
wpi.wiringPiI2CWriteReg8(a,0x01, 0b001 << 5);
mgPerDigit = float(0.92);


	#setMeasurementMode

value = wpi.wiringPiI2CReadReg8(a,0x02);
value &= 0b11111100;
value |= 0b00;	

wpi.wiringPiI2CWriteReg8(a,0x02, value);


	#setDataRate

value = wpi.wiringPiI2CReadReg8(a,0x00);
value &= 0b11100011;
value |= (0b101 << 2);	

wpi.wiringPiI2CWriteReg8(a,0x00, value);


	#setSamples

value = wpi.wiringPiI2CReadReg8(a,0x00);
value &= 0b10011111;
value |= (0b11 << 5);

wpi.wiringPiI2CWriteReg8(a,0x00, value);


	#setOffset

xOffset = float(141);
yOffset = float(167);


	#compass

while True:
        


#        x=wpi.wiringPiI2CReadReg8(a,0x03) << 8 | wpi.wiringPiI2CReadReg8(a,0x04);
#        if x >> 15 ==1 :
#            XAxis = float(256*256-x-xOffset) * mgPerDigit;
#            print "Diao"
#        else:
#            XAxis = float(x - xOffset) * mgPerDigit;
        X=wpi.wiringPiI2CReadReg8(a,0x03) << 8  | wpi.wiringPiI2CReadReg8(a,0x04)
        Y=wpi.wiringPiI2CReadReg8(a,0x07) << 8  | wpi.wiringPiI2CReadReg8(a,0x08)
        Z=wpi.wiringPiI2CReadReg8(a,0x05) << 8  | wpi.wiringPiI2CReadReg8(a,0x06)

        if X>32768:    
            X = -(0xFFFF - X + 1);
        if Y>32768:
            Y = -(0xFFFF - Y + 1);
        if Z>32768:
            Z = -(0xFFFF - Z + 1);
                                                                    
        XAxis = (float(X) - xOffset) * mgPerDigit;
        YAxis = (float(Y) - yOffset) * mgPerDigit;
        ZAxis =  float(Z) * mgPerDigit;
        print "X="
        print XAxis
        print "Y="
        print YAxis

	heading = math.atan2(YAxis, XAxis);
        print "atan2="
        print heading
        declinationAngle = (4.0 + (26.0 / 60.0)) / (180 / math.pi);
	heading = heading + declinationAngle;#change to BG6.


	if (heading < 0):
		heading += 2 * math.pi;

	if (heading > 2 * math.pi):
		heading -= 2 * math.pi;


	headingDegrees = heading * 180/math.pi;


	print " Degress = "
	print headingDegrees


	time.sleep(0.1)
