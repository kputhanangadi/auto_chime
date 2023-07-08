import pygame

pygame.init()

chime = pygame.mixer.Sound("rpi/chime.wav")

playing = chime.play()

while playing.get_busy():
    pygame.time.delay(100)
