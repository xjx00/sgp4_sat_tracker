# sgp4_sat_tracker
Use SGP4 model,HMC5883L and MMA8452Q on Raspberry Pi  
to calculate how the stepper motors should move  
and control the stepper motors  
to make the antenna follow the sat.  

# wri_sattrack
Run well on Linux(use UTC).  
Just python it!  

sudo pip install sgp4 jdcal python-pyserial requests
python wri_sattrack.py  

Follow the guide to enter the name of the Sat you want to follow  
and where you are.  

You can change the code to choose "print" or "ser.write".
