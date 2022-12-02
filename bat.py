import pygame
import math

class Bat:

    def __init__(self, screen, startX, startY, width=30, heigth=70):
        self.startX = startX-(math.ceil(startX/2))
        self.startY = startY-(math.ceil(startY/2))
        self.screen = screen
        self.rect = pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(startX, startY, width, heigth))
