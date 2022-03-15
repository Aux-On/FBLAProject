import sys

from src.Menu import Menu

import pygame

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()

#HERE YOU CAN CHANGE THE IMAGE UR SOURCING
backgrd_img = pygame.image.load("images/Template.jpg")
img_2 = pygame.image.load("images/button2.jpg")
img_3 = pygame.image.load("images/button1.jpg")


#CAN CHANGE WINDOW SIZE (WIDTH , HEIGHT)
WINDOW_SIZE = (backgrd_img.get_width(), backgrd_img.get_height())


screen = pygame.display.set_mode(WINDOW_SIZE,0,32)

image_index = 0

game_index = 0

menu = Menu(screen,backgrd_img,img_2,img_3)


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
        game_index = menu.main_menu(clock,(13,17), (13,22))
    if game_index == 1:
        pygame.mixer.init()
        game_index = game(image_index,screen)




