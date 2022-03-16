import sys, pygame

from pygame.locals import *

class Mobs:

    def __init__(self, pygameImage, is_hostile):
        self.pygameImage = pygameImage
        self.is_hostile = is_hostile