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

	XAxis = (float(wpi.wiringPiI2CReadReg16(a,0x03)) - xOffset) * mgPerDigit;
	YAxis = (float(wpi.wiringPiI2CReadReg16(a,0x07)) - yOffset) * mgPerDigit;
	ZAxis = float(wpi.wiringPiI2CReadReg16(a,0x05)) * mgPerDigit;


	heading = math.atan2(YAxis, XAxis);
	declinationAngle = (4.0 + (26.0 / 60.0)) / (180 / math.pi);
	heading = heading + declinationAngle;


	if (heading < 0):
		heading += 2 * math.pi;

	if (heading > 2 * math.pi):
		heading -= 2 * math.pi;


	headingDegrees = heading * 180/math.pi;


	print " Degress = "
	print headingDegrees


	time.delay(100)