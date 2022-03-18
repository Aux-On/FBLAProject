import sys

from src.Menu import Menu
from src.Level3 import Level3

import pygame

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()

#HERE YOU CAN CHANGE THE IMAGE UR SOURCING
backgrd_img = pygame.transform.scale(pygame.image.load("images/Template.jpg"),(720,640))
img_2 = pygame.transform.scale(pygame.image.load("images/button2.jpg"),(380,40))
img_3 = pygame.transform.scale(pygame.image.load("images/button1.jpg"),(380,40))


#CAN CHANGE WINDOW SIZE (WIDTH , HEIGHT)
WINDOW_SIZE = (backgrd_img.get_width(), backgrd_img.get_height())


screen = pygame.display.set_mode(WINDOW_SIZE,0,32)

image_index = 0

game_index = 0

player_image = pygame.image.load("images/level_3/Guyy/idle/Guyy_0.png")
dirt_image = pygame.image.load("images/Dirt1.jpg")
grass_image = pygame.image.load("images/Grass1.jpg")

menu = Menu(clock,screen,backgrd_img,img_2,img_3)

level3 = Level3(clock,screen,player_image,"map/level_3/map_0.txt",dirt_image,grass_image,16)





while True:


    if game_index == 0:
        #pygame.mixer.quit()
        game_index = menu.main_menu((130,170), (130,220))
    if game_index == 1:
        pygame.mixer.init()
        game_index = level3.level3(game_index)

    if game_index == 2:
        game_index = 0



