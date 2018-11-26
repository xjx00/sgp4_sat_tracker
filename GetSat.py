#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import sys

from sgp4.earth_gravity import wgs72
from sgp4.ext import invjday, newtonnu, rv2coe
from sgp4.io import twoline2rv
from sgp4.propagation import sgp4


class Eci(object):
	Position=[]
	Velocity=[]


'''
#Sat Data
line1 = ('1 07530U 74089B   18146.86533424 -.00000045  00000-0 -12660-5 0  9999')
line2 = ('2 07530 101.6853 114.5065 0012343  18.5684  35.1273 12.53632685991694')
'''




eciSat  = Eci()

def generate(line1,line2):
  
    global satellite
    satellite = twoline2rv(line1, line2, wgs72)

def get_eciSat():

  tt =time.time()
  date_now_utc = time.gmtime(tt)
  P,V = satellite.propagate(date_now_utc.tm_year, date_now_utc.tm_mon, date_now_utc.tm_mday,
                               date_now_utc.tm_hour, date_now_utc.tm_min, date_now_utc.tm_sec + tt%1 )

  #list & tuple
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
