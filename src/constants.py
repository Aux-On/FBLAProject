import os
import sys, pygame
#from src import functions, mobs, level

game_frames_per_second = 90

WINDOWSIZE = (900,600)
scale_Window_by = 5
# if 5, SS = [180,120]
surface_size = (WINDOWSIZE[0]/scale_Window_by,WINDOWSIZE[1]/scale_Window_by)


game_index = 0


#listed as [scrollfactorx,scrollfactory,x,y,xdem,ydem]
level_3_background = []

levels_as_list = ['main_menu','level_1','level_3']


level3_tile_image_list = [pygame.image.load('images/level_3/map/Dirt1.jpg'),pygame.image.load('images/level_3/map/Grass1.jpg')]

level1_tile_image_list = [pygame.image.load('images/level_1/map/caveeee2.png'),pygame.image.load('images/level_1/map/caveee1.png'), "2", "3"]

level3_collidable_indexs = [1,2,3]

