# Mynthos : A World Generator (Prototype)
# By Dylan Wolfe
# Created October, 2020

#--- Imports ---#
import pygame
import random
import noise
import terrain

#--- Init ---#
pygame.init()

display_width = 600
display_height = 600

window = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Mynthos")

#--- Variables ---#

# Colors
bgc = (32,32,32)
ln = (38,38,38)
barren = (210, 162, 120)
verdant = (0, 178, 60)
ocean = (52, 152, 255)
ocean_alt = (76, 166, 255)
mountain = (168, 158, 148)

# Game Objects
tile_size = 2
ttile_list = [[0 for y in range(0, int(display_height/tile_size))] for x in range(0, int(display_width/tile_size))] # 2D array that holds terrain

# Terrain Var
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

def draw_terrain():

    for j in range (0, int(display_height/tile_size)): # populate ttile_list
        for i in range(0, int(display_height/tile_size)):
            ttile_list[i][j] = noise.pnoise2(i/100.0, # 2d perlin noise from native noise module
                                    j/100.0,
                                    octaves = noise_oct,
                                    persistence = noise_pers,
                                    lacunarity= noise_lac,
                                    repeatx = display_width,
                                    repeaty = display_height,
                                    base = perlin_base)

    for y in range (0, display_height, tile_size): # horizontal fill until vertical end of display
        for x in range(0, display_width, tile_size): # create a rect size tile_size until horizontal end of display

            if ((ttile_list[int(y/tile_size)][int(x/tile_size)]) < -0.05): # TEMP if statement for color selection
                rcolor = ocean
            elif ((ttile_list[int(y/tile_size)][int(x/tile_size)]) < 0):
                rcolor = barren
            elif ((ttile_list[int(y/tile_size)][int(x/tile_size)]) < 0.2):
                rcolor = verdant
            elif ((ttile_list[int(y/tile_size)][int(x/tile_size)]) < 1.0):
                rcolor = mountain
            else:
                rcolor = bgc

            pygame.draw.rect(window, rcolor, (x, y, tile_size, tile_size))


#--- Runtime ---#

run = True
while run:
    pygame.time.delay(100)

    while (pygame.time.get_ticks()) < 1000: # Draw once TEMP

        draw_back()
        draw_grid()
        draw_terrain()

        print(ttile_list)

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

                perlin_base = (random.randint(1,100)) # Init new base seed
                draw_back()
                draw_grid()
                draw_terrain()

        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
