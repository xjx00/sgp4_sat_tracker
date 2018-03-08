import os
import re
import sys
import serial
from doctest import DocTestSuite, ELLIPSIS
from unittest import TestCase
from math import pi, isnan

from sgp4.earth_gravity import wgs72
from sgp4.ext import invjday, newtonnu, rv2coe
from sgp4.io import twoline2rv
from sgp4.propagation import sgp4

ser=serial.Serial("/dev/ttyAMA0",9600,timeout=0.5) #使用树莓派的GPIO口连接串行口

line1 = ('1 00005U 58002B   00179.78495062  '
          '.00000023  00000-0  28098-4 0  4753')
line2 = ('2 00005  34.2682 348.7242 1859667 '
          '331.7664  19.3264 10.82419157413667')

satellite = twoline2rv(line1, line2, wgs72)

position, velocity = satellite.propagate(2011, 7, 18, 3, 03, 49)
#	position	X(km) Y(km) Z(km)
#	velocity	Vx(km/s) Vy(km/s) Vz(km/s)
#	TEME2ECEF