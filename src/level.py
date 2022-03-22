import sys, pygame

from src import constants, mobs, functions

from pygame.locals import *

class Level:
    def __init__(self, clock, screen, game_map_location):
        self.clock = clock
        self.display = pygame.Surface(constants.surface_size)
        self.screen = screen
        self.player_image = 'images/level_3/Guyy'
        self.game_map_location = game_map_location
        self.TILESIZE = 16
        self.small_font = functions.Font('images/gui/small_font.png', (0,0,0))
        self.large_font = functions.Font('images/gui/large_font.png',(0,0,0))

    def dialogue_box(self,text, locationxy, quit_key_pygame):
        dialouge_surf = pygame.image.load("images/gui/lower_dialogue.png")
        box = pygame.image.load("images/gui/text_box.png")
        dialouge_surf.set_colorkey((0,0,0))

        running = True
        while running:
            self.small_font.render(dialouge_surf,text,(10,6))
            self.display.blit(dialouge_surf,locationxy)
            #dialouge_surf.blit(pygame.transform.scale(box, sizexy), (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == quit_key_pygame:
                        running = False
                        return False

            surf = pygame.transform.scale(self.display, constants.WINDOWSIZE)
            self.screen.blit(surf, (0, 0))
            pygame.display.update()
            self.clock.tick(constants.game_frames_per_second)



########################################################################################################################
#                                                    SUB CLASS
########################################################################################################################

class Level3(Level):
    def __init__(self, clock, display,game_map_location,pygame_tile_image_list):
        Level.__init__(self, clock, display,game_map_location)
        #super.__init__(clock,display,game_map_location)


        self.player = mobs.Player(self.player_image,True, [50,50],self.display,[30],[30],[30])


        self.map_dictionary = {}
        n = 1
        for image in pygame_tile_image_list:
            self.map_dictionary[str(n)] = image
            # { '1' : pygame_image_1 , '2' : pyga,e_image_2 ....  }
            n += 1


    def loadANDreturn_collidable_tiles(self, colidable_index_list):
        game_map = functions.read_map(self.game_map_location)
        # list: [ [3,0,0,...] , [3,0,0,...] , ...]
        collidable_tiles = []

        y =0
        for row in game_map:
            x = 0
            for tile_num in row:
                if tile_num != '0' and tile_num != '3':
                    self.display.blit(self.map_dictionary[tile_num], (x*self.TILESIZE - self.player.scroll[0],y*self.TILESIZE - self.player.scroll[1]))
                if tile_num == '1' or tile_num == '2' or tile_num == '3':
                    collidable_tiles.append(pygame.Rect(x * self.TILESIZE,y * self.TILESIZE,self.TILESIZE,self.TILESIZE))
                x += 1

            y += 1

        return collidable_tiles


    def game(self):
        diobox_test = False

        running = True
        while running:

            self.display.fill((146, 244, 255))
            self.display.blit(pygame.transform.scale(pygame.image.load("images/level_3/map/stickyfingers.png"),[16,16]),[7*16 - (self.player.scroll[0]/2),13*16 - (self.player.scroll[1])])

            self.player.collidable_tiles = self.loadANDreturn_collidable_tiles(constants.level3_collidable_indexs)
            self.player.update()

            if diobox_test:
                diobox_test = self.dialogue_box("Hello Peter!",[10,self.display.get_height() - (self.display.get_height()/2.5)],K_w)
                self.player.is_movingRight = False
                self.player.is_movingLeft = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        diobox_test = True
                self.player.check_event(event)

            surf = pygame.transform.scale(self.display, constants.WINDOWSIZE)
            self.screen.blit(surf, (0, 0))
            pygame.display.update()
            self.clock.tick(constants.game_frames_per_second)