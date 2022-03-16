import pygame, sys

from pygame.locals import *

class Level3:

    def __init__(self, clock):
        self.clock = clock


    def level3(self):
        running = True
        while running:



            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        return 0

            pygame.display.update()
            self.clock.tick(60)

