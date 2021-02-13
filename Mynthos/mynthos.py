# Mynthos : A World Generator (Prototype)
# By Dylan Wolfe
# Created October, 2020

#--- Imports ---#
import pygame
import random
import terrain
from noise import pnoise2

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

# Game Objects
tile_size = 6
ttile_list = [['X' for y in range(0, int(display_height/tile_size))] for x in range(0, int(display_width/tile_size))] # 2D array that holds terrain

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
            ttile_list[i][j] = random.choice(["O","L"])

    for y in range (0, display_height, tile_size): # horizontal fill until vertical end of display
        for x in range(0, display_width, tile_size): # create a rect size tile_size until horizontal end of display
            #rtype = random.choice(["ocean","barren"]) # cycle terrain type
            rcolor = random.choice([ocean,barren]) # TEMP
            pygame.draw.rect(window, rcolor, (x, y, tile_size, tile_size))


#--- Runtime ---#

run = True
while run:
    pygame.time.delay(200)

    while (pygame.time.get_ticks()) < 2000: # Draw once TEMP

        draw_back()
        draw_grid()
        draw_terrain()

        print(ttile_list)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
