import pygame, sys

from pygame.locals import *
from src import constants, functions



class Menu:

    def __init__(self, clock):
        # self.surface = surface
        # self.background_img = background_img
        # self.buttonInitImg = buttonInitImg
        # self.buttonFinalImg = buttonFinalImg
        self.clock = clock

    # def main_menu(self, location_b1, location_b2):
    #
    #     index = 0
    #
    #     click = False
    #     running = True
    #     while running:
    #         self.surface.blit(self.background_img,(0,0))
    #
    #         mx,my = pygame.mouse.get_pos()
    #
    #         button_1 = pygame.Rect(location_b1[0], location_b1[1], self.buttonInitImg.get_width(), self.buttonInitImg.get_height())
    #         self.surface.blit(self.buttonInitImg,location_b1)
    #
    #         if button_1.collidepoint(mx,my):
    #             self.surface.blit(self.buttonFinalImg, location_b1)
    #             if click:
    #                 running = False
    #                 index = 1
    #                 return index
    #
    #         button_2 = pygame.Rect(location_b2[0], location_b2[0], self.buttonInitImg.get_width(), self.buttonInitImg.get_height())
    #         self.surface.blit(self.buttonInitImg, location_b2)
    #
    #         if button_2.collidepoint(mx,my):
    #             self.surface.blit(self.buttonFinalImg, location_b2)
    #             if click:
    #                 running = False
    #                 index = 2
    #                 return index
    #
    #         click = False
    #
    #         for event in pygame.event.get():
    #             if event.type == QUIT:
    #                 sys.exit()
    #             if event.type == MOUSEBUTTONDOWN:
    #                 if event.button == 1:
    #                     click = True
    #
    #         pygame.display.update()
    #         self.clock.tick(30)

    def pause_return_running(self, display, screen):
        game_index_current = constants.game_index
        running = True
        click = False
        frames_ran = 0
        while running:

            mx, my = pygame.mouse.get_pos()

            button_1 = pygame.Rect(constants.WINDOWSIZE[0]/4,constants.WINDOWSIZE[1]/4,constants.WINDOWSIZE[0]/4,constants.WINDOWSIZE[1]/4)
            pygame.draw.rect(display, (100, 95, 124), button_1)


            if button_1.collidepoint(mx,my):
                if click == True:
                    running = False
                    #constants.game_index = (functions.return_list_Index(constants.levels_as_list,'level_3')-1)
                    if game_index_current == constants.game_index:
                        print("src/functions Line 75: Element not within list")
                    return False

            if frames_ran == 0:

                for y in range(display.get_height()):

                    for x in range(display.get_width()):
                        color = display.get_at((x,y))
                        fc = []
                        for col in color:
                            if col-50 < 0:
                                fc.append(50)
                            else:
                                fc.append(col-50)

                        display.set_at((x,y), (fc[0], fc[1],fc[2]))



            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            frames_ran += 1
            surf = pygame.transform.scale(display, constants.WINDOWSIZE)
            screen.blit(surf, (0, 0))
            pygame.display.update()
            self.clock.tick(constants.game_frames_per_second)





