import pygame, sys

from pygame.locals import *

def renderImageCartesian(display, pygame_image, cartesian_coordinates):
    display.blit(pygame_image,cartesian_coordinates)

def load_animations(animation_base_path, frame_durations):
    animation_name = animation_base_path.split("/")[-1]
    animation_fram_data = []

def read_map(path):
    file = open(path, 'r')
    game_map = []
    map = []
    i = -1
    j = []
    for line in file:
        game_map.append(list(line))
        i += 1
        j.append(i)
    for k in j:
        for thing in game_map[k]:
            if thing == "\n":
                game_map[k].remove("\n")
    file.close()
    return game_map

def to_textfile(matrix, file_path):
    line_string = ''
    file = open(file_path,'a')
    for row in matrix:
        line_string = ''
        for col in row:
            line_string = line_string + col
        file.write(line_string + "\n")
    file.close()

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles): #player rect, its (x,y), and potential collistions
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

