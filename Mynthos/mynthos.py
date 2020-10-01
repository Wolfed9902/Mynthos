# Mynthos : A World Generator
# By Dylan Wolfe
# Created October, 2020

#--- Imports ---#
import pygame
import random

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
ocean = (52, 152, 255)
ocean_alt = (76, 166, 255)

# Game Objects
tile_size = 12
land_start = random.choice([12,48,96,192])
land_end = random.choice([12,48,96,192])

def draw_back():
    window.fill(bgc)

def draw_grid():

    for x in range(0, display_width, tile_size):
        pygame.draw.line(window, ln, (x, 0), (x, display_height))
    for y in range(0, display_height, tile_size):
        pygame.draw.line(window, ln, (0, y), (display_width, y))

def draw_ocean():

    for y in range (0, display_height, tile_size): # horizontal fill until vertical end of display
        for x in range(0, display_width, tile_size): # create a rect size tile_size until horizontal end of display
            rcolor = random.choice([ocean,ocean_alt]) # cycle ocean colors
            pygame.draw.rect(window, rcolor, (x, y, tile_size, tile_size))

def draw_land():
    # TEMPORARY
    for y in range (0, land_start, tile_size):
        for x in range (0, land_end, tile_size):
            pygame.draw.rect(window, barren, (x, y, tile_size, tile_size))


#--- Runtime ---#
run = True
while run:
    pygame.time.delay(100)

    draw_back()
    draw_grid()
    draw_ocean()
    draw_land()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
