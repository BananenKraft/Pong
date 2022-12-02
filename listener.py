import pygame
from bat import Bat


class Listener:

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.K_DOWN:
                pass
