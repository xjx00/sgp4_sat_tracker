#!/usr/bin/python
# -*- coding: utf-8 -*-



#import os
#import re
#import sys
#from doctest import DocTestSuite, ELLIPSIS
#from unittest import TestCase


import math
from numpy import deg2rad

from sgp4.earth_gravity import wgs72
from sgp4.ext import invjday, newtonnu, rv2coe
from sgp4.io import twoline2rv
from sgp4.propagation import sgp4


class Eci(object):
	position=[]
	velocity=[]

F                        =        1.0 / 298.26
XKMPER_WGS72             =        6378.135
EPOCH_JAN1_12H_2000      =        2451545.0
SEC_PER_DAY              =        86400.0
OMEGA_E                  =        1.00273790934





line1 = ('1 00005U 58002B   00179.78495062  '
          '.00000023  00000-0  28098-4 0  4753')
line2 = ('2 00005  34.2682 348.7242 1859667 '
          '331.7664  19.3264 10.82419157413667')

satellite = twoline2rv(line1, line2, wgs72)


eciSat  = Eci()



def get_eciSat(date_now):


  P,V = satellite.propagate(2000, 6, 28, 0, 50, 19.733567)

  ##list & tuple
  eciSat.Position = list(P)
  eciSat.Velocity = list(V)
  
  return eciSat







'''

          date_julian_epoch = satellite.jdsatepoch


          satellite.epochyr
          2000
          satellite.epochdays
          179.78495062
          satellite.jdsatepoch
          2451723.28495062
          satellite.epoch
          datetime.datetime(2000, 6, 27, 18, 50, 19, 733567)


'''
