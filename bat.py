import pygame
import math

class Bat:

    def __init__(self, screen, startX, startY, speed, width=20, height=80):
        self.startX = startX-(math.ceil(width/2))
        self.startY = startY-(math.ceil(height/2))
        self.screen = screen
        self.speed = speed
        self.width = width
        self.height = height
        self.rect = self.drawCurrent()

    def drawCurrent(self):
        self.rect = pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(self.startX, self.startY, self.width, self.height))
        return self.rect

    def move(self, down):
        if down:
            self.startY += self.speed
        else:
            self.startY -= self.speed
