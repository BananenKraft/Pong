import sys
import pygame
from settings import Settings
from bat import Bat
from listener import Listener

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
    screen.fill(background_color)
    mainlistener = Listener()
    bat = Bat(screen, 20,20)
    enemy_bat = Bat(screen, settings.screen_width-50, 20)

    #Main game loop
    while True:

        mainlistener.checkEvents()
        pygame.display.flip()

run_game()
    
    