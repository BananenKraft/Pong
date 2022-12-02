import pygame
import math

class Bat:

    def __init__(self, screen, startX, startY, width=30, height=70):
        self.startX = startX-(math.ceil(width/2))
        self.startY = startY-(math.ceil(height/2))
        self.screen = screen
        self.width = width
        self.height = height
        self.rect = self.drawCurrent()

    def drawCurrent(self):
        self.rect = pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(self.startX, self.startY, self.width, self.height))
        return self.rect

    def move(self,y):
        self.startY += y
        return self.rect