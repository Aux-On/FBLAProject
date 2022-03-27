import sys, pygame

from src import functions, constants, level


clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode(constants.WINDOWSIZE, 0, 32)

level1 = level.Level1(clock, screen, "map/level_3/map_1.txt", constants.level1_tile_image_list)
level3 = level.Level3(clock, screen, "map/level_3/map_0.txt", constants.level3_tile_image_list)


def game_index_cycle():
    constants.game_index += 1
    if constants.game_index > 1:
        constants.game_index = 0

while True:
    if constants.game_index == 0:
        level3.game()
        game_index_cycle()
    if constants.game_index == 1:
        level1.game()
        game_index_cycle()