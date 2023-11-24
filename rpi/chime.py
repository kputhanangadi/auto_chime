import pygame

def main():

	pygame.init()

	file_path = 'chime.wav'

	chime = pygame.mixer.Sound(file_path)

	playing = chime.play()

	# hi this is a comment from riyne :D

	while playing.get_busy():
		pygame.time.delay(100)

if __name__ == "__main__":
	main()
