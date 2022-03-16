import pygame, sys

from pygame.locals import *



class Menu:

    def __init__(self, clock, surface, background_img, buttonInitImg, buttonFinalImg):
        self.surface = surface
        self.background_img = background_img
        self.buttonInitImg = buttonInitImg
        self.buttonFinalImg = buttonFinalImg
        self.clock = clock

    def main_menu(self, location_b1, location_b2):

        index = 0

        click = False
        running = True
        while running:
            self.surface.blit(self.background_img,(0,0))

            mx,my = pygame.mouse.get_pos()

            button_1 = pygame.Rect(location_b1[0], location_b1[1], self.buttonInitImg.get_width(), self.buttonInitImg.get_height())
            self.surface.blit(self.buttonInitImg,location_b1)

            if button_1.collidepoint(mx,my):
                self.surface.blit(self.buttonFinalImg, location_b1)
                if click:
                    running = False
                    index = 1
                    return index

            button_2 = pygame.Rect(location_b2[0], location_b2[0], self.buttonInitImg.get_width(), self.buttonInitImg.get_height())
            self.surface.blit(self.buttonInitImg, location_b2)

            if button_2.collidepoint(mx,my):
                self.surface.blit(self.buttonFinalImg, location_b2)
                if click:
                    running = False
                    index = 2
                    return index

            click = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            self.clock.tick(60)
