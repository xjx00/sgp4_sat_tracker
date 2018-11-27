#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
import sys
import time
import jdcal
import serial
import GetUserData
import GetSat
import GetLook
import threading


def start():

	Sat=e1.get()
	Lon=float(e2.get())
	Lat=float(e3.get())
	kmAlt=float(e4.get())
	
	global AZ,EL
	AZ=0
	EL=0

	if mode.get() == 2 or mode.get() == 3 :
		if sys.platform == "linux2":
			ser=serial.Serial("COM"+e5.get(),9600,timeout=0.5)
		if sys.platform == "win32":
			ser=serial.Serial("/dev/ttyUSB"+e5.get(),9600,timeout=0.5)


	print "You are tracking "+str.upper(Sat)+"."
	print "You are at Lon: "+str(Lon)+" Lat: "+str(Lat)+" Altitude "+str(kmAlt)+"."

	line1,line2,Lat,Lon,kmAlt = GetUserData.get_user_data("gui",Sat,Lon,Lat,kmAlt)
	GetSat.generate(line1,line2)
	GetLook.generate(Lat,Lon,kmAlt)

	global timer
	timer = threading.Timer(1, fun_timer)
	timer.start()


def stop():
	if timer.is_alive():
		timer.cancel()

def update():
	GetUserData.update("gui")

def fun_timer():

	timer = threading.Timer(0.1, fun_timer)
	timer.start()

	if mode.get() == 1 or mode.get()==3 :

		AZ_flash.set(str(AZ))
		EL_flash.set(str(EL))

	if mode.get() == 2 or mode.get() ==3 :
		ser.write(AZ,EL)

	while True:
		eciSat = GetSat.get_eciSat()
		tl = time.gmtime(time.time())
		date_now_julian = sum(jdcal.gcal2jd(tl.tm_year,tl.tm_mon,tl.tm_mday))+tl.tm_hour/24.0+tl.tm_min/24.0/60.0+tl.tm_sec/24.0/3600.0
		AZ,EL = GetLook.GetLook(date_now_julian,eciSat)
	




root = Tk()
root.title("WRI_Sat_Tracker")
root.wm_minsize(400, 360) 
if sys.platform == "win32":
	root.iconbitmap(sys.path[0]+"/radio.ico")


#Button
ButtonStart = Button(	root, text="Start",			command=start)
ButtonStop = Button(	root, text="Stop",			command=stop)
ButtonUpdate = Button(	root, text="Update Data",	command=update)
#ButtonUpdate = Button(	root, text="Update Data",	command=lambda:update)


ButtonStart.grid(   row=0, column=0, padx=30, pady=5)
ButtonStop.grid(    row=0, column=1, padx=20, pady=5)
ButtonUpdate.grid(  row=0, column=2, padx=20, pady=5)


#UserData
Label(root, text="Sat Name:").grid(		row=1)
Label(root, text="Lon:").grid(			row=2)
Label(root, text="Lat:").grid(			row=3)
Label(root, text="kmAlt:").grid(		row=4)
Label(root, text="kmAlt:").grid(		row=4)
Label(root, text="Serial COM").grid(	row=4, column=2)


e1 = Entry(root, width=10)
e2 = Entry(root, width=10)
e3 = Entry(root, width=10)
e4 = Entry(root, width=10)
e5 = Entry(root, width=10)

e1.insert(0,"SO-50")
e2.insert(0,"30")
e3.insert(0,"30")
e4.insert(0,"0")

e1.grid(row=1, column=1, padx=20, pady=5)
e2.grid(row=2, column=1, padx=20, pady=5)
e3.grid(row=3, column=1, padx=20, pady=5)
e4.grid(row=4, column=1, padx=20, pady=5)
e5.grid(row=5, column=2, padx=20, pady=5)

#Joke
Label(root, text="Author:BG6WRI").grid(	row=7, column=2)
ButtonJoke = Button(root, text="一键日卫星", command=lambda:var.set("和我没关系啊，你找OpenATS去"))
ButtonJoke.grid(row=8, column=2)
var = StringVar()
Label(root, textvariable=var).grid(	row=9, column=2)


#Output

#Scereen Ready
Label(root,text="AZ").grid(row=5,column=0)
Label(root,text="EL").grid(row=5,column=1)
AZ_flash=IntVar()
EL_flash=IntVar()
Entry(root, textvariable=AZ_flash, width=10).grid(row=6, column=0)
Entry(root, textvariable=EL_flash, width=10).grid(row=6, column=1)

#Mode Choose
group = LabelFrame(root, text="Output Mode", padx=5, pady=5)
group.grid(row=1, column=2, padx=10, pady=10, rowspan=3)
LANGS = [("Screen", 1), ("Serial", 2),("Both", 3)]

mode = IntVar()
mode.set(1)

for lang, num in LANGS:
	b = Radiobutton(group, text=lang, variable=mode, value=num)
	b.pack(anchor=W)




root.mainloop()
