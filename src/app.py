import sys

import pygame

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()

pygame.display.set_caption("Le Pygame Window!!")

#HERE YOU CAN CHANGE THE IMAGE UR SOURCING
backgrd_img = pygame.image.load("images/Rengoku.jpg")


#CAN CHANGE WINDOW SIZE (WIDTH , HEIGHT)
WINDOW_SIZE = (backgrd_img.get_width(), backgrd_img.get_height())


screen = pygame.display.set_mode(WINDOW_SIZE,0,32)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()



    screen.blit(backgrd_img, (0,0))

    pygame.display.update()
    clock.tick(60)


