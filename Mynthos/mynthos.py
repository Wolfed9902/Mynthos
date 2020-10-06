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
verdant = (0, 178, 60)
ocean = (52, 152, 255)
ocean_alt = (76, 166, 255)

# Game Objects
tile_size = 6
land_origin = (random.randint(0,(display_width/4))) * 2
land_height = (random.randint(land_origin,(display_height/2))) * 2
land_width = (random.randint(land_origin,(display_height/2))) * 2 # FIX! - land tiles exceed even numbers
land_clrlist = []

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

    # TEMPORARY - Draw a rect for continent
    for y in range (land_origin, land_height, tile_size):
        for x in range (land_origin, land_width, tile_size):
            rcolor = random.choice([barren,verdant])
            pygame.draw.rect(window, rcolor, (x, y, tile_size, tile_size))

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
