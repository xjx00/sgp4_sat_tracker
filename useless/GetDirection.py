#!/usr/bin/python
# -*- coding: utf-8 -*-


import GetSat
import GetLook
import time
import jdcal



def GetDirection( AZ_old , AZ , EL_old , EL):


	if(AZ > AZ_old):
		Direction_x = '1'
	else:
		Direction_x = '0'

	if(EL > EL_old):
		Direction_y = '1'
	else:
		Direction_y = '0'

	return Direction_x,Direction_y