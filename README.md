# SGP4_SAT_TRACKER
Author: BG6WRI  
Email: <bg6wri@gmail.com>  

## wri_sattrack
Run successfully on both Linux & Windows.  
Just python it!  

```
$ sudo pip install sgp4 jdcal pyserial requests  
$ python wri_sattrack.py  
```
Follow the guide to enter the name of the Sat you want to track and enter your Coordinates.  

You can change the code to make the data output by `print()` or `ser.write()` .

## GUI Version
In order to use this program in both Opration Systems  
Some code shoule be changed by user.
```
$ sudo pip install sgp4 jdcal pyserial requests 
$ sudo apt-get install python-tk  
$ python GUI.py  
```
Output Mode include Screen,Serial,or both of them.  
You can choose it freely. 

## sat_tracker
Use SGP4 model,HMC5883L and MMA8452Q on Raspberry Pi  
```
$ sudo pip install sgp4 jdcal python-pyserial requests  
$ python track.py
```