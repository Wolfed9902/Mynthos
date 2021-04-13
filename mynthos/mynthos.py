# Mynthos : A World Generator (Prototype)
# By Dylan Wolfe
# Created October, 2020

#--- Imports ---#
import pygame
import random
import noise
from terrain import TerrainTile

#--- Init ---#
pygame.init()

display_width = 600
display_height = 600

window = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Mynthos")

#--- Variables ---#

# Colors
color_dict = { 'bgc' : {'color': (32,32,32)},
                'barren' : {'color': (210, 162, 120)},
                'verdant' : {'color': (0, 178, 60)},
                'ocean' : {'color': (52, 152, 255)},
                'ocean_alt' : {'color': (76, 166, 255)},
                'mountain' : {'color': (168, 158, 148)},
                'peak' : {'color': (215, 215, 215)}
                }

bgc = (32,32,32)
ln = (38,38,38)

# Game Objects
tile_size = 4
tgen_list = [[0 for y in range(0, int(display_height/tile_size))] for x in range(0, int(display_width/tile_size))] # list that holds perlin grid
ttile_list = [[TerrainTile('barren') for y in range(0, int(display_height/tile_size))] for x in range(0, int(display_width/tile_size))] # list that holds terrain
sel_tile_x = 0
sel_tile_y = 0

# Terrain Generation Variables
noise_oct = 6
noise_pers = 0.5
noise_lac = 2
perlin_base = (random.randint(1,100))


def draw_back():
    window.fill(bgc)

def draw_grid():

    for x in range(0, display_width, tile_size):
        pygame.draw.line(window, ln, (x, 0), (x, display_height))
    for y in range(0, display_height, tile_size):
        pygame.draw.line(window, ln, (0, y), (display_width, y))

def generate_terrain():

        for j in range (0, int(display_height/tile_size)): # populate tgen_list
            for i in range(0, int(display_width/tile_size)):
                tgen_list[i][j] = noise.pnoise2(i/100.0, # 2d perlin noise from native noise module
                                        j/100.0,
                                        octaves = noise_oct,
                                        persistence = noise_pers,
                                        lacunarity= noise_lac,
                                        repeatx = display_width,
                                        repeaty = display_height,
                                        base = perlin_base)

        for y in range (0, int(display_height/tile_size)): # populate ttile_list types based off of tgen_list
            for x in range(0, int(display_width/tile_size)):

                if ((tgen_list[y][x]) < -0.05):
                    (ttile_list[y][x]).type = 'ocean'
                    (ttile_list[y][x]).passable = False
                elif ((tgen_list[y][x]) < 0):
                    (ttile_list[y][x]).type = 'barren'
                elif ((tgen_list[y][x]) < 0.2):
                    (ttile_list[y][x]).type = 'verdant'
                elif ((tgen_list[y][x]) < 0.35):
                    (ttile_list[y][x]).type = 'mountain'
                elif ((tgen_list[y][x]) < 1.0):
                    (ttile_list[y][x]).type = 'peak'
                    (ttile_list[y][x]).passable = False
                else:
                    (ttile_list[y][x]).type = 'bgc'


def draw_terrain():

    for y in range (0, display_height, tile_size): # horizontal fill until vertical end of display
        for x in range(0, display_width, tile_size): # create a rect size tile_size until horizontal end of display

            if ( (((ttile_list[int(y/tile_size)][int(x/tile_size)]).selected)) == False ):
                rcolor = ((ttile_list[int(y/tile_size)][int(x/tile_size)]).type)
            else:
                rcolor = 'bgc'

            pygame.draw.rect(window, (color_dict[rcolor]["color"]), (x, y, tile_size, tile_size)) # draw in color matching terrain type


#--- Runtime ---#

run = True
while run:
    pygame.time.delay(100)

    while (pygame.time.get_ticks()) < 1060: # Draw once TEMP

        (ttile_list[int(sel_tile_y)][int(sel_tile_x)]).selected = True

        draw_back()
        draw_grid()
        generate_terrain()
        draw_terrain()

        print(tgen_list) # Debug TEMP

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                perlin_base = (random.randint(1,100)) # Init new base seed
                draw_back()
                draw_grid()
                generate_terrain()
                print(tgen_list) # Debug TEMP

            if event.key == pygame.K_UP: # Selected tile according to key input (TODO: streamline this!)
                (ttile_list[int(sel_tile_y)][int(sel_tile_x)]).selected = False
                if (sel_tile_y > 0):
                    sel_tile_y -= 1
                (ttile_list[int(sel_tile_y)][int(sel_tile_x)]).selected = True
            if event.key == pygame.K_DOWN:
                (ttile_list[int(sel_tile_y)][int(sel_tile_x)]).selected = False
                if (sel_tile_y < (len(ttile_list) - 1)):
                    sel_tile_y += 1
                (ttile_list[int(sel_tile_y)][int(sel_tile_x)]).selected = True
            if event.key == pygame.K_LEFT:
                (ttile_list[int(sel_tile_y)][int(sel_tile_x)]).selected = False
                if (sel_tile_x > 0):
                    sel_tile_x -= 1
                (ttile_list[int(sel_tile_y)][int(sel_tile_x)]).selected = True
            if event.key == pygame.K_RIGHT:
                (ttile_list[int(sel_tile_y)][int(sel_tile_x)]).selected = False
                if (sel_tile_x < (len(ttile_list) - 1)):
                    sel_tile_x += 1
                (ttile_list[int(sel_tile_y)][int(sel_tile_x)]).selected = True

            draw_terrain()

        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
