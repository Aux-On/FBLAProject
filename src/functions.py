import random
import sys, pygame



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


def applyFunctionToAllInList(list,function):
    finallist = []
    for element in list:
        finallist.append(function(element,True,False))
    return finallist

def clip(surf,x,y,x_size,y_size):
    handle_surf = surf.copy()
    clipR = pygame.Rect(x,y,x_size,y_size)
    handle_surf.set_clip(clipR)
    image = surf.subsurface(handle_surf.get_clip())
    return image.copy()





def generate_clouds (display, number_of_clouds, cloud_images_list, cloud_index, spacing_factor, image_y_locations, scrollxy):

    for i in range(number_of_clouds):
        display.blit(pygame.image.load(cloud_images_list[cloud_index[i]]),[i*16*spacing_factor - scrollxy[0],image_y_locations[i]- scrollxy[1]])



def rand_list(a,b,number_of_items):
    lista = []
    for i in range(number_of_items):
        lista.append(random.randint(a,b))
    return lista




class Font:
    def __init__(self, path, color):
        self.spacing = 1
        self.character_order = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','.','-',',',':','+','\'','!','?','0','1','2','3','4','5','6','7','8','9','(',')','/','_','=','\\','[',']','*','"','<','>',';']
        font_img = pygame.image.load(path).convert()
        font_img.set_colorkey((0,0,0))
        #self.fill(font_img,pygame.Color(color))
        current_char_width = 0
        self.characters = {}
        character_count = 0
        for x in range(font_img.get_width()):
            c = font_img.get_at((x, 0))
            if c[0] == 127:
                char_img = clip(font_img, x - current_char_width, 0, current_char_width, font_img.get_height())
                self.characters[self.character_order[character_count]] = char_img.copy()
                character_count += 1
                current_char_width = 0
            else:
                current_char_width += 1
        self.space_width = self.characters['A'].get_width()

    def fill(self, surface, color):
        """Fill all pixels of the surface with color, preserve transparency."""
        w, h = surface.get_size()
        r, g, b, _ = color
        for x in range(w):
            for y in range(h):
                a = surface.get_at((x, y))[3]
                surface.set_at((x, y), pygame.Color(r, g, b, a))

    def render(self, surf, text, loc):
        x_offset = 0
        for char in text:
            if char != ' ':
                surf.blit(self.characters[char], (loc[0] + x_offset, loc[1]))
                x_offset += self.characters[char].get_width() + self.spacing
            else:
                x_offset += self.space_width + self.spacing