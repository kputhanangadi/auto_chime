import pygame

def main():

	pygame.init()

	file_path = 'sample.wav'

	chime = pygame.mixer.Sound('sample.wav')

	playing = chime.play()

	while playing.get_busy():
		pygame.time.delay(100)

if __name__ == "__main__":
	main()
