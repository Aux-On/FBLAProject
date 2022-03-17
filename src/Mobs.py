import sys, pygame

from pygame.locals import *

class Mobs:

    def __init__(self, pygameImage, is_hostile, is_collidable):
        self.pygameImage = pygameImage
        self.is_hostile = is_hostile
        self.is_collidable = is_collidable


class Slime(Mobs):

    def __init__(self):

    pass