import sys, pygame

from src import functions, constants, level


clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode(constants.WINDOWSIZE, 0, 32)
display = pygame.Surface(constants.surface_size)
#this is for the screen

level1 = level.Level1(clock, screen, "map/level_3/map_1.txt", constants.level1_tile_image_list)
level3 = level.Level3(clock, screen, "map/level_3/map_0.txt", constants.level3_tile_image_list)
#level2 = level.level2(clock, screen, "map/level_3/map_2.txt", constants.level2_tile_image_list)
#I assume making level 2 here :) level = class and refers to the map

##### Main Menu down there for image, so i bet i can make the intro and the leaderboard set up

menu_image = pygame.image.load("images/Menuu.png")


click = False

#music. seems to only apply to main menu? -1 = forever, which is probably what we will stick to
pygame.mixer.music.load("sounds/music/Victor.mp3")
pygame.mixer.music.play(-1)


game_index = "Level_1"

while True:
    display.fill((menu_image.get_at((1,1))[0],menu_image.get_at((1,1))[1],menu_image.get_at((1,1))[2]))
    display.blit(menu_image,[0,0])

    mx,my = pygame.mouse.get_pos()
    mx = mx/5
    my = my/5

    #print((mx,my))
#how to make buttons, let's make intro and leaderboard here... and exit?
    button1_rect = pygame.rect.Rect(75,58,25,9)
    if button1_rect.collidepoint(mx,my):
        display.blit(pygame.image.load("images/playy.png"), [75,58])
        if click:
            click = False
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
#music to add per map
            if game_index == "Level_1":
                ##Level 1 MUSIC
                pygame.mixer.music.load("sounds/music/McAfee.mp3")
                pygame.mixer.music.play(-1)
                game_index = level1.game()
                # Reloading menu music
                pygame.mixer.music.load("sounds/music/Victor.mp3")
                pygame.mixer.music.play(-1)
            if game_index == "Level_2":
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                #game_index = level2.game()
            #Reloading menu music
            pygame.mixer.music.load("sounds/music/Victor.mp3")
            pygame.mixer.music.play(-1)

    button2_rect = pygame.rect.Rect(74,73,pygame.image.load("images/Intro.png").get_width(),pygame.image.load("images/Intro.png").get_height())
    if button2_rect.collidepoint(mx,my):
        display.blit(pygame.image.load("images/Intro.png"), [73,72])

    button3_rect = pygame.rect.Rect(52, 86, pygame.image.load("images/leaderboard.png").get_width(),
                                    pygame.image.load("images/leaderboard.png").get_height())
    if button3_rect.collidepoint(mx, my):
        display.blit(pygame.image.load("images/leaderboard.png"), [52, 86])

    button4_rect = pygame.rect.Rect(76, 101, pygame.image.load("images/exit.png").get_width(),
                                    pygame.image.load("images/exit.png").get_height())
    if button4_rect.collidepoint(mx, my):
        display.blit(pygame.image.load("images/exit.png"), [76, 101])
        if click:
            sys.exit()





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
#Above refers to levels, copy and paste for level 2?