import pygame

class Ball:

    def __init__(self, screen, startX, startY) -> None:
        self.screen = screen
        self.startX = startX
        self.startY = startY
        self.circle = self.drawCurrent()
    
    def drawCurrent(self):
        self.circle = pygame.draw.circle(self.screen, (255,255,255), (self.startX, self.startY), 10)
        return self.circle