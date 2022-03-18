import pygame, functions, sys

from pygame.locals import *




scale_value = 3

class Level1:

    def __init__(self, clock, screen, pygame_player_image, game_map_path, pygame_cave_dirt_image, pygame_cave_image, TILE_SIZE):
        self.clock = clock
        self.screen = screen
        self.display = pygame.Surface((300,200))
        self.player_image = pygame_player_image
        self.game_map_path = game_map_path
        self.true_scroll = [0,0]
        self.TILE_SIZE = TILE_SIZE
        self.dirt_image = pygame_cave_dirt_image
        self.cave_image = pygame_cave_image

        self.jump_index = 0
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.player_dy = 0
        self.jump_index = 0
        self.air_timer = 0

        self.player_rect = pygame.Rect(1 * self.TILE_SIZE, 1 * self.TILE_SIZE, self.player_image.get_width(), self.player_image.get_height())
        self.game_map = functions.read_map(self.game_map_path)
        self.animation_list, self.animation_list_flipped, self.jump_image, self.animations_idle, self.animations_idle_flipped = functions.process_animations("images/level_3/Guyy",".png",[5],[5])

        self.moving_player_frame = 0
        self.idle_player_frame = 0
        self.flip_player = False

    def level1(self,game_index):

        running = True

        while running:
            self.display.fill((146, 244, 255))
            tile_rects = []

            self.true_scroll[0] += (self.player_rect.x - self.true_scroll[0] - 152) / 20
            self.true_scroll[1] += (self.player_rect.y - self.true_scroll[1] - 100) / 20
            scroll = self.true_scroll.copy()
            scroll[0] = int(self.true_scroll[0])
            scroll[1] = int(self.true_scroll[1])

            y = 0  # top pixel of screen
            for row in self.game_map:
                x = 0  # Left most pixel of screen
                for tile in row:
                    if tile == '1':
                        self.display.blit(self.dirt_image, (x * self.TILE_SIZE - scroll[0], y * self.TILE_SIZE - scroll[1]))
                    if tile == '2':
                        self.display.blit(self.cave_image, (x * self.TILE_SIZE - scroll[0], y * self.TILE_SIZE - scroll[1]))  # must multiply pixel location with tile width (so it moves smoothly)
                    # if tile == '4':
                    #    display.blit(cave_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE - scroll[1]))
                    if tile != '0' and tile != '4':
                        tile_rects.append(pygame.Rect(x * self.TILE_SIZE, y * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE))
                    x += 1
                y += 1

            player_movement = [0, 0]
            if self.moving_right:
                player_movement[0] += 1
            if self.moving_left:
                player_movement[0] -= 1
            if self.moving_up:
                player_movement[1] -= 1
            if self.moving_down:
                player_movement[1] += 1

            player_rect, collisions = functions.move(self.player_rect, player_movement, tile_rects)
            self.player_image.set_colorkey((255, 255, 255))

            #self.display.blit(self.player_image, (self.player_rect.x - scroll[0], self.player_rect.y - scroll[1]))

            self.moving_player_frame, self.idle_player_frame, self.flip_player = functions.load_object_animations(self.display,self.moving_player_frame,self.idle_player_frame,self.flip_player,self.animation_list,self.animation_list_flipped,self.jump_image,player_movement,(self.player_rect.x - scroll[0], self.player_rect.y - scroll[1]),self.animations_idle,self.animations_idle_flipped)
            print(self.idle_player_frame,self.moving_player_frame,self.flip_player)

            if collisions['bottom']:
                self.player_dy = 0
                self.jump_index = 0
                self.air_timer = 0
            else:
                self.air_timer += 1
            if collisions['top']:
                self.player_dy = 0

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        return game_index+1
                    #if event.key == K_q:
                        #if music_index == 0:
                            #pygame.mixer.quit()
                            #music_index = 1
                    if event.key == K_RIGHT:
                        self.moving_right = True
                    if event.key == K_LEFT:
                        self.moving_left = True
                    if event.key == K_UP:
                        self.moving_up = True
                    if event.key == K_DOWN:
                        self.moving_down = True
                if event.type == KEYUP:
                    if event.key == K_RIGHT:
                        self.moving_right = False
                    if event.key == K_LEFT:
                        self.moving_left = False
                    if event.key == K_UP:
                        self.moving_up = False
                    if event.key == K_DOWN:
                        self.moving_down = False

            surf = pygame.transform.scale(self.display, (720,640))
            self.screen.blit(surf,(0,0))
            pygame.display.update()
            self.clock.tick(functions.frames_per_second)

