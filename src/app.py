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

menu = Menu(clock,screen,backgrd_img,img_2,img_3)
level3 = Level3(clock,screen,player_image,"map/level_3/map_1.txt",dirt_image,grass_image,16)


def game(image_index,screen):
    pygame.display.set_caption("Le Pygame Window!!")
    pygame.mixer.music.load("sounds/music/SYKO_music.wav")
    pygame.mixer.music.play(-1)
    running = True
    while running:

        if image_index == 6:
            image_index = 0
        if image_index == 0:
            screen.fill((0,0,0))
            screen.blit(backgrd_img, (0, 0))
            image_index += 1
        if image_index == 2:
            screen.fill((0,0,0))
            screen.blit(img_2, (0, 0))
            image_index += 1
        if image_index == 4:
            screen.fill((0,0,0))
            screen.blit(img_3, (0, 0))
            image_index += 1


        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    image_index += 1
                if event.key == K_ESCAPE:
                    running = False
                    return 0


        pygame.display.update()
        clock.tick(60)



while True:


    if game_index == 0:
        pygame.mixer.quit()
        game_index = menu.main_menu((130,170), (130,220))
    if game_index == 1:
        pygame.mixer.init()
        game_index = game(image_index,screen)
    if game_index == 2:
        game_index = 0



