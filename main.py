import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

# Creates images with smooth gradients
def create_scales(height):
    red_scale_surface   = pygame.surface.Surface((640, height))
    green_scale_surface = pygame.surface.Surface((640, height))
    blue_scale_surface  = pygame.surface.Surface((640, height))

    for x in range(640):
        c = int((x/639.)*255.)
        red   = (c, 0, 0)
        green = (0, c, 0)
        blue  = (0, 0, c)
        line_rect = Rect(x, 0, 1, height)
        pygame.draw.rect(red_scale_surface, red, line_rect)
        pygame.draw.rect(green_scale_surface, green, line_rect)
        pygame.draw.rect(blue_scale_surface, blue, line_rect)

    return red_scale_surface, green_scale_surface, blue_scale_surface


def invert_color(color):
    red, green, blue = color
    red = 255 - red
    green = 255 - green
    blue = 255 - blue

    return int(red), int(green), int(blue)


def color_lerp(color1, color2, factor): # L = v1+(v2-v1)*f

    red1, green1, blue1 = color1
    red2, green2, blue2 = color2

    red = red1 + (red2 - red1) * factor
    green = green1 + (green2 - green1) * factor
    blue = blue1 + (blue2 - blue1) * factor

    return int(red), int(green), int(blue)


red_scale, green_scale, blue_scale = create_scales(80)

color = [127, 127, 127]

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))

    # Draw the scales to the screen
    screen.blit(red_scale, (0, 00))
    screen.blit(green_scale, (0, 80))
    screen.blit(blue_scale, (0, 160))

    x, y = pygame.mouse.get_pos()

    # If the mouse was pressed on one of the sliders, adjust the color component
    if pygame.mouse.get_pressed()[0]:
        for component in range(3):
            if y > component*80 and y < (component+1)*80:
                color[component] = int((x/639.)*255.)
            pygame.display.set_caption("RDNCK Palette Generator - "+str(tuple(color)))

    # Draw a circle for each slider to represent the current setting
    for component in range(3):
        pos = ( int((color[component]/255.)*639), component*80+40 )
        pygame.draw.circle(screen, (255, 255, 255), pos, 20)

    # Color calculation
    color_a = color
    color_b = invert_color(color_a)
    color_1 = color_lerp(color_a, color_b, 0.25)
    color_2 = color_lerp(color_a, color_b, 0.50)
    color_3 = color_lerp(color_a, color_b, 0.75)

    # Main section - Selected Color and it's inverse
    pygame.draw.rect(screen, tuple(color_a), (0, 240, 320, 180))
    pygame.draw.rect(screen, tuple(color_b), (320, 240, 320, 180))

    # lower section - Color Palette
    pygame.draw.rect(screen, tuple(color_a), (0, 430, 128, 50))
    pygame.draw.rect(screen, tuple(color_1), (128, 430, 128, 50))
    pygame.draw.rect(screen, tuple(color_2), (128*2, 430, 128, 50))
    pygame.draw.rect(screen, tuple(color_3), (128*3, 430, 128, 50))
    pygame.draw.rect(screen, tuple(color_b), (128*4, 430, 128, 50))

    pygame.display.update()
