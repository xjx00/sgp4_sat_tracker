#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import time
import sys

from sgp4.earth_gravity import wgs72
from sgp4.ext import invjday, newtonnu, rv2coe
from sgp4.io import twoline2rv
from sgp4.propagation import sgp4


class Eci(object):
	Position=[]
	Velocity=[]


file_list = ('amateur.txt','noaa.txt','stations.txt')


#Sat Data
print "Do you want to update the Satellite Data?[Y/n]"
update = raw_input()

if update == 'Y'or update == 'y':
  for i in file_list:
    r=requests.get("http://www.celestrak.com/NORAD/elements/"+i)
    with open(sys.path[0]+"/"+i, "wb") as code:
     code.write(r.content)



print "Please enter the name of the Satellite:"
name = str.upper(raw_input())

for i in range(3):
  for i in range(len(file_list)):
    f = open(sys.path[0]+"/"+file_list[i],"r")
    while True:
      line=f.readline()
      if line.find(name) != -1:
        line1 = f.readline()[0:68]
        line2 = f.readline()[0:68]
        f.close()
        break
      if line == "":
        break
    if ('line1' in dir())==False and i==len(file_list)-1:
      print "No date about this Sat.Please Enter The Correct Sat Name."
      name = str.upper(raw_input())


'''
#Sat Data
line1 = ('1 07530U 74089B   18146.86533424 -.00000045  00000-0 -12660-5 0  9999')
line2 = ('2 07530 101.6853 114.5065 0012343  18.5684  35.1273 12.53632685991694')
'''

satellite = twoline2rv(line1, line2, wgs72)


eciSat  = Eci()



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
