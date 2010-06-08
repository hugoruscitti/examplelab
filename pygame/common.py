# -*- encoding: utf-8 -*-
import pygame

white = (255, 255, 255)
pos_image = (20, 10)
pos_convert = (180, 10)

pygame.init()
image = pygame.image.load('example.png')

font = pygame.font.Font("gnome_vera_mono.ttf", 11)

def restore(screen, background=None):
    if background:
        screen.blit(background, (0, 0))
    else:
        screen.fill((255, 255, 255))


def save_screen(name, code=None):
    screen = pygame.display.get_surface()
    font_color = (100, 100, 100)

    # Text "after"
    if code:
        after = font.render(code, 1, font_color)
        rect = after.get_rect()
        rect.centerx = 160
        rect.top = 183
        screen.blit(after, rect)

    filename = "result/%s.png" %(name)

    pygame.image.save(screen, filename)
    print "Saving:", filename

def save_screenshot(screen, name, convert, code):
    global image
    global pos_image, pos_convert
    global font


    font_color = (100, 100, 100)

    screen.blit(image, pos_image)
    screen.blit(convert, pos_convert)

    # Text "after"
    after = font.render(code, 1, font_color)
    rect = after.get_rect()
    rect.centerx = 160
    rect.top = 183
    screen.blit(after, rect)

    filename = "result/%s.png" %(name)

    pygame.image.save(screen, filename)
    print "Saving:", filename


def draw_code(screen, code):
    global font

    code = code.strip()
    lines = code.split('\n')
    color = (100, 100, 100)

    surfaces = [font.render(line, 1, color) for line in lines]
    dst = surfaces[-1].get_rect()
    dst.x = 10
    dst.bottom = screen.get_height() - 10
    dst.y -= (len(surfaces) - 1) * (dst.height)

    for surface in surfaces:
        screen.blit(surface, dst)
        dst.y += dst.height
