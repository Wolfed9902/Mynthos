# Mynthos : A World Generator
# By Dylan Wolfe
# Created October, 2020

#--- Imports ---#
import pygame

#--- Init ---#
pygame.init()

display_width = 600
display_height = 600

window = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Mynthos")

#--- Variables ---#

# Colors
bgc = (32,32,32)
crust = (210, 162, 120)

# Game Objects
x = 50
y = 50
width = 12
height = 12
vel = 5

def draw_back():
    window.fill(bgc)

# Runtime
run = True
while run:
    pygame.time.delay(100)

    draw_back()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(window, crust, (x, y, width, height))
    pygame.display.update()

pygame.quit()
