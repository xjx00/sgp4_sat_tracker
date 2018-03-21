import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
###GPIO.output(15,1)

x=GPIO.PWM(15,1600)
y=GPIO.PWM(16,1600)

x.start(1)
x.start(close)
