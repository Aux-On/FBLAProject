import sys, pygame, math

from src import constants, Mobs, functions

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


        self.player = Mobs.Player(self.player_image,True, [50,50],self.display,[30],[30],[30])
        self.slime = Mobs.Slime(self.display,[16*5,16*13],'images/level_3/Slime', [16,16],[30,30],[30],[30])
        #self.slime1 = Mobs.Slime(self.display, [16*10,16*13], 'images/level_3/Slime', [16, 16], [30, 30], [30], [30])
        #self.slime2 = Mobs.Slime(self.display, [16*15,16*13], 'images/level_3/Slime', [16, 16], [30, 30], [30], [30])
        #self.slime3 = Mobs.Slime(self.display, [16*18,16*13], 'images/level_3/Slime', [16, 16], [30, 30], [30], [30])
        #self.slime4 = Mobs.Slime(self.display, [16*20,16*13], 'images/level_3/Slime', [16, 16], [30, 30], [30], [30])
        #self.slime5 = Mobs.Slime(self.display, [16*42,16*13], 'images/level_3/Slime', [16, 16], [30, 30], [30], [30])
        #self.slime6 = Mobs.Slime(self.display, [16*49,16*13], 'images/level_3/Slime', [16, 16], [30, 30], [30], [30])
        #self.slime7 = Mobs.Slime(self.display, [16*52,16*13], 'images/level_3/Slime', [16, 16], [30, 30], [30], [30])
        #self.slime8 = Mobs.Slime(self.display, [16*55,16*13], 'images/level_3/Slime', [16, 16], [30, 30], [30], [30])
        #self.slime9 = Mobs.Slime(self.display, [16*67,16*13], 'images/level_3/Slime', [16, 16], [30, 30], [30], [30])
        #self.slime10 = Mobs.Slime(self.display, [16*77,16*13], 'images/level_3/Slime', [16, 16], [30, 30], [30], [30])
        #self.slime11 = Mobs.Slime(self.display, [16*80,16*13], 'images/level_3/Slime', [16, 16], [30, 30], [30], [30])
        #self.slime12 = Mobs.Slime(self.display, [16*90,16*13], 'images/level_3/Slime', [16, 16], [30, 30], [30], [30])
        #self.slime13 = Mobs.Slime(self.display, [16*100,16*13], 'images/level_3/Slime', [16, 16], [30, 30], [30], [30])
        #self.slime14 = Mobs.Slime(self.display, [16*120,16*13], 'images/level_3/Slime', [16, 16], [30, 30], [30], [30])
        #self.slime15 = Mobs.Slime(self.display, [16*140,16*13], 'images/level_3/Slime', [16, 16], [30, 30], [30], [30])


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

#           ^color stuff for background here!!

    def game(self):
        diobox_test = False
        running = True

        cloudyvals = functions.rand_list(8*16,16*16,50)
        cloud_idexes = functions.rand_list(0,1,50)

        while running:


            self.display.fill((146, 244 , 245))

            functions.generate_clouds(self.display,25,['images/cloud1.png','images/cloud2.png'], cloud_idexes,5,cloudyvals,self.player.scroll)


            self.player.collidable_tiles = self.loadANDreturn_collidable_tiles(constants.level3_collidable_indexs)
            self.slime.collidable_tiles = self.loadANDreturn_collidable_tiles(constants.level3_collidable_indexs)
            self.player.update()
            self.slime.update(self.player.collidable_tiles,self.player.scroll)
            #self.slime1.update(self.player.collidable_tiles, self.player.scroll)
            #self.slime2.update(self.player.collidable_tiles, self.player.scroll)
            #self.slime3.update(self.player.collidable_tiles, self.player.scroll)
            #self.slime5.update(self.player.collidable_tiles, self.player.scroll)
            #self.slime6.update(self.player.collidable_tiles, self.player.scroll)
            #self.slime7.update(self.player.collidable_tiles, self.player.scroll)
            #self.slime8.update(self.player.collidable_tiles, self.player.scroll)
            #self.slime9.update(self.player.collidable_tiles, self.player.scroll)
            #self.slime10.update(self.player.collidable_tiles, self.player.scroll)
            #self.slime11.update(self.player.collidable_tiles, self.player.scroll)
            #self.slime12.update(self.player.collidable_tiles, self.player.scroll)
            #self.slime13.update(self.player.collidable_tiles, self.player.scroll)
            #self.slime14.update(self.player.collidable_tiles, self.player.scroll)
            #self.slime15.update(self.player.collidable_tiles, self.player.scroll)


            if diobox_test:
                diobox_test = self.dialogue_box("Hello Peter! And Jaffar! You Are in Misery",[10,self.display.get_height() - (self.display.get_height()/2.5)],K_w)
                self.player.is_movingRight = False
                self.player.is_movingLeft = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_q:
                        diobox_test = True
                self.player.check_event(event)

            surf = pygame.transform.scale(self.display, constants.WINDOWSIZE)
            self.screen.blit(surf, (0, 0))
            pygame.display.update()
            self.clock.tick(constants.game_frames_per_second)






########################################################################################################################
#                                                    SUB CLASS
########################################################################################################################



class Level1(Level):
    def __init__(self, clock, display,game_map_location,pygame_tile_image_list):
        Level.__init__(self, clock, display,game_map_location)
        #super.__init__(clock,display,game_map_location)


        self.player = Mobs.Player(self.player_image,True, [16*8,13*16+1],self.display,[30],[30],[30])

        self.map_dictionary = {}
        n = 0
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
                if tile_num != '3':
                    self.display.blit(self.map_dictionary[tile_num], (x*self.TILESIZE - self.player.scroll[0],y*self.TILESIZE - self.player.scroll[1]))
                if tile_num == '1' or tile_num == '2' or tile_num == '3':
                    collidable_tiles.append(pygame.Rect(x * self.TILESIZE,y * self.TILESIZE,self.TILESIZE,self.TILESIZE))
                x += 1

            y += 1

        return collidable_tiles
#           ^color stuff for background here!!

    def game(self):
        diobox_test = False
        running = True

        cloudyvals = functions.rand_list(8*16,16*16,50)
        cloud_idexes = functions.rand_list(0,1,50)
        r = 0
        g = 0
        b = 0
        isr = False
        isg = False
        isb = False

        while running:

            if isr:
                r+=1
                if r > 255:
                    r = 0
            if isg:
                g+=1
                if g > 255:
                    g = 0
            if isb:
                b+=1
                if b > 255:
                    b = 0


            self.display.fill((r, g , b))

            self.player.collidable_tiles = self.loadANDreturn_collidable_tiles(constants.level3_collidable_indexs)
            self.player.update()


            for y in range(self.display.get_height()):

                for x in range(self.display.get_width()):
                    dist = [self.player.Rect.x + 8 - x - self.player.true_scroll[0], self.player.Rect.y - y - self.player.true_scroll[1]]
                    if math.sqrt((dist[0]*dist[0]) + (dist[1]*dist[1])) < 64:
                        color = self.display.get_at((x,y))
                        fc = []
                        for col in color:
                            if col+50 > 255:
                                fc.append(col)
                            else:
                                fc.append(col+50)

                        self.display.set_at((x,y), (fc[0], fc[1],fc[2]))


            if diobox_test:
                diobox_test = self.dialogue_box("Hello Peter! And Jaffar! You Are in Misery",[10,self.display.get_height() - (self.display.get_height()/2.5)],K_w)
                self.player.is_movingRight = False
                self.player.is_movingLeft = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == KEYUP:
                    if event.key == K_r:
                        isr = False
                    if event.key == K_g:
                        isg = False
                    if event.key == K_b:
                        isb = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_q:
                        diobox_test = True
                    if event.key == K_r:
                        isr = True
                    if event.key == K_g:
                        isg = True
                    if event.key == K_b:
                        isb = True
                self.player.check_event(event)

            surf = pygame.transform.scale(self.display, constants.WINDOWSIZE)
            self.screen.blit(surf, (0, 0))
            pygame.display.update()
            self.clock.tick(constants.game_frames_per_second)