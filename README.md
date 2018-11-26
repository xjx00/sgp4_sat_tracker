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

## sat_tracker
Use SGP4 model,HMC5883L and MMA8452Q on Raspberry Pi  
```
$ sudo pip install sgp4 jdcal python-pyserial requests  
$ python track.py
```