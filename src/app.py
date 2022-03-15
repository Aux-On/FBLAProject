import sys

import os

import playsound

import pygame

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()

pygame.display.set_caption("Le Pygame Window!!")

#HERE YOU CAN CHANGE THE IMAGE UR SOURCING
backgrd_img = pygame.image.load("images/Rengoku.jpg")
img_2 = pygame.image.load("images/cube.jpg")
img_3 = pygame.image.load("images/gojo.jpg")


#CAN CHANGE WINDOW SIZE (WIDTH , HEIGHT)
WINDOW_SIZE = (backgrd_img.get_width(), backgrd_img.get_height())


screen = pygame.display.set_mode(WINDOW_SIZE,0,32)

pygame.mixer.music.load("sounds/music/SYKO_music.wav")
pygame.mixer.music.play(1)


image_index = 0

while True:

    print(image_index)

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


    pygame.display.update()
    clock.tick(60)


