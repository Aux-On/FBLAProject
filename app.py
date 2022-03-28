import sys, pygame

from src import functions, constants, level


clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode(constants.WINDOWSIZE, 0, 32)
display = pygame.Surface(constants.surface_size)

level1 = level.Level1(clock, screen, "map/level_3/map_1.txt", constants.level1_tile_image_list)
level3 = level.Level3(clock, screen, "map/level_3/map_0.txt", constants.level3_tile_image_list)

##### Main Menu

menu_image_raw = pygame.image.load("images/Template.jpg")
yfactor = display.get_height()/menu_image_raw.get_height()
menu_image = pygame.transform.scale(menu_image_raw,[menu_image_raw.get_width()*yfactor,menu_image_raw.get_width()*yfactor])

button1_image = pygame.transform.scale(pygame.image.load("images/button1.jpg"),[pygame.image.load("images/button1.jpg").get_width()*yfactor,pygame.image.load("images/button1.jpg").get_height()*yfactor])
button2_image = pygame.transform.scale(pygame.image.load("images/button2.jpg"),[pygame.image.load("images/button2.jpg").get_width()*yfactor,pygame.image.load("images/button2.jpg").get_height()*yfactor])


base_button_location = [13.2,18]
adjusted_button_location = [base_button_location[0]*yfactor,base_button_location[1]*yfactor]

click = False

surface_scale_factor = [constants.WINDOWSIZE[0]/constants.surface_size[0],constants.WINDOWSIZE[1]/constants.surface_size[1]]


pygame.mixer.music.load("sounds/music/WS-Calm-flat-_1.wav")
pygame.mixer.music.play(-1)
while True:
    display.fill((menu_image.get_at((1,1))[0],menu_image.get_at((1,1))[1],menu_image.get_at((1,1))[2]))
    display.blit(menu_image,[(display.get_width()/2)-(menu_image.get_width()/2),0])

    mx,my = pygame.mouse.get_pos()

    print(surface_scale_factor)

    button_rect = pygame.rect.Rect(adjusted_button_location[0]*surface_scale_factor[0],adjusted_button_location[1]*surface_scale_factor[1],button1_image.get_width()*yfactor*surface_scale_factor[0],button1_image.get_height()*surface_scale_factor[1])
    if button_rect.collidepoint(mx,my):
        menu_image.blit(button2_image,adjusted_button_location)
        if click:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load("sounds/music/Torn_1.wav")
            pygame.mixer.music.play(-1)
            click = False
            level1.game()
    else:
        menu_image.blit(button1_image,adjusted_button_location)




    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                click = False

    surf = pygame.transform.scale(display, constants.WINDOWSIZE)
    screen.blit(surf, (0, 0))
    pygame.display.update()
    clock.tick(constants.game_frames_per_second)



# def game_index_cycle():
#     constants.game_index += 1
#     if constants.game_index > 1:
#         constants.game_index = 0
#
# while True:
#     if constants.game_index == 0:
#         level3.game()
#         game_index_cycle()
#     if constants.game_index == 1:
#         level1.game()
#         game_index_cycle()