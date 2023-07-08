import RPi.GPIO as GPIO
from time import sleep
from chime import main as chime

GPIO.setmode(GPIO.BCM)

switch_pin = 2

GPIO.setup(switch_pin, GPIO.IN )

while True: 
	if not GPIO.input(switch_pin):
		print("Switch is HIGH")
		chime()
GPIO.cleanup()
