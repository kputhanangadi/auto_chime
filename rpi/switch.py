import RPi.GPIO as GPIO
from time import sleep
from chime import main as chime

GPIO.setmode(GPIO.BCM)

switch_pin = 2

GPIO.setup(switch_pin, GPIO.IN)

playing = False

while True: 
	if not GPIO.input(switch_pin):
		thread = chime()
GPIO.cleanup()
