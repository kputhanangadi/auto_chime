import pygame
from pathlib import Path
import os
import threading

def play_sound():
	pygame.init()

	file_path = os.path.abspath('/home/pi/Desktop/auto_chime/rpi/sample.wav')

	chime = pygame.mixer.Sound(file_path)

	playing = chime.play()

	while playing.get_busy():
		pygame.time.delay(100)

def main():
	thread = threading.Thread(target=play_sound)

	thread.start()

	return thread

if __name__ == "__main__":
	main()
