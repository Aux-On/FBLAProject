import os
import sys, pygame
#from src import functions, mobs, level

game_frames_per_second = 15

WINDOWSIZE = (900,600)
scale_Window_by = 5
# if 5, SS = [180,120]
surface_size = (WINDOWSIZE[0]/scale_Window_by,WINDOWSIZE[1]/scale_Window_by)

#listed as [scrollfactorx,scrollfactory,x,y,xdem,ydem]
level_3_background = []


level3_tile_image_list = [pygame.image.load('images/level_3/map/Dirt1.jpg'),pygame.image.load('images/level_3/map/Grass1.jpg')]

level3_collidable_indexs = [1,2,3]

