import pygame

class Ball:

    def __init__(self, screen, startX, startY, speedX, speedY) -> None:
        self.screen = screen
        self.startX = startX
        self.startY = startY
        self.originX = startX
        self.originY = startY
        self.speedX = speedX
        self.speedY = speedY
        self.circle = self.drawCurrent()
    
    def drawCurrent(self):
        self.circle = pygame.draw.circle(self.screen, (255,255,255), (self.startX, self.startY), 10)
        return self.circle

    def move(self):
        self.startX += self.speedX
        self.startY += self.speedY
    
    def reset(self):
        self.startX = self.originX
        self.startY = self.originY
        self.speedX = 0
        self.speedY = 0