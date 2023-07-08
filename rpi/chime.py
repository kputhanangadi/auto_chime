import pygame

def main():

	pygame.init()

	file_path = 'chime.wav'

	chime = pygame.mixer.Sound(file_path)

	playing = chime.play()

	while playing.get_busy():
		pygame.time.delay(100)

if __name__ == "__main__":
	main()
