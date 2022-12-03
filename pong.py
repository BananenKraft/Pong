import sys
import pygame
import math
from settings import Settings
from bat import Bat
from ball import Ball
from random import *

def run_game():

    # Define settings
    input_settings = input("Please input your desired screen heigth and width in this format: width,heigth: ")
    settings = Settings()
    if input_settings != "d":
        input_settings = input_settings.split(",")
        settings.screen_width = input_settings[0]
        settings.screen_height = input_settings[1]


    # Innit game variables and screen, bats, and listener
    pygame.init()
    screen = pygame.display.set_mode((int(settings.screen_width), int(settings.screen_height)))
    pygame.display.set_caption("Pong")
    background_color = (30,30,30)
    bat = Bat(screen, 30,50, 0)
    enemy_bat = Bat(screen, screen.get_width()-30, 50, 0)
    ball = Ball(screen,math.ceil(settings.screen_width/2), math.ceil(settings.screen_height/2), 0, 0)
    clock = pygame.time.Clock()
    moveDown, moveUp = False, False
    playerScore, enemyScore = 0,0



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
                if event.key == pygame.K_s:
                    ball.speedX, ball.speedY, bat.speed, enemy_bat.speed = -6, -6, 6, 6
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    moveDown = False
                if event.key == pygame.K_UP:
                    moveUp = False

        # Move bat
        if moveUp and bat.rect.top > 0:
            bat.move(False)
        if moveDown and bat.rect.bottom < settings.screen_height:
            bat.move(True) 

        # Check for ball collision
        if ball.circle.top == 0 or ball.circle.bottom == settings.screen_height:
            ball.speedY *= -1
        if bat.rect.colliderect(ball.circle):
            ball.speedX *= randint(100,110)*-0.01
            ball.speedY *= randint(100,110)*0.01
            ball.startX += 10
        if enemy_bat.rect.colliderect(ball.circle):
            ball.speedX *= randint(100,110)*-0.01
            ball.speedY *= randint(100,110)*0.01
            ball.startX -= 10

        # Check for score
        if ball.circle.left < 0:
            enemyScore += 1
            ball.reset()
        if ball.circle.right > settings.screen_width:
            playerScore += 1
            ball.reset()
            

        # Make opponent move
        if enemy_bat.rect.centery < ball.circle.centery:
            enemy_bat.move(True)
        if enemy_bat.rect.centery > ball.circle.centery:
            enemy_bat.move(False)
                    
        # Update screen
        clock.tick(60)
        screen.fill(background_color)
        ball.move()
        ball.drawCurrent()
        bat.drawCurrent()
        enemy_bat.drawCurrent()
        pygame.display.flip()

run_game()
