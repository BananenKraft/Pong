import sys
import pygame
from settings import Settings
from bat import Bat

def run_game():

    # Define settings
    input_settings = input("Please input your desired screen heigth and width in this format: width,heigth: ")
    settings = Settings()
    if input_settings != "d":
        input_settings = input_settings.split(",")
        settings.screen_width = input_settings[0]
        settings.screen_height = input_settings[1]

    # Innit game and screen, bats, and listener
    pygame.init()
    screen = pygame.display.set_mode((int(settings.screen_width), int(settings.screen_height)))
    pygame.display.set_caption("Pong")
    background_color = (30,30,30)
    bat = Bat(screen, 30,50)
    enemy_bat = Bat(screen, screen.get_width()-30, 50)

    #Main game loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    bat.move(-10)
                if event.key == pygame.K_UP:
                    bat.move(10)
                    print("Done")
                    
        screen.fill(background_color)
        bat.drawCurrent()
        enemy_bat.drawCurrent()
        pygame.display.flip()

run_game()
