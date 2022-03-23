import sys, pygame

from src import functions, constants, level


clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode(constants.WINDOWSIZE, 0, 32)

level3 = level.Level3(clock, screen, "map/level_3/map_0.txt", constants.level3_tile_image_list)


while True:
    level3.game()