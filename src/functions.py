import pygame, sys
from pygame.locals import *



global frames_per_second
global flip

##Constants
frames_per_second = 30
flip = False

def is_divisible(Dividend, Divisor):
    if ((Dividend % Divisor) != 0):
        return False
    else:
        return True

def renderImageCartesian(display, pygame_image, cartesian_coordinates):
    display.blit(pygame_image,cartesian_coordinates)

def is_positive(value):
    if value > 0:
        return True
    if value < 0:
        return False
def false_to_true(bool):
    if bool == True:
        return False
    if bool == False:
        return True

#Want: Input: base folder of animations, desired length of each animation output: animation for given frame
#is meant only to be called once
#Returns normal animation list, flipped lisst, and jumped list
def process_animations(animation_base_path, extentiontype, second_durations):
    animation_name = animation_base_path.split("/")[-1]
    animation_rawpath = []
    animation_id = []
    frame_durations = []
    animation_list = []
    animation_list_flipped = []

    n = 0
    for item in second_durations:
        frame_durations.append((second_durations[n]*frames_per_second))
        n += 1


    for frame in range(len(frame_durations)):
        animation_rawpath.append(animation_base_path + "/" + animation_name + "_%s" + extentiontype %frame)

    n = 0
    for image in animation_rawpath:
        animation_id.append(animation_rawpath[n])
        n += 1

    n = 0
    for duration in frame_durations:
        for frame in range(duration):
            animation_list.append(pygame.image.load(animation_id[n]))
        n += 1

    n = 0
    for duration in frame_durations:
        for frame in range(duration):
            animation_list_flipped.append(pygame.transform.flip(pygame.image.load(animation_id[n]),True,False))
        n += 1

    return animation_list, animation_list_flipped, pygame.image.load(animation_base_path + "/" + animation_name + "_jump" + extentiontype)


#set equal to frame rate (init frame rate at 0
def load_object_animations(screen, frame, flip, animation_list, animation_list_flipped, jump_animation, objectmovementxy, objectxy):
    if flip == False:
        if objectmovementxy[1] != 0:
            screen.blit(jump_animation, objectxy)
        else:
            screen.blit(animation_list[frame], objectxy)
    if flip == True:
        if objectmovementxy[1] != 0:
            screen.blit(pygame.transform.flip(jump_animation,True,False), objectxy)
        else:
            screen.blit(animation_list_flipped[frame], objectxy)


    if objectmovementxy[0] > 0:
        flip = False
    if objectmovementxy[0] < 0:
        flip = True
    frame += 1
    if frame >= len(animation_list):
        frame = 0
    return frame, flip


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

