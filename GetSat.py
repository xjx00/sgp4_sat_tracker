#!/usr/bin/python
# -*- coding: utf-8 -*-


import math
import time

from sgp4.earth_gravity import wgs72
from sgp4.ext import invjday, newtonnu, rv2coe
from sgp4.io import twoline2rv
from sgp4.propagation import sgp4


class Eci(object):
	Position=[]
	Velocity=[]





#Sat Data

line1 = ('1 27607U 02058C   18140.55815610 -.00000026  00000-0  17076-4 0  9996')
line2 = ('2 27607  64.5538 174.4882 0062245 334.4772  25.3260 14.75449147828752')



satellite = twoline2rv(line1, line2, wgs72)


eciSat  = Eci()



def get_eciSat():


#time.struct_time(tm_year=2018, tm_mon=2, tm_mday=8, 
#   tm_hour=13, tm_min=37, tm_sec=31, tm_wday=3, tm_yday=39, tm_isdst=0)

  tt=time.time()
  date_now = time.localtime(tt)

  P,V = satellite.propagate(date_now.tm_year, date_now.tm_mon, date_now.tm_mday,
                               date_now.tm_hour, date_now.tm_min, date_now.tm_sec + tt%1 )

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
