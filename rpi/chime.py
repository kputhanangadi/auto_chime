import pygame
from pathlib import Path
import os

def main():

	pygame.init()

	file_path = os.path.abspath('/home/pi/Desktop/auto_chime/rpi/sample.wav')

	chime = pygame.mixer.Sound(file_path)

	playing = chime.play()

	while playing.get_busy():
		pygame.time.delay(100)

if __name__ == "__main__":
	main()
