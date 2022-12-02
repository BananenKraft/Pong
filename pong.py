import sys
import pygame
import math
from settings import Settings
from bat import Bat
from ball import Ball

def run_game():

    # Define settings
    input_settings = input("Please input your desired screen heigth and width in this format: width,heigth: ")
    settings = Settings()
    if input_settings != "d":
        input_settings = input_settings.split(",")
        settings.screen_width = input_settings[0]
        settings.screen_height = input_settings[1]
    speed = 1

    # Innit game and screen, bats, and listener
    pygame.init()
    screen = pygame.display.set_mode((int(settings.screen_width), int(settings.screen_height)))
    pygame.display.set_caption("Pong")
    background_color = (30,30,30)
    bat = Bat(screen, 30,50)
    enemy_bat = Bat(screen, screen.get_width()-30, 50)
    ball = Ball(screen, math.ceil(settings.screen_width/2), math.ceil(settings.screen_height/2))
    moveDown, moveUp = False, False


    #Main game loop
    while True:

        # Check for inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    moveDown = True
                if event.key == pygame.K_UP:
                    moveUp = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    moveDown = False
                if event.key == pygame.K_UP:
                    moveUp = False

        # Move bat
        if moveUp and bat.rect.top > 0:
            bat.move(-1)
        if moveDown and bat.rect.bottom < settings.screen_height:
            bat.move(1) 
                    
        # Update screen
        screen.fill(background_color)
        ball.drawCurrent()
        bat.drawCurrent()
        enemy_bat.drawCurrent()
        pygame.display.flip()

run_game()
